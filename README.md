# openSourceBasic
## 오픈소스기초설계(나반)2팀
### 주제: 일반인과 대학생 프로그래머를 위한 아이디어 공유 웹/앱
***요약***

- 일반인과 대학생 프로그래머들의 아이디어 공유를 통한 다양한 프로젝트 구현하는 것이 목표이다.
- 핵심 기술로는 **개발자 전문용어 통역기**와 **AI 코드-플로우 차트 변환기**가 있다. 
- 개발자와 사용자 간 원활한 소통과 코드의 논리적 오류 파악이 용이하다는 장점이 있다. 
---
```python
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
plt.axis('off')  
plt.show()
```
---
![출력이미지](https://github.com/Choedayeon/openSourceBasic/blob/main/%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%20%EC%9D%B4%EB%AF%B8%EC%A7%80.png?raw=true)
---
