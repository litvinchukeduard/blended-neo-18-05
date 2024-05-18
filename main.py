
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