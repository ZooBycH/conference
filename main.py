import timeit


test_1 = """
list_1 = []
for i in range(1000):
    list_1.append(i)
"""

test_2 = """
list_2 = [i for i in range(1000)]
"""

test_3 = """
list_1 = []
list_1_app = list_1.append
for i in range(1000):
    list_1_app(i)
"""
elapsed_time_t1 = timeit.timeit(test_1, number=100)/100
elapsed_time_t2 = timeit.timeit(test_2, number=100)/100
elapsed_time_t3 = timeit.timeit(test_3, number=100)/100


print("Стандартный цикл:", "{:.10f}".format(elapsed_time_t1))
print("ListComprehension:", "{:.10f}".format(elapsed_time_t2))
print("Ст.цикл с выносом метода из цикла:", "{:.10f}".format(elapsed_time_t3))

