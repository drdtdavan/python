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

Si1=StockItem()
Si1.SOH=5
Si2=StockItem()
Si2.SOH=2
Si3=StockItem()
Si3.SOH=3

ls=[Si1,Si2,Si3]

for x in ls:
    print(x.SOH)

for x in ls:
    print(x.SOH)
