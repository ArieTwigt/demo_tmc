from game.games import Game
from game.dices import Dice
from game import MY_VAR

name = "Dirk"

pass

if __name__ == '__main__':
    my_dice = Dice(color="blue", sides=8)

    my_game = Game(my_dice)
    my_game_2 = Game(my_dice)
    print(MY_VAR)
    pass

