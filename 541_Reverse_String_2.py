class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)



        #return ''.join([s[i*k:(i+1)*k][::((-1)**(i+1))] for i in range(len(s)//k+1)])

if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))