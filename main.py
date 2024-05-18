
# Створити клас-персонаж гри, в якого є імʼя, кількість здоровʼя та інвентар. 
# Дати можливість віднімати здоровʼя, додавати здоровʼя та додавати речі в інвентар

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self._health = health
        self.inventory = []

    @property
    def health(self):
        return self._health

    @health.setter
    def set_health(self, amount):
        # if amount > 100:
        #     amount = 100
        self._health = min(amount, 100)

    def add_health(self, amount):
        self._health += amount

    def substract_health(self, amount):
        self._health -= amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

# Створити ієрархію предметів, які можна додавати в інвентар. 
# В базового класу має бути властивість name, для якої задати геттер та сеттер

class Item:
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


class Weapon(Item):
    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.damage = damage


class Potion(Item):
    def __init__(self, name, health_amount) -> None:
        super().__init__(name)
        self.health_amount = health_amount


if __name__ == '__main__':
    item_one = Item('Sword')
    print(item_one.name)

    item_one.name = 'Shield'
    print(item_one.name)
