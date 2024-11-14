from game.dices import Dice

class Game:

    def __init__(self, 
                 dice=Dice,
                 name:str="My Game",
                 max_turns:int=5):
        self.name = name
        self.dice = dice
        self.throws = []
        self.score = 0
        self.max_turns = max_turns


    
    def take_turn(self):
        if len(self.throws) < self.max_turns:
            result = self.dice.throw()
            self.throws.append(result)

            # update score
            self.score += result
        else:
            print("Game is over")

        

    def show_score(self):
        print(f"Current score: {self.score}")



    def __repr__(self) -> str:
        description = f'''
                      Game: {self.name}
                      Throws: {self.throws}
                      Score: {self.score}
                      Turn: {len(self.throws)}
                      Max turns: {self.max_turns}
                       '''
        return description