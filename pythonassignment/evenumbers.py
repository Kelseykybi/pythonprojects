#python function to output even numbers
def filter_even_numbers(numbers):  
    return [num for num in numbers if num % 2 == 0]  

input_list = [2, 3, 10, 14, 17, 9, 4, 11]
even_numbers = filter_even_numbers(input_list)  
print(even_numbers)
