
# Створити клас-персонаж гри, в якого є імʼя, кількість здоровʼя та інвентар. 
# Дати можливість віднімати здоровʼя, додавати здоровʼя та додавати речі в інвентар

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def add_health(self, amount):
        self.health += amount

    def substract_health(self, amount):
        self.health -= amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

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
