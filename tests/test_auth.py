import unittest
from app.controllers.auth_controller import AuthController
from app.models.user import User

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.auth_controller = AuthController()
        self.test_user = User(id=1, username='testuser', password='testpassword')

    def test_login_success(self):
        self.auth_controller.create_user(self.test_user.username, self.test_user.password)
        result = self.auth_controller.login(self.test_user.username, self.test_user.password)
        self.assertTrue(result)

    def test_login_failure(self):
        result = self.auth_controller.login(self.test_user.username, 'wrongpassword')
        self.assertFalse(result)

    def test_logout(self):
        self.auth_controller.create_user(self.test_user.username, self.test_user.password)
        self.auth_controller.login(self.test_user.username, self.test_user.password)
        result = self.auth_controller.logout()
        self.assertTrue(result)

    def tearDown(self):
        self.auth_controller.delete_user(self.test_user.username)

if __name__ == '__main__':
    unittest.main()