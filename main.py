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
        return groups + runs

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

    def get_runs(self):
        runs = []
        for color in ["Blue", "Red", "Black", "Orange"]:
            filtered = [tile for tile in self.tiles if tile.color == color]
            potential_runs = []
            # get all combinations of 3+
            for i in range(3, len(filtered) + 1):
                potential_runs += list(combinations(filtered, i))
            # sort by value within the combinations for processing
            sorted_potential_runs = []
            for run in potential_runs:
                sorted_potential_runs.append(sorted(run, key=lambda tile: tile.value))
            for run in sorted_potential_runs:
                if is_subsequent_increasing(run):
                    runs.append(run)
        return runs

    def highest_possible_score(self):
        playable_options = self.get_possible_combos()
        if len(playable_options) == 0:
            return 0
        else:
            max_score = 0
            for option in playable_options:
                # "play" it
                for tile in option:
                    self.tiles.remove(tile)

                score = sum([t.value for t in option]) + self.highest_possible_score()

                # unplay it
                for tile in option:
                    self.tiles.append(tile)

                max_score = max(max_score, score)
            return max_score

    def can_enter_game(self):
        return self.highest_possible_score() >= 30


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

def is_subsequent_increasing(list):
    for i in range(len(list) - 1):
        if list[i].value != list[i + 1].value - 1:
            return False
    return True

def simulate_n_starts(n):
    could_enter = 0
    for i in range(n):
        print(i)
        if Player().can_enter_game():
            could_enter += 1
    return could_enter / n

if __name__ == '__main__':
    print(simulate_n_starts(1000000))


