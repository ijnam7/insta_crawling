from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import csv

daegu_mask = np.array(Image.open("source\Daegu-ko.png"))

daegu_counts = {}
with open("source\daegu-counts.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    daegu_counts = {rows[0]:int(rows[1]) for rows in reader}

wc = WordCloud(
    width=1000,
    height=600,
    mask=daegu_mask,
    background_color="white",
    random_state=0, 
    font_path=r'C:\Windows\Fonts\Kopubworld Dotum_Pro Bold.OTF')

plt.imshow(wc.generate_from_frequencies(daegu_counts))
plt.axis("off")
plt.savefig("source/wordCloud.png")
plt.show()