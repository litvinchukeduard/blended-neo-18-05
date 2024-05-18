import copy
# from main import Character

def mirror_clone_shallow(character): #-> Character:
    return copy.copy(character)

def copyramus(character): #-> Character:
    return copy.deepcopy(character)
