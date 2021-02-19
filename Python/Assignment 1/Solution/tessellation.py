# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10588281
#    Student name: Kaspar Kielland
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.
cell_size = 100  # pixels (default is 100)
grid_width = 8  # squares (default is 10)
grid_height = 7  # squares (default is 7)
x_margin = cell_size * 2.75  # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2  # pixels, the size of the margin below/above the grid
window_height = (grid_height * cell_size + y_margin * 2)
window_width = (grid_width * cell_size + x_margin * 2)
small_font = ('Garamond', 18, 'normal')  # font for the coords
big_font = ('Garamond', 25, 'bold')  # font for any other text
NERO_BLACK_COLOR = "#282828"
BACKGROUND_COLOR = NERO_BLACK_COLOR
LINE_COLOR = 'dark goldenrod'

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'


#
# --------------------------------------------------------------------#


# -----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour=BACKGROUND_COLOR,
                          line_colour=LINE_COLOR,
                          draw_grid=True, mark_legend=True):
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0)  # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90)  # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27  # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align='center', font=small_font)
        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10  # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align='right', font=small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, -25)
        write('Put your\nlegend here', align='right', font=big_font)
        # Right side
        goto((grid_width * cell_size) // 2 + 75, -25)
        write('Put your\nlegend here', align='left', font=big_font)

        # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
# --------------------------------------------------------------------#


# -----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

# Small tile
fixed_pattern_0 = [['A1', 'O']]
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']]
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']]
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']]
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']]
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']]
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']]
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']]
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G7', 'H7', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]


# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.

#
# --------------------------------------------------------------------#


# -----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.
#
# noinspection SpellCheckingInspection
def random_pattern(print_pattern=True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
                (not [column, row + 1] in been_there) and \
                (not [column + 1, row] in been_there) and \
                (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
                (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
                (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            # noinspection SpellCheckingInspection
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.
#

# Colors used in the turtle drawings
BLACK_COLOR = "#000000"
LIGHT_GRAY_COLOR = "#9FA0A4"
ANTIQUE_WHITE_COLOR = "#FAEBD7"
OLD_GOLD_COLOR = "#CFB53B"
GOLDEN_ROD_COLOR = "#DAA520"
DIM_GRAY_COLOR = "#696969"
SILVER_COLOR = "#C0C0C0"
EDEN_GREEN_COLOR = "#2A6F62"
SADDLE_BROWN_COLOR = "#8B4513"
LIGHT_BLUE_COLOR = "#A9D4E6"
ALLPORTS_BLUE_COLOR = "#1A4B6D"
DARK_RED_COLOR = "#880000"
GREY_COLOR = "#808080"
PALE_GOLDEN_ROD_COLOR = "#EEE8AA"

# Defines the standard pen size
STANDARD_PEN_SIZE = 0


def draw_filled_square(width, height, fill_color=BLACK_COLOR, pen_color=BLACK_COLOR, pen_size=float(STANDARD_PEN_SIZE)):
    setheading(0)
    pensize(pen_size)
    pencolor(pen_color)
    pendown()
    fillcolor(fill_color)
    begin_fill()
    # Draws a square or rectangle (depends on the width and height)
    for corner in range(2):
        forward(width)
        setheading(heading() + 90)
        forward(height)
        setheading(heading() + 90)
    end_fill()
    # Sets pensize back to standard
    pensize(STANDARD_PEN_SIZE)
    penup()


def apply_frame(x_pos, y_pos, width, height, pen_color=LINE_COLOR, pen_size=3.0):
    setheading(0)
    goto(x_pos, y_pos)
    pensize(pen_size)
    pencolor(pen_color)
    pendown()
    # Draws the outside of a square or rectangle (depends on the width and height)
    for corner in range(4):
        forward(width)
        setheading(heading() + 90)
        forward(height)
        setheading(heading() + 90)
    penup()


def draw_viking_shield(width=80.0, height=80.0, x_start=xcor(), y_start=ycor(), shield_color=DARK_RED_COLOR):
    pensize(STANDARD_PEN_SIZE)
    pencolor(BLACK_COLOR)
    # Positions the turtle so the circle are drawn in the middle of the square
    goto(x_start + width / 2, y_start + height / 10)
    pendown()
    fillcolor(shield_color)
    begin_fill()
    # Draws the shield circle
    circle(2 * width / 5)
    end_fill()
    penup()
    goto(x_start + 9 * width / 20, y_start + height / 10)
    # Makes the vertical rectangle
    draw_filled_square((width / 10), width - width / 5, SADDLE_BROWN_COLOR, ANTIQUE_WHITE_COLOR, width / 50)
    goto(x_start + width / 10, y_start + 9 * height / 20)
    # Makes the horizontal rectangle
    draw_filled_square(width - width / 5, (width / 2 - width / 10) / 4, SADDLE_BROWN_COLOR, ANTIQUE_WHITE_COLOR,
                       width / 50)
    goto(x_start + width / 2, y_start + width / 2)
    # Makes the "metal bolt" in the middle of the shield
    dot(width / 5, GREY_COLOR)
    dot(width / 10, DIM_GRAY_COLOR)
    dot(width / 13, SILVER_COLOR)
    for bolt_no in range(12):
        goto(x_start + width / 2, y_start + width / 2)
        forward(width / 12)
        dot(width / 50, DIM_GRAY_COLOR)
        dot(width / 100, SILVER_COLOR)
        setheading(heading() + 360 / 12)
    goto(x_start + width / 2, y_start + width / 10)
    pencolor(GREY_COLOR)
    pensize(width / 15)
    pendown()
    # Makes the outer line of the shield
    circle(width / 2 - width / 10)
    penup()


def draw_viking_helmet_tile(width=cell_size * 2, height=cell_size):
    # Stores the starting position of the tile (lower left corner)
    x_start = xcor()
    y_start = ycor()
    draw_filled_square(width, height, LIGHT_GRAY_COLOR)

    # Draws horns. "Fixer"-variable fixes the rotations and heading so that the horn will get mirrored.
    #fixer = 1
    for horn_no in range(2):
        fixer = 1 - 2*horn_no
        goto(x_start + (2 * width / 8) * horn_no + (3 * width / 8), y_start + height / 3)
        pendown()
        setheading(180 - 180 * horn_no)
        fillcolor(ANTIQUE_WHITE_COLOR)
        begin_fill()
        circle(fixer * - height / 2, 100)
        setheading(270)
        circle(fixer * 3 * height / 8, 109)
        goto(x_start + (2 * width / 8) * horn_no + (3 * width / 8), y_start + height / 3)
        end_fill()
        penup()
        #fixer -= 2

    # Draws helmet
    goto(x_start + 3 * width / 4, y_start + height / 4)
    pendown()
    setheading(90)
    fillcolor(OLD_GOLD_COLOR)
    begin_fill()
    circle(height / 2, 180)
    end_fill()
    goto(x_start + 3 * width / 4, y_start + height / 4)
    penup()
    setheading(0)

    # Draws golden rods
    goto(x_start + 15 * width / 28, y_start + 10 * height / 56)
    fillcolor(GOLDEN_ROD_COLOR)
    pendown()
    begin_fill()
    for rod_no in range(3):
        forward(3 * height / 7)
        setheading(heading() + 90)
        forward(height / 7)
        setheading(heading() + 90)
        forward(3 * height / 7)
        setheading(heading() - 90)
    setheading(0)
    forward(height / 7)
    end_fill()
    penup()

    # Draws bolts
    goto(x_start + width / 2, y_start + 15 * height / 56)
    dot(width / 20, DIM_GRAY_COLOR)
    dot(width / 30, SILVER_COLOR)
    goto(x_start + width / 2, y_start + height / 4)
    for rod_no in range(3):
        for bolt_no in range(2):
            forward(6 * height / 28)
            dot(width / 30, DIM_GRAY_COLOR)
            dot(width / 40, SILVER_COLOR)
        goto(x_start + width / 2, y_start + height / 4)
        setheading(heading() + 90)
    setheading(0)

    apply_frame(x_start, y_start, width, height)


def draw_viking_axe_tile(width=80, height=160):
    x_start = xcor()
    y_start = ycor()
    draw_filled_square(width, height, EDEN_GREEN_COLOR)
    # Draws the wooden handle
    goto(x_start + width / 3, y_start + height / 20)
    pendown()
    fillcolor(SADDLE_BROWN_COLOR)
    begin_fill()
    forward(width / 3)
    setheading(95)
    forward(8 * height / 10)
    setheading(180)
    forward(width / 15)
    goto(x_start + width / 3, y_start + height / 20)
    end_fill()
    setheading(0)
    penup()
    # Draws the axe-blades
    goto(x_start + width / 2, y_start + 8 * height / 10)
    pendown()
    fillcolor(DIM_GRAY_COLOR)
    begin_fill()
    for blade_no in range(2):
        setheading(90 * blade_no + 45)
        forward(width / 3)
        setheading(heading() - 90 + 2 * 90 * blade_no)
        circle(- width / 3 + 2 * width / 3 * blade_no, 90)
        goto(x_start + width / 2, y_start + 8 * height / 10)
    end_fill()
    penup()
    setheading(0)

    apply_frame(x_start, y_start, width, height)


def draw_viking_ship_tile(width=160, height=160):
    # Stores the starting position of the tile (lower left corner)
    x_start = xcor()
    y_start = ycor()
    draw_filled_square(width, height, LIGHT_BLUE_COLOR)
    # Draws the sail mast
    goto(x_start + width / 2, y_start + height / 5)
    setheading(90)
    pencolor(SADDLE_BROWN_COLOR)
    pensize(height / 50)
    pendown()
    forward(14 * height / 20)
    penup()
    # Draws the flag on top of the sail mast
    pensize(0)
    pencolor(ANTIQUE_WHITE_COLOR)
    backward(height / 100)
    setheading(0)
    fillcolor(DARK_RED_COLOR)
    begin_fill()
    forward(width / 30)
    setheading(350)
    circle(width, 10)
    setheading(190)
    circle(width, 10)
    forward(width / 30)
    goto(x_start + width / 2, ycor())
    end_fill()
    # Draws the the haul of the ship
    pencolor(SADDLE_BROWN_COLOR)
    pensize(height / 50)
    goto(x_start + width / 10, y_start + height / 2)
    # Makes the dragon on the front of the ship (part of the haul)
    pensize(height / 80)
    pendown()
    # Draws upper lip
    setheading(160)
    forward(width / 20)
    backward(width / 20)
    # Draws lower lip
    setheading(210)
    forward(width / 25)
    backward(width / 25)
    # Draws eye
    setheading(0)
    forward(width / 40)
    setheading(90)
    fillcolor(ANTIQUE_WHITE_COLOR)
    begin_fill()
    circle(width / 40, 160)
    end_fill()
    penup()
    goto(x_start + width / 10, y_start + height / 2)
    setheading(0)
    pendown()
    # Makes the front of the ship (part of the haul)
    circle(- height / 16, 150)
    circle(height / 10, 50)
    # Draws middle haul of the ship
    fillcolor(SADDLE_BROWN_COLOR)
    begin_fill()
    circle(height / 10, 100)
    goto(x_start + width - (xcor() - x_start), ycor())
    circle(height / 10, 100)
    height_of_ship_deck = ycor()
    end_fill()
    # Draws the back of the ship (part of the haul)
    circle(height / 10, 50)
    for rotation in range(4):
        circle(- height / (16 + 10 * rotation), 150)
    penup()
    # Draws the sail
    pensize(width / 20)
    for stripe_no in range(11):
        # Every other colour are red and white
        if stripe_no % 2 == 0:
            pencolor(DARK_RED_COLOR)
        else:
            pencolor(ANTIQUE_WHITE_COLOR)
        goto(x_start + 3 * width / 10 + stripe_no * (width / 26), y_start + 3 * height / 4)
        setheading(250)
        pendown()
        circle(width / 2, 40, 10)
        penup()
    # Draws the upper beam
    goto(x_start + width / 4, y_start + 31 * height / 40)
    setheading(0)
    pencolor(SADDLE_BROWN_COLOR)
    pensize(width / 30)
    pendown()
    forward(123 * width / 260)
    penup()
    # Draws the lower beam
    goto(x_start + width / 4, y_start + 24 * height / 60)
    pendown()
    forward(123 * width / 260)
    penup()
    # Draws shields where every other shield are green and red
    ship_shield_colors = [EDEN_GREEN_COLOR, DARK_RED_COLOR]
    for shield_number in range(8):
        draw_viking_shield(width / 10, width / 10, x_start + (shield_number + 1) * width / 10,
                           height_of_ship_deck - width / 20, ship_shield_colors[round(shield_number % 2)])
    # Draws the waves
    pencolor(BLACK_COLOR)
    fillcolor(ALLPORTS_BLUE_COLOR)
    begin_fill()
    goto(x_start, y_start)
    goto(x_start, y_start + height / 5)
    pendown()
    for wave in range(9):
        setheading(90)
        circle(- width / 16, 90)
        setheading(225)
        circle(width / 16, 60)
        setheading(0)
        goto(xcor(), y_start + height / 5)
        forward(width / 16)
    goto(x_start + width, ycor())
    penup()
    goto(x_start + width, y_start)
    goto(x_start, y_start)
    end_fill()

    apply_frame(x_start, y_start, width, height)


def draw_viking_shield_tile(width=80, height=80):
    # Stores the starting position of the tile (lower left corner)
    x_start = xcor()
    y_start = ycor()
    draw_filled_square(width, height, PALE_GOLDEN_ROD_COLOR)
    draw_viking_shield(width, height, x_start, y_start)
    apply_frame(x_start, y_start, width, height)


def break_tile(width, height):
    # Stores the starting position of the tile (lower left corner)
    x_start = xcor()
    y_start = ycor()

    fillcolor(BACKGROUND_COLOR)

    # Draws the smashed piece of the tile
    goto(x_start + width / 2, y_start + height / 4)
    begin_fill()
    goto(x_start + 3 * width / 4, y_start + 2 * height / 3)
    goto(x_start + width / 3, y_start + 3 * height / 5)
    goto(x_start + 3 * width / 10, y_start + height / 3)
    end_fill()

    # Draws the bottom left cut in the tile
    goto(x_start + 3 * width / 10, y_start + height / 3)
    begin_fill()
    goto(x_start, y_start + height / 80)
    goto(x_start + 2 * width / 5, y_start + height / 2)
    end_fill()

    # Draws the bottom right cut in the tile
    goto(x_start + width / 2, y_start + height / 2)
    begin_fill()
    goto(x_start + 19 * width / 20, y_start)
    goto(x_start + 8 * width / 15, y_start + 8 * height / 15)
    end_fill()

    # Draws the top left cut in the tile
    goto(x_start + 2 * width / 5, y_start + height / 2)
    begin_fill()
    goto(x_start + width / 20, y_start + height)
    goto(x_start + 5 * width / 12, y_start + 8 * height / 15)
    end_fill()

    # Draws the top right cut in the tile
    goto(x_start + width / 2, y_start + height / 2)
    begin_fill()
    goto(x_start + width, y_start + 4 * height / 5)
    goto(x_start + 7 * width / 15, y_start + 17 * height / 30)
    end_fill()

    # Draws the bottom middle cut in the tile
    goto(x_start + width / 2, y_start + height / 4)
    begin_fill()
    goto(x_start + 39 * width / 40, y_start)
    goto(x_start + 3 * width / 8, y_start + 3 * height / 8)
    end_fill()

    # Apply the frame to smooth things out
    apply_frame(x_start, y_start, width, height)


def write_legend_description(description):
    pencolor(LINE_COLOR)
    # Move turtle position to underneath the legend illustration
    right(90)
    forward(cell_size / 4)
    write(description, False, align="Center", font=small_font)


def tessellate_legend():
    pencolor(LINE_COLOR)
    # Move turtle position to top center off screen
    goto(0, window_height / 2 - y_margin)
    write("BACK TO THE VIKING AGE", False, align="Center", font=big_font)

    # region Left side
    # region Top left legend
    # Makes the turtle go to a little above the centered horizontal line on the left side of the grid
    goto(-(grid_width * cell_size) / 2 - 3 * cell_size / 2, cell_size / 2)
    write_legend_description("Viking Ship")
    # Moves turtle upwards and to the left to draw the tile
    goto(-(grid_width * cell_size) / 2 - 5 * cell_size / 2, cell_size / 2)
    draw_viking_ship_tile(2 * cell_size, 2 * cell_size)
    # endregion

    # region Bottom left legend
    # Makes the turtle go to a little below the centered horizontal line on the left side of the grid
    goto(-(grid_width * cell_size) // 2 - 3 * cell_size / 2, - 2 * cell_size + cell_size / 2)
    write_legend_description("Viking Shield")
    # Moves turtle upwards and to the left to draw the tile
    goto(-(grid_width * cell_size) // 2 - 2 * cell_size, - 2 * cell_size + cell_size / 2)
    draw_viking_shield_tile(cell_size, cell_size)
    # endregion
    # endregion

    # region Right side
    # region Top right legend
    # Makes the turtle go to a little above the centered horizontal line on the right side of the grid
    goto((grid_width * cell_size) / 2 + 3 * cell_size / 2, - 2 * cell_size)
    write_legend_description("Viking Axe")
    # Moves turtle upwards and to the left to draw the tile
    goto((grid_width * cell_size) / 2 + cell_size, - 2 * cell_size)
    draw_viking_axe_tile(cell_size, 2 * cell_size)
    # endregion

    # region Top left legend
    # Makes the turtle go to a little above the centered horizontal line on the left side of the grid
    goto((grid_width * cell_size) / 2 + 3 * cell_size / 2, cell_size / 2)
    write_legend_description("Viking Helmet")
    # Moves turtle upwards and to the left to draw the tile
    goto((grid_width * cell_size) // 2 + cell_size / 2, cell_size / 2)
    draw_viking_helmet_tile(2 * cell_size, cell_size)
    # endregion
    # endregion

def find_start_position(tile):
    # Determine the bottom-left coordinates of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    for tile_coordinate in tile:
        start_x, start_y = 0.0, 0.0

        # region Calculates the x-value (inspired by the "Draw each of the labels on the x axis"-code)
        for x_value in range(0, grid_width):
            # Checks to see what column character the first tile of the "tile image" (bottom-left) will be placed in
            if tile_coordinate[0] == chr(x_value + ord('A')):
                # Calculates the starting x position (for the bottom-left corner for the bottom-left tile)
                start_x = left_edge + (x_value * cell_size)
                # Breaks out of loop
                break
        # endregion
        # region Calculates the x-value (inspired by the "Draw each of the labels on the x axis"-code)
        for y_value in range(0, grid_height):
            # Checks to see what row number the first tile of the "tile image" (bottom-left) will be placed in
            if float(tile_coordinate[1]) == y_value + 1:
                # Calculates the starting y position (for the bottom-left corner for the bottom-left tile)
                start_y = bottom_edge + (y_value * cell_size)
                # Breaks out of loop
                break
        # endregion
        # Return the coordinates
        return [start_x, start_y]


# Fill the grid with tiles as per the provided data set
def tessellate(pattern):
    tessellate_legend()
    for tile in pattern:
        if len(tile) == 2:
            # region What to do if it's a small tile
            # print("Small tile")
            goto(find_start_position(tile))
            draw_viking_shield_tile(cell_size, cell_size)
            if check_the_mystery_value(tile):
                break_tile(cell_size, cell_size)
            # endregion
        elif len(tile) == 3:
            if tile[0][0] == tile[1][0]:
                # region What to do if it's a vertical tile
                # print("Vertical tile")
                goto(find_start_position(tile))
                draw_viking_axe_tile(cell_size, 2 * cell_size)
                if check_the_mystery_value(tile):
                    break_tile(cell_size, 2 * cell_size)
                # endregion
            elif tile[0][1] == tile[1][1]:
                # region What to do if it's a horizontal tile
                # print("Horizontal tile")
                goto(find_start_position(tile))
                draw_viking_helmet_tile(2 * cell_size, cell_size)
                if check_the_mystery_value(tile):
                    break_tile(2 * cell_size, cell_size)
                # endregion
            else:
                # region Error handling if none of the above checks gets accepted
                print("Error when checking if vertical or horizontal")
                exit(1)
                # endregion
        elif len(tile) == 5:
            # region What to do if it's a large tile
            # print("Large tile")
            goto(find_start_position(tile))
            draw_viking_ship_tile(2 * cell_size, 2 * cell_size)
            if check_the_mystery_value(tile):
                break_tile(2 * cell_size, 2 * cell_size)
            # endregion
        else:
            # region Error handling if none of the above checks gets accepted
            print("Error when checking tile length")
            exit(1)
            # endregion


# region Mystery value check function used in part B
def check_the_mystery_value(sub_list):
    if sub_list[-1] == 'X':
        # print("The mystery value is X")
        return True
    elif sub_list[-1] == 'O':
        # print("The mystery value is O")
        return False
    else:
        # region Error handling if none of the above checks gets accepted (Possible to use try/catch here?)
        print("Failed to find the mystery value")
        exit(1)
        # endregion
# endregion


#
# --------------------------------------------------------------------#


# -----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas(mark_legend=False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("Back to the viking age [Viking ship, Viking shield, Viking axe and Viking helmet]")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
# tessellate(fixed_pattern_17) # <-- used for code development only, not marking
tessellate(random_pattern())  # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
# --------------------------------------------------------------------#
