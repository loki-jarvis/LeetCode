class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countr = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for s in ransomNote:
            if s in countr:
                countr[s] += 1
            else:
                countr[s] = 1
        counts = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for s in magazine:
            if s in counts:
                counts[s] += 1
            else:
                counts[s] = 1
        filt=0
        for i in countr:
            if(countr[i]>counts[i]):
                filt += 1
        if(filt != 0):
            return False
        else:
            return True
