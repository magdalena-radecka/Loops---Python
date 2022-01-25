# Author: Magdalena Radecka (magdalenaradecka0@gmail.com)

str_to_check_1 = "taco cat"
str_to_check_2 = "niebieski"

def Exercise_4(char):

    char = char.replace(" ", "")
    result = "True"

    for i in range(len(char)):

        if (char[i].lower() != char[len(char) - 1 - i].lower()):
            result = "False"
            break

    print("Is the same for word {} : {}".format(char, result))

Exercise_4(str_to_check_1)
Exercise_4(str_to_check_2)