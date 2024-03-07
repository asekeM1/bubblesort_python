# nums = []
# print("Введите длину сортировки: ")
# tot = int(input())

# print("введите " + str(tot) + " чисел: ")
# for i in range(tot):
#     nums.insert(i, int(input()))

# for i in range(tot-1):
#     for j in range(tot-i-1):
#         if nums[j]>nums[j+1]:
#             temp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = temp

# print("отсортированный список:")
# for i in range(tot):
#     print(nums[i])

#пирамидальная сортировка(самая красивая и моя любимая!!)
def heapify(sort_nums, heap_size, root):  
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)
def heap(sort_nums):  
    size = len(sort_nums)
    for i in range(size, -1, -1):
        heapify(sort_nums, size, i)
    for i in range(size - 1, 0, -1):
        sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
        heapify(sort_nums, i, 0)
nums = [54, 43, 3, 11, 0]  
heap(nums)
print(nums)