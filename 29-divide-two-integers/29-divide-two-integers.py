class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		if dividend==0:
			return 0

		def helper(dividend, divisor):
			ans = 0
			if dividend==0:
				return ans
			i = 0
			try_divisor = divisor 
			try_dividend = dividend
			while try_dividend-try_divisor>=0:
				i += 1
				try_divisor += try_divisor
			if i>=1:
				ans += 1<<(i-1)    
			try_dividend-=try_divisor//2 
			if try_dividend>0:
				# print(try_dividend, divisor)
				ans += helper(try_dividend, divisor)
			return ans
		if dividend>0 and divisor>0:
			res = helper(dividend, divisor)
			if res>=2147483647:
				res = 2147483647
			return res 

		elif dividend>0 and divisor<0:
			pos_divisor = 0-divisor
			res = helper(dividend, pos_divisor)   
			if 0-res<=-2147483648:
				return -2147483648
			return 0-res    

		elif dividend<0 and divisor>0:
			pos_dividend = 0-dividend
			res = helper(pos_dividend, divisor)         
			if 0-res<=-2147483648:
				return -2147483648
			return 0-res    

		elif dividend<0 and divisor<0:
			pos_dividend = 0-dividend
			pos_divisor = 0-divisor
			res = helper(pos_dividend, pos_divisor)       
			if res>=2147483647:
				res = 2147483647
			return res