import json
with open ('quotes.json') as json_file:
    data = json.load(json_file)
    f=open('text.txt','a')
    f.write("\n",join(data))
    f.close()

