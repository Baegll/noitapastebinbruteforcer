import requests
import os, glob


def brutealgo(file_string):
    pastebin = "https://pastebin.com/"

    path_list = [file_string[i: j] for i in range(len(file_string)) for j in range(i + 1, len(file_string) + 1)]

    print(path_list)

    for path in path_list:
        r = requests.get(pastebin + path)

        if r.status_code == 200:
            print(f"potentially valid path: {path}")


for filename in glob.glob('*.dmp'):
    if filename != 'pastebin.py':
        print(f"Attempting bruteforce on file: {filename}")
        with open(os.path.join(os.getcwd(), filename), 'r') as f:  #open file in readonly
            # pull string from file
            file_string = f.read()
            print(file_string)
