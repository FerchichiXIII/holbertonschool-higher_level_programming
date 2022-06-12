#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [0] * list_length
    for i in range(0, list_length):
        try:
            reset = my_list_1[i] / my_list_2[i]
            list[i] = reset
        except TypeError:
            reset = 0
            print("wrong type")
        except ZeroDivisionError:
            reset = 0
            print("division by 0")
        except IndexError:
            reset = 0
            print("out of range")
        finally:
            continue
    return list
