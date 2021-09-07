import json
name='{"company":"dell","product":"lappy","com":"hp"}'
name_dic=json.loads(name)
print(name_dic["company"])
print(type(name_dic))

json_name=json.dumps(name_dic,indent=4)
print(json_name)
print(type(json_name))
json.dump(name_dic,open("output.json","w"))