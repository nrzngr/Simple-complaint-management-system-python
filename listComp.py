from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('daftar komplain')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#Nama', '#Gender', '#Comment'))
		tv.heading('#Nama', text='Nama')
		tv.heading('#Gender', text='Gender')
		tv.heading('#Comment', text='Comment')
		cursor = self._dbconnect.ListRequest()
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Nama',row['Nama'])
			tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
			tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
			
