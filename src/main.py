from src.backend.connection import DBConnection



if __name__=='__main__':
     sql_command = f"""
                                     SELECT COUNT(*)  from fisa_inscriere
                                        
               """
     with DBConnection('bd078','gabiu711',1539,'bd-dc.cs.tuiasi.ro','orcl') as connection:
          response=connection.fetch_data(sql_command)

          c=0
          r=[row for row in response]
          print(int(r[0][0]))


