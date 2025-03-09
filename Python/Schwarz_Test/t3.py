from abc import ABC


class Battleship(ABC):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity):
        self.id = id
        self.name = name
        self.color = color
        self.attack_damage = attack_damage
        self.life = life
        self.shield = shield
        self.capacity = capacity

    def attack(self, battleship):
        battleship.take_damage(self.attack_damage)

    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.life += self.shield
                self.shield = 0
        else:
            self.life -= damage

    def is_destroyed(self):
        return self.life <= 0


class Outrider(Battleship):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity, plasma_defense):
        super().__init__(id, name, color, attack_damage, life + 100, shield, capacity)
        self.plasma_defense = plasma_defense

    def attack(self, battleship):
        battleship.take_damage(self.attack_damage - 50)


class MillenniumFalcon(Battleship):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity, dodge):
        super().__init__(id, name, color, attack_damage, life, shield, capacity)
        self.dodge = dodge

    def attack(self, battleship):
        battleship.take_damage(self.attack_damage * 2)

    def take_damage(self, damage):
        super().take_damage(damage + 200)


class EbonHawk(Battleship):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity):
        super().__init__(id, name, color, attack_damage, life, shield, capacity)

    def heal(self, life):
        self.life += life
