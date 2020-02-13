def RightHandTri(num):
    return_result = ''
    for column in range(num):
        for row in range(column + 1):
            print('#', end = '')
        print()
    return return_result

triangle1_result = RightHandTri(2)
triangle2_result = RightHandTri(4)

print(triangle1_result)
print(triangle2_result)
    