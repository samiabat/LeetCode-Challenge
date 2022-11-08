class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        hour_bits, answer, minute_bits = [1, 2, 4, 8], [], [1, 2, 4, 8, 16, 32] 

        def generateH(on_left, idx,  cur_hour = 0):
            if not on_left and cur_hour<12:
                pos_hours.append(str(cur_hour))
                return
            if not on_left or idx>=4: return
            chose = generateH(on_left-1, idx+1, cur_hour + hour_bits[idx])
            notchose = generateH(on_left, idx + 1, cur_hour)

        def generateM(on_left, hr, idx, cur_minute = 0):
            if not on_left and cur_minute<60:
                if cur_minute<10: answer.append(hr+':0'+str(cur_minute))
                else: answer.append(hr+':' + str(cur_minute))
                return
            if not on_left or idx>=6: return
            generateM(on_left-1, hr, idx+1, cur_minute + minute_bits[idx])
            generateM(on_left, hr, idx+1, cur_minute)

        for time in range(min(4, turnedOn+1)):
            pos_hours  = []
            generateH(time, 0)
            for pos_hour in pos_hours:
                generateM(turnedOn - time, pos_hour, 0)
        return answer
