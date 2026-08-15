class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}  # 使用标准字典代替 defaultdict
        for s in strs:
            # 对字符串进行排序，作为字典的键
            sorted_s = ''.join(sorted(s))
            # 如果没有该键，初始化为空列表
            if sorted_s not in str_dict:
                str_dict[sorted_s] = []  
            # 将字符串添加到对应的组中
            str_dict[sorted_s].append(s)  
        return list(str_dict.values())  # 返回字典中所有值（即各个组）