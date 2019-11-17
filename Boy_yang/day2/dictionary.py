#coding:utf-8

'''字典的特性：  字典是一种key-value的数据类型，使用就像我们上学用的字典，通过比划、字母来查对应页的详细内容。
 dict 是无序的
 key必须是唯一的，天生去重'''


info = {
    "stu1101":"TenLan Wu",
    "stu1102":"Luo Hao",
    'stu1103':'Jeff'
}

print(info)
#print(info["stu1101"])   #查
print((info.get("stu1109")))

info["stu1101"] = "王生"    #改
info["stu1105"] = "晓峰"    #增加
print(info)

#del info['stu1105']    #删除
info.pop("stu1105")
print(info)

#循环 dict
for i in  info:
    print(i,info[i])
    
