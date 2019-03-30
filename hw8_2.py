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
import random
import argparse


def get_arguments():
    # Argument Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('num_zombies',
                        help='How many zombies would you like to face',
                        default=20)
    parser.add_argument('player_name',
                        help='What is your name',
                        default='Spartan Sammy')
    arguments = parser.parse_args()
    num_zombies = arguments.num_zombies
    player_name = arguments.player_name
    print(f'num_zombies = {repr(num_zombies)}')
    print(f'player_name = {repr(player_name)}')
    return int(num_zombies), player_name


class ZombieShooter:

    window_height = 400
    window_width = 600
    bg_color = 'white'
    sammy_image = 'sammy.gif'
    zombie_image = 'zombie.gif'
    window_title = 'Lets play the game!'



    def __init__(self, parent):
        # Utilize command line arguments
        self.num_zombies, self.player_name = get_arguments()

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
        self.bullets = []

        self.sammy_width = 50
        self.sammy_height = 50

        self.zombie_width = 50
        self.zombie_height = 50

        self.bullet_width = 20
        self.bullet_height = 20

        # Create Sammy
        self.sammy_img = tkinter.PhotoImage(file=ZombieShooter.sammy_image)
        self.sammy = self.canvas.create_image(50, 300, image=self.sammy_img)

        # Create Zombies
        for i in range(self.num_zombies):
            self.zombie_images.insert(i, tkinter.PhotoImage(
                                         file=ZombieShooter.zombie_image))
            self.zombies.insert(i, self.canvas.create_image(
                                        self.get_start_x(),
                                        self.get_start_y(),
                                        image=self.zombie_images[i]))
        print(str(len(self.zombies)) + " zombies spawned")

        # Create Start button
        start_button = tkinter.Button(parent,
                                      text="START",
                                      width=20,
                                      command=self.start)
        start_button.grid()

        self.canvas.bind_all('<Key>', self.move)
        self.canvas.bind_all('<space>', self.shoot)

        self.go = False
        self.canvas.grid()

    def start(self):
        print("Start button pressed: Let the zombie horde out!")
        self.go = True

        # Start Zombies
        for zombie in self.zombies:
            self.canvas.move(zombie, 2, 0)

        self.animate()

    def move(self, event):
        x, y = self.canvas.coords(self.sammy)
        if event.keysym == 'w':
            if y > 0:
                self.canvas.move(self.sammy, 0, -10)
        if event.keysym == 's':
            print("s pressed")
            if y < 400:
                self.canvas.move(self.sammy, 0, 10)
        if event.keysym == 'j':
            print('j')


    def shoot(self, event):
        sammy_x, sammy_y = self.canvas.coords(self.sammy)
        self.bullets.append(self.canvas.create_oval(25, sammy_y + 20,
                                                    35,
                                                    sammy_y + 30,
                                                    fill='red'))

    def shooting(self):
        if self.go:
            for b in self.bullets:
                self.canvas.move(b, 1, 0)
        self.parent.after(10, self.shooting)

    def get_start_y(self):
        return random.randrange(1, self.window_height, 25)

    def get_start_x(self):
        return self.window_width + random.randrange(1, self.window_width, 25)

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


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
