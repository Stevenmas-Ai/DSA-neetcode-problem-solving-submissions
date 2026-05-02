class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res=res + str(len(s))+ "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res=[ ]
        i=0

        while i < len(s):
            j=i
            while s[j]!='#':
                j=j+1
            

          #get the length
            length = int(s[i:j])

          #Extract the string
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res