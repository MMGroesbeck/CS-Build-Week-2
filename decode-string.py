#https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s):
        if s == "":
            return s
        def decoder(st):
            if st == "":
                return st
            out = ""
            while len(st) >0 and (st[0] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "["]):
                out += st[0]
                st = st[1:]
            if st == "":
                return out
            if st[0] == "[":
                multiplier = 1
            else:
                multiplier = int(st[0:st.find("[")])
            st = st[st.find("[")+1:]
            ind = 0
            layers = 1
            while layers > 0:
                ind += 1
                if st[ind] == "[":
                    layers += 1
                if st[ind] == "]":
                    layers -= 1
            out += multiplier * decoder(st[:ind])
            if len(st) > ind + 1:
                out += decoder(st[ind+1:])
            return out
        return decoder(s)

soln = Solution()
print(soln.decodeString("3[a]2[bc]"))
print(soln.decodeString("3[a2[c]]"))
print(soln.decodeString("2[abc]3[cd]ef"))