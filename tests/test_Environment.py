import unittest
import os
from Quotes.Environment import Environment


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = Environment()
        os.environ["ALPACA_API_KEY_ID"] = "test-key-id"
        os.environ["ALPACA_API_SECRET_KEY"] = "test-secret"

    def tearDown(self):
        # Clean up environment so tests are isolated
        os.environ.pop("ALPACA_API_KEY_ID", None)
        os.environ.pop("ALPACA_API_SECRET_KEY", None)

    def test_call_returns_env_var_value(self):
        result = self.env("ALPACA_API_KEY_ID")
        self.assertEqual(result, "test-key-id")

    def test_call_raises_error_if_missing(self):
        with self.assertRaises(EnvironmentError) as context:
            self.env("NON_EXISTENT_VAR")
        self.assertIn("Missing required environment variable: NON_EXISTENT_VAR", str(context.exception))

    def test_alpaca_api_key_property(self):
        result = self.env.alpaca_api_key
        self.assertEqual(result, "test-key-id")

    def test_alpaca_secret_key_property(self):
        result = self.env.alpaca_secret_key
        self.assertEqual(result, "test-secret")

    def test_constants_are_correct(self):
        self.assertEqual(self.env.ALPACA_API_KEY_ID, "ALPACA_API_KEY_ID")
        self.assertEqual(self.env.ALPACA_API_SECRET_KEY, "ALPACA_API_SECRET_KEY")


if __name__ == "__main__":
    unittest.main()
