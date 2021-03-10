class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
            
        result = self.getIp(s, 1)
        
        if not result:
            return
        
        ips = []
        for num1, remaining1 in result:
            for num2, remaining2 in remaining1:
                for num3, remaining3 in remaining2:
                    ips.append("{}.{}.{}.{}".format(num1, num2, num3, remaining3))   
        
        return ips
        
    def getIp(self, nums, depth):
        if len(nums) > (5 - depth) * 3:
            return
        
        if len(nums) < (4 - depth):
            return
        
        valid_ips = []
        
        for i in range(1,4):
            if i > len(nums):
                break
                
            current_num = str(nums[:i])
            if int(current_num) > 255:
                break
            
            if current_num[0] == '0' and len(current_num) > 1:
                break
            
            remaining = ""
            
            #print(i + 1 , "<", len(nums))
            if i + 1 <= len(nums):
                remaining = nums[i:]
                

            ip = self.getIp(remaining, depth + 1)
            if ip:
                valid_ips.append((current_num, ip))

            
            
            if (depth == 4 and remaining == ""):
                return current_num

            
        return valid_ips