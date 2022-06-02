#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from datetime import date

if __name__ == '__main__':
    school = {
        "1a": 20,
        "1b": 15,
        "2b": 33,
        "5a": 17,
        "7b": 15,
        }
    print(school)
    #a/change
    school["1b"] = 19
    print("в 1b классе количество учеников изминилось на " + str(school["1b"]) + "учеников")
    #b/new class
    school["2a"] = 20
    print("в школе появился новый класс 2a,  имеет  " + str(school["2a"]) + " учеников." )
    #c/delet class
    del school["7b"]
    print("в школе, класс 7б был реформерован")
    #sum all classes
    print(f"Общая количество учеников ранаяется к {sum(school.values())}")