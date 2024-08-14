import re

data = 'かなり昔のRX-７で東京駅まで送ってもらい、成田空港からBoeing787で高松空港まで行き、帰りはN700系で岡山から戻りました。'
g = re.findall(r'[a-zA-Z-]+\d+', data)

print(g)

