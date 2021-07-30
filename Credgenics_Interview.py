import numpy

list_test = [12, 4, -48, 5, -1, 6, 3]

list_negative_numbers = list()
for counter, value in enumerate(list_test):
    if value < 0:
        negative_number = list_test.pop(counter)
        list_negative_numbers.append(abs(negative_number))

test_list_negative_numbers = list()
length_negative_numbers = len(list_negative_numbers)
flag_len = True
while flag_len:
    max_value = max(list_negative_numbers)
    max_index = list_negative_numbers.index(max_value)
    number_1 = list_negative_numbers.pop(max_index)
    test_list_negative_numbers.append(number_1)
    if length_negative_numbers - 2 == len(list_negative_numbers):
        flag_len = False

product_of_negative_number = numpy.prod(test_list_negative_numbers)

max_value = max(list_test)
max_index = list_test.index(max_value)
number_1 = list_test.pop(max_index)
product_max = product_of_negative_number * number_1
