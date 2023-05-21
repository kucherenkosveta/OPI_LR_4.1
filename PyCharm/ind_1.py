#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_number(s):
    try:
        int(s)
    except ValueError:
        return False
    return True


def make_conversion(first, second):
    if is_number(first) and is_number(second) and first > 0 and second > 0:
        conversion = Conversion(first, second)
        return conversion
    else:
        raise ValueError


class Conversion:
    def __init__(self, first=0, second=0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.__first = first
                self.__second = second
            else:
                raise ValueError
        else:
            raise ValueError

    def read(self):
        self.__first = int(input("Enter the first value: "))
        self.__second = int(input("Enter the second value: "))

    def display(self):
        print(f"First value: {self.__first}")
        print(f"Second value: {self.__second}")

    def cost(self):
        return 60 * self.__first + self.__second


if __name__ == '__main__':
    p1 = make_conversion(3, 45)
    p1.display()
    print(f"Time in minutes: {p1.cost()}")
    p1.read()
    print(f"Time in minutes: {p1.cost()}")
    p2 = make_conversion("fhhfhf", 4)
    p2.display()
    p2.cost()