import requests
import sys


url=str(sys.argv[1])
resp = requests.get(url)
print(resp.json())

