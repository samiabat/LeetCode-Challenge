class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        map = {"0":"","1":"One ", "2":"Two ","3":"Three ", "4":"Four ", "5":"Five ","6":"Six ","7":"Seven ","8":"Eight ", "9":"Nine ", "10":"Ten ", "11":"Eleven ", "12":"Twelve ","13":"Thirteen ","14":"Fourteen ","15":"Fifteen ","16":"Sixteen ", "17":"Seventeen ", "18":"Eighteen ","19":"Nineteen ","20":"Twenty ", "30":"Thirty ", "40":"Forty ", "50":"Fifty ", "60":"Sixty ", "70":"Seventy ", "80":"Eighty ", "90":"Ninety ", "100":"One Hundred ", "200":"Two Hundred ", "300":"Three Hundred ", "400":"Four Hundred ", "500":"Five Hundred ", "600":"Six Hundred ", "700":"Seven Hundred ", "800":"Eight Hundred ", "900":"Nine Hundred "}
        def three(number):
            if len(number) == 1:
                return  one(number)
            elif len(number) == 2:
                return two(number)
            elif number[0] == '0':
                return two(number[1:])
            else:
                return map[number[0]] + 'Hundred ' + two(number[1:])
        def two(number):
            if number in map:
                return map[number]
            elif number[0] == '0':
                return one(number[1])
            else:
                return map[(number[0]+'0')] + one(number[1:])
        def one(number):
            return map[number]
        
        arr =  []
        
        num = str(num)
        left = len(num) % 3
        if left:
            arr.append(num[:left])
        num = num[left:]
        while num:
            cur = num[:3]
            num = num[3:]
            arr.append(cur)
        final = ''
        add = {4:'Billion ', 3:'Million ', 2:'Thousand '}
        
        
        for idx, num in enumerate(arr):
            key = len(arr) - idx
            final += three(num)
            if key in add:
                if int(num):
                    final += add[key]
        print(arr)
        return final.rstrip()
            
            