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


params = {"name":"Parul","work":"wipro", "hobbies":
        ["Java","Python"],"likings": {"fb": "Facebook",
            "Ln": "LinkedIn"}}
url = "http://httpbin.org"
r = rq.get(url+"/get",params=params)
print_dict(r.json())
