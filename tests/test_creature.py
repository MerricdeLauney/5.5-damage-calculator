from unittest.mock import patch
from src.damage_calculator.creature import Creature
from src.damage_calculator.attack import Attack
from pytest_mock import mocker

test_dummy = Creature("test_dummy", 0, [], 10000, 0)


# lvl 3 rogue weilding a rapier and using steady aim
rogue_attacks = [Attack(5, 3, [8, 6, 6])]
rogue = Creature("player", 5, rogue_attacks, 24, 16, origin_advantage=True)

basic_attack = Attack(5, 3 [8])
basic_creature = Creature("player", 5, [basic_attack], 24, 16)

@patch("random.randint")
def test_rogue(randint_mock):
    randint_mock.return_value = 1
    rogue.take_attacks([test_dummy])
    assert rogue.total_damage_dealt == 9

def _side_effect_randint(var1, var2):
        return var2

@patch('random.randint', side_effect='_side_effect_randint')
def test_attack(randint_mock):
    basic_attacker.attack(target_dummy)
    assert rogue.total_damage_dealt == 9
    
    


# def test_rogue():
#     mocked_random_choice = lambda : 1
#     with mocker.patch('random.randint', mocked_random_choice):
#         for _ in range(1):
#             rogue.attack([test_dummy])
#     assert(rogue.total_damage_dealt > 0 )