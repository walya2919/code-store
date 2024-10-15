# type differential function in and df
# type learning rate in lambda
def df(x):
    return round(4 * (x**3),2)
Lambda = 0.01
x = 2.0

# return same number that is subscript
SUBSCRIPT = [chr(_ + 8320) for _ in range (10)]
def print_subscript(num):
    num_list = list(str(num))
    sub_list = list()

    for i in num_list:
        sub_list.append(SUBSCRIPT[int(i)])
    sub_str = "".join(sub_list)

    return sub_str

# excute program
print("x{0} = {1}".format(print_subscript(0), x))
for i in range(10):
    x_prime = round(x - Lambda * df(x), 4)
    print("x{0} = {1} - {2} X {3} = {4}"\
          .format(print_subscript(i + 1), str(x),\
                  Lambda, df(x), x_prime))
    x = x_prime