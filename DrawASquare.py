def drawsquare(size):
    return_result = ''
    for row in range(size):
        for column in range(size):
            print('#', end='')
        print()
    return return_result

square_size1 = drawsquare(2)
square_size2 = drawsquare(4)

print(square_size1)
print(square_size2)