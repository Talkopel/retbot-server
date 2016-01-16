from flask import *
import json
import MySQLdb as mysql

app = Flask(__name__)

DBPASS = 'test'
DBNAME = 'open_records'
DBUNAME = 'test'

class AlertsInput(object):
	db = None
	table_name = 'alerts'


def init_db():
	AlertsInput.db = mysql.connect("localhost", DBUNAME, DBPASS, DBNAME)

@app.route("/alerts", methods=['GET'])
def get_alerts():

	init_db()
	c = AlertsInput.db.cursor()
	select = "SELECT * from {};".format(AlertsInput.table_name)
	c.execute(select)
	alert = c.fetchone()

	if alert == None:
		return ""

	# data = {'file':alert[0], 'uid':alert[1], 'time':alert[2], 'ip':alert[3]}
	data = [alert[3], alert[0], alert[2], alert[1]]
	delete = "TRUNCATE {};".format(AlertsInput.table_name)
	c.execute(delete)
	AlertsInput.db.commit()
	c.close()
	AlertsInput.db.close()

	return json.dumps(data)
	


if __name__ == "__main__":

	init_db()
	app.run(host="127.0.0.1", port=4444)


