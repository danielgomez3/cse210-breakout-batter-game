import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}
    
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y) #lets pass x and y
                            #now position will exists, let's fuse it with paddle
    paddle = Actor() #paddle is an Actor now
    paddle.set_text("===========") #IOW, actor.set_text
                #paddle is now a unique version of actor!
                #everything will be saved into actor now in memory!
    paddle.set_position(position) #fusing position with paddle now!
    cast["paddle"] = [paddle] #now put it into to cast{} as a set!
   
    cast["brick"] = []
    for x in range(5, 75):  #now we need to make about 5-75 bricks
        #and by making x equal every int between 5 & 75,
        #we can create 5-75 bricks with their own x values
       for y in range(2, 6):
            position = Point(x, y)
            brick = Actor() # each individual brick is now an Actor!
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)

    # make a unique spawn point for the ball now!
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1) # we just made up something called 
                #velocity based on these coordinates!
                #Now it will permenately encumber the balls position
                #every time it is updated
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen) #called on only once!
    output_service = OutputService(screen) #called on once
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    #randomize_positions_actions = RandomizePositionAction() 
    # we don't need this
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,handle_collisions_action ]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
