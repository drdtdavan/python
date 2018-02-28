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
    ls=(i for i in siL if i.SAME==s)
    for x in ls:
        print("getSame"+ x.MN+" "+x.NC+" "+str(x.SAME)+str(x.UP))
    soh=sum(i.SOH for i in ls) 
    up=max(for i in ls)  
    print("getSame TOTAL QUANTITY = "+str(soh)+ " TOTAL PRICE = " +str(soh*up))
    for i in ls:
        print(i.MN+"\t"+i.SOH)    
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
cur.execute("select first 10 NC,SAME,STDATE,STOCKQ from STOCK WHERE SAME!=0 ORDER BY SAME ")

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
#s.remove(0)
for x in s:
    print("x in s -- "+str(x))
    getSame(siList,x)



















    



    