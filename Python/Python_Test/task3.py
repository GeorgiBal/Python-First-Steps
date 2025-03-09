class Properties:
    def __init__(self, id, name, color, attack_damage, life, shield, capacity):
        self.id = int(id)
        self.name = str(name)
        self.color = str(color)
        self.attack_damage = int(attack_damage)
        self.life = int(life)
        self.shield = int(shield)
        self.capacity = int(capacity)


class Outrider(Properties):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity, plasma_defence):
        super().__init__(id, name, color, attack_damage, life, shield, capacity)
        self.plasma_defense = int(plasma_defence)
        self.life += 100

    def attack(self, battleship):
        if battleship == 'Millennium Falcon':
            MillenniumFalcon.take_damage(millenniumFalcon, self.attack_damage)
        elif battleship == 'Ebon Hawk':
            EbonHawk.take_damage(ebonHawk, self.attack_damage)

    def take_damage(self, damage):
        if self.shield - damage <= 0:
            self.life -= damage + self.shield - 50
            self.shield = 0
        else:
            self.shield -= damage - 50
        self.is_destroyed()

    def is_destroyed(self):
        if self.life <= 0:
            return True
        else:
            return False


class MillenniumFalcon(Properties):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity, dodge):
        super().__init__(id, name, color, attack_damage, life, shield, capacity)
        self.dodge = int(dodge)

    def attack(self, battleship):
        if battleship == 'Outrider':
            Outrider.take_damage(outrider, self.attack_damage*2)
        elif battleship == 'Ebon Hawk':
            EbonHawk.take_damage(ebonHawk, self.attack_damage*2)

    def take_damage(self, damage):
        if self.shield - damage <= 0:
            self.life -= damage + self.shield + 200
            self.shield = 0
        else:
            self.shield -= damage + 200
        self.is_destroyed()

    def is_destroyed(self):
        if self.life <= 0:
            return True
        else:
            return False


class EbonHawk(Properties):
    def __init__(self, id, name, color, attack_damage, life, shield, capacity):
        super().__init__(id, name, color, attack_damage, life, shield, capacity)

    def attack(self, battleship):
        if battleship == 'Outrider':
            Outrider.take_damage(outrider, self.attack_damage)
        elif battleship == 'Millennium Falcon':
            MillenniumFalcon.take_damage(millenniumFalcon, self.attack_damage)

    def take_damage(self, damage):
        if self.shield - damage <= 0:
            self.life -= damage + self.shield
        else:
            self.shield -= damage
        self.is_destroyed()

    def is_destroyed(self):
        if self.life <= 0:
            return True
        else:
            return False

    def heal(self, heal):
        self.life += heal


outrider = Outrider(1, 'Outrider', 'Black', 500, 500, 100, 150, 100)
millenniumFalcon = MillenniumFalcon(2, 'Millennium Falcon', 'White', 60, 500, 100, 150, 50)
ebonHawk = EbonHawk(3, 'Ebon Hawk', 'Black', 40, 500, 100, 150)
