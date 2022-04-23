class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        def chenk(n):
            dic = {"0":"","1":"One ", "2":"Two ","3":"Three ", "4":"Four ", "5":"Five ", "6":"Six ","7":"Seven ","8":"Eight ", "9":"Nine ", "10":"Ten ", "11":"Eleven ", "12":"Twelve ","13":"Thirteen ","14":"Fourteen ","15":"Fifteen ","16":"Sixteen ", "17":"Seventeen ", "18":"Eighteen ","19":"Nineteen ","20":"Twenty ", "30":"Thirty ", "40":"Forty ", "50":"Fifty ", "60":"Sixty ", "70":"Seventy ", "80":"Eighty ", "90":"Ninety ", "100":"One Hundred ", "200":"Two Hundred ", "300":"Three Hundred ", "400":"Four Hundred ", "500":"Five Hundred ", "600":"Six Hundred ", "700":"Seven Hundred ", "800":"Eight Hundred ", "900":"Nine Hundred "}
            if str(n) in dic:
                return dic[str(n)]
            if 11<=n%100<20:
                hund = dic[str(n//100)]
                if hund:
                    hund += "Hundred "
                return hund + dic[str(n%100)]
            first = n%10
            n-=first
            if not n:
                return dic[str(first)]
            second = n%100
            n-=second
            if not  n:
                return dic[str(second)] + dic[str(first)]
            third = n%1000
            n-=third
            return dic[str(third)] + dic[str(second)] + dic[str(first)]
        def secondh(num):
            first = num%1000
            oneth = chenk(first)
            num = num//1000
            if not num:
                return oneth
            second = num%1000
            tenth = chenk(second)
            num = num//1000
            if not num:
                return tenth + 'Thousand ' + oneth
            third = num%1000
            hund = chenk(third)
            num = num//1000
            if not num:
                if tenth:
                    tenth = tenth + 'Thousand '
                return hund + 'Million ' + tenth + oneth
            fourth = num%1000
            tow = chenk(fourth)
            num = num//1000
            if tenth:
                    tenth = tenth + 'Thousand '
            if hund:
                hund = hund + 'Million '
            return  tow + 'Billion ' + hund + tenth + oneth
        return secondh(num).strip()