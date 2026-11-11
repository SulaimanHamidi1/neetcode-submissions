class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.counter, tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        users = self.followMap[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tid = self.tweets[user][idx]
                heap.append((time, user, tid, idx))
        heapq.heapify(heap)

        while heap and len(res) < 10:
            time, user, tid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                nt, ntid = self.tweets[user][idx-1]
                heapq.heappush(heap, (nt, user, ntid, idx - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)