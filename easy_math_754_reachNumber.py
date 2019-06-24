class Solution:
    def reachNumber(self, target: int) -> int:
        """
        在一根无限长的数轴上，你站在0的位置。终点在target的位置。
        每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
        返回到达终点需要的最小移动次数。
        """
        # 如果sum=target，毫无疑问那么k就是最终答案。(#1)
        # 当sum-target为偶数，1+...-（sum-target）/2+...+k=target，那么答案依然是k。(#2)
        # 当sum-target为奇数，那么sum-target+1是一个偶数
        # 类似(#2)的证明，1+...-(sum-target+1)/2+...k=target-1
            # 如果k是偶数并且k>sum-target+1
                # 那么1+...-(sum-target+1)/2+....-(k/2)...+k+(k+1)=target
                # 由(#2)相似可证，相当于在1+2....+k+(k+1)减去了sum-target+1和k。
                # 等价于sum+（k+1）-sum+target-1-k====>target也就是答案是k+1.(#3)
                # 如果k=sum-target+1，由(#3)可知依然是k+1.(#4)
            # 如果k是奇数：
                # 1+2+...-(sum-target+1)/2.....+k-(k+1)+(k+2)=sum-(sum-target+1)+1=target,
                # 因此答案是k+2.(#5)

# class Solution {
#     public int reachNumber(int target) {
#         int t=Math.abs(target);
#         int s=0;
#         int dis=0;
#         while(dis<t){
#             s++;
#             dis+=s;
            
#         }
#         int dt=dis-t;
#         if(dt%2==0)
#             return s;
#         else{
#             if(s%2==0)
#                 return s+1;
#             else
#                 return s+2;
#         }
        
        
#     }
# }       