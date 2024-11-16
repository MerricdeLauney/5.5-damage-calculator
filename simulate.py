import pprint
import random
from typing import List

class Attack:
    attack_bonus = 0
    attack_damage_bonus = 0
    attack_damage_dice = []

    def __init__(self, attack_bonus,attack_damage_bonus, attack_damage_dice):
        self.attack_bonus = attack_bonus
        self.attack_damage_bonus = attack_damage_bonus
        self.attack_damage_dice = attack_damage_dice


class Creature:
    name = str
    initiative_bonus = 0
    attacks = List[Attack]
    health = int
    armorClass = int

    def __init__(self, name, initiative_bonus, attacks, health, armor_class):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.attacks = attacks
        self.health = health
        self.armor_class = armor_class

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
    def quick_stats(self):
        return f"""name: {self.name}, health: {self.health}"""
    
    # simulates making all the attacks and returns the list of foes killed this turn
    def attack(self, foes: List) -> List:
        foes_iter = iter(foes)
        try:
            foe = next(foes_iter)
        except StopIteration:
            return []
        dead_foes = []
        for attack in self.attacks:
            attack_roll = random.randrange(1,20) + attack.attack_bonus
            print(f'{self.name} attacks, {attack_roll} to hit')
            if attack_roll >= foe.armor_class:
                damage = sum([random.randrange(1,die_type) for die_type in attack.attack_damage_dice]) + attack.attack_damage_bonus
                print(f'{damage} damage')
                foe.health -= damage
                if foe.health <= 0:
                    dead_foes.append(foe)
                    try:
                        foe = next(foes_iter)
                    except StopIteration:
                        break
            else:
                print('miss')
        return dead_foes
                
                    
def simuate(player: Creature, monsters: List[Creature]):
    # roll initiative
    turns = []
    player.initiative = random.randrange(1,20) + player.initiative_bonus

    for monster in monsters:
        monster.initiative = random.randrange(1,20) + monster.initiative_bonus

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
                

        
        


