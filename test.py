import main as alpaca_engine

window = alpaca_engine.Window()
engine = alpaca_engine.Engine(window=window)


def was_key_pressed(window_object: alpaca_engine.Window):
    if engine.was_key_pressed("space"):
        print("space was pressed")
        window_object.__window__.fill("white")


engine.add_to_loop(was_key_pressed)
engine.start()
