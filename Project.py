# Project

import pandas as pd
import matplotlib.pyplot as plt

# Research question: Comapre the energy production from nuclear in 5 european countries (Belgium, France, Germany, Italy and Netherlands, from 1965 to 2025.

# Load data (CSV file)
data = pd.read_csv("electricity-generation-from-nuclear.csv")

# Clean data (only include 5 countries: Belgium, France, Germany, Italy and Netherlands)
countries = ['Belgium', 'France', 'Germany', 'Italy', 'Netherlands'] 

# Create new CSV with only the 5 countries
filtered = data[(data["Entity"].isin(countries)) & (data["Year"] >= 1965) & (data["Year"] <= 2025)]

# Save as a new CSV file (I will only use this data from now on)
filtered.to_csv("5 nuclear countries.csv", index=False)

# Graph 1: Line graph showing the energy production from nuclear in Belgium, France, Germany, Italy and Netherlands from 1965 to 2025
import matplotlib.pyplot as plt

# List of countries
countries = ["France", "Belgium", "Germany", "Netherlands", "Italy"]

# Create the graph
plt.figure(figsize=(10, 6))

# Different color for each country
colors = ["blue", "midnightblue", "dodgerblue", "darkslateblue", "royalblue"]

# Plot each country
for country in countries:
    country_data = data[data["Entity"] == country]
    plt.plot(country_data["Year"], country_data["Nuclear"], label=country, color=colors[countries.index(country)])

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Nuclear electricity production (TWh)")
plt.title("Annual Nuclear Electricity Production, 1965–2025")

# Add legend and grid
plt.legend()
plt.grid(True)

# Show graph
plt.show()

# Graph 2: Bar graph showing cumulative energy production from nuclear in Belgium, France, Germany, Italy and Netherlands from 1965 to 2025

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("5 nuclear countries.csv")

# Select the five countries
countries = ["France", "Belgium", "Germany", "Netherlands", "Italy"]

df = df[df["Entity"].isin(countries)]

# Calculate the total nuclear production for each country (cumulative)
france = df[df["Entity"] == "France"]["Nuclear"].sum()
belgium = df[df["Entity"] == "Belgium"]["Nuclear"].sum()
germany = df[df["Entity"] == "Germany"]["Nuclear"].sum()
netherlands = df[df["Entity"] == "Netherlands"]["Nuclear"].sum()
italy = df[df["Entity"] == "Italy"]["Nuclear"].sum()

# Put the totals into a list
values = [france, belgium, germany, netherlands, italy]

# Country names
names = ["France", "Belgium", "Germany", "Netherlands", "Italy"]

# Create the graph
plt.figure(figsize=(10, 6))

# Create five bars with five different colors
plt.bar(
    names,
    values,
    color=["blue", "midnightblue", "dodgerblue", "darkslateblue", "royalblue"]
)

# Labels
plt.xlabel("Country")
plt.ylabel("Total nuclear electricity production (TWh)")
plt.title("Cumulative Nuclear Electricity Production, 1965–2025")

# Grid
plt.grid(axis="y", alpha=0.3)
plt.gca().set_axisbelow(True)

# Show the graph
plt.show()