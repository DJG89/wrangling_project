# note, this script only works with VPN 

import requests
import time

URL = "https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv"
# page = requests.get(URL)

response = requests.get(URL)

print('the script is working')
time.sleep(4)
print(response)
print('downloading file...please wait')
time.sleep(4)

with open('image_predictions.tsv', mode='wb') as file:
    file.write(response.content)

print('All done')