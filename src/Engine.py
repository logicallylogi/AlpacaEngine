from src.Window import Window
from src.EngineWarning import EngineWarning
from src.utils import *
import pygame as pg


class Engine:
    def __init__(self, *args, **kwargs):
        # Engine Statics
        self.__version__ = "0.0.1"
        self.__name__ = "AlpacaEngine"
        self.__author__ = "Logic Kenzie"
        self.__license__ = "MPL-2.0"
        self.__description__ = "The primary Cython/CPython game engine for WWAlpaca games."
        self.__url__ = "logicallylogi.me/alpacaengine"
        self.__github__ = "github.com/logickenzie/alpacaengine"
        self.__issues__ = "github.com/logickenzie/alpacaengine/issues"

        # Window
        self.window = if_in_else_default(kwargs, "window", lambda: Window(*args, **kwargs))
        self.special_keys = {
            "left_shift": pg.K_LSHIFT,
            "right_shift": pg.K_RSHIFT,
            "left_control": pg.K_LCTRL,
            "right_control": pg.K_RCTRL,
            "left_alt": pg.K_LALT,
            "right_alt": pg.K_RALT,
            "left_meta": pg.K_LMETA,
            "right_meta": pg.K_RMETA,
            "left_super": pg.K_LSUPER,
            "right_super": pg.K_RSUPER,
            "numpad_0": pg.K_KP_0,
            "numpad_1": pg.K_KP_1,
            "numpad_2": pg.K_KP_2,
            "numpad_3": pg.K_KP_3,
            "numpad_4": pg.K_KP_4,
            "numpad_5": pg.K_KP_5,
            "numpad_6": pg.K_KP_6,
            "numpad_7": pg.K_KP_7,
            "numpad_8": pg.K_KP_8,
            "numpad_9": pg.K_KP_9,
            "numpad_divide": pg.K_KP_DIVIDE,
            "numpad_minus": pg.K_KP_MINUS,
            "numpad_multiply": pg.K_KP_MULTIPLY,
            "numpad_period": pg.K_KP_PERIOD,
            "numpad_plus": pg.K_KP_PLUS,
            "numpad_enter": pg.K_KP_ENTER,
            "numpad_equals": pg.K_KP_EQUALS
        }

    def add_to_loop(self, function: callable):
        self.window.loop_functions.append(function)

    def was_key_pressed(self, key):
        key = key.lower()

        if key in self.window.keys:
            return True
        else:
            try:
                return pg.key.key_code(key) in self.window.keys
            except ValueError:
                try:
                    return self.special_keys[key] in self.window.keys
                except KeyError:
                    try:
                        return self.special_keys["left_" + key] in self.window.keys
                    except KeyError:
                        EngineWarning(f"Key {key} not findable using PyGame nor Special Keys.")

    def start(self):
        self.window.__start__()
