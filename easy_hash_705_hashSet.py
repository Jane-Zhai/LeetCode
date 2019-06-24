class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 10
        self.itemperbucket = 10
        self.hash = [[] for _ in range(self.bucket)]
        print(self.hash)
        

    def add(self, key):
        if not self.hash[key%self.bucket]:
            self.hash[key%self.bucket]=[0]*self.itemperbucket
        self.hash[key%self.bucket][key//self.bucket] = 1 
        print(self.hash)
        

    def remove(self, key):
        if self.hash[key%self.bucket]:
            self.hash[key%self.bucket][key//self.bucket]=0
        print(self.hash)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        print((self.hash[key%self.bucket]!=[]) and (self.hash[key%self.bucket][key//self.bucket]==1))
        return (self.hash[key%self.bucket]!=[]) and (self.hash[key%self.bucket][key//self.bucket]==1)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。

hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)         
hashSet.contains(1)   # 返回 true
hashSet.contains(3)   # 返回 false (未找到)
hashSet.add(2)         
hashSet.contains(2)   # 返回 true
hashSet.remove(2)          
hashSet.contains(2)   