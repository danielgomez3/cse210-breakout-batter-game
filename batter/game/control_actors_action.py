from game import constants
from game.action import Action


class ControlActorsAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        #robot.set_velocity(direction) 
        paddle = cast["paddle"][0] #this '[0]' needs to be included otherwise it will return an error. Without it, paddle will just be assigned to "paddle" the string and not the object in the dict.
        #set_velocity is saved in the Actor() object, which paddle is an instance of Actor(), which a value now under the "paddle" key in the cast[] dict.!
  
        paddle.set_velocity(direction) #direction has a new velocity aka 'Point'        
