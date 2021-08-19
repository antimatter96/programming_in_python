# # def permute(nums):
# #   if len(nums) == 1:
# #     return [nums]
# #   result = []

# #   for i in range(len(nums)):
# #     others = nums[:i] + nums[i + 1:]
# #     other_permutations = permute(others)
# #     for permutation in other_permutations:
# #       result.append([nums[i]] + permutation)

# #   return result

# s = "abc"

# s_list = list(s)

# print(s_list)


# def permute(arr):
#   if len(arr) == 1:
#     print(arr, "returning", [arr])
#     return [arr]
#   temp = []

#   for i in range(len(arr)):
#     first_half = arr[:i]
#     second_half = arr[i + 1:]

#     permuted = permute(first_half + second_half)

#     for permutation in permuted:
#       temp.append([arr[i]] + permutation)
#       temp.append(permutation + [arr[i]])
#   print(arr, "returning", temp)
#   return temp


# temp = permute(s_list)

# s = set()
# for i in temp:
#   s.add("".join(i))
# print(s)

###############


chars = list(str(input()))
# total = chars ^ len(chars)

start = [""]

def expand(start, chars):
  new = []

  for i in chars:
    for j in start:
      new.append(i+j)
      new.append(j+i)

  new = list(set(new))

  return new

for i in range(len(chars)):
  start = expand(start, chars)
