from unittest.mock import patch
from src.damage_calculator.creature import Creature
from src.damage_calculator.attack import Attack
from pytest_mock import mocker


def test_creature(
    name="name",
    initiative_bonus=0,
    attacks=Attack(0, 0, []),
    health=0,
    armor_class=0,
    origin_advantage=False,
    origin_disadvantage=False,
    target_advantage=False,
    target_disadvantage=False,
):

    return Creature(
        name,
        initiative_bonus,
        attacks,
        health,
        armor_class,
        origin_advantage,
        origin_disadvantage,
        target_advantage,
        target_disadvantage,
    )


test_dummy = test_creature(health=1000)


# lvl 3 rogue weilding a rapier and using steady aim
rogue_attacks = [
    Attack(5, 3, [8, 6, 6]),
]
rogue = test_creature(name="player", attacks=rogue_attacks, origin_advantage=True)

basic_attack = Attack(5, 3, [8])
basic_creature = Creature("player", 5, [basic_attack], 24, 16)


def return_average(var1, var2):
    return (var1 + var2) / 2


@patch("random.randint", side_effect=return_average)
def test_roll_damage(randint_mock):
    assert basic_creature.roll_damage(basic_attack, False) == 7.5


@patch("random.randint", side_effect=return_average)
def test_take_attacks(randint_mock):
    rogue.total_damage_dealt == 0
    rogue.take_attacks([test_dummy])
    assert rogue.total_damage_dealt == 3 + 4.5 + 3.5 + 3.5


@patch("random.randint")
def test_calculate_roll_against(randint_mock):
    randint_mock.side_effect = [5, 10, 15, 20]
    # when neither creature has advantage modifiers
    straight_roll = basic_creature.calculate_roll_against(test_dummy)
    assert straight_roll == 5

    # rogue with advantage against normal target
    randint_mock.side_effect = [5, 10, 15, 20]
    advantage_roll = rogue.calculate_roll_against(test_dummy)
    assert advantage_roll == 10

    # when the target_creature provides disadvantage
    evasive_target = test_creature(target_disadvantage=True)
    randint_mock.side_effect = [20, 15, 5, 5]
    disadvantage_roll = basic_creature.calculate_roll_against(evasive_target)
    assert disadvantage_roll == 15

    # when advantage and disadvantage cancel out
    randint_mock.side_effect = [20, 15, 10, 5]
    straight_roll = rogue.calculate_roll_against(evasive_target)
    assert straight_roll == 20
    second_straight_roll = rogue.calculate_roll_against(evasive_target)
    assert second_straight_roll == 15
