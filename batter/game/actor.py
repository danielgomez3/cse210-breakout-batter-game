from game import constants
from game.point import Point

class Actor():
    def __init__(self):
        self._position = Point(0,0)
        self._text = ""
        self._velocity = Point(0,0)
   
    def set_text(self,text): #called from main
        self._text = text
    
    def set_position(self,position):
        self._position = position
   
    def set_velocity(self,velocity):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity 

    def get_position(self):
        return self._position
    
    def get_text(self):
        return self._text
    
    def get_length(self):
        return len(self._text)

# class Paddle(Actor):
    # def __init__(self):
        # super().__init__()
        # paddle_hitbox = []
        # for character in self._text:
            # paddle_hitbox.append(Point(
