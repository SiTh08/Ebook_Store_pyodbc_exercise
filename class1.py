import pyodbc
from connection import *

class ConnectMsS():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_ebooks = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_ebooks.cursor()

    def filter_query(self, query):
        return self.cursor.execute(query)

    def print_all_ebooks(self):
        query_rows = self.filter_query('SELECT * FROM ebooks')
        for row in query_rows:
            print('Title:', row[0] + ', ' + 'Author:', row[1] + ', ' + 'Date:', row[2])

    def print_specific_ebooks(self, name):
        query_rows = self.filter_query(f'SELECT * FROM ebooks where Title = {name}').fetchone()
        print(query_rows)

    def input_book(self, title, author, date):
        self.filter_query(f'INSERT INTO ebooks (Title, Author, [Date]) VALUES ({title}, {author}, {date})')
        conn_ebooks.commit()



