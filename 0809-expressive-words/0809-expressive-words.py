class Solution(object):
    def expressiveWords(self, S, words):
        s_dict = {}
        s_dict_legend = {}
        count = 0
        
        last_letter = None
        s_letter_count = 0
        for letter in S:
            if letter == last_letter:
                s_dict[s_letter_count] += 1
            else:
                s_letter_count += 1
                s_dict[s_letter_count] = 1
                s_dict_legend[s_letter_count] = letter
                last_letter = letter
                
        for word in words:
            last_letter = None
            letter_count = 0
            amt = 0
            stretchy = True
            word = word +" "
            
            for letter in word:
                if letter == last_letter:
                    amt += 1
                else:
                    if letter_count in s_dict_legend:
                        s_letter = s_dict_legend[letter_count]
                        s_count = s_dict[letter_count]
                        if last_letter != s_letter or amt > s_count:
                            stretchy = False
                            break
                        elif s_count > amt and s_count < 3:
                            stretchy = False
                            break
                    letter_count += 1
                    last_letter = letter
                    amt = 1
            
            if stretchy and letter_count == s_letter_count + 1:
                count += 1
        return count