import mock
import sqlite3
import datetime

from block_development_officer import BlockDevelopmentOfficer as BDO

bdo_detail = [1, 'fname', 'lname', 'email', '***']

complaints = {('subject 1', 'complaint 1', 'filed by', 'filed by', 'gpm fname', 'gpm lname'),
              ('subject 2', 'complaint 2', 'filed by', 'filed by', 'gpm fname', 'gpm lname'),
              ('subject 3', 'complaint 3', 'filed by', 'filed by', 'gpm fname', 'gpm lname')}

member_data = {(1, 32, 'fname', 'lname', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 1200.00, '2'),
               (2, 32, 'fname', 'lname', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 1200.00, '2'),
               (3, 34, 'fname', 'lname', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 1200.00, '2')}

project_approval_data = {(1, 'gpm_name', 'gpm_lname', 'member_fname', 'member_lname', 'project_name'),
                         (2, 'gpm_name', 'gpm_lname', 'member_fname', 'member_lname', 'project_name'),
                         (3, 'gpm_name', 'gpm_lname', 'member_fname', 'member_lname', 'project_name')}

project_data = [(1, 'tasla', 'road construction', 'Uttarakhand', 39, 2333000.0, '12-10-2019', '23-12-2020', '2')]

project_data_2 = [1, 'tasla', 'road construction', 'Uttarakhand', 39, 2333000.0, '12-10-2019', '23-12-2020', '2']

pending_project_member = {(1, 2, 3, 4)}

gpm_data = [(1, 2, 'fname', 'lname', 'state', 'address', 234190, 'email'),
            (2, 2, 'fname', 'lname', 'state', 'address', 234190, 'email'),
            (3, 1, 'fname', 'lname', 'state', 'address', 234190, 'email')]

single_gpm_data = [1, 2, 'fname', 'lname', 'state', 'address', 234190, 'email']


