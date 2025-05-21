# mine:
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_c = 0
        self.tweet_saver = {}
        self.follow_saver = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.tweet_saver:
            self.tweet_saver[userId] = []
        self.tweet_saver[userId] = [[self.time_c,tweetId]] + self.tweet_saver[userId]
        self.time_c += 1
        if userId not in self.follow_saver:
            self.follow_saver[userId] = []       
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.tweet_saver:
            self.tweet_saver[userId] = []
        if userId not in self.follow_saver:
            self.follow_saver[userId] = [] 
        tmp = self.tweet_saver[userId].copy()
        for i in range(len(self.follow_saver[userId])):
            if not tmp:
                tmp = self.tweet_saver[self.follow_saver[userId][i]]
            elif not self.tweet_saver[self.follow_saver[userId][i]]:
                continue
            else:
                res = []
                i_cp = self.tweet_saver[self.follow_saver[userId][i]].copy()
                while tmp and i_cp:
                    if i_cp[0][0] > tmp[0][0]:
                        res.append(i_cp.pop(0))
                    else:
                        res.append(tmp.pop(0))
                if tmp:
                    res += tmp
                if i_cp:
                    res += i_cp
                tmp = res.copy()
        return [i[1] for i in tmp[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_saver:
            self.follow_saver[followerId] = []
        if followeeId not in self.follow_saver:
            self.follow_saver[followeeId] = []
        if followerId not in self.tweet_saver:
            self.tweet_saver[followerId] = []
        if followeeId not in self.tweet_saver:
            self.tweet_saver[followeeId] = []
        if followerId == followeeId or followeeId in self.follow_saver[followerId]:
            return
        self.follow_saver[followerId] += [followeeId]


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_saver:
            self.follow_saver[followerId] = []
            return 
        if followeeId in self.follow_saver[followerId]:
            self.follow_saver[followerId].remove(followeeId)


# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)
