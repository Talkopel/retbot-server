import MySQLdb as mysql
import socket
from threading import Thread
import struct

class Output(object):
	db = None

DBUNAME = 'test'
DBPASS = 'test'
DBNAME = 'open_records'
LISTENPORT = 3332

def init_db():
	Output.db = mysql.connect("localhost", DBUNAME, DBPASS, DBNAME)

def listen_for_reports(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.bind(("127.0.0.1",port))
	while True:
		s.listen(1)
		client, addr = s.accept()
		m_len = client.recv(4)

		if m_len == None:
			continue;

		m_len = struct.unpack(">I", m_len)[0]
		report = client.recv(m_len)


		runner = Thread(target=parse_report, args=(report, addr[0]))
		runner.start()

def parse_report(report, ip):

	if report == None or len(report) < 2:
		return False

	records = report.split(chr(1)) # Separator is SOH
	
	if len(records) == 1:
		return False

	for record in records:
		try:
			path, user, mode, time = record.split(" ")
		except ValueError:
			continue
		if "libpcap" in path:
			insert_open_alert(path, user, mode, time, ip)

def insert_open_alert(path, user, mode, time, ip):

	insert = """ insert into alerts
				(file, uid, time, ip)
				VALUES
				(%(file)s, %(uid)s, %(time)s, %(ip)s)
			 """
	# import pdb; pdb.set_trace()
	try:
		data = {'file':path, 'uid':int(user), 'time':int(time), 'ip':ip}
		c = Output.db.cursor()
		c.execute(insert, data)
		Output.db.commit()
	except Exception as e:
		print "Couldn't insert record to db! %s" % (e,)
		Output.db.rollback()


if __name__ == "__main__":
	init_db()
	listen_for_reports(3332)
