class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        buc_max = 0
        min_height = 0

        while left != right:
            r_height = height[right]
            l_height = height[left]
            if r_height > min_height or l_height > min_height:
                width = right - left
                tall = min(r_height, l_height)
                area = width * tall
                if area > buc_max:
                    buc_max = area

            if r_height > l_height:
                left += 1
                min_height = l_height
            else:
                right -= 1
                min_height = r_height

        return(buc_max)