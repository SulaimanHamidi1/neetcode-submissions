class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())
        max_counter = list(freq.values()).count(max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_counter
        )
            


            

        

