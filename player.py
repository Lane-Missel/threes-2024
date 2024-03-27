"""
Author: Lane Missel
Created: March 25, 2024

Contains Player class and classes that inherit from Player (Skater, Goaltender).
"""

class Player:
    """
    Player object for application, teams and simulator.
    """
    def __init__(self, player_id: int, first: str, last: str, yob: int,
            position: str, passing: int, fitness: int):
        
        self.player_id = player_id
        self.first = first
        self.last = last
        self.position = position
        self.yob = yob
        self._passing = passing
        self.fitness = fitness
        self.statistics = None
        self.energy = None

    @property
    def passing(self) -> int:
        return self._correct_for_energy(self._passing)

    def play(self) -> None:
        """
        Updates time on ice and energy.
        """
        pass

    def reset(self) -> None:
        """
        Updates energy based on fitness.
        """
        self.energy += self.fitness

    def update(self, year: int) -> None:
        """
        Updates skills based on age calculated with given year.
        """
        pass

    def _correct_for_energy(self, value: int) -> int:
        """
        Corrects value for player's energy level.
        """
        pass

class Skater(Player):
    """
    Skater object for application, teams and simulator.
    """
    def __init__(self, player_id: int, first: str, last: str, yob: int,
            position: str, passing: int, fitness: int, shooting: int,
            intelligence: int, defending: int):
        
        super().__init__(player_id, first, last, yob, position, passing, fitness)

        self.position = position
        self._shooting = shooting
        self._defending = defending
        self.intelligence = intelligence

    @property
    def overall(self) -> int:
        return int((self.shooting + self.passing + self.defending + 0.5*self.intelligence)/3.5)

    @property
    def possession(self) -> int:
        return self.defending + self.passing
    
    @property
    def offense(self) -> int:
        return self.shooting + self.passing
    
    @property
    def shooting(self) -> int:
        return self._correct_for_energy(self._shooting)
    
    @property
    def defending(self) -> int:
        return self._correct_for_energy(self._defending)

    def skater_update(self, year) -> None:
        """
        Updates skills based on age calculated with given year.
        """
        pass

    @classmethod
    def random(self, position: str):
        """
        Creates a Player with random attributes.
        """
        pass

    @classmethod
    def from_tuple(self, value: tuple):
        """
        Returns object initilized from provided tuple.
        """
        pass

class Goaltender(Player):
    """
    Goaltender object for application, teams and simulator.
    """
    def __init__(self, player_id: int, first: str, last: str, yob: int,
            passing: int, fitness: int, goaltending: int, desperation: int):
        
        super().__init__(player_id, first, last, yob, "g", passing, fitness)

        self._goaltending = goaltending
        self._desperation = desperation

    @property
    def overall(self) -> int:
        return int((self.goaltending + 0.1*self.desperation + 0.1*self.passing) / 1.2)

    @property
    def goaltending(self) -> int:
        return self._correct_for_energy(self._goaltending)
    
    @property
    def deperation(self) -> int:
        return self._correct_for_energy(self._desperation)


    def goaltender_update(self, year: int) -> None:
        """
        Updates skills based on age calculated with given year.
        """
        pass

    @classmethod
    def random(self):
        """
        Creates an instance with random attributes.
        """
        pass

    @classmethod
    def from_tuple(self, value: tuple):
        """
        Returns object initilized from provided tuple.
        """
        pass