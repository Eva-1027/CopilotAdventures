class Creature:
    def __init__(self, name, power, icon, start):
        self.name = name
        self.power = power
        self.icon = icon
        self.position = start

    def move(self, direction):
        x, y = self.position
        if direction == 'UP':
            new_position = (x - 1, y)
        elif direction == 'DOWN':
            new_position = (x + 1, y)
        elif direction == 'LEFT':
            new_position = (x, y - 1)
        elif direction == 'RIGHT':
            new_position = (x, y + 1)
        else:
            new_position = self.position

        return new_position


class GridlockArena:
    def __init__(self, grid_size):
        self.grid = [['⬜️' for _ in range(grid_size)] for _ in range(grid_size)]
        self.scores = {}

    def add_creature(self, creature):
        self.scores[creature.name] = 0
        self.grid[creature.position[0]][creature.position[1]] = creature.icon

    def apply_move(self, creature, direction, move_number):
        old_position = creature.position
        new_position = creature.move(direction)
        creature.position = new_position

        # Check if another creature is in the new position
        for other_creature_name in self.scores.keys():
            if other_creature_name != creature.name:
                other_creature = next(c for c in [creature1, creature2, creature3] if c.name == other_creature_name)
                if other_creature.position == new_position:
                    # Both creatures inflict damage on each other
                    self.scores[creature.name] = creature.power - other_creature.power
                    self.scores[other_creature_name] = other_creature.power - creature.power
                    self.grid[new_position[0]][new_position[1]] = '🤺'
                    return
        # Update the grid
        self.grid[old_position[0]][old_position[1]] = '⬜️'
        if self.grid[new_position[0]][new_position[1]] != '🤺':
            self.grid[new_position[0]][new_position[1]] = creature.icon

    def print_grid(self, move_number):
        print(f"Move {move_number}")
        for row in self.grid:
            print(' '.join(row))
        print('Scores:', self.scores)

arena = GridlockArena(5)

creature1 = Creature('Dragon', 7, '🐉', (2, 2))
creature2 = Creature('Goblin', 3, '👺', (2, 3))
creature3 = Creature('Ogre', 5, '👹', (0, 0))

arena.add_creature(creature1)
arena.add_creature(creature2)
arena.add_creature(creature3)

moves = [('Dragon', 'RIGHT'), ('Goblin', 'LEFT'), ('Ogre', 'RIGHT'), ('Dragon', 'LEFT'), ('Goblin', 'RIGHT'), ('Ogre', 'DOWN'), ('Dragon', 'DOWN'), ('Goblin', 'UP'), ('Ogre', 'DOWN')]

move_counter = 1
total_moves = len(moves)/3

# Print the initial board
arena.print_grid('Initial Board')

while move_counter <= total_moves:
    name, direction = moves[move_counter - 1]
    creature = next(c for c in [creature1, creature2, creature3] if c.name == name)
    arena.apply_move(creature, direction, move_counter - 1)
    arena.print_grid(f'Move {move_counter}')
    move_counter += 1

print("Final scores:", arena.scores)