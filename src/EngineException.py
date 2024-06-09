class EngineException(Exception):
    def __init__(self, message, traceback: bool = False):
        self.__traceback__ = self.__traceback__ if traceback else None
        self.message = message
        self.name = "EngineException"
        print(f"[FATAL] {message}")
        print(f"[INFO] Tracebacks are {self.__traceback__ if self.__traceback__ is not None else 'not'} enabled.")
        if self.__traceback__:
            print(self.__traceback__)

        exit(1)
