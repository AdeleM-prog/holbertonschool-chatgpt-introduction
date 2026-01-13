#!/usr/bin/python3
import random
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than number of cells")

        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        # Nombre de cases sûres restant à révéler
        self.safe_left = width * height - len(self.mines)

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        ch = '*'
                    else:
                        count = self.count_mines_nearby(x, y)
                        ch = str(count) if count > 0 else ' '
                    print(ch, end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # ne pas compter la case elle-même
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Clique sur une mine → défaite
        if (y * self.width + x) in self.mines:
            return False

        # Case déjà révélée → ne rien faire mais ce n'est pas une défaite
        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True
        self.safe_left -= 1

        # Si aucune mine autour → propagation (révélation des voisins)
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def has_won(self):
        return self.safe_left == 0

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates must be within 0–{self.width - 1} for x "
                          f"and 0–{self.height - 1} for y.")
                    input("Press Enter to continue...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You cleared the field!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    # Optionnel : largeur, hauteur, mines passés en arguments
    if len(sys.argv) == 4:
        w = int(sys.argv[1])
        h = int(sys.argv[2])
        m = int(sys.argv[3])
        game = Minesweeper(w, h, m)
    else:
        game = Minesweeper()
    game.play()
