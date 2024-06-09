class EngineWarning(Warning):
    def __init__(self, message):
        self.__traceback__ = None
        self.message = message
        self.name = "EngineWarning"
        print(f"[WARN] {message}")
