class Solution(object):
    """
    爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
    最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

    选出任一 x，满足 0 < x < N 且 N % x == 0 。
    用 N - x 替换黑板上的数字 N 。
    如果玩家无法执行这些操作，就会输掉游戏。

    只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
    """
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 把偶数留给自己, 把奇数留给对手, 最后剩2的时候选择1即可赢得比赛.
        # 若己方拿到的是偶数, 每次选择 1, 就可以把奇数留给对手, 己方赢.
        # 若己方拿到的是奇数, 一定不能选择偶数, 留给对手的一定是偶数, 对手可以留给你奇数, 对手赢.
        return N % 2 == 0