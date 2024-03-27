"""
Author: Lane Missel
Created: March 25, 2024

Contains Team class.
"""

from simulator import Line
from player import Player

class Team:
    """
    Team object for managing players on team.
    """
    def __init__(self, team_id: int, forwards: list, defenders: list,
            goaltenders: list, thresholds: list, strategies: list):
        
        self.team_id = team_id
        self.forwards = forwards
        self.defenders = defenders
        self.goaltenders = goaltenders
        self.thresholds = thresholds
        self.strategies = strategies
        self.sort_func = lambda x: x.overall

    def add_player(self, player: Player) -> None:
        """
        Adds player to team according to position.
        """
        pass

    def get(self) -> Line:
        """
        Returns best players given current strategy.
        """
        pass

    def get_players(self) -> list:
        """
        Returns all players of team as a single list.
        """
        pass

    def update(self, diff: int) -> None:
        """
        Updates team strategy based on score differencial.
        """
        pass

    def needs(self) -> dict:
        """
        Returns a dictionary corresponding to positions missing from team.
        """
        pass

    def pick(self, players: list, yob_range: list) -> int:
        """
        Returns best player that fits team needs.
        """
        pass