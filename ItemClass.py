class Items:
    def __init__(self):
        self.Id=0
        self.Name=None
        self.Description=None
        self.PurPrice=0.0
        self.Qty=0
    @property
    def ID(self):
        return self.Id
    @ID.setter
    def ID(self,_id):
        self.Id=_id

    @property
    def name(self):
        return self.Name
    @name.setter
    def name(self, _nm):
        self.Name=_nm
    @property
    def desc(self):
        return self.Description
    @desc.setter
    def desc(self,_desc):
        self.Description=_desc
    @property
    def pur(self):
         return self.PurPrice
    @pur.setter
    def pur(self,_pur):
         self.PurPrice=_pur
    @property
    def qty(self):
        return self.Qty
    @qty.setter
    def qty(self,_qty):
        self.Qty=_qty