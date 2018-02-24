import json
from pprint import pprint

data = json.load(open('foodyo_output.json'))

#pprint(data)
#print(data['body']['Recommendations'])
for body in data['body']:
    for recomendation in body:
        print (recomendation["RestaurantName"])
        #print (recomendation.get('RestaurantID'))
        #print (recomendation)


#for i in data['body']:
 #   print i['body'][1][1]