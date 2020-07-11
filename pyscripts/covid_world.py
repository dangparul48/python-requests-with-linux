import requests as rq


def print_dict(data,count=0):
    for k in data:
        for i in range(count):
            print(" ",end="")
        print(f"{k} :",end="")
        if type(data[k]) == dict:
            print()
            print_dict(data[k], count+1)
        else:
            print(f" {data[k]}")


url = "https://api.covid19api.com/world/total"
print(url)
r = rq.get(url)
cntry_list = r.json()
print_dict(cntry_list)
