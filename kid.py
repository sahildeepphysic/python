# def kidWithCandies(candies,extraCandies):
	# for x,y in enumerate(candies):
	# 	candies[x]+=extraCandies
	# large=candies[0]
	# for x,y in enumerate(candies):
	# 	if large<=y:
	# 		candies[x]=True
	# 	else :	# 		candies[x]=False
	# return candies
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
    	maximum=max(candies)
    	for y,x in enumerate(candies):
    		if x+extraCandies>=maximum:
    			candies[y]=True
    		else:
    			candies[y]=Falses
    	return candies
a=Solution()
a.kidsWithCandies([4,2,1,1,2],1)















# kidWithCandies([4,2,1,1,2],1)
# [2,3,5,1,3]
# e=3
# [t,t,t,f,t]