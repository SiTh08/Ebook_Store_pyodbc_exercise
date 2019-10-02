import pyodbc
# In this file, we will make our connection.

# Parameters/variables for connection:
server = 'localhost,1433'
database = 'Ebook_Store_DB'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection

conn_ebooks = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_ebooks)