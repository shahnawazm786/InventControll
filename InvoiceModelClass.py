class InvoiceModel:
    def __init__(self):
        self.Inv_Id=0
        self.Item_Id=0
        self.Cust_Id=0
        self.Qty=0
    @property
    def InvID(self):
        return self.Inv_Id
    @InvID.setter
    def InvID(self,_inv):
        self.Inv_Id=_inv
    @property
    def ItemID(self):
        return  self.Item_Id
    @ItemID.setter
    def ItemID(self,_itemid):
        self.Item_Id=_itemid