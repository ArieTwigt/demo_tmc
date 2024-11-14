import random


class Dice:

    def __init__(self, sides: int, 
                       color: str="red"):
        self.sides = sides
        self.color = color
        
    
    def throw(self):
        possible_throws = range(1, self.sides + 1)
        result = random.choice(possible_throws)
        print(f"You threw: {result} 🎲")
        return result
    
    def __repr__(self) -> str:
        return f"A dice {self.color} with {self.sides} "