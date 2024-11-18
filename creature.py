import random
from attack import Attack
from typing import List


class Creature:
    name = str
    initiative_bonus = 0
    attacks = List[Attack]
    health = int
    armorClass = int
    conditions = List[str]
    origin_advantage = bool
    target_advantage = bool
    origin_disadvantage = bool
    target_disadvantage = bool
    total_damage_dealt = int

    def __init__(
        self,
        name,
        initiative_bonus,
        attacks,
        health,
        armor_class,
        origin_advantage=False,
        origin_disadvantage=False,
        target_advantage=False,
        target_disadvantage=False,
    ):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.attacks = attacks
        self.health = health
        self.armor_class = armor_class
        self.origin_advantage = origin_advantage
        self.target_advantage = target_advantage
        self.origin_disadvantage = origin_disadvantage
        self.target_disadvantage = target_disadvantage
        self.total_damage_dealt = 0

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def quick_stats(self):
        return f"""name: {self.name}, health: {self.health}, damage_dealt: {self.total_damage_dealt}"""

    # determine the attack roll acouting for origin and sources conditions
    def calculate_roll_against(self, target_creature) -> int:
        advantage = self.origin_advantage or target_creature.target_advantage
        disadvantage = self.origin_disadvantage or target_creature.target_disadvantage

        if advantage:
            if disadvantage:
                return random.randint(1, 20)
            else:
                return max(random.randint(1, 20), random.randint(1, 20))

        elif disadvantage:
            return min(random.randint(1, 20), random.randint(1, 20))

        else:
            return random.randint(1, 20)

    # simulates making all the attacks and returns the list of foes killed this turn
    def attack(self, foes: List) -> List:
        foes_iter = iter(foes)
        try:
            foe = next(foes_iter)
        except StopIteration:
            return []
        dead_foes = []
        for attack in self.attacks:
            attack_roll = self.calculate_roll_against(foe)
            to_hit = attack_roll + attack.attack_bonus
            print(f"{self.name} attacks, {to_hit} to hit")
            if to_hit >= foe.armor_class:
                dice_damage = sum(
                    [
                        random.randint(1, die_type)
                        for die_type in attack.attack_damage_dice
                    ]
                )
                if attack_roll == 20:
                    print("crit!")
                    dice_damage += sum(
                        [
                            random.randint(1, die_type)
                            for die_type in attack.attack_damage_dice
                        ]
                    )  # roll again for crit
                damage = dice_damage + attack.attack_damage_bonus
                self.total_damage_dealt += damage
                print(f"{damage} damage")
                foe.health -= damage
                if foe.health <= 0:
                    dead_foes.append(foe)
                    try:
                        foe = next(foes_iter)
                    except StopIteration:
                        break
            else:
                print("miss")
        return dead_foes
