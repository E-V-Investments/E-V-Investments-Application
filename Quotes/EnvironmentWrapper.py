import os

class EnvironmentVariable:
    def __getitem__(self, environment_variable_name: str):
        return os.getenv(environment_variable_name)
