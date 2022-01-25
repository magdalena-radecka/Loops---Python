# Author: Magdalena Radecka (magdalenaradecka0@gmail.com)

arr_to_check = [10, -40, 0, 666, 5050, -41, 653, 123, 5932, -43, -1010]

def Exercise_1(arr):

    var_max = arr[0]
    var_min = arr[0]
    var_sum = 0
    var_mean = 0
    var_even = 0
    var_odd = 0

    for i in range(len(arr)):

        if (arr[i] > var_max):
            var_max = arr[i]

        if (arr[i] < var_min):
            var_min = arr[i]

        var_sum = var_sum + arr[i]
        var_mean = var_sum / len(arr)

        if (arr[i] % 2 == 0):
            var_even = var_even + 1

        if (arr[i] % 2 != 0):
            var_odd = var_odd + 1
    
    print("Maximum value: {}".format(var_max))
    print("Minimum value: {}".format(var_min))
    print("Sum: {}".format(var_sum))
    print("Average value: {}".format(var_mean))
    print("Number of even numbers: {}".format(var_even))
    print("Number of even numbers: {}".format(var_odd))

Exercise_1(arr_to_check)