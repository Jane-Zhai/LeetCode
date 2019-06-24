class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 10
        self.itemperbucket = 10//self.bucket+1
        self.hash = [[] for _ in range (self.bucket)]
        print(self.hash)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.hash[key%self.bucket]:
            self.hash[key%self.bucket] = [None] * self.itemperbucket
        self.hash[key%self.bucket][key//self.bucket] = value
        print(self.hash)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if self.hash[key%self.bucket] and self.hash[key%self.bucket][key//self.bucket]!=None:
            return self.hash[key%self.bucket][key//self.bucket]
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if self.hash[key%self.bucket]:
            self.hash[key%self.bucket][key//self.bucket] = None
        print(self.hash)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hashMap = MyHashMap()
hashMap.put(1, 1)          
hashMap.put(2, 2)         
print(hashMap.get(1))            # 返回 1
print(hashMap.get(3))           # 返回 -1 (未找到)
hashMap.put(2, 1)         # 更新已有的值
print(hashMap.get(2))            # 返回 1 
hashMap.remove(2)         # 删除键为2的数据
print(hashMap.get(2))            # 返回 -1 (未找到) 