class TestBlockDevelopmentOfficer:

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.bdo_gpm_menu', return_value=True)
    def test_bdo_main_menu_choice_1(self, arg1, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['1', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.bdo_project_menu', return_value=True)
    def test_bdo_main_menu_choice_2(self, arg1, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['2', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.bdo_project_approval_requests', return_value=True)
    def test_bdo_main_menu_choice_3(self, arg1, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['3', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.bdo_wage_approval_requests', return_value=True)
    def test_bdo_main_menu_choice_4(self, arg1, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['4', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.complaints_filed', return_value=True)
    def test_bdo_main_menu_choice_5(self, arg1, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['5', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    def test_bdo_main_menu_choice_6(self, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    def test_bdo_main_menu_wrong_choice(self, inputs):
        """ Test bdo main menu method."""
        inputs.side_effect = ['w', '6']

        assert BDO(object).bdo_main_menu('test@gmail.com') == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.add_gpm', return_value=True)
    def test_bdo_gpm_menu_choice_1(self, arg1, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['1', '5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_gpm', return_value=True)
    def test_bdo_gpm_menu_choice_2(self, arg1, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['2', '5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.delete_gpm', return_value=True)
    def test_bdo_gpm_menu_choice_3(self, arg1, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['3', '5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.show_gpm', return_value=True)
    def test_bdo_gpm_menu_choice_4(self, arg1, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['4', '5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    def test_bdo_gpm_menu_choice_5(self, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    def test_bdo_gpm_menu_wrong_choice(self, inputs):
        """ Test bdo gpm menu method."""
        inputs.side_effect = ['w', '5']

        assert BDO(object).bdo_gpm_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_gpm_success(self, mocksql, inputs):
        """ Test add gpm method."""
        inputs.side_effect =['fname', 'lname', 'test@gmail.com', 'kerala', 'address', '122335']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).add_gpm() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_gpm_failure_wrong_state_name(self, mocksql, inputs):
        """ Test add gpm method."""
        inputs.side_effect =['fname', 'lname', 'test@gmail.com', '@@@', 'address', '122335']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).add_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_gpm_failure_email_already_exist(self, mocksql, inputs):
        """ Test add gpm method."""
        inputs.side_effect = ['fname', 'lname', 'test@gmail.com', '@@@', 'address', '122335']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [1]

        assert BDO(mocksql).add_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_gpm_failure_invalid_email(self, mocksql, inputs):
        """ Test add gpm method."""
        inputs.side_effect = ['fname', 'lname', 'invalid email', 'kerala', 'address', '122335']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [1]

        assert BDO(mocksql).add_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_gpm_failure_sqlite3_error(self, mocksql, inputs):
        """ Test add gpm method."""
        inputs.side_effect = ['fname', 'lname', 'test@gmail.com', 'kerala', 'address', '122335']
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).add_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_gpm_with_details', return_value=True)
    def test_update_gpm_success(self, arg1, mocksql, inputs):
        """ Test update gpm method."""
        inputs.side_effect = ['test@gmail.com', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_gpm_data

        assert BDO(mocksql).update_gpm() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_failure_no_gpm_record(self, mocksql, inputs):
        """ Test update gpm method."""
        inputs.side_effect = ['test@gmail.com', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = None

        assert BDO(mocksql).update_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_failure_sqlite3_error(self, mocksql, inputs):
        """ Test update gpm method."""
        inputs.return_value = 'test@gmail.com'
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).update_gpm() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_with_details_success(self, mocksql):
        """ Test update gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).update_gpm_with_details('fname', 'lanme', 'test@xyz.com', 'kerala', 'adress',
                                                    123456, 1) == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_with_details_failure_wrong_state(self, mocksql):
        """ Test update gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).update_gpm_with_details('fname', 'lanme', 'test@xyz.com', '@@@', 'adress',
                                                    123456, 1) == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_with_details_failure_email_exists(self, mocksql):
        """ Test update gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [1]

        assert BDO(mocksql).update_gpm_with_details('fname', 'lanme', 'test@xyz.com', 'kerala', 'adress',
                                                    123456, 1) == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_with_details_failure_invalid_email(self, mocksql):
        """ Test update gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).update_gpm_with_details('fname', 'lanme', 'invalidEmail', 'kerala', 'adress',
                                                    123456, 1) == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_gpm_with_details_failure_sqlite3_error(self, mocksql):
        """ Test update gpm method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).update_gpm_with_details('fname', 'lanme', 'test@gmail.com', 'kerala', 'adress',
                                                    123456, 1) == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_gpm_success(self, mocksql, inputs):
        """ Test delete gpm method."""
        inputs.side_effect = ['email', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_gpm_data

        assert BDO(mocksql).delete_gpm() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_gpm_failure_action_aborted(self, mocksql, inputs):
        """ Test delete gpm method."""
        inputs.side_effect = ['project', 'w']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_gpm_data

        assert BDO(mocksql).delete_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_gpm_failure_without_data(self, mocksql, inputs):
        """ Test delete gpm method."""
        inputs.side_effect = ['project', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = []

        assert BDO(mocksql).delete_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_gpm_failure_sqlite3_error(self, mocksql, inputs):
        """ Test delete gpm method."""
        inputs.side_effect = ['project', 'y']
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).delete_gpm() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_show_gpm_success_with_data(self, mocksql):
        """ Test show gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = gpm_data

        assert BDO(mocksql).show_gpm() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_show_gpm_success_without_data(self, mocksql):
        """ Test show gpm method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert BDO(mocksql).show_gpm() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_show_gpm_failure_sqlite3_error(self, mocksql):
        """ Test show gpm method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).show_gpm() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.add_project', return_value=True)
    def test_project_menu_choice_1(self, arg1, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['1', '5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project', return_value=True)
    def test_project_menu_choice_2(self, arg1, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['2', '5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.delete_project', return_value=True)
    def test_project_menu_choice_3(self, arg1, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['3', '5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.show_projects', return_value=True)
    def test_project_menu_choice_4(self, arg1, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['4', '5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    def test_project_menu_choice_5(self, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    def test_project_menu_wrong_input(self, inputs):
        """ Test project menu method."""
        inputs.side_effect = ['$', '5']

        assert BDO(object).bdo_project_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.add_project_action', return_value=True)
    def test_add_project_success(self, arg1, mocksql, inputs):
        """ Test add project method."""
        inputs.side_effect = ['', 'road construction', 'punjab', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).add_project() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_failure_wrong_state(self, mocksql, inputs):
        """ Test add project method."""
        inputs.side_effect = ['', 'road construction', '@@@', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).add_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_failure_wrong_project_type(self, mocksql, inputs):
        inputs.side_effect = ['', 'invalid type', '@@@', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [0]

        assert BDO(mocksql).add_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_failure_project_name_exists(self, mocksql, inputs):
        """ Test add project method."""
        inputs.side_effect = ['test', 'invalid type', '@@@', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = [1]

        assert BDO(mocksql).add_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_failure_sqlite3_error(self, mocksql, inputs):
        """ Test add project method."""
        inputs.side_effect = ['test', 'invalid type', '@@@', '', '', '', '']
        mocksql.execute.side_effect = sqlite3.DataError

        assert BDO(mocksql).add_project() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_action_success(self, mocksql):
        """ Test add project action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert BDO(mocksql).add_project_action('test', '', '', '', '', '01-11-2020', '10-11-2020') == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_action_failure_end_date_is_less(self, mocksql):
        """ Test add project action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert BDO(mocksql).add_project_action('test', '', '', '', '', '01-11-2020', '10-01-2020') == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_action_failure_value_error(self, mocksql):
        """ Test add project action method."""
        assert BDO(mocksql).add_project_action('test', '', '', '', '', '01-91-2020', '10-01-2020') == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_add_project_action_failure_sqlite3_error(self, mocksql):
        """ Test add project action method."""
        mocksql.execute.side_effect = sqlite3.DataError

        assert BDO(mocksql).add_project_action('test', '', '', '', '', '01-01-2020', '10-01-2020') == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project_action', return_value=True)
    def test_update_project_success(self, arg1, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [project_data_2, [0]]

        assert BDO(mocksql).update_project() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project_action', return_value=False)
    def test_update_project_failure_update_project_action(self, arg1, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [project_data_2, [0]]

        assert BDO(mocksql).update_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project_action', return_value=False)
    def test_update_project_failure_invalid_state(self, arg1, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '@@@', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [project_data_2, [0]]

        assert BDO(mocksql).update_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project_action', return_value=False)
    def test_update_project_failure_invalid_project_type(self, arg1, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', 'qwer', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [project_data_2, [0]]

        assert BDO(mocksql).update_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_project_action', return_value=False)
    def test_update_project_failure_project_already_exists(self, arg1, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [project_data_2, [1]]

        assert BDO(mocksql).update_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_project_failure_sqlite3_error(self, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '', '', '', '', '']
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).update_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_project_failure_no_project(self, mocksql, inputs):
        """ Test update project method."""
        inputs.side_effect = ['project', '', '', '', '', '', '', '']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.side_effect = [None, [1]]

        assert BDO(mocksql).update_project() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_project_action_success(self, mocksql):
        """ Test update project action method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert BDO(mocksql).update_project_action('12-12-2019', '12-01-2020', 'a', 'a', 'a', 'a', 'a') == True

    def test_update_project_action_failure_end_date_is_small(self):
        """ Test update project action method."""
        assert BDO(object).update_project_action('12-12-2020', '12-01-2020', 'a', 'a', 'a', 'a', 'a') == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_project_action_failure_sqlite_error(self, mocksql):
        """ Test update project action method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).update_project_action('12-12-2010', '12-01-2020', 'a', 'a', 'a', 'a', 'a') == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_project_action_failure_value_error(self, mocksql):
        """ Test update project action method."""
        mocksql.execute.side_effect = ValueError

        assert BDO(mocksql).update_project_action('12-12-2010', '12-01-2020', 'a', 'a', 'a', 'a', 'a') == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_project_success(self, mocksql, inputs):
        """ Test delete project method."""
        inputs.side_effect = ['project', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = project_approval_data

        assert BDO(mocksql).delete_project() == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_project_with_action_aborted(self, mocksql, inputs):
        """ Test delete project method."""
        inputs.side_effect = ['project', 'w']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = project_approval_data

        assert BDO(mocksql).delete_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_project_without_data(self, mocksql, inputs):
        """ Test delete project method."""
        inputs.side_effect = ['project', 'y']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = None

        assert BDO(mocksql).delete_project() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_delete_project_failure(self, mocksql, inputs):
        """ Test delete project method."""
        inputs.side_effect = ['project', 'y']
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).delete_project() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_show_projects_success(self, mocksql):
        """ Test show projects method."""
        mocksql.execute.return_value = project_data

        assert BDO(mocksql).show_projects() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_show_projects_failure(self, mocksql):
        """ Test show project method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert BDO(mocksql).show_projects() == False

    @mock.patch('block_development_officer.BlockDevelopmentOfficer.project_approval_action', return_value=True)
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_project_approval_requests_with_data(self, mocksql, bdo):
        """ Test bdo project approval requests method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert BDO(mocksql).bdo_project_approval_requests() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_project_approval_requests_without_data(self, mocksql):
        """ Test bdo project approval requests method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert BDO(mocksql).bdo_project_approval_requests() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_project_approval_requests_failure_sql_error(self, mocksql):
        """ Test bdo project approval requests method."""
        mocksql.cursor.side_effect = sqlite3.Error

        assert BDO(mocksql).bdo_project_approval_requests() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.calculate_wage', return_value=True)
    def test_project_approval_action_success(self, arg1, mocksql, inputs):
        """ Test project approval action method."""
        inputs.side_effect = ['1', '1']
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = member_data
        ids_list = ['1', '2']
        assert BDO(mocksql).project_approval_action(ids_list) == True

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_project_approval_action_failure_sql_error(self, mocksql, inputs):
        """ Test project approval action method."""
        inputs.side_effect = ['1', '1']
        mocksql.execute.side_effect = sqlite3.Error
        ids_list = ['1', '2']
        assert BDO(mocksql).project_approval_action(ids_list) == False

    @mock.patch('builtins.input')
    def test_project_approval_action_with_invalid_status_code(self, inputs):
        """ Test project approval action method."""
        inputs.side_effect = ['1', '$']
        ids_list = ['1', '2']
        assert BDO(object).project_approval_action(ids_list) == False

    @mock.patch('builtins.input')
    def test_project_approval_action_with_invalid_serial_no(self, inputs):
        """ Test project approval action method."""
        inputs.side_effect = ['3']
        ids_list = ['1', '2']
        assert BDO(object).project_approval_action(ids_list) == False

    @mock.patch('builtins.input')
    def test_project_approval_action_with_action_abort(self, inputs):
        """ Test project approval action method."""
        inputs.side_effect = ['#']
        ids_list = ['1', '2']
        assert BDO(object).project_approval_action(ids_list) == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_calculate_wage_failure_sqlite3_error(self, mocksql):
        """ Test calculate wage method."""
        mocksql.execute.side_effect = sqlite3.DataError
        assert BDO(mocksql).calculate_wage(1, 1) == False

    @mock.patch('block_development_officer.datetime')
    def test_calculate_wage_failure_value_error(self, date):
        """ Test calculate wage method."""
        date.strptime.side_effect = ValueError

        assert BDO(object).calculate_wage(1, 1) == False

    @mock.patch('block_development_officer.BlockDevelopmentOfficer.update_wage', return_value=True)
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_calculate_wage_success(self, mocksql, arg2):
        """ Test calculate wage method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = ['12-12-2020']

        assert BDO(mocksql).calculate_wage(1, 1) == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_wage_success(self, mocksql):
        """ Test update wage method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        end_date = datetime.datetime.strptime('01-10-2020', '%d-%m-%Y').date()
        start_date = datetime.datetime.strptime('12-12-2019', '%d-%m-%Y').date()

        assert BDO(mocksql).update_wage(end_date, start_date, 1) == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_wage_failure_end_date_less(self, mocksql):
        """ Test update wage method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        end_date = datetime.datetime.strptime('01-10-2020', '%d-%m-%Y').date()
        start_date = datetime.datetime.strptime('12-12-2019', '%d-%m-%Y').date()

        assert BDO(mocksql).update_wage(start_date, end_date, 1) == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_update_wage_failure_sqlite3_error(self, mocksql):
        """ Test update wage method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.side_effect = sqlite3.Error
        end_date = datetime.datetime.strptime('01-10-2020', '%d-%m-%Y').date()
        start_date = datetime.datetime.strptime('12-12-2019', '%d-%m-%Y').date()

        assert BDO(mocksql).update_wage(end_date, start_date, 1) == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_success_with_data(self, mocksql, inputs):
        """ Test bdo wage approval requests method."""
        inputs.side_effect = ['1', '1']
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert BDO(mocksql).bdo_wage_approval_requests() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_success_without_data(self, mocksql):
        """ Test bdo wage approval requests method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert BDO(mocksql).bdo_wage_approval_requests() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_failure_sql_error(self, mocksql):
        """ Test bdo wage approval requests method."""
        mocksql.cursor.side_effect = sqlite3.Error

        assert BDO(mocksql).bdo_wage_approval_requests() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_action_aborted(self, mocksql, inputs):
        """ Test bdo wage approval requests method."""
        inputs.side_effect = ['#']
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert BDO(mocksql).bdo_wage_approval_requests() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_invalid_status_code(self, mocksql, inputs):
        """ Test bdo wage approval requests method."""
        inputs.side_effect = ['1', '#']
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert BDO(mocksql).bdo_wage_approval_requests() == False

    @mock.patch('builtins.input')
    @mock.patch('block_development_officer.sqlite3.connect')
    def test_bdo_wage_approval_requests_invalid_sno(self, mocksql, inputs):
        """ Test bdo wage approval requests method."""
        inputs.return_value = '7'
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        sqlite_execute_mock.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = member_data

        assert BDO(mocksql).bdo_wage_approval_requests() == False

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_complaints_filed_with_data(self, mocksql):
        """ Test complaints filed method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = complaints

        assert BDO(mocksql).complaints_filed() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_complaints_filed_without_data(self, mocksql):
        """ Test complaints filed method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.cursor.return_value = sqlite_execute_mock
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = []

        assert BDO(mocksql).complaints_filed() == True

    @mock.patch('block_development_officer.sqlite3.connect')
    def test_complaints_filed_failure_sql_error(self, mocksql):
        """ Test complaints filed method."""
        mocksql.cursor.side_effect = sqlite3.Error

        assert BDO(mocksql).complaints_filed() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    @mock.patch('block_development_officer.BlockDevelopmentOfficer.bdo_main_menu', return_value=True)
    def test_login_bdo_success(self, arg1, input):
        """ Test login bdo method."""
        with mock.patch('block_development_officer.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = bdo_detail

            assert BDO(mocksql).login_bdo() == True

    @mock.patch('builtins.input')
    def test_login_bdo_failure_sql_error(self, inputs):
        """ Test login bdo method."""
        inputs.side_effect = ['id', 'pswd']
        with mock.patch('block_development_officer.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert BDO(mocksql).login_bdo() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    def test_login_bdo_failure_with_multiple_wrong_attempts(self, input):
        """ Test login bdo method."""
        with mock.patch('block_development_officer.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = None

            assert BDO(mocksql).login_bdo() == False
