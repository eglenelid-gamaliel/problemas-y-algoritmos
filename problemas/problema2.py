from enum import Enum


class Components(Enum):
    year = 31536000
    day = 86400
    hour = 3600
    minute = 60
    second = 1


def format_duration(seconds: int):
    if seconds == 0:
        return "now"

    date = ""
    seconds_left = seconds

    for component in Components:
        floor_division: int = seconds_left // component.value
        seconds_left = seconds_left % component.value

        if floor_division >= 1:
            date += f"{floor_division} {component.name}"
        if floor_division > 1:
            date += "s"

        if floor_division >= 1 and seconds_left:
            if seconds_left < 60:
                date += " and "
            else:
                date += ", "
    return date
