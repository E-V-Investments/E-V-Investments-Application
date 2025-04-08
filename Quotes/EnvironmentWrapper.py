import os

class EnvironmentVariable:
    def __call__(self, environment_variable_name: str):
        return os.getenv(environment_variable_name)
