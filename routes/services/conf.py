from enum import Enum


class _Enum(Enum):
    @classmethod
    def get_value_from_name(self, name):
        for e in self:
            if e.name.lower() == name.lower():
                return e.value
        return None


class GymKey(_Enum):
    eden_rock_edinburgh = 'eden_edi'
    eden_rock_carlisle = 'eden_carl'


def forDjango(cls):
    cls.do_not_call_in_templates = True
    return cls


@forDjango
class GradeSubIcon(_Enum):
    lowest = 'fa fa-arrow-circle-down fa-2x'
    low = 'fa fa-arrow-circle-right fa-2x rotate-45-right'
    medium = 'fa fa-arrow-circle-right fa-2x'
    high = 'fa fa-arrow-circle-up fa-2x rotate-45-right'
    highest = 'fa fa-arrow-circle-up fa-2x'


class Grade(_Enum):
    purple = 1
    orange = 2
    green = 3
    yellow = 4
    blue = 5
    white = 6
    red = 7
    black = 8


class GradeSub(_Enum):
    null = 0
    lowest = 1
    low = 2
    medium = 3
    high = 4
    highest = 5


class ClimbStatus(_Enum):
    unclimbed = 0
    attempted = 1
    climbed = 2
    flashed = 3
    onsight = 4

    @staticmethod
    def get_default():
        self = ClimbStatus
        return self.unclimbed


def get_grade_names():
    return [e.name for e in Grade]


def get_grade_sub_names():
    return [e.name for e in GradeSub]
