class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
                    "Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", 
                    "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", 
                    "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12" 
                 }
        date = date.split()
        if len(date[0]) == 3: date[0] = '0' + date[0]
        return date[-1] + '-' + months[date[1]] + '-' + date[0][:-2] 