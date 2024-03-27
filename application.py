"""
Author: Lane Missel
Created: March 25, 2024

Contains Application class.
"""

import sqlite3

from player import Player
from team import Team

class Application:
    """
    Class for managing application data and api.
    """
    def __init__(self, savename: str):
        self.savename: str = savename
        self.connection: sqlite3.Connection = sqlite3.connect(self.savename + ".db")
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        self.state = None

    def add_result(self, year: int, week: int, home: int, score: list, overtime: bool) -> None:
        """
        Updates given entry in database with result.
        """
        pass

    def close(self) -> None:
        """
        Saves application state.
        """
        pass

    def create_database(self) -> None:
        """
        Creates new application database.
        """
        pass
    
    def create_schedule(self) -> None:
        """
        Adds the current years game to the application database.        
        """
        pass

    def draft(self, players: list, team_ids: list, yob_range: list) -> None:
        """
        Returns teams given a list of players.
        """
        pass

    def draft_group(self, players: list, teams: list, yob_range: list) -> list:
        """
        Draft players for given teams and returns undrafted players>
        """
        pass

    def draft_round(self, players: list, teams: list, yob_range: list) -> list:
        """
        Selects a player for each team in teams adhering to the given
        yob range, returns undrafted players.
        """
        pass

    def get_goaltenders(self) -> list:
        """
        Returns all goaltenders in application database.
        """
        pass

    def get_leagues(self) -> list:
        """
        Returns list of all leagues.
        """
        pass

    def get_league_ids(self) -> list:
        """
        Returns all ids for leagues in database.
        """
        pass

    def get_league_info(self, league_id: int):
        """
        Returns league information from database.
        """
        pass

    def get_player(self, player_id: int) -> Player:
        """
        Returns player corresponding to given player_id.
        """
        pass

    def get_players(self) -> list:
        """
        Returns all players in database.
        """
        pass

    def get_player_ids(self) -> list:
        """
        Returns all player ids in application database.
        """
        pass

    def get_schedule(self) -> list:
        """
        Returns table of current years schedule.
        """
        pass

    def get_team(self, team_id: int) -> Team:
        """
        Returns team corresponding to given team_id.
        """
        pass

    def get_teams(self) -> list:
        """
        Returns list of all teams.
        """
        pass

    def get_teams_by_league(self, league_id: int) -> list:
        """
        Returns all teams assigned to the given league_id.
        """
        pass

    def get_skaters(self) -> list:
        """
        Returns all skaters in database.
        """
        pass

    def load_state(path: str = None) -> None:
        """
        Loads application state from given file.
        """
        pass

    def sim_week(self) -> None:
        """
        Simulates the current week's games and updates database.
        """
        pass

    def update_player(self, player_id: int, team_id: int = None, rights: int = None) -> None:
        """
        Updates the application database to set a player's team and rights.
        """
        pass