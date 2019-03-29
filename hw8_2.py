# ----------------------------------------------------------------------
# Name:        hw8_2
# Purpose:     Create animated video game
#
# Author:      Yiyi Zhang & Matthew Ruben
# ----------------------------------------------------------------------
"""
Implement a GUI app with animation in tkinter.

Create then animate two car images in response to a START and STOP
buttons.
"""
import tkinter


class ZombieShooter:

    window_height = 500
    window_width = 1000
    bg_color = 'white'
    sammy_image = 'sammy.gif'
    zombie_image = 'zombie.gif'
    window_title = 'Lets play the game!'

    def __init__(self, parent):
        self.parent = parent
        self.window_height = ZombieShooter.window_height
        self.window_width = ZombieShooter.window_width
        self.bg_color = ZombieShooter.bg_color

        self.canvas = tkinter.Canvas(parent,
                                     width=self.window_width,
                                     height=self.window_height,
                                     background=self.bg_color)

        self.parent.title(ZombieShooter.window_title)

        # Sprite Collections
        self.zombies = {}
        self.bullets = {}
        self.sammy = []

        # Create Sammy
        self.sammy = tkinter.PhotoImage(file=ZombieShooter.sammy_image)
        self.canvas.create_image(300, 300, image=self.sammy)

        # Create Zombie
        self.zom1 = Zombie(self.canvas, 0, 0)
        self.zom2 = Zombie(self.canvas)

        self.go = False
        self.canvas.grid()

    def start(self):
        self.go = True
        for zombie in self.zombies:
            self.canvas.move(zombie, 2, 0)

        self.animate()

    def animate(self):
        for zombie in self.zombies:
            if self.go:
                x_zom, y_zom = self.canvas.coords(zombie)
                if x_zom < 575:
                    self.canvas.move(zombie, zombie.speed)


class Zombie:

    picture = 'zombie.gif'

    def __init__(self, canvas, x=500, y=300, hp=100, speed=10):
        self.hp = hp
        self.speed = speed
        self.canvas = canvas

        self.zom = tkinter.PhotoImage(file=ZombieShooter.zombie_image)
        self.canvas.create_image(x, y, image=self.zom)

        self.canvas.grid()


    @classmethod
    def get_image_loc(cls):
        return cls.picture


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
