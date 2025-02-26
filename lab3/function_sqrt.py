# def function_sqrt(n):
#     tmp = 0
#     for i in range(n):
#         tmp = (tmp + 3) ** 0.5
#     return tmp

def function_sqrt(n):
    if n == 0:
        return 0
    else:
        return (function_sqrt(n - 1) + 3) ** 0.5


print(function_sqrt(1))
print(function_sqrt(2))
print(function_sqrt(3))
