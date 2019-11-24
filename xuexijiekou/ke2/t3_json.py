#coding:utf-8
import json

k = {"a":111,
     "b":2.00,
     "c":None,
     "d":"hello",
     "e":[1,2,3],

}
print(k)
d_json = json.dumps(k)  #字典转换为json
print(d_json)

#将字符串转化为字典
j_dict = json.loads(d_json)
print(j_dict)