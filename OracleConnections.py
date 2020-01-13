import cx_Oracle as cx
def Ora_connections():
    try:
        cn=cx.connect('scott/tiger@localhost:1521/orcl')
        cur=cn.cursor()
        return cur,cn
    except:
        print('Errors')
