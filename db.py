#!/usr/bin/python3
import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Nama varchar(255), Gender varchar(255), Comment text(1000))')
		self._db.commit()
	def Add(self, name, gender, comment):
		self._db.execute('insert into Comp (Nama, Gender, Comment) values (?,?,?)',(name,gender,comment))
		self._db.commit()
		return 'Komplain anda berhasil disubmit.'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
