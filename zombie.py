import tkinter


class Zombie:

    picture = 'zombie.gif'

    def __init__(self):
        pass

    @classmethod
    def get_image_loc(cls):
        return cls.picture
