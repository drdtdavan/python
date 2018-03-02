import fdb
import collections
from functools import reduce
GT=0
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

    def __str__(self):
        return self.MN+" "+str(self.SAME)

def getDisp(item):
    vdate=str(item.STDATE)[0:10]   
    cur.execute("select count(QUANTITY) from medicineregister where NAPPICODE="+item.NC+" and vdate>=CAST('"+vdate+"' AS TIMESTAMP)")
    arr=cur.fetchone()   
    item.DISP=arr[0]

def getName(si):
    cur.execute("select MN from MD2 where NC="+si.NC)
    arr=cur.fetchone()   
    try:
       si.MN=arr[0]
    except:
       print("getName Error for : "+si.NC)
       

def getSame(siL,s):
    global GT
    ls=[i for i in siL if i.SAME==s]
    soh=0
    for x in ls:
        soh+=x.STOCKQ
    up=max(ls, key=lambda i: i.UP)
    total=soh*up.UP
    GT += total
    print(ls[0].MN+" TOTAL QUANTITY = "+str(soh)+" "+ str(up.UP)+" TOTAL PRICE = " +str(total))    
    print("_____________________")

    
def getUP(si):
    print("class "+str(si))
    cur.execute("select UNITPRICE from PURCHASES where NC="+ si.NC +" ORDER BY PDATE DESC")
    arr=cur.fetchone()   
    try:

       si.UP=arr[0]
    except:
       print("getUP Error for : "+si.NC)
       si.UP=0
 
#con = fdb.connect(dsn='C:/Users/dtdav/Desktop/NONGOMA.GDB', user='SYSDBA', password='masterkey')
con = fdb.connect(dsn='C:/Users/Dan/Desktop/20180219/NONGOMA.GDB', user='SYSDBA', password='masterkey')

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select first 10 NC,SAME,STDATE,STOCKQ from STOCK WHERE SAME=0 ORDER BY SAME ")

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
    getName(si)
    getDisp(si)
    si.SOH=si.STOCKQ-si.DISP
    getUP(si)
    siList.append(si)

s=set(samesiList)
zList=[i for i in siList if i.SAME==0]

for x in zList:        
    total=x.SOH*x.UP
    GT += total
    print(x.MN+" TOTAL QUANTITY = "+str(x.SOH)+" "+ str(x.UP)+" TOTAL PRICE = " +str(total))    
    print("_____________________")

    
#s.remove(0)
for x in s:
    print("x in s -- "+str(x))
    getSame(siList,x)



















    



    