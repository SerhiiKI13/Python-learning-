numbers = [3, 8, 11, 14, 20, 7, 6]
def even_numbers(numbers_list):
    for num  in numbers_list:
        if num % 2 == 0:
            yield num
c = even_numbers(numbers)
for i in c:
    print(i)
        
                                                                                        



