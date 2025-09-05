from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = FixedDamageAttack(10, "test", "desc")
        snorlax1 = AttackPokemon(stat_current=Statistic(speed=100, attack=100))
        snorlax2 = AttackPokemon(stat_current=Statistic(speed=100, attack=100))

        # WHEN
        attack = snorlax.compute_damage(snorlax1, snorlax2)

        # THEN
        assert attack == 10
        

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
    snorlax1 = AttackPokemon(stat_current=Statistic(speed=100, attack=100))
