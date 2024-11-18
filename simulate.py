import random
from typing import List
from creature import Creature
from attack import Attack

def simuate(player: Creature, monsters: List[Creature]):
    # roll initiative
    turns = []
    player.initiative = random.randint(1,20) + player.initiative_bonus

    for monster in monsters:
        monster.initiative = random.randint(1,20) + monster.initiative_bonus

    turns = [player] + monsters
    turns.sort(key=lambda creature: creature.initiative ,reverse=True)

    # begin fight
    while True:
        for creature in turns:
            print(f'{creature.name}s turn!')
            if creature.name == 'player':
                killed = creature.attack(monsters)
                for dead in killed:
                    turns.remove(dead)
                    monsters.remove(dead)
                if not monsters:
                    print('all monsters dead')
                    print(player.quick_stats())
                    return
            else:
                killed = creature.attack([player])
                if killed: # player was killed
                    print('player was killed')
                    print('remaining monsters:')
                    for monster in monsters:
                        print(monster.quick_stats())
                    return
        print('round complete')
        for creature in turns:
            print(creature.quick_stats())

# create our player
player_attacks = [Attack(5, 3, [8,6])]
player = Creature('player', 5, player_attacks, 30, 16)

# create our foes
brown_bear_attacks = [Attack(5, 4, [8]), Attack(5, 4, [6,6])]
brown_bear = Creature('brown_bear', 5, brown_bear_attacks, 34, 11)
monsters = [brown_bear]
simuate(player, monsters)           
                

        
        


