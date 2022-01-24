from sense_hat import SenseHat
# from sense_emu import SenseHat
from time import sleep
from random import randint

blank = (0, 0, 0)
border_colour = (0, 0, 200)
car_colour = (100, 200, 0)
obstacle_colour = (100, 0, 0)

track = [[blank for x in range(8)] for y in range(8)]
distance = 0
car_position = 4
obstacle_buffer = 2

sense = SenseHat()


def draw(matrix):
    matrix.reverse()
    flat_list = [item for sublist in matrix for item in sublist]
    sense.set_pixels(flat_list)


def draw_car(matrix):
    global car_position
    car_position = normalise_position(car_position)

    if matrix[0][car_position] == obstacle_colour:
        sense.show_message("GAME OVER! " + str(distance-8))
        exit()

    matrix[0][car_position] = car_colour

    return matrix


def gen_track():
    global obstacle_buffer

    line = [blank for x in range(8)]

    if distance % 4 > 1:
        line[0] = border_colour
        line[7] = border_colour

    obstacle_buffer += 1

    if randint(1, 5) > 3 and obstacle_buffer > 2:
        obstacle_buffer = 0
        s = randint(1, 5)
        w = min(randint(2, 7-s), 5)

        for i in range(s, w+s):
            line[i] = obstacle_colour

    return line


def joystick_moved(event):
    global car_position
    if event.action == 'pressed':
        if event.direction == 'left':
            car_position -= 1
        elif event.direction == 'right':
            car_position += 1


def normalise_position(x):
    return max(1, min(6, x))


if __name__ == '__main__':

    sense.stick.direction_any = joystick_moved

    while True:
        track.append(gen_track())
        draw(draw_car(track[distance:distance + 8]))

        distance += 1
        sleep(0.5)
