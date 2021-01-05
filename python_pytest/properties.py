from datetime import datetime


class Person:
    def __init__(self, age: int):
        self.age = age

    def grow_older(self):
        if self.age > 100:
            raise ValueError()
        self.age += 1


def is_first_name(name: str) -> bool:
    if name is None or len(name) < 3:
        return False
    if not name.isalpha():
        return False
    if not name[0].isupper():
        return False
    if not name[1:].islower():
        return False
    return True


def is_before_datetime(from_date: datetime, to_date: datetime) -> bool:
    return from_date < to_date


