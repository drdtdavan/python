import fdb

class StockItem:
    def __init__(self):
        self.MN=""
        self.SAME=0
        self.STOCKQ=0
        self.STDATE=""
        self.DISP=0
        self.UP=0
        self.NC=""

def getDisp(item):
    vdate=str(item.STDATE)[0:10]
   
    cur.execute("select count(QUANTITY) from medicineregister where NAPPICODE="+item.NC+" and vdate>=CAST('"+vdate+"' AS TIMESTAMP)")
    arr=cur.fetchone()   
    item.DISP=arr[0]
 
con = fdb.connect(dsn='C:/Users/dtdav/Desktop/NONGOMA.GDB', user='SYSDBA', password='masterkey')

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select NC,SAME,STDATE,STOCKQ from STOCK")

# Retrieve all rows as a sequence and print that sequence:
arr=cur.fetchall()
i=-1
siList=[]
for l in arr:    
    i=StockItem()
    i.NC=l[0]
    i.SAME=l[1]
    i.STDATE=l[2]
    i.STOCKQ=l[3]
    getDisp(i)
    print("nc= "+ i.NC+" disp="+str(i.DISP))
    siList.append(i)








    



    