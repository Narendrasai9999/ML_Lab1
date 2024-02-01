import pandas as pd

data = pd.read_csv("iris.data")


print("sepal length data ")
print("max:", max(data['sl']))
print("min:", min(data['sl']))
print("standard deviation:", data['sl'].std())
print("Mean:", data['sl'].mean())

print("\nsepal width data ")
print("max:", max(data['sw']))
print("min:", min(data['sw']))
print("standard deviation:", data['sw'].std())
print("Mean:", data['sw'].mean())

print("\npetal length data ")
print("max:", max(data['pl']))
print("min:", min(data['pl']))
print("standard deviation:", data['pl'].std())
print("Mean:", data['pl'].mean())

# Petal width data
print("\npetal width data ")
print("max:", max(data['pw']))
print("min:", min(data['pw']))
print("standard deviation:", data['pw'].std())
print("Mean:", data['pw'].mean())


grouped_data = data.groupby('cc')
print(grouped_data)

for class_name, group in grouped_data:
    if class_name != 'Iris-setosa':
     
        correlation = group['sl'].corr(group['pl'])
        
        
        print(f"Correlation between Sepal Length and Petal Length for {class_name} is {correlation}")


for class_name, group in grouped_data:
    if class_name != 'Iris-virginica':
     
        correlation = group['sl'].corr(group['pl'])
        
        
        print(f"Correlation between Sepal Length and Petal Length for {class_name} is {correlation}")


