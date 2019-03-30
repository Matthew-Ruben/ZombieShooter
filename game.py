import tkinter
import random


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
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()  # register it with a geometry manager

        self.sammy_image = tkinter.PhotoImage(file='sammy.gif')
        status = tkinter.Label(parent, text='Ready to Start')
        status.grid()

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
        self.canvas.grid()

    def start(self):
        """
        This method is invoked when the user presses the START button
        :return: None
        """
        for i in range(5):
            ztx = random.randint(400, 600)
            zty = random.randint(0, 375)
            self.zombies.append(self.canvas.create_rectangle(ztx, zty,
                                                             ztx + 25,
                                                             zty + 25,
                                                             fill='black'))
        self.go = True
        self.animate()

    def restart(self):
        pass

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
                            and bullet_right == zombie_left:
                        self.zombies.remove(z)
                        self.canvas.delete(z)
                        self.bullets.remove(b)
                        self.canvas.delete(b)
                    else:
                        self.canvas.move(b, 1, 0)

                # self.check_collision(b)

        self.parent.after(10, self.shooting)

    # def check_collision(self, b):
    #     if self.canvas.coords(b):
    #         bxt, byt, bxb, byb = self.canvas.coords(b)
    #     for z in self.zombies:
    #         if self.canvas.coords(z):
    #             xt, yt, xb, yb = self.canvas.coords(z)
    #         if byt <= yb and byb >= yt and bxb == xt:
    #             self.canvas.move(z,0, 500)
    #             self.canvas.move(b, 0, 500)

    def animate(self):
        if self.go:
            for z in self.zombies:
                xt, yt, xb, yb = self.canvas.coords(z)
                if xt > 0:
                    self.canvas.move(z, -1, 0)
        self.parent.after(10, self.animate)


def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
