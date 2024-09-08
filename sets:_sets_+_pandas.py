import pandas as pd

data = {
    'article_id': [1, 2, 3, 4],
    'tags': [['python', 'data science'], ['machine learning', 'python'], ['statistics', 'data visualization'], ['python', 'web development']]
}
df = pd.DataFrame(data)

unique_tags = set()
for tags in zip(df['tags'], df['article_id']):
    unique_tags.update([(tag, tags[1]) for tag in tags[0]])

unique_tags = sorted(unique_tags, key=lambda x : x[1])
print(unique_tags)

