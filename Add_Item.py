from InventControll.ItemClass import Items
from InventControll import OracleConnections
from InventControll.QueryStringClass import QueryString
class FactoryClass:
    def InsertRecord(self,Query_string,para):
        try:
            cur, cn = OracleConnections.Ora_connections()
            cur.execute(Query_string,para)
            cn.commit()
        except:
            print('Error in transaction')
    def UpdateRecoord(self,Query_string,para):
        try:
            cur, cn = OracleConnections.Ora_connections()
            cur.execute(Query_string,para)
            cn.commit()
        except:
            print('Error in transaction')
    def DeleteRecord(self,Query_string,para):
        try:
            cur, cn = OracleConnections.Ora_connections()
            cur.execute(Query_string,para)
            cn.commit()
        except:
            print('Error in transaction')
    def SearchRecord(self,Query_String,para):
        try:
            cur, cn = OracleConnections.Ora_connections()
            rec=cur.execute(Query_String,para)
            return rec
        except:
            print('Error in transaction')




def Add_Items():
    i=Items()
    i.ID=int(input('Enter ID'))
    i.Name=input('Enter name')
    i.Description=input('Enter Description')
    i.PurPrice=float(input('Purchase Price'))
    i.Qty=int(input('Quantity'))
    cur,cn= OracleConnections.Ora_connections()
    '''
    ins_data=
    insert into Item_Master (item_id,item_name,item_desc,pur_price,qty) 
    values(:itemid,:itemname,:itemdesc,:purprice,:qty)
    
    '''
    para={'itemid':i.ID,'itemname':i.Name,'itemdesc':i.Description,'purprice':i.PurPrice,'qty':i.Qty}
    cur.execute(QueryString.ins_data,para)
    cn.commit()

Add_Items()