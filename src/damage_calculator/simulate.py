import random
from typing import List
from creature import Creature

def simulate(player: Creature, monsters: List[Creature]):
    # roll initiative
    turns = []
    player.initiative = random.randint(1, 20) + player.initiative_bonus

    for monster in monsters:
        monster.initiative = random.randint(1, 20) + monster.initiative_bonus

    turns = [player] + monsters
    turns.sort(key=lambda creature: creature.initiative, reverse=True)

    # begin fight
    rounds = 0
    while True:
        for creature in turns:
            print(f"{creature.name}s turn!")
            if creature.name == "player":
                killed = creature.take_attacks(monsters)
                for dead in killed:
                    turns.remove(dead)
                    monsters.remove(dead)
                if not monsters:
                    print("all monsters dead")
                    print(player.quick_stats())
                    return rounds
            else:
                killed = creature.take_attacks([player])
                if killed:  # player was killed
                    print("player was killed")
                    print("remaining monsters:")
                    for monster in monsters:
                        print(monster.quick_stats())
                    return rounds
        rounds += 1
        print("round complete")
        for creature in turns:
            print(creature.quick_stats())
