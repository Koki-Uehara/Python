empty_dict = {}
print(empty_dict)
# 辞書とリストはよく使用する。
# 辞書はkey : valueをカンマで区切って並べる。

bierce = {
    "day" : "a period of twenty-four hours, mostly misspent",
    "positive" : "mistaken at the top of one's voice",
    "misfortune" : "the kind of fortune that never misses"
}
print(bierce)

listA = [["a", "b"], ["c", "d"], ["e", "f"]]
listB = dict(listA)
print(listB)
