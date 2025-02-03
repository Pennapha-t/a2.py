import random

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def use(self):
        return f"Using {self.name} to attack with power {self.attack_power}"

class Monster:
    def __init__(self, name, health, attack_level):
        self.name = name
        self.health = health
        self.attack_level = attack_level
        self.weapons = []
        self.current_weapon = None

    def attack(self):
        return f"{self.name} attacks with power {self.attack_level}"

    def add_weapon(self, weapon):
        if len(self.weapons) < 2:
            self.weapons.append(weapon)
            if len(self.weapons) == 1:
                self.current_weapon = weapon

    def switch_weapon(self):
        if len(self.weapons) > 1:
            self.current_weapon = self.weapons[1] if self.current_weapon == self.weapons[0] else self.weapons[0]
            return f"{self.name} switched to {self.current_weapon.name}"
        return f"{self.name}"

    def use_weapon(self):
        if self.current_weapon:
            return self.current_weapon.use()
        return f"{self.name}"

class Dragon(Monster):
    def __init__(self, name, health, attack_level, element):
        super().__init__(name, health, attack_level)
        self.element = element

    def breathe_fire(self):
        return f"{self.name} breathes {self.element} Blow"

class MonsterNameGenerator:
    def __init__(self):
        self.animal_names = [
            "Tiger", "Lion", "Wolf", "Eagle", "Hawk", "Bear", "Panther", "Cobra", "Leopard", "Falcon",
            "Cat", "Shark", "Dog", "Cow", "Goat", "Hyena", "Jaguar", "Python", "Buffalo", "Tarantula"
        ]
        self.used_names = set()

    def generate_name(self):
        if len(self.used_names) >= len(self.animal_names):
            return "Unknown Monster"
        while True:
            name = random.choice(self.animal_names)
            if name not in self.used_names:
                self.used_names.add(name)
                return name

name_generator = MonsterNameGenerator()

weapon_list = [ Weapon("Sword", 45),Weapon("Fire Bow", 60),Weapon("Club", 65),Weapon("Shuriken", 50), ]

monsters = []
for i in range(20):
    monster_name = name_generator.generate_name()
    monster = Dragon(monster_name, random.randint(100, 200), random.randint(20, 50), "Blow")
    monster.add_weapon(random.choice(weapon_list))
    monster.add_weapon(random.choice(weapon_list))
    monsters.append(monster)

for monster in monsters:
    print(monster.attack())
    print(monster.use_weapon())
    print(monster.switch_weapon())
    print(monster.use_weapon())
    print(monster.breathe_fire())
    print("-" * 30)