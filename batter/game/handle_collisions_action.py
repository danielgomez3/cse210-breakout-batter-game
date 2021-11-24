import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):

    def execute(self, cast):
        ball = cast["ball"][0] # there's only one
        ball_position = ball.get_position()
        brick = cast["brick"]
        paddle = cast["paddle"]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #paddle_position = paddle.get_position()
        # #ball to bounce off boundaries:
        # if ball_position.get_x() == constants.MAX_X -1 or ball_position.get_x() == 1:
        #     old_velocity = ball.get_velocity()
        #     #point needs an x & y, even if y doesn't change
        #     new_velocity = Point((old_velocity.get_x() * -1), old_velocity.get_y())
        # for b in brick:
        #     #Logic for the paddle:
        #     if paddle.get_position().equals(brick.get_position()):
        #         description = brick.get_description()
        #         brick.set_text
        #     if ball.get_position().equals(b.get_position()):
        #         #description = brick.get_description()
        #         ball.set_position()
        #         brick.set_position()
