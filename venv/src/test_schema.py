import mock
import sqlite3
from schema import Schema


class TestSchema:

    @mock.patch('schema.sqlite3.connect')
    def test_setup_admin_success(self, mocksql):
        """ Test setup admin method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert Schema(mocksql).setup_admin() == True

    @mock.patch('schema.sqlite3.connect')
    def test_setup_admin_failure(self, mocksql):
        """ Test setup admin method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert Schema(mocksql).setup_admin() == False

    @mock.patch('schema.sqlite3.connect')
    def test_create_tables_success(self, mocksql):
        """ Test create tables method."""
        sqlite_execute_mock = mock.Mock()
        mocksql.execute.return_value = sqlite_execute_mock

        assert Schema(mocksql).create_tables() == True

    @mock.patch('schema.sqlite3.connect')
    def test_create_tables_failure(self, mocksql):
        """ Test create tables method."""
        mocksql.execute.side_effect = sqlite3.Error

        assert Schema(mocksql).create_tables() == False
