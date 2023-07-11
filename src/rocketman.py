import arcade


class Rocketman(arcade.Window):

    def __init__(self):
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 1000
        SCREEN_TITLE = 'Rocketman'
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CRIMSON)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()