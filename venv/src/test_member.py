import mock
import sqlite3

from member import Member

member_details = {('1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'qqq', 'l', 'm', 'n', '1'),
                  ('2', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'qqq', 'l', 'm', 'n', '0')}

single_member_detail = ['1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'test@xyz.com', '***', 'l', 'm', 'n', '1']

single_member_detail_without_password = ['1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'test@xyz.com', None, 'l', 'm',
                                         'n', '1']

complaints = {(1, 2, 'subject 1', 'complaint 1'),
              (2, 12, 'subject 2', 'complaint 2'),
              (3, 1, 'subject 3', 'complaint 3')}


class TestMember:

    @mock.patch('member.Member.member_details')
    @mock.patch('builtins.input', side_effect=['1', '3'])
    def test_member_main_menu_choice_1(self, input, md):
        """ Test member main menu method."""
        md.return_value = True
        assert Member(object).member_main_menu("test") == True

    @mock.patch('member.Member.raise_complaint_menu')
    @mock.patch('builtins.input', side_effect=['2', '3'])
    def test_member_main_menu_choice_2(self, input, cmp):
        """ Test member main menu method."""
        cmp.return_value = True
        assert Member(object).member_main_menu("test") == True

    @mock.patch('builtins.input', return_value='3')
    def test_member_main_menu_choice_3(self, input):
        """ Test member main menu method."""
        assert Member(object).member_main_menu("test@gmail.com") == True

    @mock.patch('builtins.input', side_effect=['w', '3'])
    def test_member_main_menu_wrong_choice(self, input):
        """ Test member main menu method."""
        assert Member(object).member_main_menu("test@gmail.com") == True

    @mock.patch('member.sqlite3.connect')
    def test_member_details_true_with_data(self, mocksql):
        """ Test member details method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_member_detail

        assert Member(mocksql).member_details() == True

    @mock.patch('member.sqlite3.connect')
    def test_member_details_true_without_data(self, mocksql):
        """ Test member details method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = []

        assert Member(mocksql).member_details() == True

    def test_member_details_failure_sql_error(self):
        """ Test member details method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert Member(mocksql).member_details() == False

    @mock.patch('member.Member.file_complaint')
    @mock.patch('builtins.input', side_effect=['1', '3'])
    def test_raise_complaint_menu_choice_1(self, input, fc):
        """ Test raise complaint menu method."""
        fc.return_value = True

        assert Member(object).raise_complaint_menu() == True

    @mock.patch('member.Member.show_member_complaints')
    @mock.patch('builtins.input', side_effect=['2', '3'])
    def test_raise_complaint_menu_choice_2(self, input, smc):
        """ Test raise complaint menu method."""
        smc.return_value = True

        assert Member(object).raise_complaint_menu() == True

    @mock.patch('builtins.input', return_value='3')
    def test_raise_complaint_menu_choice_3(self, input):
        """ Test raise complaint menu method."""
        assert Member(object).raise_complaint_menu() == True

    @mock.patch('builtins.input', side_effect=['w', '3'])
    def test_raise_complaint_menu_wrong_choice(self, input):
        """ Test raise complaint menu method."""
        assert Member(object).raise_complaint_menu() == True

    @mock.patch('member.sqlite3.connect')
    @mock.patch('builtins.input', side_effect=['subject', 'complaint'])
    def test_file_complaint(self, input, mocksql):
        """ Test file complaint method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert Member(mocksql).file_complaint() == True

    @mock.patch('builtins.input', side_effect=['subject', 'complaint'])
    def test_file_complaint_failure_sql_error(self, input):
        """ Test file complaint method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert Member(mocksql).file_complaint() == False

    @mock.patch('member.sqlite3.connect')
    def test_show_member_complaints_with_data(self, mocksql):
        """ Test show member complaints method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = complaints

        assert Member(mocksql).show_member_complaints() == True

    @mock.patch('member.sqlite3.connect')
    def test_show_member_complaints_without_data(self, mocksql):
        """ Test show member complaints method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchall.return_value = {}

        assert Member(mocksql).show_member_complaints() == True

    def test_show_member_complaints_failure_sql_error(self):
        """ Test show member complaints method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert Member(mocksql).show_member_complaints() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    @mock.patch('member.Member.member_main_menu', return_value='')
    def test_login_member_success(self, arg1, input):
        """ Test login member method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_member_detail

            assert Member(mocksql).login_member() == True

    @mock.patch('builtins.input', return_value='test@xyz.com')
    @mock.patch('member.Member.member_main_menu', return_value='')
    def test_login_member_failure_email_not_found(self, arg1, arg2):
        """ Test login member method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = None

            assert Member(mocksql).login_member() == False

    @mock.patch('builtins.input')
    @mock.patch('member.sqlite3.connect')
    @mock.patch('member.Member.member_main_menu', return_value='')
    def test_login_member_set_password_success(self, arg1, mocksql, inputs):
        """ Test login member method."""
        inputs.side_effect = ['test@xyz.com', 'qwe', 'qwe', '3']
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock
        sqlite_execute_mock.fetchone.return_value = single_member_detail_without_password

        assert Member(mocksql).login_member() == True

    @mock.patch('builtins.input')
    @mock.patch('member.Member.member_main_menu', return_value='')
    def test_login_member_set_password_not_match(self, arg1, inputs):
        """ Test login member method."""
        inputs.side_effect = ['test@xyz.com', '100', '2']
        with mock.patch('member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_member_detail_without_password

            assert Member(mocksql).login_member() == False

    @mock.patch('builtins.input')
    @mock.patch('member.Member.member_main_menu', return_value='')
    def test_login_member_set_password_empty(self, arg1, inputs):
        """ Test login member method."""
        inputs.side_effect = ['test@xyz.com', '', '']
        with mock.patch('member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.return_value = single_member_detail_without_password

            assert Member(mocksql).login_member() == False

    @mock.patch('builtins.input')
    def test_login_member_failure_sql_error(self, inputs):
        """ Test login member method."""
        inputs.side_effect = ['id', 'pswd']
        with mock.patch('member.sqlite3.connect') as mocksql:
            mocksql.execute.side_effect = sqlite3.Error

            assert Member(mocksql).login_member() == False

    @mock.patch('builtins.input', return_value='test@xyz.com')
    def test_login_member_failure_with_multiple_wrong_attempts(self, input):
        """ Test login member method."""
        with mock.patch('member.sqlite3.connect') as mocksql:
            sqlite_execute_mock = mock.Mock()
            mocksql.execute.return_value = sqlite_execute_mock
            sqlite_execute_mock.fetchone.side_effect = [single_member_detail, None, single_member_detail, None,
                                                        single_member_detail, None]

            assert Member(mocksql).login_member() == False
