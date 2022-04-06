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

