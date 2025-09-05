from business_object.attack.abstract_attack import AbstractAttack
from abc import ABC, abstractmethod
from business_object.pokemon.abstract_pokemon import AbstractPokemon
import numpy as np
import random 


class AbstractFormulaAttack(AbstractAttack):

    def __init__(self, power=0, name=None, description=None):
        super().__init__(power, name, description)

    @abstractmethod
    def get_attack_stat(APkm: AbstractPokemon) -> float:
        pass

    @abstractmethod
    def get_defense_stat(APkm: AbstractPokemon) -> float:
        pass

    def compute_damage(self, APkm1, APkm2) -> int:
        att = self.get_attack_stat(APkm1)
        deff = self.get_defense_stat(APkm2)
        power = self._power
        random = round(random.uniform(0.85, 1.00), 100)
        level = APkm1.level 
        num = (((2*level)/5)+2) * power * att
        denom = deff * 50
        return ((num/denom)+2)*random


    