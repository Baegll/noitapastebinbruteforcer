import requests

pastebin = "https://pastebin.com/"

test_str = "geeks"

path_list = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]

print(path_list)

for path in path_list:
    r = requests.get(pastebin+path)

    if r.status_code == 200:
        print(f"potentially valid path: {path}")
