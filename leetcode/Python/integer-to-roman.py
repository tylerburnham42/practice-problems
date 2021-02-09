import math

symbols = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        current = num
        output = ""
        
        for symbol_index in range(len(symbols)):
            value, symbol = symbols[symbol_index]
            num = int(math.floor(current / value))
            print(num, current)
            if num > 0:
                output += num * symbol
                current -= value * num

        return output