import modules as mod # Importing classes with the modules (car components)
"""Notes:

- Read the README.md file to see the naming conventions for variables,
methods, classes and constats. So the code remains consistant.

- The 'modules.py' file creates a canvas (graphical window) with specified
width and height. If you run modules.py file alone window closes imediatly
this is why in the main file (this file) in the last line of the main method
we call 'mod.canvas.mainloop()', which is another method from the tkinter
packege to keep the window from closing.

- Graphics tools are imported in 'modules.py' file, when using graphics tools
in main file (this file) we need to use 'mod.' before the grapic tools
example: 'mod.[you choice of graphic tool here]'

...

Codes Current situation:

- Creates 'airmod' (quadrotor), 'podmod' (capsule), 'grdmod' (wheels)
objects from 'modules.py' classes and calls move() method to randomly
move around the graphical window.

...

"""

def main():
    """This is the main function were the whole program will run"""
    ##########################################################
    airmod = mod.AirMod() # Creating air module (quadrotor) from class in 'mod'
    podmod = mod.PodMod() # Creating pod module (capsule) from class in 'mod'
    grdmod = mod.GrdMod() # Creating ground module (wheels) from class in 'mod'

    while True:
        airmod.move() # Calling move method from 'AirMod' class in 'mod' file
        podmod.move() # Calling move method from 'PodMod' class in 'mod' file
        grdmod.move() # Calling move method from 'PodMod' class in 'mod' file

        mod.tk.update() # Updates graphical window to show
    ##########################################################
    mod.canvas.mainloop() # Keeps graphical window from closing instantly...

if __name__ == '__main__':
    main() # calling main
