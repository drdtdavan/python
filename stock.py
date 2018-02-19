import fdb

# The server is named 'bison'; the database file is at '/temp/test.db'.
con = fdb.connect(dsn='C:/Users/dtdav/Desktop/NONGOMA.GDB', user='SYSDBA', password='masterkey')

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select * from mavisitdetails where vdate>='2018-02-19'")

# Retrieve all rows as a sequence and print that sequence:
arr=cur.fetchall()
for l in arr:
    print(l)