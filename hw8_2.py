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
        self.zombies = []
        self.bullets = set()
        self.sammy = []

        # Create Sammy
        self.sammy = tkinter.PhotoImage(file=ZombieShooter.sammy_image)
        self.canvas.create_image(300, 300, image=self.sammy)

        # Create Zombie
        self.zom1_img = tkinter.PhotoImage(file=ZombieShooter.zombie_image)
        self.zom1 = self.canvas.create_image(400, 200, image=self.zom1_img)
        self.zombies.append(self.zom1)

        # Create Start button
        start_button = tkinter.Button(parent,
                                      text="START",
                                      width=20,
                                      command=self.start)
        start_button.grid()

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
                x, y = self.canvas.coords(zombie)
                if x > 50:
                    self.canvas.move(zombie, -2, 0)

                self.parent.after(10, self.animate)  # Try again in 1ms




class Zombie:

    picture = 'zombie.gif'

    def __init__(self, canvas, x=500, y=300, hp=100, speed=10):
        self.hp = hp
        self.speed = speed
        self.canvas = canvas

        self.photo_image = tkinter.PhotoImage(file=ZombieShooter.zombie_image)
        self.canvas.create_image(x, y, image=self.photo_image)

        self.canvas.grid()

    def get_photo_image(self):
        return self.photo_image

    @classmethod
    def get_image_loc(cls):
        return cls.picture


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
