nums = []
print("Введите длину сортировки: ")
tot = int(input())

print("введите " + str(tot) + " чисел: ")
for i in range(tot):
    nums.insert(i, int(input()))

for i in range(tot-1):
    for j in range(tot-i-1):
        if nums[j]>nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print("отсортированный список:")
for i in range(tot):
    print(nums[i])