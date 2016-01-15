requirements:
MySQL-python MySQL-server libmysql-dev mysql
create user test with password test on local host
create database 'open_records'
create table alerts (file VARCHAR(100), int uid, int time, ip VARCHAR(20));
