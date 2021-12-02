from game.action import Action
from game.point import Point
from game import constants

class HandleCollisionsAction(Action):

    def execute(self, cast):
        ball = cast["ball"][0]
        bricks = cast["brick"]
        paddle = cast["paddle"][0]
        paddle_length = paddle.get_length()
        paddle_left = paddle.get_position().get_x() #This used to be the center, but we found out that the center is on the left of it
        paddle_right = paddle_length + paddle_left

        """ 
        check to see if the ball bounced off of the brick.
        Iterate through the lists of bricks
        """
        for brick in bricks: 
            current_brick_location =  brick.get_position().get_x() 
            """
            remove bricks when hit
            """
            if brick.get_position().equals(ball.get_position()):
               bricks.remove(brick)
               #get_velocity is used instead of set velocity
               #bc we are getting the Point object to manipulate and access
               #the reverse method to change, set_velocity is used to create
               #a brand new instance of point
               ball.get_velocity().reverse_y()
        """
        bounce ball off paddle
        """
        # We first need to create the left side as detectable objects
        paddle_left = paddle.get_position().get_x() #This used to be the center, but we found out that the center is on the left of it
        paddle_right = paddle_length + paddle_left
        if (paddle_left <= ball.get_position().get_x() and ball.get_position().get_x() <= paddle_right and paddle.get_position().get_y() - 1 == ball.get_position().get_y()):
            ball.get_velocity().reverse_y()

        """
        bounce baddle off the walls
        """
        # This is for the left and right wall:
        if ball.get_position().get_x() == constants.MAX_X - 2 or ball.get_position().get_x() == 1:
            ball.get_velocity().reverse_x()
        # This is for the top wall!
        if ball.get_position().get_y() <= 1: 
            ball.get_velocity().reverse_y()
        # End the game if the ball collides with the bottom wall:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
