pip install wordcloud matplotlib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

developer_terms = {
    'UI': 50,
    'API': 45,
    'Framework': 40,
    'Backend': 35,
    'Frontend': 30,
    'DevOps': 25,
    'Cloud': 20,
    'Database': 15,
    'Container': 10,
    'Microservices': 5
}

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(developer_terms)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 축 숨기기
plt.show()
