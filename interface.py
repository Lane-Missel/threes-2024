"""
Author: Lane Missel
Created: March 25, 2024

Contains Interface class for the application.
"""

from application import Application


class Interface:
    """
    Command line interface for interacting with the application.
    """
    def __init__(self, application: Application):
        self.application = application

    def run(self) -> None:
        """
        Starts loop to fetch commands from the user.
        Passes commands onto application.
        """
        pass
