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
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()  # register it with a geometry manager

        self.sammy_image = tkinter.PhotoImage(file='sammy.gif')
        status = tkinter.Label(parent, text='Ready to Start')
        status.grid()

        self.canvas = tkinter.Canvas(parent, width=400, height=400,
                                      background='blue')
        #self.canvas.create_image(200,200,image = self.sammy_image)
        self.sammy = self.canvas.create_rectangle(0, 200, 25, 250,
                                                  fill='yellow')
        self.zombies = self.canvas.create_rectangle(375, 0, 400, 25,
                                                    fill='black')
        self.bullet =[]
        self.canvas.bind_all('<Key>', self.move)
        self.go=False
        self.shooting()
        self.canvas.grid()



    def start(self):
        """
        This method is invoked when the user presses the START button
        :return: None
        """
        self.go = True
        self.animate()

    def add(self):
        """
        This method is invoked when the user presses the STOP button
        :return: None
        """
        pass

    def move(self,event):
        xt, yt, xb, yb = self.canvas.coords(self.sammy)
        if event.keysym == 'w':
            if yt > 0:
              self.canvas.move(self.sammy, 0, -25)
        if event.keysym == 's':
            if yb < 400:
              self.canvas.move(self.sammy, 0, 25)
        if event.keysym == 'j':
            self.bullet.append(self.canvas.create_oval(25, yt+20,
                                              35, yt + 30, fill='red'))
            self.go= True


    def shooting(self):
        if self.go:
            for b in self.bullet:
              self.canvas.move(b, 1, 0)
        self.parent.after(1, self.shooting)

    def check_collision(self):


    def animate(self):
        if self.go:
            xt,yt,xb,yb = self.canvas.coords(self.zombies)
            if xt>0:
                self.canvas.move(self.zombies, -1, 0)
        self.parent.after(1, self.animate)



def main():
    root = tkinter.Tk()  # create the GUI application main window
    game = ZombieShooter(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
