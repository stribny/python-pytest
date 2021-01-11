def is_color(code: str) -> bool:
    if not code:
        return False
    if not code.startswith('#'):
        return False
    if not len(code) == 7:
        return False
    return True