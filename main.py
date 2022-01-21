import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITION = [-240, -200, -160, -120, 20, 60, 100, 140, 180, 220, 240]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.keep_score()

        print("come back")

    for new_car in car_manager.all_cars:
        if player.distance(new_car) < 20:
            game_is_on = False
            print("game over")
            scoreboard.game_over()




screen.exitonclick()