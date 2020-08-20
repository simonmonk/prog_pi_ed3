#06_04_json_file
import json

f = open('books.json')
j = json.load(f)
f.close()	

print(j['books'][1]['title'])