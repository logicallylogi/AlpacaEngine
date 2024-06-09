from src.utils import *
import pygame as pg


class Window:

    def __init__(self, *args, **kwargs):
        self.width = kwargs.get("width", 1280)
        self.height = kwargs.get("height", 720)
        self.title = kwargs.get("title", "Untitled")
        self.icon = kwargs.get("icon", None)
        self.fullscreen = kwargs.get("fullscreen", False)
        self.fps = kwargs.get("fps", 60)

        self.clock = pg.time.Clock()
        self.loop_functions = []
        self.active = True
        self.delta = 0

        self.keys = pg.key.ScancodeWrapper()

    def __start__(self):
        pg.init()
        self.__window__ = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title) if self.title else None
        pg.display.set_icon(self.icon) if self.icon else None
        pg.display.toggle_fullscreen() if self.fullscreen else None
        while self.active:
            self.__update__()

    def __update__(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
                pg.quit()
                exit()

        self.__window__.fill("black")
        self.keys = pg.key.get_pressed()

        for function in self.loop_functions:
            try:
                function(self)
            except Exception as e:
                EngineException(f"Error in loop function {function.__name__}: {e}", traceback=True)

        pg.display.flip()
        self.delta = self.clock.tick(self.fps) / 1000
