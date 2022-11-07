"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730471018"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point_2: Point) -> int:
        """Returns distance between 2 points."""
        dist: int = sqrt(((self.x - point_2.x) ** 2) + ((self.y - point_2.y) ** 2))
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign object's location to location with direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        elif self.is_infected() is True:
            return "red"
        elif self.is_immune() is True:
            return "blue"

    def contract_disease(self) -> None:
        """Reassign sickness attribute to "infected"."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Return true if sickness is "vulnerable" and false otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Return true if sickness is "infected" and false otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other: Cell) -> None:
        """If an infected cell and vulnerable cell come in contact, vulnerable cell becomes infected."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        elif self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None: 
        """Reassign sickness attribute to "immune"."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Return true if sickess is "immune" and false otherwise."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_count: int, immune_count: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_count <= 0 or infected_count >= cells:
            raise ValueError("Some number of cells less than total cells must begin infected.")
        if immune_count < 0 or immune_count >= cells:
            raise ValueError("Some number of cells less than total cells must begin immune.")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected_count):
            self.population[_].contract_disease()
            self.population[_].color()
        for _ in range(immune_count):
            self.population[_].immunize()
            self.population[_].color()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks distance between any two cells to see whether they come into contact."""
        i: int = 0
        index: int = 1
        while i < len(self.population):
            index = i + 1
            while index < len(self.population):
                if self.population[i].location.distance(self.population[index].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[index])
                index += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        complete: bool = False
        while i < len(self.population):
            if self.population[i].is_infected() is True:
                complete = False
                return False
            else: 
                complete = True
            i += 1
        if complete is True:
            return True
        else:
            return False