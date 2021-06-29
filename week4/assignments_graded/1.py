# standard deviation
import math

inp = 1
arr = []
while inp != "END":
    inp = input()
    arr.append(inp)
arr.pop()
for i in range(0, len(arr)):
    arr[i] = float(arr[i])
# print(arr)
n_sum = 0
for e in arr:
    n_sum += e
x_bar = n_sum/len(arr)
# print(n_sum, x_bar)
sum_dev = 0
for e in arr:
    sum_dev += (e - x_bar)**2
# print(sum_dev)
var = (sum_dev/(len(arr)-1))
print("{:.2f}".format(math.sqrt(var)))
