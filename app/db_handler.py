import sqlite3
import sys
import _property
from sqlite3 import Error

# https://www.daleseo.com/python-sqlite3/

APP_DB = _property.APP_DB_PATH
LOG_DB = './log.db'
MEM_DB = ':memory:'


class DB_HANDLER:
    def __init__(self, db_name=APP_DB):
        self.db_name = db_name

    def set_tb_for_test(self, tb_name, create_query, insert_query, value_list):
        self.drop_tb(tb_name, "DROP TABLE {};".format(tb_name))
        self.create_tb(tb_name, create_query)
        self.insert_tb(tb_name, insert_query, value_list)
        self.select_tb(tb_name,"select * from {};".format(tb_name))

    def drop_tb(self, tb_name, query):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(query)  # ex) "CREATE TABLE PhoneBook(Name text, PhoneNum text);"
            print("\033[92m[{}] {} : Success".format(tb_name, sys._getframe().f_code.co_name))
        except Exception as e:
            print("\033[91m[{}] {} : error ({})".format(tb_name, sys._getframe().f_code.co_name, e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()


    def create_tb(self, tb_name, query):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(query)  # ex) "CREATE TABLE PhoneBook(Name text, PhoneNum text);"
            print("\033[92m[{}] {} : Success".format(tb_name, sys._getframe().f_code.co_name))
        except Exception as e:
            print("\033[91m[{}] {} : error ({})".format(tb_name, sys._getframe().f_code.co_name, e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    def select_tb(self, tb_name, query):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(query)  # ex) 'SELECT * FROM PhoneBook'
            #print('========================= [select data] ========================= ')
            data=cur.fetchall()
            # for row in data:
            #     print(row)
            #print('========================= [select data] ========================= ')
            print("\033[92m[{}] {} : Success".format(tb_name, sys._getframe().f_code.co_name))
        except Exception as e:
            print("\033[91m[{}] {} : error ({})".format(tb_name, sys._getframe().f_code.co_name, e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
            return data

    def update_tb(self, tb_name, query):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(query)  # ex) "UPDATE '210227_test' SET name = ? WHERE id_num = ?", ('YB_수정', 4)
            con.commit()
            print("\033[92m[{}] {} : Success".format(tb_name, sys._getframe().f_code.co_name))
        except Exception as e:
            print("\033[91m[{}] {} : error ({})".format(tb_name, sys._getframe().f_code.co_name, e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    def insert_tb(self, tb_name, query, value_list):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.executemany(query, value_list)  # ex) "INSERT INTO PhoneBook Values('Derick', '010-1234-5678');"
            con.commit()
            print("\033[92m[{}] {} : Success".format(tb_name, sys._getframe().f_code.co_name))
        except Exception as e:
            print("\033[91m[{}] {} : error ({})".format(tb_name, sys._getframe().f_code.co_name, e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

