"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Zhen Yang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #two_circles()
    #circle_and_rectangle()

def two_circles():
    window = rg.RoseWindow(500, 500)
    point1 = rg.Point(250, 250)
    point2 = rg.Point(330, 330)
    circle1 = rg.Circle(point1, 30)
    circle2 = rg.Circle(point2, 50)
    circle1.fill_color = 'yellow'
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow(500, 500)

    outline_thickness = 3
    fill_color = "blue"
    centers_x_coordinate = 200
    centers_y_coordinate = 200
    center = "Point(200, 200)"

    center_point = rg.Point(centers_x_coordinate, centers_y_coordinate)
    circle = rg.Circle(center_point, 50)
    circle.fill_color = 'blue'


    outline_rectangle = 3
    fill_color2 = None
    cornora = ((330 + 440) / 2)
    cornorb = ((440 + 330) / 2)


    rectangle = rg.Rectangle(rg.Point(330, 330), rg.Point(440, 440))
    center_rect = rectangle.get_center()




    circle.attach_to(window)
    rectangle.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    print(outline_thickness)
    print(fill_color)
    print(center)
    print(centers_x_coordinate)
    print(centers_y_coordinate)

    print(outline_rectangle)
    print(fill_color2)
    print(center_rect)
    print(cornora)
    print(cornorb)

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    window = rg.RoseWindow(500, 500)
    line1 = rg.Line(rg.Point(220, 220), rg.Point(440, 440))
    line2 = rg.Line(rg.Point(174, 466), rg.Point(466, 332))
    line1.thickness = 4
    goubi = line1.get_midpoint()
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    print(goubi)
    print()


    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
