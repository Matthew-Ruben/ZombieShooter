# ----------------------------------------------------------------------
# Name:        nascar0
# Purpose:     demonstrate animation with tkinter
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Implement a GUI app with animation in tkinter.

Create then animate two car images in response to a START and STOP
buttons.
branch develop
"""
import tkinter
import zombie


class ZombieShooter:

    """
    class to support a GUI with animated images.

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    parent: (tkinter.Tk) the root window object
    canvas: (tkinter.Canvas) A Canvas widget defining the race area.
    red_car_image: (tkinter.PhotoImage) image of a red car.
    old_car_image: (tkinter.PhotoImage) image of an old car.
    red_car: (integer) object ID of the red car image created on canvas.
    old_car: (integer) object ID of the old car image created on canvas.
    """

    def __init__(self, parent):
        parent.title('Lets play the game!')
        self.parent = parent

        # create a START button and associate it with the start method
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)

        start_button.grid()  # register it with a geometry manager

        # # create a STOP button and associate it with the stop method
        # stop_button = tkinter.Button(parent, text='STOP', width=20,
        #                              command=self.stop)
        # stop_button.grid() # register it with a geometry manager
        # # create a Canvas widget for the animated objects

        # self.sammy_image = tkinter.PhotoImage(file='sammy1.jpg')
        self.zombie_image = tkinter.PhotoImage(file=zombie.Zombie.get_image_loc())
        status = tkinter.Label(parent, text='Ready to Start')
        status.grid()

        self.canvas = tkinter.Canvas(parent, width=500, height=500,
                                     background='blue')

        # Sprite Collections
        self.zombies = []
        self.sammy = []
        self.bullets = {}

        self.go = False

        self.canvas.grid()

    def start(self):
        """
        This method is invoked when the user presses the START button
        :return: None
        """
        self.zombies = self.canvas.create_image(25, 50,
                                                image=Zombie.get_image)
        self.go = True
        self.animate()

    def add(self):
        """
        This method is invoked when the user presses the STOP button
        :return: None
        """
        self.go = False
        self.animate()

    def animate(self):
        pass


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
