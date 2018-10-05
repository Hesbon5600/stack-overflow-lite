import unittest
from oop import User


class TestUser(unittest.TestCase):
    def test_update_user(self):
        user1 = User(1, "UserA", "PassA", "EmailA")
        data = {'id': 1, 'username': 'Userz', 'password': 'Passz',
                'email': 'Emailz'}
        result = user1.update_user(data)
        self.assertTrue(result, msg='Could not update user')
        self.assertEqual(user1.username, "Userz",
                         msg='Could not update user')

if __name__ == "__main__":
    unittest.main(verbosity=2)
