#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('CREATE TABLE players (name text, dciNumber text, regId text, secretToken text)')

conn.commit()
conn.close()

print '''You need to change apache2 conf to restrict access to /actions/public
Order deny,allow
Deny from all
Allow from dev.example.com'''
