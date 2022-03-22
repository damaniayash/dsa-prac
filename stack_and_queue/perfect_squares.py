import math
import numpy as np
import matplotlib.pyplot as plt
def numSquares(target: int):
	count = []
	solution_set = []
	search_set = [i*i for i in range(1,target) if i*i <= target]
	master_ss = []
	for i in range(1, len(search_set)):
		print('sub', i)
		solution_set = []
		count = []
		helper(target,count,solution_set,i,master_ss)
		print('ans:',len(count))
		print('solution_set',solution_set)

	print(min(master_ss))

def helper(target: int,count,solution_set, sub, master_ss):

	search_set = [i*i for i in range(1,target) if i*i <= target]
	print('current search_set length:',len(search_set))
	print('current search_set:',search_set)

	if target == 1:
		target = target- 1
		count.append(1)
		solution_set.append(1)

	if target == 0:
		return 

	target = target - search_set[len(search_set)-sub]
	print('target to be passed', target)
	count.append(1)
	solution_set.append(search_set[len(search_set)-sub])
	master_ss.append(len(solution_set))
	if sub != 1:
		sub = 1
	helper(target,count,solution_set,sub,master_ss)
 

numSquares(98)

# import math
# import numpy as np
# import matplotlib.pyplot as plt
# def numSquares(target: int):
# 	count = []
# 	solution_set = []
# 	search_set = [i*i for i in range(1,target) if i*i <= target]
# 	master_ss = []
# 	for i in range(1, len(search_set)):
# 		print('sub', i)
# 		solution_set = []
# 		count = []
# 		helper(target,count,solution_set,i,master_ss)
# 		print('ans:',len(count))
# 		print('solution_set',solution_set)

# 	master_ss = list(set(tuple(x) for x in master_ss))
# 	ans_array = []
# 	for i in master_ss:
# 		ans_array.append(len(i))
# 	minlen = min(ans_array)
# 	for i in master_ss:
# 		if len(i) == minlen:
# 			ans_set = i
# 			break
# 	for i in master_ss:
# 		print(i)
# 	print(minlen)

# 	# master_ss_len = []
# 	# plot_len = []
# 	# cnt=0
# 	# for i in master_ss:
# 	# 	master_ss_len.append(len(i))
# 	# 	cnt+=1
# 	# 	plot_len.append(cnt)
# 	# fig, ax = plt.subplots(1,1)
# 	# ax.bar(plot_len,master_ss_len)
# 	# ax.set_xlabel('Number of Unique Possible Solutions')
# 	# ax.set_ylabel('Length of Solution Set')
# 	# ax.set_title(f'perfect_squares for {target} solution : {ans_set}')
# 	# plt.show()


# def helper(target: int,count,solution_set, sub, master_ss):

# 	search_set = [i*i for i in range(1,target) if i*i <= target]
# 	print('current search_set length:',len(search_set))
# 	print('current search_set:',search_set)

# 	if target == 1:
# 		target = target- 1
# 		count.append(1)
# 		solution_set.append(1)

# 	if target == 0:
# 		return 

# 	target = target - search_set[len(search_set)-sub]
# 	print('target to be passed', target)
# 	count.append(1)
# 	solution_set.append(search_set[len(search_set)-sub])
# 	master_ss.append(solution_set)
# 	if sub != 1:
# 		sub = 1
# 	helper(target,count,solution_set,sub,master_ss)
 

# numSquares(10000)




# # nums=[1,2,3,4,5,6,7]
# # def binary_search(nums, target:int):
# # 	low, high = 0, len(nums) - 1
# # 	while low <= high:
# # 		mid = (low + high)//2 
# # 		if target == nums[mid]: return mid
# # 		elif target < nums[mid]: high = mid - 1
# # 		elif target > nums[mid]: low = mid + 1
# # 	return -1

# # x = binary_search(nums,2)
# # if x == -1: print('target not found')
# # else: print('target found at index:', x)
