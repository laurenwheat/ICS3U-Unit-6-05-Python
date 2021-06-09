#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the smallest of 10 numbers

def avg_marks(list_of_marks):

    sum = 0
    numbers = len(list_of_marks)

    for loop_counter in list_of_marks:
        sum += loop_counter

    avg = sum / numbers

    return avg


def main():

    list_of_marks = []
    temp_mark = 0

    while True:
        try:
            temp_mark = input("Enter a mark (%): ")
            temp_mark_int = int(temp_mark)
            list_of_marks.append(temp_mark_int)

            while temp_mark_int != -1:
                temp_mark = input("Enter a mark (%): ")
                temp_mark_int = int(temp_mark)
                list_of_marks.append(temp_mark_int)

            list_of_marks.pop()

            list_avg = avg_marks(list_of_marks)
            avg_rounded = '{0:.5g}'.format(list_avg)

            print("The average is: {0}%".format(avg_rounded))
            break

        except Exception:
            print("That is not a valid input!!")


if __name__ == "__main__":
    main()
