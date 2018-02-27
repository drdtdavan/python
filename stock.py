import fdb
import collections
class StockItem:
    def __init__(self):
        self.MN=""
        self.SAME=0
        self.STOCKQ=0
        self.STDATE=""
        self.DISP=0
        self.UP=0
        self.NC=""
        self.SOH=0

def getDisp(item):
    vdate=str(item.STDATE)[0:10]   
    cur.execute("select count(QUANTITY) from medicineregister where NAPPICODE="+item.NC+" and vdate>=CAST('"+vdate+"' AS TIMESTAMP)")
    arr=cur.fetchone()   
    item.DISP=arr[0]

def getName(item):
    cur.execute("select MN from MD2 where NC="+item.NC)
    arr=cur.fetchone()   
    item.MN=arr[0]

def getSame(siL,s):
    ls=(i for i in siL if i[1]==s)
    soh=sum(i.SOH for i in ls)   
    print("TOTAL QUANTITY = "+str(soh)+ " TOTAL PRICE = " +str(soh*ls[0].UP))
    for i in ls:
        print(i.MN+"\t"+i.SOH)    
    print("_____________________")

    
def getUP(si):
    cur.execute("select UNITPRICE from PURCHASES where NC="+ si.NC +" ORDER BY PDATE DESC")
    arr=cur.fetchone()   
    try:

       si.UP=arr[0]
    except:
       print("Error for : "+si.NC)
 
#con = fdb.connect(dsn='C:/Users/dtdav/Desktop/NONGOMA.GDB', user='SYSDBA', password='masterkey')
con = fdb.connect(dsn='C:/Users/Dan/Desktop/20180219/NONGOMA.GDB', user='SYSDBA', password='masterkey')

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select NC,SAME,STDATE,STOCKQ from STOCK ORDER BY SAME")

# Retrieve all rows as a sequence and print that sequence:
arr=cur.fetchall()

siList=[]
samesiList=[]
zeroList=[]

for i in arr:
    samesiList.append(i[1])
    si=StockItem()
    si.NC=i[0]
    si.SAME=i[1]
    si.STDATE=i[2]
    si.STOCKQ=i[3]
    getDisp(si)
    si.SOH=si.STOCKQ-si.DISP
    getUP(si)
    siList.append(si)

s=set(samesiList)

for x in s:
    getSame(siList,x)



















    



    