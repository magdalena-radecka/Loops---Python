# Author: Magdalena Radecka (magdalenaradecka0@gmail.com)

arr_to_check_1 = ["ala", "ma", "kota"]
arr_to_check_2 = ["a", "b", "c"]
arr_to_check_3 = ["jan", "kowalski"]

def Exercise_3(arr):

    longest_word = arr[0]
    longest_word_length = len(arr[0])

    for i in range(len(arr)):

        if (len(arr[i]) >= longest_word_length):
            longest_word = arr[i]
            longest_word_length = len(arr[i])

    print("Longest word for array {} : {}" .format(arr, longest_word))

Exercise_3(arr_to_check_1)
Exercise_3(arr_to_check_2)
Exercise_3(arr_to_check_3)