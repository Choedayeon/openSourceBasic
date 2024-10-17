pip install wordcloud matplotlib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 개발자들이 자주 사용하는 용어와 빈도수(예시)
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

# WordCloud 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(developer_terms)

# 워드 클라우드 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 축 숨기기
plt.show()
