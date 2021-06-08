import pyodbc
connstr = pyodbc.connect('DRIVER={SQL Server};SERVER=CATL0DB728\INTCCIPROD;DATABASE=itt;Trusted_Connection=yes;')
cursor = connstr.cursor()
cursor.execute("SELECT u_server_name FROM LCM_SNOW")
 
#for row in cursor:
#    print(row)

columns = [column[0] for column in cursor.description]