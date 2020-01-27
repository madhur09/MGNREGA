""" File for all operations performed under Members."""

import sqlite3


class Member:
    try_left = 3

    def __init__(self, connection):
        # sqlite3 connection
        self.conn = connection

        # logged in member id
        self.member_id = None

    def member_main_menu(self, email):
        """
        Display all features a member is allowed to do.
        :param email:
        :return: True
        """
        print("\nMember\nWELCOMES -> {}".format(email))
        print("\n### Member MENU ###\n1. View Details\n2. Raise Complaint\n3. Logout")
        choice = input("Choice: ")

        if choice == '1':
            self.member_details()
        elif choice == '2':
            self.raise_complaint_menu()
        elif choice == '3':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '3':
            self.member_main_menu(email)

        return True

    def member_details(self):
        """ Display complete details of logged in member.

        :return: True/ False
        """
        try:
            result = self.conn.execute("SELECT * FROM members WHERE id={}".format(self.member_id))
            row = result.fetchone()
            if len(row) > 0:
                print("\nDETAILS\n-------")
                print("\nFNAME\tLNAME\tAGE\tGENDER\tPLACE\tEMAIL\tSTATE\tADDRESS\tPINCODE\tDAYS_WORKED"
                      "\tWAGE\tWAGE STATUS")
                print("-----\t-----\t---\t------\t-----\t-----\t-----\t-------\t-------\t-----------"
                      "\t----\t-----------")

                status = "REJECT" if (row[14] == 0) else "APPROVED" if (row[14] == 1) else "PENDING"
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}"
                      .format(row[2], row[3], row[4], row[5], row[11], row[9], row[6], row[7], row[8], row[12],
                              row[13], status))
            else:
                print("\nNo records to display.")

            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
            return False

    def raise_complaint_menu(self):
        """
        Display menu for complaints to member.
        :return: True
        """
        print("\n%%% RAISE COMPLAINT MENU %%%")
        print("1. File complaint\n2. See complaint(s) status\n3. Go Back")
        choice = input("Enter choice: ")

        if choice == '1':
            self.file_complaint()
        elif choice == '2':
            self.show_member_complaints()
        elif choice == '3':
            print("")
        else:
            print("\nWrong Input!  Try again.")

        if choice != '3':
            self.raise_complaint_menu()

        return True

    def file_complaint(self):
        """
        Raise the complaint by the member by inserting value in complaints table.
        :return: True/False
        """
        print("\nRAISE A COMPLAINT\n-----------------")
        subject = input("Subject: ")
        complaint = input("Complaint: ")

        try:
            self.conn.execute("INSERT INTO complaints(MEMBER_ID,SUBJECT,COMPLAINT,STATUS) VALUES({},'{}','{}',{})"
                              .format(self.member_id, subject, complaint, 2))
            self.conn.commit()
            print("\nComplaint raised.")
            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
            return False

    def show_member_complaints(self):
        """
        Display List of complaints raise by the member itself.
        :return: True/False
        """
        try:
            result = self.conn.execute("SELECT * from complaints WHERE member_id={}".format(self.member_id))
            result = result.fetchall()
            if len(result) > 0:
                print("\nCOMPLAINTS LIST\n---------------")
                print("\nSUBJECT\tCOMPLAINT")
                print("-------\t---------")
                for row in result:
                    print("{}\t\t{}".format(row[2], row[3]))
            else:
                print("\nNo complaint(s) filed.")
            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
        return False

    def validate_login(self, email):
        """ Validate email and password entered by the user from backend.

        :param email: email entered by the user
        :return: True/False
        """
        password = input("Enter password: ")

        cursor = self.conn.execute("SELECT * FROM members where lower(email)='{}' AND password='{}'"
                                   .format(email, password))
        cursor = cursor.fetchone()
        if cursor is None:
            print("\nName & Password does not match!")
            self.try_left -= 1
            print("{} attempts left!\n".format(self.try_left))
            self.login_member()
            return False
        else:
            self.member_id = cursor[0]
            self.member_main_menu(email)
            return True

    def setup_password(self, email, result):
        """Stores the password for member when it is logging for the first time.

        :param email: email entered by the user as member
        :param result: data of member for corresponding email
        :return: True/False
        """
        print("\nSetup Password\n--------------")
        pswd = input("New password: ")
        pswd2 = input("Repeat password: ")

        if pswd == pswd2:
            if len(pswd) > 0:
                self.conn.execute("UPDATE members SET password='{}' WHERE lower(email)='{}'"
                                  .format(pswd, email))
                self.conn.commit()
                print("\nPassword successfully set.")
                self.member_id = result[0]
                self.member_main_menu(email)
                return True
            else:
                print("\nPassword cannot be empty.")
        else:
            print("\nPassword does not match.")

        return False

    def login_member(self):
        """
        Check if user(member/labour) exists in record with given password or if it's the first time user is login then
        setup the password for that user.
        :return: True/False
        """
        if not self.try_left < 1:
            print("\n~~~ LOGIN as Member ~~~")
            email = input("Enter email: ").lower()

            try:
                result = self.conn.execute("SELECT * FROM members where lower(email)='{}'".format(email))
                result = result.fetchone()
                if result is not None:
                    if result[10] is not None:
                        if self.validate_login(email):
                            return True
                    else:
                        if self.setup_password(email, result):
                            return True
                else:
                    print("\nEmail does not found.")
            except sqlite3.Error as e:
                print(type(e).__name__, ": ", e)
        else:
            print("Too much Wrong Attempts!")

        return False
