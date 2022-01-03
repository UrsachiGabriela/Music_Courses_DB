from src.backend.connection import DBConnection
from src.backend.transactions import Transaction
from src.frontend.application import App
from src.frontend.pages.BasePage import BasePage
import tkinter as tk

if __name__=='__main__':
     # sql_command = f"""
     #
     # SELECT * from cursuri
     # """

     with DBConnection('bd078','gabiu711',1539,'bd-dc.cs.tuiasi.ro','orcl') as connection:
          # response=connection.fetch_data(sql_command,[])
          #response=connection.exec_cmd(sql_command,[])
          #print(response)
          # r1=[row for row in response]
          # if r1:
          #      count1=int(r1[0][0])
          # else:
          #      count1=0
          #
          # print(count1)
          # # c=0
          # for row in r1:
          #      print(row)
          # print(int(r[0][0]))

          # r=Transaction.endCourse(connection,7)
          #print(r1)


          a=App(connection)
          a.mainloop()

