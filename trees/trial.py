import re
text = 'varchar()'
pattern = re.compile(r'varchar2?\s?\(?(\d*)\)?')
print(pattern)
matches = pattern.match(text)
print(matches)
# asd = [1,2,3,4,5]
# # asd.append(45)
# # print(asd)

# # asd = asd + [50]
# # print(asd)
# # ind = asd.index(3)
# # print(asd[ind+1:])
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# ind = inorder.index(postorder[-1])
# print(ind)
# leftpost = []
# for j,i in enumerate(postorder):
#     if i in inorder[0:ind]:
#         leftpost = leftpost + postorder[j : len(inorder[0:ind])]
#         break
# print(leftpost)
# rightpost = []
# for j,i in enumerate(postorder):
#     if i in inorder[ind+1:]:
#         print(j)
#         rightpost = rightpost + postorder[j : len(inorder[ind+1:])]
#         break
# print(rightpost)
# print(len(inorder[ind+1:]))
# print(postorder[1 : len(inorder[ind+1:])+1])