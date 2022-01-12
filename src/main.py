from src.backend.connection import DBConnection
from src.backend.transactions import Transaction
from src.frontend.application import App
from src.frontend.pages.BasePage import BasePage
import tkinter as tk

if __name__=='__main__':

     with DBConnection('bd078','gabiu711',1539,'bd-dc.cs.tuiasi.ro','orcl') as connection:

          a=App(connection)
          a.mainloop()


