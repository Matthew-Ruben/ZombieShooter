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
        self.zombie_images = []
        self.zombies = []
        self.bullets = set()
        self.sammy = []

        # Create Sammy
        self.sammy = tkinter.PhotoImage(file=ZombieShooter.sammy_image)
        self.canvas.create_image(300, 300, image=self.sammy)
        self.canvas.create_image(400, 300, image=self.sammy)

        # Create Zombie
        for i in range(20):
            self.zombie_images.insert(i, tkinter.PhotoImage(
                file=ZombieShooter.zombie_image))
            self.zombies.insert(i, self.canvas.create_image(
                ZombieShooter.window_width,
                i * 25,
                image=self.zombie_images[i]))
            # self.zombies.append(zombie)
            print(f'zombie # {i} created')
        print(len(self.zombies))

        zom_images = {i: tkinter.PhotoImage(file=ZombieShooter.zombie_image)
                      for i in range(20)}
        print(zom_images)
        zoms = {zom_images[i]:
                self.canvas.create_image(ZombieShooter.window_width,
                                         i * 5,
                                         image=zom_images[i])
                for i in range(20)
                }
        print(zoms)

        # Create Start button
        start_button = tkinter.Button(parent,
                                      text="START",
                                      width=20,
                                      command=self.start)
        start_button.grid()

        self.go = False
        self.canvas.grid()

    def start(self):
        print("Start button - pressed")
        self.go = True

        for zombie in self.zombies:
            self.canvas.move(zombie, 2, 0)

        self.animate()

    def get_start_pos(self):


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

        self.photo_image = tkinter.PhotoImage(file=Zombie.picture)
        self.canvas_item = self.canvas.create_image(x,
                                                    y,
                                                    image=self.photo_image)

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
