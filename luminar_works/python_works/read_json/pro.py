from json import load
path="C:\\Users\\VICTUS\\OneDrive\\Desktop\\adulpy\\read_json\\data.json"

with open(path) as f:
    records=load (f)
# print(str(records))    

fw_names=[f.get("name") for f in records]
print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

# print python frame woks

py_fw=[r.get("name") for f in records if r.get("language")=="python"]
print((py_fw))




# backend frame works
