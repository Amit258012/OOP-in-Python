"""
1) What is Enum?
=> enumeration is a set of members that have associated unique constant values. Enumeration is often called enum.

These are immutable, cannot be inherited

2) when to use?
( https://www.pythontutorial.net/python-oop/python-enum-unique/ )

=> Enums are used when you have a fixed set of related values that you want to group together and refer to by name. They make your code more readable and maintainable by giving meaningful names to these values instead of using arbitrary numbers or strings.

3) Real world Example (How)?
"""

from enum import Enum


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


# Usage in code
current_light = TrafficLight.RED

if current_light == TrafficLight.RED:
    print("Stop")
elif current_light == TrafficLight.YELLOW:
    print("Ready")
elif current_light == TrafficLight.GREEN:
    print("Go")


# example 2:
class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1

    # success
    SUCCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3


code = "OK"
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print("The request completed successfully")

# for unique values use
# @enum.unique

# to set auto value for enums
# RED = auto()
