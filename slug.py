# Based on https://projects.raspberrypi.org/en/projects/slug

from sense_hat import SenseHat
# from sense_emu import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

slug_colour = (255, 255, 255)
veg_colour = (0, 0, 255)
blank = (0, 0, 0)

slug = [[2, 4], [3, 4], [4, 4]]  # starting point
vegetables = []

direction = 'right'
score = 0
dead = False
pause = 1


def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], slug_colour)


def move():
    global score, dead, pause
    # Find the last and first items in the slug list
    last = slug[-1]
    first = slug[0]
    next = list(last)     # Create a copy of the last item

    # Find the next pixel in the direction the slug is currently moving
    if direction == "right":
        # Move along the column
        next[0] = last[0] + 1
    elif direction == "left":
        next[0] = last[0] - 1
    elif direction == "up":
        next[1] = last[1] - 1
    elif direction == "down":
        next[1] = last[1] + 1
    else:
        dead = True

    next = wrap(next)

    if next in vegetables:
        vegetables.remove(next)
        score += 1
        pause = pause - 0.05
    else:
        # Set the first pixel in the slug list to blank
        sense.set_pixel(first[0], first[1], blank)

        # Remove the first pixel from the list
        slug.remove(first)

    if next in slug:
        dead = True

    # Add this pixel at the end of the slug list
    slug.append(next)

    # Set the new pixel to the slug's colour
    sense.set_pixel(next[0], next[1], slug_colour)


def make_veg():
    while True:
        x = randint(0, 7)
        y = randint(0, 7)
        new = [x, y]

        if new not in slug:
            sense.set_pixel(new[0], new[1], veg_colour)
            return new


def wrap(pix):
    # Wrap x coordinate
    if pix[0] > 7:
        pix[0] = 0
    if pix[0] < 0:
        pix[0] = 7
    # Wrap y coordinate
    if pix[1] < 0:
        pix[1] = 7
    if pix[1] > 7:
        pix[1] = 0

    return pix


def joystick_moved(event):
    global direction
    direction = event.direction


if __name__ == '__main__':

    sense.stick.direction_any = joystick_moved

    sense.show_message('Slug v1')

    draw_slug()

    vegetables.append(make_veg())
    vegetables.append(make_veg())
    vegetables.append(make_veg())

    while True:
        sleep(pause)
        move()

        if dead:
            sense.clear((255, 0, 0))
            sleep(0.5)
            sense.show_message("Score: " + str(score) + "!")
            exit()

        # Let there be a 20% chance of making a veggie if there aren't many about
        if len(vegetables) < 3 and randint(1, 5) > 4:
            vegetables.append(make_veg())

        if len(vegetables) < 1:
            sense.show_message("WINNER! Score: " + str(score) + "!")
            exit()
