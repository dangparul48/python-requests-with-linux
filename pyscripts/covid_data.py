import requests as rq
import sys


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


country = sys.argv[1]
status = sys.argv[2]
url = f"https://api.covid19api.com/live/country/{country}/status/{status}"
print(url)
r = rq.get(url)
cntry_list = r.json()
for cntry in cntry_list:
    print_dict(cntry)
