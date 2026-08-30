class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[""]:
            return ''
        if strs==[]:
            return 'NA'
        to_send=strs[0]
        for i in range(1,len(strs)):
            to_send+='/:;:;/'
            to_send+=strs[i]
        return to_send

    def decode(self, s: str) -> List[str]:
        if s=='':
            return [""]
        if s=='NA':
            return []
        if '/:;:;/' not in s:
            return [s]
        
        return s.split('/:;:;/')
