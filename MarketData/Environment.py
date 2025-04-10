# This class wraps access to environment variables so that we are not directly calling os.getenv()
# all over the codebase. Centralizing access here makes it easier to mock the environment during
# unit tests and avoids repeating the same string constants in multiple places.
#
# To access an environment variable, either:
#     * Use the __call__ method with the string name (e.g., env("ALPACA_API_KEY_ID"))
#     * Or use a named property (e.g., env.alpaca_api_key)
#
# This class also holds constants for known environment variable names.
# Please keep these constants in alphabetical order.
#
# To add support for a new environment variable:
#     1. Add a new constant (e.g., FOO_SERVICE_TOKEN = "FOO_SERVICE_TOKEN")
#     2. Optionally add a property for more readable access (e.g., .foo_service_token)

import os


class Environment:
    # Constants for environment variable names
    # Please keep this list in alphabetical order.
    ALPACA_API_KEY = "ALPACA_API_KEY"
    ALPACA_SECRET_KEY = "ALPACA_SECRET_KEY"

    def __call__(self, environment_variable_name: str):
        value = os.getenv(environment_variable_name)
        if value is None:
            raise EnvironmentError(f"Missing required environment variable: {environment_variable_name}")
        return value

    @property
    def alpaca_api_key(self) -> str:
        return self(self.ALPACA_API_KEY)

    @property
    def alpaca_secret_key(self) -> str:
        return self(self.ALPACA_SECRET_KEY)
