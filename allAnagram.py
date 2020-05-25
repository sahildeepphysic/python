class Solution:
	def findAnagrams(self,s,p):
		dict={}
		dict1={}
		list=[]
		returnList=[]
		for x in p:
			if x not in dict:
				dict[x]=1
			else:
				dict[x]+=1

		print(dict)
		for x in range(0, len(s)-len(p)+1):
			list.append(s[x:x+len(p)])
		# print(list)
		for y,word in enumerate(list):
			for x in word:
				if x not in dict1:
					dict1[x]=1
				else:
					dict1[x]+=1
			
			if dict1==dict:
				returnList.append(y)
			dict1={}
		print(returnList)


a=Solution()

print(a.findAnagrams("abab","ab"))


















# 		# print(len(p))
# 		for x in range(0, len(s)-len(p)+1):
# 			list.append(s[x:x+len(p)])
# 		print(list)
# 	# 	for y,word in enumerate(list):
# 	# 		for x in set(word):
# 	# 			if x in p:
# 	# 				count+=1
# 	# 			if count==len(p):
# 	# 				list1.append(word)
# 	# 				list2.append(y)
# 	# 				# count=0
# 	# 		count=0
# 	# # print(list1)
# 	# 	return list2
# 	for x,word in enumerate(list):
# 		if p==word:
# 			list1.append(x)
# 	print(list1)

