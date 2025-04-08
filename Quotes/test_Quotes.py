import os
import unittest

from EnvironmentWrapper import EnvironmentVariable

class TestEnvironmentVariable(unittest.TestCase):

    def setUp(self):
        self.var_name = "MY_TEST_VAR"
        self.var_value = "my_test_value"
        os.environ[self.var_name] = self.var_value

    def tearDown(self):
        # Clean up environment variable after each test
        os.environ.pop(self.var_name, None)

    def test_returns_value_when_env_var_exists(self):
        # Arrange
        env = EnvironmentVariable()

        # Act
        result = env(self.var_name)

        # Assert
        self.assertEqual(result, self.var_value)

    def test_returns_none_when_env_var_missing(self):
        # Arrange
        env = EnvironmentVariable()

        # Act
        result = env("SOME_MISSING_VAR")

        # Assert
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
