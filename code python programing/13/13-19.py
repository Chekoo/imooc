#coding=utf-8
class SortedKeyDict(dict):
    def skeys(self):
        return sorted(self.keys())
d = SortedKeyDict((('hello', 66), ('world', 88), ('xinyi', 99)))
print d.skeys()