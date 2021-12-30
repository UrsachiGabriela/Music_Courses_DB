from src.backend.connection import DBConnection
from src.backend.transactions import Transaction

if __name__=='__main__':
     sql_command = f"""          
        BEGIN    
            delete from  profesori where id_profesor=1022;
            delete from  profesori where id_profesor=2423;    
        END;
        """
     with DBConnection('bd078','gabiu711',1539,'bd-dc.cs.tuiasi.ro','orcl') as connection:
          #response=connection.fetch_data(sql_command)
          # response=connection.exec_cmd(sql_command)
          # print(response)
          # # c=0
          # for row in response:
          #      print(row)
          # print(int(r[0][0]))

          r=Transaction.registerToCourse(connection,'20-jun-1998',7,2)
          print(r)

