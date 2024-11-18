import random
from attack import Attack
from typing import List

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
    
    # determine the attack roll acouting for origin and sources conditions
    def calulculate_roll_against(self, target_creature) -> int:
        return random.randint(1,20)
    
    # simulates making all the attacks and returns the list of foes killed this turn
    def attack(self, foes: List) -> List:
        foes_iter = iter(foes)
        try:
            foe = next(foes_iter)
        except StopIteration:
            return []
        dead_foes = []
        for attack in self.attacks:
            attack_roll = self.calulculate_roll_against(foe)
            to_hit = attack_roll + attack.attack_bonus
            print(f'{self.name} attacks, {to_hit} to hit')
            if to_hit >= foe.armor_class:
                dice_damage = sum([random.randint(1,die_type) for die_type in attack.attack_damage_dice])
                if attack_roll == 20:
                    print('crit!')
                    dice_damage += sum([random.randint(1,die_type) for die_type in attack.attack_damage_dice]) # roll again for crit
                damage = dice_damage + attack.attack_damage_bonus
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