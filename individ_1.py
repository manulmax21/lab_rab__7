#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from datetime import date
if __name__ == '__main__':
    students = []
    count = 0
    while True:
        command = input("Что вы хотите? ").lower()

        if command == "exit":
            break
        
        elif command == "add":
            name = input("Фамилия и инициалы? ")
            number = input("Номер группы? ")
            z = int(input("Оценка? "))
            z_1 = str(input("Успеваемость? "))

            student = {
                "name": name,
                "number": number,
                "z": z,
                "z_1": z_1
            }

            students.append(student)
            if len(student) > 1:
                students.sort(key=lambda item: item.get("name", ""))
                for idx, worker in enumerate(students, 1):
                    line =  "| {:^3} | {:^25} | {:^15} | {:^10} | {:^15} |".format(
                                idx,
                                worker.get("name", ""),
                                worker.get("number", ""),
                                worker.get("z", 0),
                                worker.get("z_1", 0)
                            )
                    print(line)
        elif command == "list":
            line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
                "-" * 3,
                "-" * 25,
                "-" * 15,
                "-" * 10,
                "-" * 15
            )
            print(line)
            print(
                "| {:^3} | {:^25} | {:^15} | {:^10} | {:^15} |".format(
                    "№",
                    "Ф.И.О.",
                    "Номер группы",
                    "Оценка",
                    "Успеваемость",
                    )
                )
            print(line)
            for idx, worker in enumerate(students, 1):
                print(
                    "| {:^3} | {:^25} | {:^15} | {:^10} | {:^15} |".format(
                        idx,
                        worker.get("name", ""),
                        worker.get("number", ""),
                        worker.get("z", 0),
                        worker.get("z_1", 0)
                    )
                
                )
                print(line)
            
        elif command == "select":
            count == 0
            mark = student.get("z", 0)
            for student in students:
                if 4 == mark or 5 == mark:
                    count -= 1
                    print(
                        "{:>5} {}".format("*",student.get("name", "")),
                        "{:>1} {}".format("группа №", student.get("number", ""))
                    )
                if count == 0:
                    print("таких студентов нет")
        elif command == "help":
            print("cписок команд:\n")
            print("add - добавить студента;")
            print("list - cписок студентов;")
            print("select - вывести список студентов имеющих оценку 4 и 5")
            print("help - тобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)