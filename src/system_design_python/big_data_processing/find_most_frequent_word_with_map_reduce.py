from typing import List


class MapReduceWordCounter:
    def __init__(self):
        pass
    #becasue counter must be stateless -> from problem description.
        


    def mostFrequent(self, lines: List[str]) -> str:
        freq={}
        for line in lines:
            for word in line.split():
                normalized=word.lower()
                freq[normalized]=freq.get(normalized,0)+1
        return min(freq,key=lambda word:(-freq[word],word))