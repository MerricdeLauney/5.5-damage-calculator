from creature import Creature
from attack import Attack
from simulate import simulate

# create our players
# lvl 3 rogue weilding a longbow and steady aim
rogue_attacks = [Attack(5, 3, [8, 6, 6])]
rogue = Creature("player", 5, rogue_attacks, 24, 16, origin_advantage=True)

# lvl 3 fighter wielding two scimitars 
fighter_attacks = [Attack(5, 3, [6]), Attack(5, 3, [6])]
fighter = Creature("player", 5, fighter_attacks, 28, 16)

# lvl 3 barbarian with great sword and reckless
barbarian_attacks = [Attack(5, 5, [12])]
barbarian = Creature("player", 5, barbarian_attacks, 32, 16, origin_advantage=True, origin_disadvantage=True)


# create our foes
brown_bear_attacks = [Attack(5, 4, [8]), Attack(5, 4, [6, 6])]
brown_bear = Creature("brown_bear", 5, brown_bear_attacks, 34, 11)
monsters = [brown_bear]

print('rogue')
simulate(rogue, monsters)
brown_bear = Creature("brown_bear", 5, brown_bear_attacks, 34, 11)
print('fighter')
simulate(fighter, [brown_bear])
brown_bear = Creature("brown_bear", 5, brown_bear_attacks, 34, 11)
print('barbarian')
simulate(barbarian, [brown_bear])
