
# Створити клас-персонаж гри, в якого є імʼя, кількість здоровʼя та інвентар. 
# Дати можливість віднімати здоровʼя, додавати здоровʼя та додавати речі в інвентар

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self._weapon = None

    @property
    def weapon(self):
        return self._weapon
    
    # @weapon.setter
    def set_weapon(self, weapon_name: str):
        try:
            weapon = next(filter(lambda item: item.name == weapon_name, self.inventory))
            self._weapon = weapon
        except StopIteration:
            pass
        # for item in self.inventory:
        #     if item.name == weapon_name:
        #         self._weapon = item

    def add_health(self, amount):
        self.health += amount

    def subtract_health(self, amount):
        self.health -= amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def attack(self, other_character):
        if self.weapon is not None:
            other_character.subtract_health(self.weapon.damage)
        else:
            other_character.subtract_health(5)

# Створити ієрархію предметів, які можна додавати в інвентар. 
# В базового класу має бути властивість name, для якої задати геттер та сеттер

class InventoryItem:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        # print('Using item getter')
        return self._name
    
    @name.setter
    def name(self, new_name):
        # print('Using item setter')
        self._name = new_name

    def __str__(self) -> str:
        return f'Item(name={self.name})'


class Weapon(InventoryItem):
    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.damage = damage


class Potion(InventoryItem):
    def __init__(self, name, health_amount) -> None:
        super().__init__(name)
        self.health_amount = health_amount


if __name__ == '__main__':
    item_one = InventoryItem('Sword')
    print(item_one.name)

    item_one.name = 'Shield'
    print(item_one.name)

    character = Character('Hero')
    sword = Weapon('Sword', 15)

    character.add_to_inventory(sword)
    character.set_weapon('Sword')

    print(character.weapon)

    character_two = Character('Villain')
    print(character_two.health)
    character.attack(character_two)
    print(character_two.health)

    character_two.attack(character)
    print(character.health)
