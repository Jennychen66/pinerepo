import random
import pandas as pd 
train_x = []
train_y = []
for i in range(1,2000):
    x = random.random()*random.randrange(1,100, 2)
    y = random.random()*random.randrange(1,100, 2)
    train_x.append(x)
    train_y.append(y)
dataframe = pd.DataFrame({'X_NAME':train_x,'Y_NAME':train_y})
#index equals to truw means shwoing the index
dataframe.to_csv("example_data.csv",index=False,sep=',')

