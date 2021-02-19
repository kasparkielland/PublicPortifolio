# from turtle import *
#
#
# def draw_filled_square(width, height, fill_color, pen_color="#000000", pen_size=3.0):
#     setheading(0)
#     pensize(pen_size)  # Sets the pensize to 3 pixels
#     pencolor(pen_color)  # Sets the pencolor to black
#     pendown()
#     fillcolor(fill_color)  # Sets the fillcolor to the defined color
#     begin_fill()  # Make sure that the tiles background color is filled in
#     for corner in range(2):  # Draws the square
#         forward(width)
#         left(90)
#         forward(height)
#         left(90)
#     end_fill()
#     pensize(3)
#     penup()
#
#
# def apply_frame(x_pos, y_pos, width, height, pen_color="#000000", pen_size=3.0):
#     setheading(0)
#     goto(x_pos, y_pos)
#     pensize(pen_size)
#     pencolor(pen_color)
#     pendown()
#     for corner in range(4):
#         forward(width)
#         setheading(heading() + 90)
#         forward(height)
#         setheading(heading() + 90)
#     penup()
#
#
# def draw_viking_helmet(width=160, height=80):
#     x_start = xcor()
#     y_start = ycor()
#     draw_filled_square(width, height,
#                        "#9fa0a4")  # Calls the draw_filled_square function with the defined width, height and a mose green color
#
#     # TODO: Make loop for horn drawings
#
#     # Draws the left horn
#     goto(x_start + width / 2 - height / 4, y_start + height / 3)
#     pendown()
#     setheading(180)
#     fillcolor("#FAEBD7")
#     begin_fill()
#     circle(- height / 2, 100)
#     setheading(270)
#     circle(3 * height / 8, 109)
#     goto(x_start + width / 2 - height / 4, y_start + height / 3)
#     end_fill()
#     penup()
#
#     # Draws the right horn
#     goto(x_start + width / 2 + height / 4, y_start + height / 3)
#     pendown()
#     begin_fill()
#     setheading(0)
#     circle(height / 2, 100)
#     setheading(270)
#     circle(- 3 * height / 8, 109)
#     goto(x_start + width / 2 + height / 4, y_start + height / 3)
#     end_fill()
#     penup()
#
#     # Draws helmet
#     goto(x_start + width / 2 + height / 2, y_start + height / 4)
#     pendown()
#     setheading(90)
#     fillcolor("#CFB53B")
#     begin_fill()
#     circle(height / 2, 180)
#     end_fill()
#     goto(x_start + width / 2 + height / 2, y_start + height / 4)
#     penup()
#     setheading(0)
#
#     # Draws golden rods
#     goto(x_start + width / 2 + height / 14, y_start + height / 4 - height / 14)
#     fillcolor("#DAA520")
#     pendown()
#     begin_fill()
#     for rod_no in range(3):
#         forward(height / 2 - height / 14)
#         setheading(heading() + 90)
#         forward(height / 7)
#         setheading(heading() + 90)
#         forward(height / 2 - height / 14)
#         setheading(heading() - 90)
#     goto(x_start + width / 2 + height / 14, y_start + height / 4 - height / 14)
#     end_fill()
#     penup()
#     setheading(0)
#
#     # Draws bolts
#     goto(x_start + width / 2, y_start + height / 4 + 2 * height / 112)
#     dot(width / 20, "#696969")
#     dot(width / 30, "#C0C0C0")
#     goto(x_start + width / 2, y_start + height / 4)
#     for rod_no in range(3):
#         for bolt_no in range(2):
#             forward(height / 4 - height / 28)
#             dot(width / 30, "#696969")
#             dot(width / 40, "#C0C0C0")
#         goto(x_start + width / 2, y_start + height / 4)
#         setheading(heading() + 90)
#     setheading(0)
#
#     apply_frame(x_start, y_start, width, height)
#
#
# def draw_viking_axe(width=80, height=160):
#     x_start = xcor()
#     y_start = ycor()
#     draw_filled_square(width, height,
#                        "#2a6f62")  # Calls the draw_filled_square function with the defined width, height and a light gray color
#
#     goto(x_start + width / 2 - width / 6, y_start + height / 20)
#     pendown()
#     fillcolor("#8B4513")
#     begin_fill()
#     forward(width / 3)
#     setheading(95)
#     forward(8 * height / 10)
#     setheading(180)
#     forward(width / 15)
#     goto(x_start + width / 2 - width / 6, y_start + height / 20)
#     end_fill()
#     setheading(0)
#     penup()
#     goto(x_start + width / 2, y_start + 8 * height / 10)
#     pendown()
#     fillcolor("#696969")
#     begin_fill()
#     for i in range(2):
#         setheading(90 * i + 45)
#         forward(width / 3)
#         setheading(heading() - 90 + 2 * 90 * i)
#         circle(- width / 3 + 2 * width / 3 * i, 90)
#         goto(x_start + width / 2, y_start + 8 * height / 10)
#     end_fill()
#     penup()
#     setheading(0)
#
#     apply_frame(x_start, y_start, width, height)
#
#
# def draw_viking_ship(width=160, height=160):
#     x_start = xcor()
#     y_start = ycor()
#     draw_filled_square(width, height, "#a9d4e6")  # Calls the draw_filled_square function with the defined width, height and a light blue color
#     goto(x_start + width / 2, y_start + height / 5)
#     setheading(90)
#     pencolor("#8B4513")
#     pensize(height / 50)
#     pendown()
#     forward(13 * height / 20)
#     penup()
#     goto(x_start + width / 10, y_start + height / 2)
#     setheading(0)
#     pensize(height / 80)
#     pendown()
#     circle(- height / 16, 150)
#     circle(height / 10, 50)
#     fillcolor("#8B4513")
#     begin_fill()
#     circle(height / 10, 100)
#     goto(x_start + width - (xcor() - x_start), ycor())
#     circle(height / 10, 100)
#     height_of_ship_deck = ycor()
#     end_fill()
#     circle(height / 10, 50)
#     for rotation in range(4):
#         circle(- height / (16 + 10 * rotation), 150)
#     penup()
#
#     pensize(width / 20)
#     for stripe_no in range(11):
#         if stripe_no % 2 == 0:
#             pencolor("red")
#         else:
#             pencolor("white")
#         goto(x_start + width / 4 + width / 20 + stripe_no * (width / 26), y_start + 15 * height / 20)
#         setheading(250)
#         pendown()
#         circle(width / 2, 40, 10)
#         penup()
#     goto(x_start + width / 4, y_start + 31 * height / 40)
#     setheading(0)
#     pencolor("#8B4513")
#     pensize(width / 30)
#     pendown()
#     forward(11 * (width / 26) + width / 20)
#     penup()
#     goto(x_start + width / 4, y_start + 24 * height / 60)
#     pendown()
#     forward(11 * (width / 26) + width / 20)
#     penup()
#
#     for shield_number in range(8):
#         #if shield_number == 0:
#             #draw_viking_shield(0, 0, x_start + (shield_number + 1) * width / 10, height_of_ship_deck - width / 20)
#         #else:
#         draw_viking_shield(width / 10, width / 10, x_start + (shield_number + 1) * width / 10, height_of_ship_deck - width / 20, "#13579F")
#
#
#     pencolor("#000000")
#     fillcolor("#1a4b6d")
#     begin_fill()
#     goto(x_start, y_start)
#     goto(x_start, y_start + height / 5)
#     pendown()
#     for wave in range(9):
#         setheading(90)
#         circle(- width / 16, 90)
#         setheading(225)
#         circle(width / 16, 60)
#         setheading(0)
#         goto(xcor(), y_start + height / 5)
#         forward(width / 16)
#     goto(x_start + width, ycor())
#     penup()
#     goto(x_start + width, y_start)
#     goto(x_start, y_start)
#     end_fill()
#
#     apply_frame(x_start, y_start, width, height)
#
#
# def draw_viking_shield_tile(width=80, height=80):
#     x_start = xcor()
#     y_start = ycor()
#     draw_filled_square(width, height, "#EEE8AA")  # Calls the draw_filled_square function with the defined width, height and a sea green color
#     draw_viking_shield(width, height, x_start, y_start)
#     apply_frame(x_start, y_start, width, height)
#
#
# def draw_viking_shield(width=80.0, height=80.0, x_start = xcor(), y_start = ycor(), shield_color = "#880000"):
#     pensize(0)
#     pencolor("#FFFFFF")
#     goto(x_start + width / 2, y_start + width / 10)
#     pendown()
#     fillcolor(shield_color)
#     begin_fill()
#     circle(width / 2 - width / 10)
#     end_fill()
#     penup()
#     goto(x_start + width / 2 - ((width / 2 - width / 10) / 4) / 2, y_start + width / 10)
#     draw_filled_square((width / 2 - width / 10) / 4, width - width / 5, "#8B4513", "#FAEBD7", width / 50)
#     goto(x_start + width / 10, y_start + width / 2 - ((width / 2 - width / 10) / 4) / 2)
#     draw_filled_square(width - width / 5, (width / 2 - width / 10) / 4, "#8B4513", "#FAEBD7", width / 50)
#     goto(x_start + width / 2, y_start + width / 2)
#     dot(width / 5, "#808080")
#     dot(width / 10, "#696969")
#     dot(width / 13, "#C0C0C0")
#     for dot_no in range(12):
#         goto(x_start + width / 2, y_start + width / 2)
#         forward(width / 12)
#         dot(width / 50, "#696969")
#         dot(width / 100, "#C0C0C0")
#         setheading(heading() + 360 / 12)
#     goto(x_start + width / 2, y_start + width / 10)
#     pencolor("#808080")
#     pensize(width / 15)
#     pendown()
#     circle(width / 2 - width / 10)
#     penup()
#
#


# setup(800, 800)
# hideturtle()
# tracer(False)
# speed(0)
#
# penup()
#
# goto(-100, -100)
# draw_viking_helmet()
# goto(100, -100)
# draw_viking_axe()
# goto(100, 100)
# draw_viking_shield_tile()
# goto(-100, 20)
# draw_viking_ship(160, 160)
#
# hideturtle()
# done()

