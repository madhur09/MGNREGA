import mock
import sqlite3
import datetime

from gram_panchayat_member import GramPanchayatMember as GPM


gpm_data = [(1, 1, 'Anirudh', 'Rana', 'Uttarakhand', '12/1 kaveri mohalla', 248001, 'ranaa@gmail.com', '111'),
            (2, 1, 'Shubham', 'Bhatt', 'punjab', '12/12 kashmiri colo', 123456, 'bhatt@gmail.com', '###')]

single_gpm_data = [1, 1, 'Anirudh', 'Rana', 'Uttarakhand', '12/1 kaveri mohalla', 248001, 'ranaa@gmail.com', '111']

single_gpm_data_without_password = [1, 1, 'Anirudh', 'Rana', 'Uttarakhand', '12/1 kaveri mohalla', 248001,
                                    'ranaa@gmail.com', None]

complaints_filed = ['subject', 'complaint', 'fname', 'lname']

request_list = [('fname', 'lname', 'project 1', 1),
                ('fname', 'lname', 'project 2', 2),
                ('fname', 'lname', 'project 3', 0)]

single_member_data = [1, 1, 'Shivam', 'Singh', 23, 'M', 'punjab', '78 mohalla kabuli gate', 455722, 'singh@gmail.com',
                      'qqq', 'Amritsar', 334, 33400.0, 2]

member_data = [(1, 1, 'Shivam', 'Singh', 23, 'M', 'punjab', '78 mohalla kabuli gate', 455722, 'singh@gmail.com',
                      'qqq', 'Amritsar', 334, 33400.0, 2),
               (1, 1, 'Shivam', 'Singh', 23, 'M', 'punjab', '78 mohalla kabuli gate', 455722, 'singh@gmail.com',
                      'qqq', 'Amritsar', 334, 33400.0, 2),
               (1, 1, 'Shivam', 'Singh', 23, 'M', 'punjab', '78 mohalla kabuli gate', 455722, 'singh@gmail.com',
                      'qqq', 'Amritsar', 334, 33400.0, 2)]

single_project_data = [1, 'tasla', 'road construction', 'Uttarakhand', 39, 2333000.0, '12-10-2019', '23-12-2020']


