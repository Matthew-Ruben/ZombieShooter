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
                        help='How many zombies you would like to face',
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
    y_top_margin = 25
    y_bottom_margin = 15
    window_height = 400
    window_width = 600
    bg_color = 'white'
    sammy_image = 'sammy.gif'
    zombie_image = 'zombie.gif'
    window_title = 'Lets play the game!'

    sammy_width = 50
    sammy_height = 50
    sammy_offset = sammy_width / 2
    zombie_width = 50
    zombie_height = 50
    zombie_speed = 2
    zombie_offset = zombie_width / 2
    bullet_width = 15
    bullet_height = 15
    bullet_speed = 2

    sammy_step = 10

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
        self.check_collisions()

        # Create Start button
        start_button = tkinter.Button(parent,
                                      text="START",
                                      width=20,
                                      command=self.start)
        start_button.grid()

        self.canvas.bind_all('<Key>', self.handle_key_presses)
        self.canvas.bind_all('<space>', self.shoot)
        self.canvas.bind('<Button-1>', self.mouse_clicked)

        self.go = False
        self.shooting()
        self.canvas.grid()

    def mouse_clicked(self, event):
        print(f'click at (x:{event.x}, y:{event.y})')

    def start(self):
        print("Start button pressed: Let the zombie horde out!")
        # returns early if go is already true
        # this prevents unwanted behavior of animated objects
        if self.go:
            return
        self.go = True

        # Start Zombies
        for zombie in self.zombies:
            self.canvas.move(zombie, ZombieShooter.zombie_speed, 0)

        self.animate()

    def handle_key_presses(self, event):
        x, y = self.canvas.coords(self.sammy)
        if event.keysym == 'w':
            if y > ZombieShooter.y_top_margin:
                self.canvas.move(self.sammy, 0, -1 * ZombieShooter.sammy_step)
        if event.keysym == 's':
            if y < ZombieShooter.window_height - ZombieShooter.y_bottom_margin:
                self.canvas.move(self.sammy, 0, ZombieShooter.sammy_step)
        if event.keysym == 'j':
            print('j')

    def shoot(self, event):
        sammy_x, sammy_y = self.canvas.coords(self.sammy)
        sammy_x_offset = ZombieShooter.sammy_width / 2
        sammy_y_offset = ZombieShooter.sammy_height / 2
        x_offset = 5
        y_offset = -20

        self.bullets.append(self.canvas.create_oval(
            sammy_x + x_offset + sammy_x_offset,  # x0
            sammy_y + y_offset + sammy_y_offset,  # y0
            sammy_x + x_offset + ZombieShooter.bullet_width,  # x1
            sammy_y + y_offset + ZombieShooter.bullet_height,  # y1
            fill='red')
        )

    def shooting(self):

        if self.go:
            for b in self.bullets:
                self.canvas.move(b, ZombieShooter.bullet_speed, 0)
        self.parent.after(10, self.shooting)

    def get_start_y(self):
        return random.randrange(ZombieShooter.y_top_margin,
                                self.window_height,
                                25)

    def get_start_x(self):
        return self.window_width + random.randrange(1, self.window_width, 25)

    def animate(self):
        for zombie in self.zombies:
            if self.go:
                x, y = self.canvas.coords(zombie)
                if x > 50:
                    self.canvas.move(zombie, -2, 0)

        self.parent.after(10, self.animate)  # Try again in 1ms

    def check_collisions(self):
        for z in self.zombies:
            zombie_mid_x, zombie_mid_y = self.canvas.coords(z)
            print(zombie_mid_x)
            print(zombie_mid_y)


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
