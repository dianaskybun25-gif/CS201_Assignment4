import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json

df = pd.read_csv("random_walk.csv")

df["distance"] = round(((df["x"])**2 + (df["y"])**2)**0.5, 2)

max_distance = round(df["distance"].max(), 2)
average_distance = round(df["distance"].mean(), 2)
min_distance = df["distance"].min() # додатково :)

print("max distance:", max_distance)
print("average distance:", average_distance)
print("min distance:", min_distance) # додатково :)

filter_1 = df["distance"] > average_distance
filtered_df = df[filter_1]
print(filtered_df)

data_to_save = filtered_df.to_dict(orient='records')

with open('filtered_walk.json', 'w', encoding='utf-8') as f:
    json.dump(data_to_save, f, indent=4)

last_x = df["x"].iloc[-1]
last_y = df["y"].iloc[-1]

start_x = df["x"].iloc[0]
start_y = df["y"].iloc[0]

plt.figure(figsize=(12, 6))
plt.plot(df["x"], df["y"], color="green", label="Path Trajectory")
plt.scatter(last_x, last_y, color='red', s=75, label="Finish")
plt.scatter(start_x, start_y, color='green', s=75, label="Start", alpha=1, edgecolor='black')
plt.legend()
plt.xlabel("X coords")
plt.ylabel("Y coords")
plt.title("Walk")
plt.grid(True, linestyle='--', alpha=0.5)
#plt.show()

# додатково :)

plt.figure(figsize=(12, 6))
df['x_smooth'] = df['x'].rolling(window=3, center=True).mean()
df['y_smooth'] = df['y'].rolling(window=3, center=True).mean()
plt.plot(df['x_smooth'], df['y_smooth'], color="green", linewidth=2, label="Smooth Path")
plt.scatter(last_x, last_y, color='red', s=75, label="Finish")
plt.scatter(start_x, start_y, color='green', s=75, label="Start", alpha=1, edgecolor='black')
plt.legend()
plt.xlabel("X coords")
plt.ylabel("Y coords")
plt.title("Smoothed Walk Visualization")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
