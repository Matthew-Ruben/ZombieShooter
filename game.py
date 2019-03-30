# ----------------------------------------------------------------------
# Name:        hw8
# Purpose:     Create animated video game
#
# Date:       3/29/2019
# ----------------------------------------------------------------------
"""
Implement a shooting game with animation in tkinter.

Create then animate two car images in response to a START and STOP
buttons.
"""
import tkinter
import random
import argparse

class ZombieShooter:
    """
    class to support a GUI with animated images.

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    parent: (tkinter.Tk) the root window object

    """

    def __init__(self, parent):
        self.num_zombies, self.player_name = get_arguments()
        parent.title(f'{self.player_name}! Let\'s play the game!')
        self.parent = parent
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()  # register it with a geometry manager
        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                        command=self.restart)
        restart_button.grid()

        self.sammy_image = tkinter.PhotoImage(file='sammy.gif')
        self.status = tkinter.Label(parent, text='Ready to Start')
        self.status.grid()
        rule = tkinter.Label(parent, text="w => up; s => down; j => shoot")
        rule.grid()
        self.canvas = tkinter.Canvas(parent, width=400, height=400,
                                     background='blue')
        self.canvas.create_image(200, 200, image=self.sammy_image)
        self.sammy = self.canvas.create_rectangle(0, 200, 25, 250,
                                                  fill='yellow')
        self.zombies = []
        self.bullets = []
        self.canvas.bind_all('<Key>', self.move)
        self.go = False
        self.shooting()
        self.animate()
        self.canvas.grid()

    def start(self):
        """
        This method is invoked when the user presses the START button
        :return: None
        """
        for i in range(self.num_zombies):
            ztx = random.randint(400, 600)
            zty = random.randint(0, 375)
            self.zombies.append(self.canvas.create_rectangle(ztx, zty,
                                                             ztx + 25,
                                                             zty + 25,
                                                             fill='black'))
        self.status.configure(text='Score: 0', foreground='red')
        self.go = True


    def restart(self):
        for z in self.zombies:
            self.canvas.delete(z)
        for b in self.bullets:
            self.canvas.delete(b)
        self.zombies=[]
        self.bullets=[]
        self.start()


    def move(self, event):
        sammy_left, \
            sammy_top, \
            sammy_right, \
            sammy_bottom = self.canvas.coords(self.sammy)
        if event.keysym == 'w':
            if sammy_top > 0:
                self.canvas.move(self.sammy, 0, -25)
        if event.keysym == 's':
            if sammy_bottom < 400:
                self.canvas.move(self.sammy, 0, 25)
        if event.keysym == 'j':
            self.bullets.append(self.canvas.create_oval(25, sammy_top + 20,
                                                        35, sammy_top + 30,
                                                        fill='red'))
            self.go = True

    def shooting(self):
        if self.go:
            for b in self.bullets:
                bullet_left, \
                    bullet_top, \
                    bullet_right, \
                    bullet_bottom = self.canvas.coords(b)
                for z in self.zombies:
                    zombie_left, \
                        zombie_top, \
                        zombie_right, \
                        zombie_bottom = self.canvas.coords(z)
                    if bullet_top <= zombie_bottom \
                            and bullet_bottom >= zombie_top \
                            and bullet_right >= zombie_left:
                        self.zombies.remove(z)
                        self.canvas.delete(z)
                        self.bullets.remove(b)
                        self.canvas.delete(b)
                    else:
                        self.canvas.move(b, 1, 0)
            score = self.num_zombies - len(self.zombies)
            self.status.configure(text=f'Score: {score}', foreground='red')
            if not len(self.zombies):
                self.status.configure(text='YOU WIN', foreground='red')

        self.parent.after(10, self.shooting)


    def animate(self):
        if self.go:
            for z in self.zombies:
                xt, yt, xb, yb = self.canvas.coords(z)
                if xt > 0:
                    self.canvas.move(z, -1, 0)
        self.parent.after(10, self.animate)

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


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
