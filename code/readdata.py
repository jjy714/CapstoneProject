import pandas as pd

df = pd.read_json('data/yelp_dataset/yelp_academic_dataset_user.json', lines=True, nrows=500)
df.info()