""" File for all operations performed under GPM."""

import sqlite3
import re


class GramPanchayatMember:
    try_left = 3

    def __init__(self, connection):
        # sqlite3 connection
        self.conn = connection

        # logged in gpm id
        self.gpm_id = None

        # regular expression for validating email
        self.regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        # list of states
        self.state_list = ['andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chattisgarh', 'goa', 'gujarat',
                           'haryana', 'himachal pradesh', 'jharkhand', 'karnataka', 'kerala', 'madhya pradesh',
                           'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'punjab',
                           'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand',
                           'west bengal']

    def gpm_main_menu(self, email):
        """
        Display all features a GPM is allowed to do.
        :param email: email of logged in GPM
        :return: True
        """
        print("\nGram Panchayat Member\nWELCOMES -> {}".format(email))
        print("\n### GPM MENU ###\n1. Members\n2. Issue Job card\n3. Work allotment\n4. Work allotment List"
              "\n5. Complaints filed\n6. Logout")
        choice = input("Choice: ")

        if choice == '1':
            self.gpm_members_menu()
        elif choice == '2':
            self.gpm_job_card()
        elif choice == '3':
            self.gpm_work_allotment()
        elif choice == '4':
            self.request_list()
        elif choice == '5':
            self.complaints_filed()
        elif choice == '6':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '6':
            self.gpm_main_menu(email)

        return True

    def gpm_members_menu(self):
        """
        Display CRUD operations for member to GPM.
        :return: True
        """
        print("\n### MEMBERS MENU ###\n1. Add Member\n2. Update Member\n3. Remove Member\n4. Show Members\n5. GO Back")
        choice = input("Choice: ")

        if choice == '1':
            self.add_member()
        elif choice == '2':
            self.update_member()
        elif choice == '3':
            self.delete_member()
        elif choice == '4':
            self.show_members()
        elif choice == '5':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '5':
            self.gpm_members_menu()
        return True

    def add_member(self):
        """
        Fetch member details from user.
        :return: True/False
        """
        print("\nAdd Member\n----------")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        email = input("Email: ").lower()
        age = input("Age: ")
        gender = input("Gender (M/F): ").upper()
        state = input("State: ")
        address = input("Address: ")
        pincode = input("Pincode: ")
        place = input("Place: ")

        if re.search(self.regex, email):
            if self.add_member_action(fname, lname, email, age, gender, state, address, pincode, place):
                return True
        else:
            print("\nInvalid email.")
        return False

    def add_member_action(self, fname, lname, email, age, gender, state, address, pincode, place):
        """ Add member with the given data.

        :param fname: first name of member
        :param lname: last name of member
        :param email: email of member
        :param age: age of member
        :param gender: gender of member
        :param state: state of member
        :param address: address of member
        :param pincode: pincode of member
        :param place: place of member
        :return: True/False
        """
        try:
            result = self.conn.execute("SELECT count(*) from members WHERE lower(email)='{}'".format(email))
            if result.fetchone()[0] < 1:
                if state.lower() in self.state_list:
                    if gender == 'M' or gender == 'F':
                        self.conn.execute("INSERT INTO members(GPM_ID,FNAME,LNAME,EMAIL,AGE,GENDER,STATE,ADDRESS, \
                                          PINCODE,PLACE) VALUES({},'{}','{}','{}',{},'{}','{}','{}',{},'{}')"
                                          .format(self.gpm_id, fname, lname, email, age, gender, state, address,
                                                  pincode, place))
                        self.conn.commit()
                        print("\n'{}' added as Member".format(fname))
                        return True
                    else:
                        print("\nInvalid gender type.")
                else:
                    print("\n'{}' is not a state.".format(state))
            else:
                print("\n'{}' already exists.\nTry again with new Email".format(email))
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
        return False

    def update_member(self):
        """ Fetch record of member who comes under the logged in GPM w.r.t. member email.

        :return: True/False
        """
        print("\nUpdate Member\n-------------")
        email = input("Enter email: ").lower()

        try:
            member = self.conn.execute("SELECT * from members WHERE lower(email)='{}' AND gpm_id={}"
                                       .format(email, self.gpm_id))
            member = member.fetchone()
            if member is None:
                print("\nNo matching record found with '{}'.".format(email))
            else:
                print("\nEnter new details for '{}'\n(Press ENTER to skip the change in value.)".format(email))
                fname = input("First Name: ") or member[2]
                lname = input("Last Name: ") or member[3]
                new_email = input("Email: ").lower() or member[9]
                age = input("Age: ") or member[4]
                gender = input("Gender (M/F): ").upper() or member[5]
                state = input("State: ") or member[6]
                address = input("Address: ") or member[7]
                pincode = input("Pincode: ") or member[8]
                place = input("Place: ") or member[11]

                if self.update_member_action(fname, lname, new_email, age, gender, state, address, pincode, place,
                                             member[0]):
                    return True

        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def update_member_action(self, fname, lname, email, age, gender, state, address, pincode, place, member_id):
        """ Update data of member w.r.t. member id.

        :param fname: first name of member
        :param lname: last name of member
        :param email: email of member
        :param age: age of member
        :param gender: gender of member
        :param state: state of member
        :param address: address of member
        :param pincode: pincode of member
        :param place: place of member
        :param member_id: id of member
        :return: True/False
        """
        try:
            if re.search(self.regex, email):
                result = self.conn.execute("SELECT count(*) from members WHERE lower(email)='{}' AND id!={}"
                                           .format(email, member_id))
                if result.fetchone()[0] < 1:
                    if state.lower() in self.state_list:
                        if gender == 'M' or gender == 'F':
                            self.conn.execute("UPDATE members SET FNAME='{}',LNAME='{}',EMAIL='{}',STATE='{}',\
                                              ADDRESS='{}',PINCODE={},AGE={},GENDER='{}',PLACE='{}' WHERE ID={}"
                                              .format(fname, lname, email, state, address, pincode, age, gender, place,
                                                      member_id))
                            self.conn.commit()
                            print("\nRecord Updated.")
                            return True
                        else:
                            print("\nInvalid gender type.")
                    else:
                        print("\n'{}' is not a state.".format(state))
                else:
                    print("\n'{}' already exists.\nTry again with new Email".format(email))
            else:
                print("\nInvalid email.")
        except sqlite3.Error as e:
            print("\n", type(e), ": ", e)

        return False

    def delete_member(self):
        """
        Delete member comes under the logged in GPM.
        :return: True/False
        """
        print("\nDelete Member\n-------------")
        email = input("Enter email: ").lower()

        try:
            result = self.conn.execute("SELECT * from members WHERE lower(email)='{}' AND gpm_id={}"
                                       .format(email, self.gpm_id))
            if result.fetchone() is not None:
                ch = input("Want to delete '{}' (y/n): ".format(email))
                if ch == 'y' or ch == 'Y':
                    self.conn.execute("DELETE from members WHERE lower(email)='{}'".format(email))
                    self.conn.commit()
                    print("\nRecord deleted.")
                    return True
                else:
                    print("\nAction aborted!")
            else:
                print("\nNo record found with '{}'".format(email))
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def show_members(self):
        """
        Display all members comes under the logged in GPM.
        :return: True/False
        """
        try:
            result = self.conn.execute("SELECT * FROM members WHERE gpm_id={}".format(self.gpm_id))
            result = result.fetchall()
            if len(result) > 0:
                print("\nMEMBERS LIST\n------------")
                print("\nFNAME\tLNAME\tAGE\tGENDER\tPLACE\tEMAIL\tSTATE\tADDRESS\tPINCODE\tDAYS_WORKED\tWAGE")
                print("-----\t-----\t---\t------\t-----\t-----\t-----\t-------\t-------\t-----------\t----")
                for row in result:
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}"
                          .format(row[2], row[3], row[4], row[5], row[11], row[9], row[6], row[7], row[8], row[12],
                                  row[13]))
                return True
            else:
                print("\nNo data found.")
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def gpm_job_card(self):
        """
        Issue job card of the member.
        :return: True/False
        """
        print("\nISSUE JOB CARD\n--------------")
        email = input("Enter member's email: ").lower()

        try:
            result = self.conn.execute("SELECT * from members WHERE lower(email)='{}' AND gpm_id={}"
                                       .format(email, self.gpm_id))
            result = result.fetchone()
            if result is not None:
                print("\nJob card issued.")
                print("\nName\tAge\tGender\tPlace\tAddress\n----\t---\t------\t-----\t-------\n{} {}\t{}\t{}\t{}\t{}"
                      .format(result[2], result[3], result[4], result[5], result[11], result[7]))
                return True
            else:
                print("\nMember Not Found.")
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def gpm_work_allotment(self):
        """ Fetch member's email and project name.

        :return: True/False
        """
        print("\nWORK ALLOTMENT\n--------------")
        email = input("Enter member's email: ").lower()
        project_name = input("Enter project name: ").lower()

        try:
            member_result = self.conn.execute("SELECT * from members WHERE lower(email)='{}'".format(email))
            project_result = self.conn.execute("SELECT * from projects WHERE lower(name)='{}'".format(project_name))

            member_result = member_result.fetchone()
            project_result = project_result.fetchone()

            if member_result is not None:
                if project_result is not None:
                    choice = input("Add '{}' in project - '{}' (y/n): ".format(email, project_name))
                    if choice == 'Y' or choice == 'y':
                        if self.work_allotment_action(project_result, member_result):
                            return True
                    else:
                        print("\nAction aborted!")
                else:
                    print("\nNo Project match with '{}'".format(project_name))
            else:
                print("\nNo Email match with '{}'".format(email))

        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def work_allotment_action(self, project_result, member_result):
        """ Issuing project to member.

        :param project_result: project detail of a project
        :param member_result: member detail of a member
        :return: True/False
        """
        res = self.conn.execute("SELECT * from project_members WHERE project_id={} AND member_id={}"
                                .format(project_result[0], member_result[0]))
        res = res.fetchone()

        res2 = self.conn.execute("SELECT * from project_members WHERE member_id={}"
                                 .format(member_result[0]))
        res2 = res2.fetchone()
        if res is None:
            if res2 is None:
                self.conn.execute("INSERT INTO project_members(PROJECT_ID,MEMBER_ID,STATUS) VALUES({},{},{})"
                                  .format(project_result[0], member_result[0], 2))
            else:
                self.conn.execute("UPDATE project_members SET project_id ={},status={} WHERE member_id={}"
                                  .format(project_result[0], 2, member_result[0]))
            self.conn.commit()
            print("\nRequest generated for adding '{} {}' in '{}'."
                  .format(member_result[2], member_result[3], project_result[1]))
            return True
        else:
            print("\nMember already associated with this project.")

        return False

    def request_list(self):
        """
        Display list of all members assigned to the projects with their approval status.
        :return: True/False
        """
        try:
            c = self.conn.cursor()
            result = c.execute("SELECT project_members.status,members.fname,members.lname,projects.name \
                                from project_members \
                                JOIN members ON project_members.member_id=members.id \
                                JOIN projects ON project_members.project_id=projects.id")
            result = result.fetchall()
            if len(result) > 0:
                print("\nPROJECT REQUEST LIST\n------------")
                print("\nMEMBER NAME\tPROJECT NAME\tSTATUS")
                print("-----------\t------------\t------")
                for row in result:
                    status = "REJECT" if (row[0] == 0) else "APPROVED" if (row[0] == 1) else "PENDING"
                    print("{} {}\t\t{}\t\t{}".format(row[1], row[2], row[3], status))
                    return True
            else:
                print("\nNo pending request(s).")
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def complaints_filed(self):
        """
        Display all complaints filed by the members under logged in GPM.
        :return: True/False
        """
        try:
            c = self.conn.cursor()
            c.execute("SELECT complaints.subject,complaints.complaint,members.fname,members.lname \
                        from complaints \
                        INNER JOIN members ON complaints.member_id=members.id \
                        WHERE members.gpm_id={}".format(self.gpm_id))

            result = c.fetchall()
            if len(result) > 0:
                print("\nCOMPLAINTS LIST\n---------------")
                print("\nSUBJECT\tCOMPLAINT\tFILED BY")
                print("-------\t---------\t--------")
                for row in result:
                    print("{}\t\t{}\t\t{} {}".format(row[0], row[1], row[2], row[3]))
                return True
            else:
                print("\nNo complaint(s) filed.")
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
        return False

    def login_gpm(self):
        """
        Check if user(gram panchayat member) exists in record with given password or if it's the first time user is
        login then setup the password for that user.
        :return: True/False
        """
        if not self.try_left < 1:
            print("\n~~~ LOGIN as GPM ~~~")
            email = input("Enter email: ").lower()

            try:
                result = self.conn.execute("SELECT * FROM gpm where lower(email)='{}'".format(email))
                result = result.fetchone()
                if result is not None:
                    if result[8] is not None:
                        password = input("Enter password: ")

                        cursor = self.conn.execute("SELECT * FROM gpm where lower(email)='{}' AND password='{}'"
                                                   .format(email, password))
                        cursor = cursor.fetchone()
                        if cursor is None:
                            print("\nName & Password does not match!")
                            self.try_left -= 1
                            print("{} attempts left!\n".format(self.try_left))
                            self.login_gpm()
                        else:
                            self.gpm_id = cursor[0]
                            self.gpm_main_menu(email)
                            return True
                    else:
                        print("\nSetup Password\n--------------")
                        pswd = input("New password: ")
                        pswd2 = input("Repeat password: ")

                        if pswd == pswd2:
                            if len(pswd) > 0:
                                self.conn.execute("UPDATE gpm SET password='{}' WHERE lower(email)='{}'".format(pswd,
                                                                                                                email))
                                self.conn.commit()
                                print("\nPassword successfully set.")
                                self.gpm_id = result[0]
                                self.gpm_main_menu(email)
                                return True
                            else:
                                print("\nPassword cannot be empty.")
                        else:
                            print("\nPassword does not match.")
                else:
                    print("\nEmail does not found.")
            except sqlite3.Error as e:
                print(type(e).__name__, ": ", e)
        else:
            print("Too much Wrong Attempts!")

        return False
