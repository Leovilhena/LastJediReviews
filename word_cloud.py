import requests
from lxml import etree
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

word_string = ''


initial_page = 'https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?type=user'

tree = etree.HTML(requests.get(initial_page).content)

xpages = tree.xpath('//span[@class="pageInfo"]/text()')
pages = int(xpages[0].replace('Page 1 of ', '').strip())

# TODO Crawl each page
# https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=2
pagination = [
    'https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page={}'.format(page)
    for page in range(1, pages+1)
]

# TODO Extract words with values and feelings
paragraphs = [
    ' '.join(p.strip() for p in paragraph.itertext())
    for paragraph in tree.xpath('//div[@class="user_review"]')
]

grades = [
    grade.xpath('count(./span[@class="glyphicon glyphicon-star"])')
    for grade in tree.xpath('//span[@class="fl"]')
]

data_weighted = tuple(zip(paragraphs, grades))


wordcloud = WordCloud(
    stopwords=STOPWORDS,
    background_color='black',
    width=1200,
    height=1000
).generate(word_string)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()
