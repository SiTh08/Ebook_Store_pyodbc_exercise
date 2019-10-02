import pyodbc

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
            print('Title', row[0])
            print('Author', row[1])
            print('Date', row[2])
        print('The end')


