from src.EngineException import EngineException


def if_in_else_default(list_searched: dict, key: str | int, default: callable):
    return list_searched[key] if key in list_searched else default()


__all__ = ["if_in_else_default", "EngineException"]
