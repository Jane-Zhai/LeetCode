class Solution:
    def subdomainVisits(self, cpdomains):
        """
        一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。
        给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。
        接下来会给出一组访问次数和域名组合的列表cpdomains 。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。
        """
        dic = dict()
        for s in cpdomains:
            num,domain=s.split(" ")
            num = int(num)

            dic[domain] = dic.get(domain,0)+num
            while "." in domain:
                domain = domain.split(".",1)[1]
                dic[domain] = dic.get(domain,0)+num
            
        lis= list()
        for key, value in dic.items():
            lis.append(str(value)+" "+key)
        return lis

    
sol=Solution()
print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))