class CustomerModel:
    def __init__(self):
        self.Cust_ID=0
        self.Cust_Name=None
        self.Cust_Address=None
        self.Cust_City=None
    @property
    def ID(self):
        return self.Cust_ID
    @ID.setter
    def ID(self,_id):
        self.Cust_ID=_id
    @property
    def Name(self):
        return self.Cust_Name
    @Name.setter
    def Name(self,_nm):
        self.Cust_Name=_nm
    @property
    def Address(self):
        return  self.Cust_Address
    @Address.setter
    def Address(self,_addr):
        self.Cust_Address=_addr
    @property
    def City(self):
        return self.Cust_City
    @City.setter
    def City(self,_city):
        self.Cust_City=_city
