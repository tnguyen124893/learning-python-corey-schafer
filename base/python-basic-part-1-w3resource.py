# https://www.w3resource.com/python-exercises/python-basic-exercises.php

#1 
# print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')

#2
# import platform
# print(platform.python_version_tuple())

#3
# from datetime import datetime
# today = datetime.today()
# print(today.strftime("%Y-%m-%d %H:%M:%S"))

#4
# from math import pi
# r = float(input())
# area = pi*r**2
# print(area)

#5
# first_name = input("Your first name is:")
# last_name = input("Your last name is:")
# print(last_name + " " + first_name)

#6
# seq = input("Your sequence is ")
# list = seq.split(",")
# tuple = tuple(list)
# print(list)
# print(tuple)

#7
# filename = input("Filename is ")
# filename_split = filename.split(".")
# print(filename_split[1])

#8
# color_list = ["red", "green", "white", "black"]
# print(color_list[0])
# print(color_list[-1])

#9
# import datetime
# exam_st_date = (11,12,2014)
    # exam_date = datetime.date(year=exam_st_date[2], month=exam_st_date[1], day=exam_st_date[0])
    # print(exam_date)
    # print("The exam starts from: %i / %i / %i"%exam_st_date)

#10
# n = input("Your integer is ")
# # first = int(n)
# # second = int(n+n)
# # third = int(n+n+n)

# first = int("%s" %n)
# second = int("%s%s" %(n,n))
# third = int("%s%s%s" %(n,n,n))

# print(first+second+third)

#11
# print(abs.__doc__)

#12
# import calendar
# month = int(input("Month is "))
# year = int(input("Year is "))
# print(calendar.month(year, month))

# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

#13
# print("""
# a string that you "don't" have to escape
# This
# is a .... multi-line
# heredoc string --> example
# """
# )

#14
# import datetime
# first_date = datetime.date(2014,7,2)
# second_date = datetime.date(2014,7,11)
# delta = second_date - first_date
# print(delta)

#15
# import math
# vol_sphere = (4/3) * math.pi * 6**3
# print(vol_sphere)

#16
# n = int(input("Your number is: "))
# delta = n-17
# if delta > 0:
#     print(delta * 2)

# def diff(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2

# print(diff(22))
# print(diff(2))

#17
# def near_thousands(n):
#     return ((abs(n - 1000) <= 100) or (abs(n - 2000) <= 100))

# print(near_thousands(1009))

#18
# def random_sum(n1, n2, n3):
#     sum = n1 + n2 + n3
#     if n1 == n2 == n3:
#         return sum * 3
#     else:
#         return sum

# print(random_sum(3,3,3))

#19
# def check_string(s):
#     if s[:2] == "Is":
#         return s
#     else:
#         return "Is " + s

# print(check_string("Is it me you're looking for?"))

#20
# def multiply_str(str, n):
#     result = ""
#     for i in range(n):
#         result = result + str
#     return result

# print(multiply_str("Hello", 3))
