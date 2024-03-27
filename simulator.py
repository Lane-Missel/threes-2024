"""
Author: Lane Missel
Created: March 25, 2024

Contains Simulator class.
"""

class Simulator:
    """
    Object for simulating a hockey game.
    """
    def __init__(self, config: dict = None):
        self.teams = None
        self.score = None
        self.event_log = None
        self.period = None
        self.overtime = None
        self.config = {"periods": 3,
                       "length": 600,
                       "overtime": False}
        
        if config is None:
            return
        
        # modify optional configuration of game engine.
        for key, value in config:
            self.config[key] = value

    def new_game(self, teams: list) -> None:
        """
        Prepares object for running new simulation.
        """
        pass

    def start(self) -> None:
        """
        Starts the simulation.
        """
        pass

    def sim_period(self, overtime = False) -> None:
        """
        Simulates a period of hockey given object state.
        """
        pass


    def sim_shift(self, lines) -> int:
        """
        Takes given players and simualtes a shift.
        Returns -1 on no goal, otherwise index of scoring team.
        """
        pass

class Line:
    """
    Represents the players a team currently has on the ice.
    """
    def __init__(self):
        pass