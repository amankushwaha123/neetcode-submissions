class Solution:
    def trap(self, height: List[int]) -> int:
        sz = len(height) 
        lmax = [0]*sz
        rmax = [0]*sz
        res = 0
        if sz < 1:
            return 0
        else:
            for i in range(sz):
                if i == 0:
                    lmax[i] = height[i]
                else:
                    lmax[i] = max(lmax[i-1],height[i])
            for i in range(sz-1,-1,-1):
                if i == sz-1:
                    rmax[i] = height[i]
                else:
                    rmax[i] = max(rmax[i+1],height[i])
            # print("lft boundry ",lmax)
            # print("right boundry ",rmax)
            for i in range(1,sz-1):
                res += min(lmax[i],rmax[i])-height[i]
            return res
        

        
        