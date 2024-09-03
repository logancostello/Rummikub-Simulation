import random
from itertools import combinations

class Tile:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"{self.color} {self.value}"

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color

class Player:

    def __init__(self):
        self.bag = []
        for _ in range(2):
            for v in range(1, 14):
                for c in ["Blue", "Red", "Black", "Orange"]:
                    self.bag.append(Tile(c, v))

        self.tiles = []
        for _ in range(14):
            self.tiles.append(self.draw())

    def draw(self):
        tile = random.choice(self.bag)
        self.bag.remove(tile)
        return tile

    def __repr__(self):
        return f"{self.tiles}"

    def get_possible_combos(self):
        groups = self.get_groups()
        runs = self.get_runs()
        return groups + sets

    def get_groups(self):
        groups = []
        for value in range(1, 14):
            filtered = [tile for tile in self.tiles if tile.value == value]
            groups_of_three = list(combinations(filtered, 3))
            groups_of_four = list(combinations(filtered, 4))
            potential_groups = groups_of_three + groups_of_four
            for group in potential_groups:
                if not has_duplicates(group):
                    groups.append(group)
            return groups

def has_duplicates(list):
    seen = []
    # print("duplicates check" + f"{list}")
    for item in list:
        if item in seen:
            return True
        seen.append(item)
    return False

def remove_all(list, val):
    while val in list:
        list.remove(val)

if __name__ == '__main__':
    p = Player()
    print(p)
    print(p.get_groups())
