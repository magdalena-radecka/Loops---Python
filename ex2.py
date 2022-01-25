# Author: Magdalena Radecka (magdalenaradecka0@gmail.com)

n_to_check_1 = 1
n_to_check_2 = 5
n_to_check_3 = 8

def Exercise_2(n):

    var_sum = 0

    for i in range(n+1):
        var_sum = var_sum + i

    print("Sum of {} first integers: {}".format(n, var_sum))

Exercise_2(n_to_check_1)
Exercise_2(n_to_check_2)
Exercise_2(n_to_check_3)