import copy
from spells import mirror_clone_shallow, copyramus
# Створити клас-персонаж гри, в якого є імʼя, кількість здоровʼя та інвентар. 
# Дати можливість віднімати здоровʼя, додавати здоровʼя та додавати речі в інвентар

class Character:
    def __init__(self, name, health=100):
        self.name = name
        # self._health = Character.limit_health_amount(health)
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

    # @staticmethod
    # def limit_health_amount(amount):
    #     return min(amount, 100)
    # @classmethod

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, amount):
        # if amount > 100:
        #     amount = 100
        self._health = min(amount, 100)

    def add_health(self, amount):
        self._health += amount

    def subtract_health(self, amount):
        self.health -= amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def attack(self, other_character):
        if self.weapon is not None:
            other_character.subtract_health(self.weapon.damage)
        else:
            other_character.subtract_health(5)

    def __copy__(self):
        # Character('fsf')
        # cls = Character
        cls = self.__class__
        new_character = cls.__new__(cls)
        new_character.__dict__.update(self.__dict__)
        new_character.__dict__['name'] += ' Shallow copy'
        # new_character.name += ' Shallow copy'
        return new_character
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        new_character = cls.__new__(cls)
        memo[id(self)] = new_character
        for k, v in self.__dict__.items():
            # new_character.__dict__[k] = copy.deepcopy(v, memo)
            setattr(new_character, k, copy.deepcopy(v, memo))
        new_character.name += ' Evil clone'
        return new_character

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

    # def __str__(self) -> str:
    #     return f'Item(name={self.name})'


class Weapon(InventoryItem):
    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.damage = damage


class Potion(InventoryItem):
    def __init__(self, name, health_amount) -> None:
        super().__init__(name)
        self.health_amount = health_amount


if __name__ == '__main__':
    print('Create items')
    # InventoryItem.__new__(InventoryItem)
    item_one = InventoryItem('Sword')
    print(item_one.name)

    item_one.name = 'Shield'
    print(item_one.name)

    print('\nCreate hero and set health')
    character_one = Character('Hero')
    print(character_one.health)
    character_one.health = 120
    print(character_one.health)
    character_one.health = 50
    print(character_one.health)
    
    print('\nCreate sword and set as hero weapon')
    sword = Weapon('Sword', 15)

    character_one.add_to_inventory(sword)
    character_one.set_weapon('Sword')

    print(character_one.weapon)

    print('\nCreate villain and attack')
    character_two = Character('Villain')
    print(character_two.health)
    character_one.attack(character_two)
    print(character_two.health)

    character_two.attack(character_one)
    print(character_one.health)


    # print(InventoryItem.__new__(InventoryItem).name)
    # item = InventoryItem('Sword')
    # print(item.__dict__)
    # # item.__dict__.update({'damage', 15})
    # item.__dict__['damage'] = 15
    # print(item.__dict__)
    # print(item.damage)

    character_three = mirror_clone_shallow(character_one)
    print(character_three.name)

    character_four = copyramus(character_one)
    print(character_four.name)
