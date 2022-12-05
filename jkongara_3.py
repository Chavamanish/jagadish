# importing libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Dataset pre processing
df = pd.read_csv("cleaned.csv")
df.drop(labels=['Unnamed: 0','full_name'],axis=1,inplace=True)

# Column seperation for target and dependent values
x = df.drop(labels=['selling_price','new-price'],axis=1)
y = df['selling_price']

# model building
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = RandomForestRegressor(n_estimators=170,min_samples_split=4,min_samples_leaf=2,max_features='log2',criterion='poisson')
model.fit(x_train,y_train)



