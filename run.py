from class1 import *

server = 'localhost,1433'
database = 'Ebook_Store_DB'
username = 'SA'
password = 'Passw0rd2018'

ebook = ConnectMsS(server, database, username, password)

print(ebook.print_all_ebooks())

