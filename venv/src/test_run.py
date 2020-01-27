import mock
import sqlite3

import run
from run import Run


class TestRun:

    @mock.patch('run.sqlite3')
    def test_sql_connection_success(self, mocksql):
        """ Test sql connection method."""
        mocksql.connect().return_value = object
        assert run.sql_connection().return_value == object

    @mock.patch('run.sqlite3')
    def test_sql_connection_failure(self, mocksql):
        """ Test sql connection method."""
        mocksql.connect().return_value = None
        assert run.sql_connection().return_value is None

    @mock.patch('run.BlockDevelopmentOfficer.login_bdo')
    @mock.patch('builtins.input')
    @mock.patch('run.sqlite3.connect')
    def test_login_menu_choice_1(self, mocksql, inputs, bdo):
        """ Test login menu method."""
        bdo.return_value = True
        inputs.side_effect = ['1', '4']
        assert Run(mocksql).login_menu() == True

    @mock.patch('run.GramPanchayatMember.login_gpm')
    @mock.patch('builtins.input')
    @mock.patch('run.sqlite3.connect')
    def test_login_menu_choice_2(self, mocksql, inputs, gpm):
        """ Test login menu method."""
        gpm.return_value = True
        inputs.side_effect = ['2', '4']
        assert Run(mocksql).login_menu() == True

    @mock.patch('run.Member.login_member')
    @mock.patch('builtins.input')
    @mock.patch('run.sqlite3.connect')
    def test_login_menu_choice_3(self, mocksql, inputs, member):
        """ Test login menu method."""
        member.return_value = True
        inputs.side_effect = ['3', '4']
        assert Run(mocksql).login_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('run.sqlite3.connect')
    def test_login_menu_choice_4(self, mocksql, inputs):
        """ Test login menu method."""
        inputs.return_value = '4'
        assert Run(mocksql).login_menu() == True

    @mock.patch('builtins.input')
    @mock.patch('run.sqlite3.connect')
    def test_login_menu_wrong_choice(self, mocksql, inputs):
        """ Test login menu method."""
        inputs.side_effect = ['e', '4']
        assert Run(mocksql).login_menu() == True

    @mock.patch('run.sql_connection')
    def test_main_if_condition(self, conn):
        """ Test main method."""
        conn.return_value = None

        assert run.main() == False

    @mock.patch('run.Schema.setup_admin')
    @mock.patch('run.Schema.create_tables')
    @mock.patch('run.Run.login_menu')
    @mock.patch('run.sql_connection')
    def test_main_else_condition(self, conn, lm, ct, sa):
        """ Test main method."""
        lm.return_value = True
        ct.return_value = True
        sa.return_value = True
        conn.return_value = mock.Mock()

        assert run.main() == True

    @mock.patch('run.sql_connection')
    def test_main_failure_sql_error(self, mocksql):
        """ Test main method."""
        mocksql.side_effect = sqlite3.Error

        assert run.main() == False
