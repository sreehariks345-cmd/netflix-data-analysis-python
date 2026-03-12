import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("netflix_titles.csv")

# Show first rows
print(data.head())

# Count Movies vs TV Shows
type_counts = data["type"].value_counts()
print(type_counts)

# Plot Movie vs TV Shows
type_counts.plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

# Top 10 countries producing Netflix content
country_counts = data["country"].value_counts().head(10)
print(country_counts)

country_counts.plot(kind="bar")

plt.title("Top Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.show()