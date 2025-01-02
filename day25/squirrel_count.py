import pandas as pd

# Load the data
data = pd.read_csv("day25/squirrel_data.csv")

# Group by fur color and count
fur_color_count = data['Primary Fur Color'].value_counts()

# Rename the columns

print(type(fur_color_count))

Data = pd.DataFrame(fur_color_count)

# Display the DataFrame
Data.to_csv("day25/squirrel_color_count.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_count = len(data[data['Primary Fur Color'] == "Black"])
dictonary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
df = pd.DataFrame(dictonary)

print(dictonary)
print(df)