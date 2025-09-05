from business_object.attack.abstract_formula_attack import AbstractFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SpecialFormulaAttack(AbstractFormulaAttack): 

    def __init__(self, power=0, name=None, description=None):
        super().__init__(power, name, description)

    def get_attack_stat(APkm: AbstractPokemon) -> float:
        return APkm.attack_current
    
    def get_defense_stat(APkm: AbstractPokemon) -> float:
        return APkm.defense_current


    


