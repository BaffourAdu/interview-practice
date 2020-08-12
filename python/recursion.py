def get_fib(position):
    if position == 0 or position == 1:
        return position
    
    print("Position : " , position - 1 , " + ", "Position : " , position - 2)
    result = get_fib(position - 1) + get_fib(position - 2)
    print("Result : " , result)

    return result

# Test cases
print(get_fib(9))
# print(get_fib(11))
# print(get_fib(0))
