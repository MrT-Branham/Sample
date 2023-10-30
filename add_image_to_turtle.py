import turtle as trtl
# 1.) Add the image to the folder your code is in.

# 2.) Store the file name of your shape
    # Note that it needs to a .gif file.
    # You can use a file type converter online.
    # https://cloudconvert.com/
bruin = 'bruin_logo.gif'

# 3.) Add the image to the window.
wn = trtl.Screen()
wn.addshape(bruin)

# 4.) Set the shape of a turtle to the image.
mascot = trtl.Turtle(shape = bruin)
# OR
mascot.shape(bruin)

# Optional: If you wish to resize the shape, you must resize it before using it.
  # You can use https://redketchup.io/gif-resizer

# Testing
mascot.penup() # To stop is drawing
#mascot.forward(150)
mascot2 = trtl.Turtle()
mascot.setheading(90)
mascot.shape(bruin)



wn.mainloop()