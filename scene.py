"""
File Name: scene.py

Author: NTyam Adjomo Francky Ludovic

Purpose: 
write a Python program that draws a semi-realistic outdoor scene in a computer window. Your program can draw any outdoor scene that you like as long as it meets these requirements:

    1. The scene must be outdoor and include part of the sky.
    2. The sky must have clouds.
    3. The scene must include repetitive objects, such as blades of grass, trees, leaves on a tree, birds, flowers, insects, fish, pickets in a fence, dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles.
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
  
    draw_sky(canvas, scene_width, scene_height)
    
    
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

    # Call draw_cloud function inside draw_sky function
    draw_cloud(canvas)

    # Call draw_sun function inside draw_sky function
    draw_sun(canvas)
   
    

def draw_ground(canvas, scene_width, scene_height):
    """
    draw the ground and all the objects on the ground
    """
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="green4")

     # Draw first pine tree.
    tree_center_x = 100
    tree_bottom = 130
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw second pine tree.
    tree_center_x = 700
    tree_bottom = 130
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

   # Draw third pine tree.
    tree_center_x = 700
    tree_bottom = 130
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #Call draw_road function
    draw_road(canvas, scene_width, scene_height)

def draw_cloud(canvas):
    """
    draw the clouds
    Parameters
        canvas: The canvas where this function
        
    Return: nothing
    """
    # the first cloud create
    draw_arc (canvas,100, 400, 200, 450, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,100, 400, 200, 450, start=150, extent=215, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,150, 400, 300, 450, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,150, 400, 300, 450, start=150, extent=215, outline="lavender", width=0, fill="lavender")

    # The second cloud create
    draw_arc (canvas,500, 400, 600, 450, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,500, 400, 600, 450, start=150, extent=215, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,550, 400, 650, 450, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,550, 400, 650, 450, start=150, extent=215, outline="lavender", width=0, fill="lavender")

     # The second cloud create
    draw_arc (canvas,300, 250, 400, 200, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,300, 250, 400, 200, start=150, extent=215, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,350, 250, 450, 200, start=0, extent=150, outline="lavender", width=0, fill="lavender")
    draw_arc (canvas,350, 250, 450, 200, start=150, extent=215, outline="lavender", width=0, fill="lavender")


def draw_sun(canvas):
    """
    Draw a sun.
    Parameters
        canvas: The canvas where this function.
       
    Return: nothing
    """
    draw_arc (canvas,10, 450, 70, 490, start=0, extent=150, outline="yellow1", width=0, fill="yellow1")
    draw_arc (canvas,10, 450, 70, 490, start=150, extent=215, outline="yellow1", width=0, fill="yellow1")
    
   

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")   

def draw_road(canvas, scene_width, scene_height):
    """
    Draw a sun.
    Parameters
        canvas: The canvas where this function will draw sun.
        scene_width: width of the scene in pixels.
        scene_height: the height of the scene in pixels.
       
    Return: nothing
    """ 

    draw_rectangle(canvas, 0, 100, scene_width,0, fill="honeydew4" )
    
    for x in range(0, scene_width, 60):
        draw_rectangle(canvas, x, 55, x + 60, 45, fill="lavender" )
    
    draw_rectangle(canvas, 350, scene_height/3, 450, 100, fill="honeydew4" )
    for y in range(100, 163, 21):
         draw_rectangle(canvas, 395, y + 21, 405, y, fill="lavender" )

# Call the main function so that
# this program will start executing.
main()