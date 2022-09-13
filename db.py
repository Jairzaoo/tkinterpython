from msilib.schema import Error
import ibm_db
import ibm_db_dbi
from ibm_db_dbi import Error
import pandas as pd

conn_string = "DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=xrl14403;PWD=lEbtvSLFGIUJwrhC;SECURITY=SSL"
conn = ibm_db_dbi.connect(conn_string,"","")

#def create_server_connection(conn):
#    conn = None
#    try:
#        conn_string = "DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=xrl14403;PWD=lEbtvSLFGIUJwrhC;SECURITY=SSL"
#        conn = ibm_db_dbi.connect(conn_string,"","")
#        print("conectado ao banco de dados")
#    except Error as err:
#        print(f"Erro: '{err}'")
#    return conn

def create_database(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso")
    except Error as err:
        print(f"Erro: '{err}'")
        
def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("executado com sucesso")
    except Error as err:
        print(f"Erro: '{err}'")
        
def read_query(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Erro: '{err}'")
        


'''

delete_order = """
delete from orders where order_id=105;
"""
execute_query(conn, delete_order)
--------------------------------------
update = """
update orders
set unit_price = 45
where order_id = 103
"""

execute_query(conn, update)
--------------
from_db[]
for result in results:
    result = list(result)
    from_db.appends(results)
columns = [login, password]
df = pd.DataFrame(from_db, columns = columns)
display(df)
-------------------------------
readquery = """
select * from Logins
"""
results = read_query(conn, readquery)
for result in results:
    print(result)

----------------------
criar_tabela_teste = """
create table Produtos(
    nome varchar(30) primary key not null,
    medida varchar(30) not null,
    quantidade int)    """

create_database(conn, criar_tabela_teste)
---------------------------------------
criarlogin = """
insert into Logins values(3, 3, False)"""
execute_query(conn, criarlogin)
'''
'''
# Multiple values single statement/execution
c.execute('SELECT * FROM stocks WHERE symbol=? OR symbol=?', ('RHAT', 'MSO'))
print c.fetchall()
c.execute('SELECT * FROM stocks WHERE symbol IN (?, ?)', ('RHAT', 'MSO'))
print c.fetchall()
# This also works, though ones above are better as a habit as it's inline with syntax of executemany().. but your choice.
c.execute('SELECT * FROM stocks WHERE symbol=? OR symbol=?', 'RHAT', 'MSO')
print c.fetchall()
# Insert a single item
c.execute('INSERT INTO stocks VALUES (?,?,?,?,?)', ('2006-03-28', 'BUY', 'IBM', 1000, 45.00))

cursor.execute("INSERT INTO table VALUES (?, ?, ?)", (var1, var2, var3))
'''


#print("Creating connection.......")

#conn_string = "DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=xrl14403;PWD=lEbtvSLFGIUJwrhC;SECURITY=SSL"
#conn = ibm_db_dbi.connect(conn_string,"","")
#def databaseOn():
#    conn = ibm_db.connect(conn_string,"","")
#    if conn:
#        print("Connection ...... [SUCCESS]")
#    else:
#        print("Connection ...... [FAILURE]")
#def databaseOff():
#    ibm_db.close(conn)
#pconn = ibm_db_dbi.Connection(conn)#connection for pandas



#if conn:
#    print("Connection ...... [SUCCESS]")
#else:
#    print("Connection ...... [FAILURE]")
    
    
#dropQuery = "drop table Logins"#delete
#dropStmt = ibm_db.exec_immediate(conn, dropQuery)
    
#createQuery = "create table Logins(USERNAME VARCHAR(50) PRIMARY KEY NOT NULL, PASSWORD VARCHAR(255) NOT NULL, ADMIN BOOLEAN)"
#createStmt = ibm_db.exec_immediate(conn, createQuery)

    
#insertQuery = "insert into LoginS values('2', '2', FALSE)"
#insertStmt = ibm_db.exec_immediate(conn, insertQuery)

#insertQuery = "insert into Logins values('1', '1', TRUE)"
#insertStmt = ibm_db.exec_immediate(conn, insertQuery)
#SELECT Result FROM resultstable WHERE QuizID=? AND UserID=?", usuario, UserID)

#select = ('SELECT * from Logins WHERE USERNAME=?', (user))

#"INSERT INTO table VALUES (?, ?, ?)", (var1, var2, var3))
#cur = conn.cursor()
#user = ['1']
#cur.execute("SELECT * from Logins where USERNAME='%user'")
#row=cur.fetchall()
#print(row)
#cur.close()

#selectQuery = "select * from Logins"
#stmt = ibm_db.exec_immediate(conn, selectQuery)

#while ibm_db.fetch_row(stmt) != False:
#    print ("The Employee number is : ",  ibm_db.result(stmt, 0))
#    print ("The last name is : ", ibm_db.result(stmt, "PASSWORD"))

#selectQuery = "select * from Login"
#pdf = pd.read_sql(selectQuery, pconn)
#pdf.LOGIN[0]




#ibm_db_dbi.close(conn)

