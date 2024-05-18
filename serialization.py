import json
# from main import Character

def save_to_json_file(file_path: str, character):
    with open(file_path, 'w') as json_file:
        json.dump(character, json_file, default=lambda o: o.__dict__)

# def load_from_json_file(file_path: str):
#     with open(file_path, 'r') as json_file:
#         data = json.load(json_file)
#         character = Character(data['name'], data['health'])
#         character.inventory = []
#         for item in data['inventory']:
#             if 'damage' in item:
#                 weapon = Weapon(**item)

def save_to_pickle_file(file_path: str):
    pass