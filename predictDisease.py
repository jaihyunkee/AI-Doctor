import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

train_data = pd.read_csv("Testing.csv")
test_data = pd.read_csv("Training.csv")

x = train_data.drop(columns=['prognosis'])
y = train_data["prognosis"]

print(y)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)
model = DecisionTreeClassifier()
model.fit(x.values, y)

count = 0
for col in x:
    count += 1
    print("["+ str(count) +"]"+col)
x_input = []
temp = input("Enter the number of symptoms you have: ")
temp_array = temp.split(',')
index = 0
for count in range(132):
    if count == temp_array[index]:
        x_input.append(1)
    else:
        x_input.append(0)

prediction = model.predict([x_input])
print(prediction)
