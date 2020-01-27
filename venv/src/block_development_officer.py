""" File for all operations performed under BDO."""

from datetime import datetime, date

import sqlite3
import re


class BlockDevelopmentOfficer:
    try_left = 3

    def __init__(self, connection):
        # sqlite3 connection
        self.conn = connection

        # logged in BDO id
        self.bdo_id = None

        # regular expression for validating email
        self.regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        # list of states
        self.state_list = ['andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chattisgarh', 'goa', 'gujarat',
                           'haryana', 'himachal pradesh', 'jharkhand', 'karnataka', 'kerala', 'madhya pradesh',
                           'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'punjab',
                           'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand',
                           'west bengal']

        # list of types of project
        self.project_type = ['road construction', 'sewage treatment', 'building construction']

    def bdo_main_menu(self, email):
        """
        Display all features a BDO is allowed to perform.
        :param email: email of logged in BDO
        :return: True
        """
        print("\nBlock Development Officer\nWELCOMES -> {}".format(email))
        print("\n### BDO MENU ###\n1. Gram Panchayat Member\n2. Projects\n3. Pending project requests\n"
              "4. Pending wage requests\n5. Complaints filed\n6. Logout")
        choice = input("Choice: ")

        if choice == '1':
            self.bdo_gpm_menu()
        elif choice == '2':
            self.bdo_project_menu()
        elif choice == '3':
            self.bdo_project_approval_requests()
        elif choice == '4':
            self.bdo_wage_approval_requests()
        elif choice == '5':
            self.complaints_filed()
        elif choice == '6':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '6':
            self.bdo_main_menu(email)

        return True

    def bdo_gpm_menu(self):
        """
        CRUD operations for GPM.
        :return: True
        """
        print("\n### GRAM PANCHAYAT MENU ###\n1. Add GPM\n2. Update GPM\n3. Remove GPM\n4. Show all GPM\n5. GO Back")
        choice = input("Choice: ")

        if choice == '1':
            self.add_gpm()
        elif choice == '2':
            self.update_gpm()
        elif choice == '3':
            self.delete_gpm()
        elif choice == '4':
            self.show_gpm()
        elif choice == '5':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '5':
            self.bdo_gpm_menu()

        return True

    def add_gpm(self):
        """
        Add GPM under logged in BDO.
        :return: True/False
        """
        print("\nAdding GPM")
        print("----------")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        email = input("Email: ").lower()
        state = input("State: ")
        address = input("Address: ")
        pincode = input("Pincode: ")

        if re.search(self.regex, email):
            try:
                result = self.conn.execute("SELECT count(*) from gpm WHERE lower(email)='{}'".format(email))
                if result.fetchone()[0] < 1:
                    if state.lower() in self.state_list:
                        self.conn.execute("INSERT INTO gpm(BDO_ID,FNAME,LNAME,EMAIL,STATE,ADDRESS,PINCODE)  \
                                          VALUES('{}','{}','{}','{}','{}','{}',{})"
                                          .format(self.bdo_id, fname, lname, email, state, address, pincode))
                        self.conn.commit()
                        print("\n'{}' added as GPM".format(fname))
                        return True
                    else:
                        print("\n'{}' is not a state.".format(state))
                else:
                    print("\n'{}' already exists.\nTry again with new Email".format(email))
            except sqlite3.Error as e:
                print(type(e).__name__, ": ", e)
        else:
            print("\nInvalid email.")

        return False

    def update_gpm(self):
        """
        Get the updated data of GPM falls under logged in BDO only.
        :return: True/False
        """
        print("\nUpdating GPM")
        print("-----------")
        email = input("Enter email: ").lower()

        try:
            gpm = self.conn.execute("SELECT * from gpm WHERE lower(email)='{}' AND bdo_id={}"
                                    .format(email, self.bdo_id))
            gpm = gpm.fetchone()
            if gpm is None:
                print("\nNo matching record found with '{}'.".format(email))
            else:
                print("\nEnter new details for '{}'\n(Press ENTER to skip the change in value.)\n".format(email))
                fname = input("First Name: ") or gpm[2]
                lname = input("Last Name: ") or gpm[3]
                new_email = input("Email: ").lower() or gpm[7]
                state = input("State: ") or gpm[4]
                address = input("Address: ") or gpm[5]
                pincode = input("Pincode: ") or gpm[6]

                if self.update_gpm_with_details(fname, lname, new_email, state, address, pincode, gpm[0]):
                    return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def update_gpm_with_details(self, fname, lname, email, state, address, pincode, gpm_id):
        """ Update the GPM record.

        :param fname: first name of gpm
        :param lname: last name of gpm
        :param email: email of gpm
        :param state: state of gpm
        :param address: address of gpm
        :param pincode: pincode of gpm
        :param gpm_id: id of gpm
        :return: True/False
        """
        try:
            if re.search(self.regex, email):
                result = self.conn.execute("SELECT count(*) from gpm WHERE lower(email)='{}' AND id!={}"
                                           .format(email, gpm_id))
                if result.fetchone()[0] < 1:
                    if state.lower() in self.state_list:
                        self.conn.execute("UPDATE gpm SET FNAME='{}',LNAME='{}',EMAIL='{}',STATE='{}',ADDRESS='{}' \
                                              ,PINCODE={} WHERE ID={}".format(fname, lname, email, state,
                                                                              address, pincode, gpm_id))
                        self.conn.commit()
                        print("\nRecord Updated.")
                        return True
                    else:
                        print("\n'{}' is not a state.".format(state))
                else:
                    print("\n'{}' already exists.\nTry again with new Email".format(email))
            else:
                print("\nInvalid Email.")
        except sqlite3.Error as e:
            print(type(e), ": ", e)

        return False

    def delete_gpm(self):
        """
        Delete GPM falls under logged in BDO only.
        :return: True/False
        """
        print("\nDelete GPM")
        print("----------")
        email = input("Enter email: ").lower()

        try:
            result = self.conn.execute("SELECT * from gpm WHERE lower(email)='{}' AND bdo_id={}"
                                       .format(email, self.bdo_id))
            if result.fetchone():
                ch = input("Want to delete '{}' (y/n): ".format(email))
                if ch == 'y' or ch == 'Y':
                    self.conn.execute("DELETE from gpm WHERE lower(email)='{}'".format(email))
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

    def show_gpm(self):
        """
        Display all GPMs list falls under logged in BDO only.
        :return: True
        """
        try:
            result = self.conn.execute("SELECT * FROM gpm WHERE bdo_id={}".format(self.bdo_id))
            result = result.fetchall()
            if len(result) > 0:
                print("\nGRAM PANCHAYAT MEMBERS LIST")
                print("---------------------------")
                print("\nFNAME\tLNAME\tEMAIL\tSTATE\tADDRESS\tPINCODE")
                print("-----\t-----\t-----\t-----\t-------\t-------")
                for row in result:
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(row[2], row[3], row[7], row[4], row[5], row[6]))
            else:
                print("\nNo data found.")
            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)
        return False

    def bdo_project_menu(self):
        """
        CRUD operation menu for project.
        :return: True
        """
        print("\n### PROJECT MENU ###\n1. Add project\n2. Update project\n3. Remove project\n4. Show Projects "
              "\n5. GO Back")
        choice = input("Choice: ")

        if choice == '1':
            self.add_project()
        elif choice == '2':
            self.update_project()
        elif choice == '3':
            self.delete_project()
        elif choice == '4':
            self.show_projects()
        elif choice == '5':
            print()
        else:
            print("\nWrong Input!  Try again.")

        if choice != '5':
            self.bdo_project_menu()

        return True

    def add_project(self):
        """
        Fetches values for project.
        :return: True/False
        """
        print("\nAdding Project")
        print("--------------")
        project_name = input("Project Name: ").lower()
        print("Project type: ", self.project_type)
        project_type = input("Enter type: ")
        state = input("State: ")
        members_req = input("Members req.: ")
        cost_est = input("Cost est.: ")
        start_date_est = input("Start date est. (DD-MM-YYYY): ")
        end_date_est = input("End date est. (DD-MM-YYYY): ")

        try:
            result = self.conn.execute("SELECT count(*) from projects WHERE lower(name)='{}'".format(project_name))
            if result.fetchone()[0] < 1:
                if project_type.lower() in self.project_type:
                    if state.lower() in self.state_list:
                        if self.add_project_action(project_name, project_type, state, members_req, cost_est,
                                                   start_date_est, end_date_est):
                            return True
                    else:
                        print("\n'{}' is not a state.".format(state))
                else:
                    print("\n'{}' is not from the given project type.".format(project_type))
            else:
                print("\nProject name - {} already exists.\nTry again with new Project Name".format(project_name))
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def add_project_action(self, project_name, project_type, state, members_req, cost_est, start_date_est,
                           end_date_est):
        """ Insert project with given values.

        :param project_name:  name of the project
        :param project_type: type of the project
        :param state: state name
        :param members_req: members requires in project
        :param cost_est: cost of the project
        :param start_date_est: start date of the project
        :param end_date_est: end date of the project
        :return: True/False
        """
        try:
            start_date_est_object = datetime.strptime(start_date_est, '%d-%m-%Y').date()
            end_date_est_object = datetime.strptime(end_date_est, '%d-%m-%Y').date()

            if end_date_est_object > start_date_est_object:
                self.conn.execute("INSERT INTO projects(NAME,TYPE,STATE,MEMBERS_REQ,COST_EST, \
                                  START_DATE_EST,END_DATE_EST) VALUES('{}','{}','{}',{},{},'{}','{}')"
                                  .format(project_name, project_type, state, members_req, cost_est,
                                          start_date_est, end_date_est))
                self.conn.commit()
                print("\n'{}' added as project".format(project_name))
                return True
            else:
                print("\nEnd date should be ahead of start date")
        except (ValueError, sqlite3.Error) as e:
            print('\n', type(e), ': ', e)
        return False

    def update_project(self):
        """ Fetch data for updating project.

        :return: True/False
        """
        print("\nUpdating project")
        print("---------------")
        project_name = input("Enter project name: ").lower()

        try:
            project = self.conn.execute("SELECT * from projects WHERE lower(name)='{}'".format(project_name))
            project = project.fetchone()
            if project is None:
                print("\nNo matching record found with '{}'.".format(project_name))
            else:
                print("\nEnter new details for '{}'\n(Press ENTER to skip the change in value.\n)".format(project_name))
                new_project_name = input("Project Name: ").lower() or project[1]
                print("Project type: ", self.project_type)
                project_type = input("Enter type: ") or project[2]
                state = input("State: ") or project[3]
                members_req = input("Members req.: ") or project[4]
                cost_est = input("Cost est.: ") or project[5]
                start_date_est = input("Start date est. (DD-MM-YYYY): ") or project[6]
                end_date_est = input("End date est. (DD-MM-YYYY): ") or project[7]

                result = self.conn.execute("SELECT count(*) from projects WHERE lower(name)='{}' and id!={}"
                                           .format(new_project_name, project[0]))
                if result.fetchone()[0] < 1:
                    if project_type.lower() in self.project_type:
                        if state.lower() in self.state_list:
                            if self.update_project_action(start_date_est, end_date_est, new_project_name, state,
                                                          members_req, cost_est, project[0]):
                                return True
                        else:
                            print("\n'{}' is not a state.".format(state))
                    else:
                        print("\n'{}' is not from the given project type.".format(project_type))
                else:
                    print("\nProject name - {} already exists.\nTry again with new Project Name"
                          .format(new_project_name))
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def update_project_action(self, start_date_est, end_date_est, project_name, state, members_req, cost_est,
                              project_id):
        """ Update project data with given values.

        :param start_date_est: start date of the project
        :param end_date_est: end date of the project
        :param project_name: project name
        :param state: state name
        :param members_req: members required in project
        :param cost_est: estimated cost of the project
        :param project_id: id of the project
        :return: True/False
        """
        try:
            start_date_est_object = datetime.strptime(start_date_est, '%d-%m-%Y').date()
            end_date_est_object = datetime.strptime(end_date_est, '%d-%m-%Y').date()

            if end_date_est_object > start_date_est_object:
                self.conn.execute("UPDATE projects SET NAME='{}',STATE='{}',MEMBERS_REQ={},COST_EST={},\
                                  START_DATE_EST='{}',END_DATE_EST='{}' WHERE ID={}"
                                  .format(project_name, state, members_req, cost_est,
                                          start_date_est, end_date_est, project_id))
                self.conn.commit()
                print("\nRecord Updated.")
                return True
            else:
                print("\nEnd date should be ahead of start date")
        except (ValueError, sqlite3.Error) as e:
            print(type(e), ": ", e)

        return False

    def delete_project(self):
        """
        Delete project.
        :return: True/False
        """
        print("\nDelete Project")
        print("--------------")
        project_name = input("Enter project name: ").lower()

        try:
            result = self.conn.execute("SELECT * from projects WHERE lower(name)='{}'".format(project_name))
            result = result.fetchone()
            if result is not None:
                ch = input("Want to delete '{}' (y/n): ".format(project_name))
                if ch == 'y' or ch == 'Y':
                    self.conn.execute("DELETE from projects WHERE lower(name)='{}'".format(project_name))
                    self.conn.commit()
                    print("\nRecord deleted.")

                    return True
                else:
                    print("\nAction aborted!")
            else:
                print("\nNo record found with '{}'".format(project_name))
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def show_projects(self):
        """
        Display list of all projects.
        :return: True/False
        """
        print("\nPROJECTS LIST\n-------------")
        print("\nNAME\tTYPE\tSTATE\tMEMBERS_REQ\tCOST_EST\tSTART_DATE_EST\tEND_DATE_EST")
        print("----\t----\t-----\t-----------\t--------\t--------------\t------------")
        try:
            result = self.conn.execute("SELECT * FROM projects")
            for row in result:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}"
                      .format(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def bdo_project_approval_requests(self):
        """
        Approve/reject requests for project allotment of members made by GPM.
        :return: True/False
        """
        try:
            c = self.conn.cursor()
            result = c.execute("SELECT project_members.id,gpm.fname,gpm.lname,members.fname,members.lname,projects.name\
                                from project_members \
                                JOIN members ON project_members.member_id=members.id \
                                JOIN projects ON project_members.project_id=projects.id \
                                JOIN gpm ON members.gpm_id=gpm.id \
                                WHERE project_members.status=2")
            result = result.fetchall()
            if len(result) > 0:
                print("\nPROJECT REQUEST LIST\n--------------------")
                print("\nS.NO.\tGPM NAME\tMEMBER NAME\tPROJECT NAME")
                print("-----\t--------\t-----------\t------------")
                ids_list = []
                for row in result:
                    print("{}\t{} {}\t{} {}\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
                    ids_list.append(str(row[0]))

                if self.project_approval_action(ids_list):
                    return True
            else:
                print("\nNo pending request(s).")
                return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def project_approval_action(self, ids_list):
        """ Accepting/Rejection project approval request.

        :param ids_list: approval request id
        :return: True/False
        """
        while True:
            print("\nEnter # to Go Back otherwise.")
            approval_id = input("Enter S.No.: ")
            if approval_id == '#':
                print("\nAction aborted.")
                break
            elif approval_id in ids_list:
                print("\nStatus: 1. Approved  0. Reject")
                new_status = input("Enter status: ")
                if new_status == '1' or new_status == '0':
                    try:
                        self.conn.execute("UPDATE project_members SET status={} WHERE ID={}"
                                          .format(new_status, approval_id))
                        self.conn.commit()

                        # fetching projectId, memberId w.r.t. approvalId
                        updated_result = self.conn.execute("SELECT * from project_members WHERE ID={}"
                                                           .format(approval_id))
                        updated_result = updated_result.fetchone()

                        self.calculate_wage(updated_result[1], updated_result[2])
                        print("\nRequest {}".format("Approved." if new_status == '1' else "Rejected"))

                        return True
                    except sqlite3.Error as e:
                        print(type(e), ": ", e)
                        break
                else:
                    print("\nInvalid Status code.")
                    break
            else:
                print("\nInvalid S.No.")
                break

        return False

    def calculate_wage(self, project_id, member_id):
        """
        Calculate Working days and wage of member.
        :param project_id: Project id
        :param member_id: member id
        :return: True/False
        """
        try:
            today = date.today().strftime("%d-%m-%Y")
            member_joining_date = datetime.strptime(today, '%d-%m-%Y').date()
            ending_date = self.conn.execute("SELECT end_date_est FROM projects WHERE id={}".format(project_id))
            ending_date = ending_date.fetchone()[0]
            project_ending_date = datetime.strptime(ending_date, '%d-%m-%Y').date()

            if self.update_wage(project_ending_date, member_joining_date, member_id):
                return True
        except (ValueError, sqlite3.Error) as e:
            print(type(e).__name__, ": ", e)

        return False

    def update_wage(self, project_ending_date, member_joining_date, member_id):
        """ Update's wage data for member.

        :param project_ending_date: ending date of project
        :param member_joining_date: joining date of member
        :param member_id: member id
        :return: True/False
        """
        try:
            if project_ending_date > member_joining_date:
                working_days = project_ending_date - member_joining_date
                wage = int(working_days.days) * 100.0

                self.conn.execute("UPDATE members SET DAYS_WORKED={},WAGE={},WAGE_STATUS={} WHERE id={}"
                                  .format(working_days.days, wage, 2, member_id))
                self.conn.commit()
                return True
            else:
                print("\nProject end date is ahead of member joining date in project")
        except (ValueError, sqlite3.Error) as e:
            print(type(e).__name__, ": ", e)

        return False

    def bdo_wage_approval_requests(self):
        """
        Approve/reject requests for wage approval of members made by GPM.
        :return: True/False
        """
        try:
            c = self.conn.cursor()
            result = c.execute("SELECT * from members WHERE wage_status=2")
            result = result.fetchall()
            if len(result) > 0:
                print("\nWAGE REQUEST LIST\n-----------------")
                print("\nS.NO.\tMEMBER NAME\t\tWAGE")
                print("-----\t-----------\t\t----")
                ids_list = []
                for row in result:
                    print("{}\t\t{} {}\t{}".format(row[0], row[2], row[3], row[13]))
                    ids_list.append(str(row[0]))

                if self.wage_approval_action(ids_list):
                    return True
            else:
                print("\nNo pending request(s).")
                return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def wage_approval_action(self, ids_list):
        """ Approve/Reject wage request.

        :param ids_list: wage request id
        :return: True/False
        """
        while True:
            print("\nEnter # to Go Back otherwise.")
            approval_id = input("Enter S.No.: ")
            if approval_id == '#':
                print("\nAction aborted.")
                break
            elif approval_id in ids_list:
                print("\nStatus: 1. Approved  0. Reject")
                new_status = input("Enter status: ")
                if new_status == '1' or new_status == '0':
                    self.conn.execute("UPDATE members SET wage_status={} WHERE ID={}"
                                      .format(new_status, approval_id))
                    self.conn.commit()
                    print("\nRequest {}".format("Approved." if new_status == '1' else "Rejected"))

                    return True
                else:
                    print("\nInvalid Status code.")
            else:
                print("\nInvalid S.No.")

            return False

    def complaints_filed(self):
        """
        Display all complaints filed by the members.
        :return: True/False
        """
        try:
            c = self.conn.cursor()
            c.execute("SELECT complaints.subject,complaints.complaint,members.fname,members.lname,gpm.fname,gpm.lname \
                        from complaints \
                        INNER JOIN members ON complaints.member_id=members.id \
                        INNER JOIN gpm ON members.gpm_id=gpm.id")

            result = c.fetchall()
            if len(result) > 0:
                print("\nCOMPLAINTS LIST\n---------------")
                print("\nSUBJECT\t\tCOMPLAINT\tFILED BY\tGPM NAME")
                print("-------\t\t---------\t--------\t--------")
                for row in result:
                    print("{}\t\t{}\t\t{} {}\t{} {}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            else:
                print("\nNo complaint(s) filed.")

            return True
        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

        return False

    def login_bdo(self):
        """
        Validate the email and password of the user(BDO).
        :return: True/False
        """
        if not self.try_left < 1:
            print("\n~~~ LOGIN as BDO ~~~")
            email = input("Enter email: ").lower()
            password = input("Enter password: ")

            try:
                cursor = self.conn.execute("SELECT * FROM bdo where lower(email)='{}' AND password='{}'"
                                           .format(email, password))
                cursor = cursor.fetchone()
                if cursor is None:
                    print("\nEmail & Password does not match!")
                    self.try_left -= 1
                    print("{} attempts left!\n".format(self.try_left))
                    self.login_bdo()
                else:
                    self.bdo_id = cursor[0]
                    self.bdo_main_menu(email)
                    return True
            except sqlite3.Error as e:
                print(type(e).__name__, ": ", e)
        else:
            print("Too much Wrong Attempts!")

        return False
