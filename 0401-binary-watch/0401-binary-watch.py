class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    hour = str(h)
                    pre = "0" if m<10 else ""

                    result.append(hour + ":" + pre+str(m))
            
        return result