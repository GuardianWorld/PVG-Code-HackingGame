# Hacking Version 2
from uagame import *
from time import sleep

# Create Window
window = Window('Hacking Ver 2.0', 800, 600)

# configure Window
window.set_font_name('couriernew')
window.set_font_size(20)
window.set_font_color('green')
window.set_bg_color('black')
line_y = 1
string_height = window.get_font_height()


# easierToControlDefinition
def draw_combo(text, x, y):
    window.draw_string(text, x, y)
    window.update()
    sleep(0.3)
    y = y + string_height + 1
    return y


def jump_line(y):
    y = y + string_height + 1
    return y


def get_x(string):
    x_space = window.get_width() - window.get_string_width(string)
    x = x_space // 2
    return x


def get_y():
    outcome_height = 7 * string_height
    y_space = window.get_height() - outcome_height
    y = y_space // 2
    return y


# display header
line_y = draw_combo("DEBUG MODE", 1, line_y)
line_y = draw_combo("1 ATTEMPT(S) LEFT", 1, line_y)

# display Passwords
line_y = jump_line(line_y)
line_y = draw_combo("PROVIDE", 1, line_y)
line_y = draw_combo("SETTING", 1, line_y)
line_y = draw_combo("CANTINA", 1, line_y)
line_y = draw_combo("CUTTING", 1, line_y)
line_y = draw_combo("HUNTERS", 1, line_y)
line_y = draw_combo("SURVIVE", 1, line_y)
line_y = draw_combo("HEARING", 1, line_y)
line_y = draw_combo("HUNTING", 1, line_y)
line_y = draw_combo("REALIZE", 1, line_y)
line_y = draw_combo("NOTHING", 1, line_y)
line_y = draw_combo("OVERLAP", 1, line_y)
line_y = draw_combo("FINDING", 1, line_y)
line_y = draw_combo("PUTTING", 1, line_y)
line_y = jump_line(line_y)

# display guess
guess = window.input_string("ENTER PASSWORD > ", 1, line_y)

window.clear()

# display ending
line_x = get_x(guess)
line_y = get_y()

line_y = draw_combo(guess, line_x, line_y)
line_y = jump_line(line_y)

line_x = get_x("LOGIN FAILURE - TERMINAL LOCKED")
line_y = draw_combo("LOGIN FAILURE - TERMINAL LOCKED", line_x, line_y)
line_y = jump_line(line_y)
line_x = get_x("PLEASE CONTACT AN ADMINISTRATOR")
line_y = draw_combo("PLEASE CONTACT AN ADMINISTRATOR", line_x, line_y)
line_y = jump_line(line_y)
line_x = get_x("PRESS ENTER TO EXIT")
window.input_string("PRESS ENTER TO EXIT", line_x, line_y)

# close window
window.close()
