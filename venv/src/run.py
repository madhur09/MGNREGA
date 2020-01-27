""" Initial file for stating the project."""

from block_development_officer import BlockDevelopmentOfficer
from gram_panchayat_member import GramPanchayatMember
from member import Member
from schema import Schema

import sqlite3


def sql_connection():
    """
    Setup connection with sqlite3 backend.
    :return: sqlite3 connection object
    """
    return sqlite3.connect('database.db')


class Run:

    def __init__(self, connection):
        self.conn = connection

    def login_menu(self):
        """ Display Login options for users to choose.

        :return: True
        """
        print("\n**** LOGIN MENU ****")
        print("1. Login as BDO \n2. Login as GPM \n3. Login as Member\n4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            BlockDevelopmentOfficer(self.conn).login_bdo()
        elif choice == '2':
            GramPanchayatMember(self.conn).login_gpm()
        elif choice == '3':
            Member(self.conn).login_member()
        elif choice == '4':
            print("\nExiting...")
            self.conn.close()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '4':
            self.login_menu()

        return True


def main():
    """

    :return: True/False
    """
    try:
        conn = sql_connection()

        if conn is None:
            print("Error while connecting with database")
            print("Retry after sometime!!!")
        else:
            Schema(conn).setup_admin()
            Schema(conn).create_tables()
            Run(conn).login_menu()
            conn.close()
            return True
    except sqlite3.Error as e:
        print(type(e), ": ", e)

    return False


if __name__ == "__main__":
    main()