class TestGramPanchayatMember:

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_members_menu', return_value=True)
    def test_gpm_main_menu_choice_1(self, arg1, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['1', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_job_card', return_value=True)
    def test_gpm_main_menu_choice_2(self, arg1, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['2', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_work_allotment', return_value=True)
    def test_gpm_main_menu_choice_3(self, arg1, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['3', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.request_list', return_value=True)
    def test_gpm_main_menu_choice_4(self, arg1, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['4', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.complaints_filed', return_value=True)
    def test_gpm_main_menu_choice_5(self, arg1, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['5', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    def test_gpm_main_menu_choice_6(self, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    def test_gpm_main_menu_wrong_choice(self, inputs):
        """ Test gpm main menu method."""
        inputs.side_effect = ['@', '6']

        assert GPM(object).gpm_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.add_member', return_value=True)
    def test_gpm_members_menu_choice_1(self, arg1, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['1', '5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.update_member', return_value=True)
    def test_gpm_members_menu_choice_2(self, arg1, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['2', '5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.delete_member', return_value=True)
    def test_gpm_members_menu_choice_3(self, arg1, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['3', '5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.show_members', return_value=True)
    def test_gpm_members_menu_choice_4(self, arg1, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['4', '5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    def test_gpm_members_menu_choice_5(self, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    def test_gpm_members_menu_wrong_choice(self, inputs):
        """ Test gpm members menu method."""
        inputs.side_effect = ['@', '5']

        assert GPM(object).gpm_members_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.add_member_action', return_value=True)
    def test_add_member_success(self, arg1, inputs):
        """ Test add member method."""
        inputs.side_effect = ['', '', 'test@gmail.com', '', '', '', '', '', '']

        assert GPM(object).add_member() == True

    @mock.patch('builtins.input')
    def test_add_member_invalid_email(self, inputs):
        """ Test add member method."""
        inputs.side_effect = ['', '', 'test', '', '', '', '', '', '']

        assert GPM(object).add_member() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_add_member_action_success(self, mocksql):
        """ Test add member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert GPM(mocksql).add_member_action('', '', '', '', 'M','west bengal', '', '', '') == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_add_member_action_failure_invalid_gender(self, mocksql):
        """ Test add member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert GPM(mocksql).add_member_action('', '', '', '', '5', 'west bengal', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_add_member_action_failure_invalid_state(self, mocksql):
        """ Test add member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert GPM(mocksql).add_member_action('', '', '', '', '5', 'bengal', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_add_member_action_failure_email_exist(self, mocksql):
        """ Test add member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [1]

        assert GPM(mocksql).add_member_action('', '', '', '', '5', 'west bengal', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_add_member_action_failure_sqlite3_error(self, mocksql):
        """ Test add member action method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).add_member_action('', '', '', '', '5', 'west bengal', '', '', '') == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.update_member_action', return_value=True)
    def test_update_member_success(self, arg1, mocksql, inputs):
        """ Test update member method."""
        inputs.side_effect = ['', '', '', '', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_member_data

        assert GPM(mocksql).update_member() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.update_member_action', return_value=True)
    def test_update_member_failure_no_data(self, arg1, mocksql, inputs):
        """ Test update member method."""
        inputs.return_value = ''
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = None

        assert GPM(mocksql).update_member() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_failure_sqlite3_error(self, mocksql, inputs):
        """ Test update member method."""
        inputs.side_effect = ['', '', '', '', '', '', '', '', '', '']
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).update_member() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_success(self, mocksql):
        """ Test update member method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [[0], member_data]

        assert GPM(mocksql).update_member_action('', '', 'test@gmail.com', '', 'F', 'punjab', '', '', '', '') == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_failure_invalid_gender(self, mocksql):
        """ Test update member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [[0], member_data]

        assert GPM(mocksql).update_member_action('', '', 'test@gmail.com', '', 'y', 'punjab', '', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_failure_invalid_state(self, mocksql):
        """ Test update member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [[0], member_data]

        assert GPM(mocksql).update_member_action('', '', 'test@gmail.com', '', 'y', '@@@', '', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_failure_email_exist(self, mocksql):
        """ Test update member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [[1], member_data]

        assert GPM(mocksql).update_member_action('', '', 'test@gmail.com', '', 'y', 'punjab', '', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_failure_invalid_email(self, mocksql):
        """ Test update member action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [[0], member_data]

        assert GPM(mocksql).update_member_action('', '', 'invalid email', '', 'y', 'punjab', '', '', '', '') == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_update_member_action_failure_sqlite3_error(self, mocksql):
        """ Test update member action method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).update_member_action('', '', 'test@gmail.com', '', 'y', 'punjab', '', '', '', '') == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_delete_member_success(self, mocksql, inputs):
        """ Test delete member method."""
        inputs.side_effect = ['test@gmail.com', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = member_data

        assert GPM(mocksql).delete_member() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_delete_member_failure_action_aborted(self, mocksql, inputs):
        """ Test delete member method."""
        inputs.side_effect = ['test@gmail.com', 'n']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = member_data

        assert GPM(mocksql).delete_member() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_delete_member_failure_no_data(self, mocksql, inputs):
        """ Test delete member method."""
        inputs.side_effect = ['test@gmail.com', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = None

        assert GPM(mocksql).delete_member() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_delete_member_failure_sqlite3_error(self, mocksql, inputs):
        """ Test delete member method."""
        inputs.side_effect = ['test@gmail.com', 'y']
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).delete_member() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_show_members_success(self, mocksql):
        """ Test show members method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert GPM(mocksql).show_members() == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_show_members_failure_no_data(self, mocksql):
        """ Test show members method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert GPM(mocksql).show_members() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_show_members_failure_sqlite3_error(self, mocksql):
        """ Test show members method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).show_members() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_job_card_success(self, mocksql, inputs):
        """ Test gpm job card method."""
        inputs.return_value = 'tets@gmail.com'
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [single_member_data]

        assert GPM(mocksql).gpm_job_card() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_job_card_failure_no_data(self, mocksql, inputs):
        """ Test gpm job card method."""
        inputs.return_value = 'tets@gmail.com'
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [None]

        assert GPM(mocksql).gpm_job_card() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_job_card_failure_sqlite3_error(self, mocksql, inputs):
        """ Test gpm job card method."""
        inputs.return_value = 'tets@gmail.com'
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).gpm_job_card() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.work_allotment_action', return_value=True)
    def test_gpm_work_allotment_success(self, arg1, mocksql, inputs):
        """ Test gpm work allotment method."""
        inputs.side_effect = ['email', 'project', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [single_member_data, single_project_data]

        assert GPM(mocksql).gpm_work_allotment() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_work_allotment_failure_action_aborted(self, mocksql, inputs):
        """ Test gpm work allotment method."""
        inputs.side_effect = ['email', 'project', 'u']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [single_member_data, single_project_data]

        assert GPM(mocksql).gpm_work_allotment() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_work_allotment_failure_no_member_data(self, mocksql, inputs):
        """ Test gpm work allotment method."""
        inputs.side_effect = ['email', 'project', 'u']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [None, single_project_data]

        assert GPM(mocksql).gpm_work_allotment() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_work_allotment_failure_no_project_data(self, mocksql, inputs):
        """ Test gpm work allotment method."""
        inputs.side_effect = ['email', 'project', 'u']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [single_member_data, None]

        assert GPM(mocksql).gpm_work_allotment() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_gpm_work_allotment_failure_sqlite3_error(self, mocksql, inputs):
        """ Test gpm work allotment method."""
        inputs.side_effect = ['email', 'project']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.side_effect = sqlite3.Error

        assert GPM(mocksql).gpm_work_allotment() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_work_allotment_action_success_insert_data(self, mocksql):
        """ Test gpm work allotment action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = None

        assert GPM(mocksql).work_allotment_action(single_project_data, single_member_data) == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_work_allotment_action_success_update_data(self, mocksql):
        """ Test gpm work allotment action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [None, single_member_data]

        assert GPM(mocksql).work_allotment_action(single_project_data, single_member_data) == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_work_allotment_action_failure_member_exist_in_project(self, mocksql):
        """ Test gpm work allotment action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [None]

        assert GPM(mocksql).work_allotment_action(single_project_data, single_member_data) == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_request_list_success(self, mocksql):
        """ Test request list method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = request_list

        assert GPM(mocksql).request_list() == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_request_list_failure_without_data(self, mocksql):
        """ Test request list method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert GPM(mocksql).request_list() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_request_list_failure_sqlite3_error(self, mocksql):
        """ Test request list method."""
        mocksql.cursor.side_effect = sqlite3.Error

        assert GPM(mocksql).request_list() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_complaints_filed_success(self, mocksql):
        """ Test complaints filed method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = complaints_filed

        assert GPM(mocksql).complaints_filed() == True

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_complaints_filed_failure_without_data(self, mocksql):
        """ Test complaints filed method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert GPM(mocksql).complaints_filed() == False

    @mock.patch('gram_panchayat_member.sqlite3.connect')
    def test_complaints_filed_failure_sqlite3_error(self, mocksql):
        """ Test complaints filed method."""
        mocksql.cursor.side_effect = sqlite3.Error

        assert GPM(mocksql).complaints_filed() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_main_menu', return_value=True)
    def test_login_gpm_success(self, arg1, input):
        """ Test login gpm method."""
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_gpm_data

            assert GPM(mocksql).login_gpm() == True

    @mock.patch('builtins.input', return_value='test@xyz.com')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_main_menu', return_value=True)
    def test_login_gpm_failure_email_not_found(self, arg1, arg2):
        """ Test login gpm method."""
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = None

            assert GPM(mocksql).login_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.sqlite3.connect')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_main_menu', return_value=True)
    def test_login_gpm_set_password_success(self, arg1, mocksql, inputs):
        """ Test login gpm method."""
        inputs.side_effect = ['test@xyz.com', 'qwe', 'qwe', '3']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_gpm_data_without_password

        assert GPM(mocksql).login_gpm() == True

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_main_menu', return_value=True)
    def test_login_gpm_set_password_not_match(self, arg1, inputs):
        """ Test login gpm method."""
        inputs.side_effect = ['test@xyz.com', '100', '2']
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_gpm_data_without_password

            assert GPM(mocksql).login_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('gram_panchayat_member.GramPanchayatMember.gpm_main_menu', return_value=True)
    def test_login_gpm_set_password_empty(self, arg1, inputs):
        """ Test login gpm method."""
        inputs.side_effect = ['test@xyz.com', '', '']
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_gpm_data_without_password

            assert GPM(mocksql).login_gpm() == False

    @mock.patch('builtins.input')
    def test_login_gpm_failure_sql_error(self, inputs):
        """ Test login gpm method."""
        inputs.side_effect = ['id', 'pswd']
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert GPM(mocksql).login_gpm() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    def test_login_gpm_failure_with_multiple_wrong_attempts(self, input):
        """ Test login gpm method."""
        with mock.patch('gram_panchayat_member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.side_effect = [single_gpm_data, None, single_gpm_data, None, single_gpm_data,
                                                        None]

            assert GPM(mocksql).login_gpm() == False