def summation(list1, list2):
  return [x + y for x, y in zip(list1, list2)]

def find_min_max(numbers):
  return min(numbers), max(numbers)


n = int(input(": "))

print(": ")
list1 = []
for _ in range(n):
    list1.append(int(input()))

print(": ")
list2 = []
for _ in range(n):
    list2.append(int(input()))


result = summation(list1, list2)
min_value, max_value = find_min_max(result)


print(result)
print(f"({min_value},{max_value})")
