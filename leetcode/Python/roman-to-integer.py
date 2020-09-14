class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        num_arr = [conversion[roman] for roman in s]
        print(num_arr)
        total = 0
        last = 4000
        for num in num_arr:
            print(num)
            if num > last:
                total -= last * 2
                total += num
            else:
                total += num
                
            
            last = num
            
        return total
