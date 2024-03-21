import os
import sys
import unittest
from unittest.mock import MagicMock, patch
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Modules.authorization import insert_user_data, verify_credentials

class TestAuthorization(unittest.TestCase):

    @patch('Modules.authorization.connect_to_mongodb')
    def test_insert_user_data(self, connect_to_mongodb):
        # connect to db
        db = MagicMock()
        connect_to_mongodb.return_value = db

        # insert login data
        insert_user_data("test_user", "test_password")

        # assert method called correctly
        db.users.insert_one.assert_called_once_with({
            'username': "test_user",
            'password': "test_password",
            'documents': []
        })

    @patch('Modules.authorization.connect_to_mongodb')
    def test_verify_credentials(self, connect_to_mongodb):
        
        # connect to db
        db = MagicMock()
        users = MagicMock()
        db.users = users
        connect_to_mongodb.return_value = db

        # test valid username password
        users.find_one.return_value = {'username': 'user', 'password': 'pwd'}
        self.assertTrue(verify_credentials("user", "pwd"))

        # test non existant username/passsword 
        users.find_one.return_value = None
        self.assertFalse(verify_credentials("no_usr", "pwd"))

        # test invalid paswrod
        users.find_one.return_value = None 
        self.assertFalse(verify_credentials("test_user", "wrong_password"))

        
if __name__ == '__main__':
    unittest.main()
