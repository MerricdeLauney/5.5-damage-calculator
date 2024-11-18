class Attack:
    attack_bonus = 0
    attack_damage_bonus = 0
    attack_damage_dice = []

    def __init__(self, attack_bonus,attack_damage_bonus, attack_damage_dice):
        self.attack_bonus = attack_bonus
        self.attack_damage_bonus = attack_damage_bonus
        self.attack_damage_dice = attack_damage_dice