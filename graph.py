import matplotlib.pyplot as plt
import numpy as np

# Dados do gráfico
labels = [
    "Root", "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5",
    "Sensor 6", "Sensor 7", "Sensor 8", "Sensor 9"
]

values = [1572, 1630, 1586, 858, 792, 1570, 924, 924, 924, 792] #t5

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color='skyblue')

for bar, value in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2, 
        bar.get_height() + 100,
        f'{value}', 
        ha='center', 
        va='bottom', 
        fontsize=10, 
        color='black'
    )

ax.set_title("Total Packet Lengths - Non-Storing (5s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
ax.set_ylabel("Bytes", fontsize=14, color='black')
ax.set_xlabel("Sensors", fontsize=14, color='black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.label.set_color('black')
ax.xaxis.label.set_color('black')
ax.title.set_color('black')
plt.ylim(0,2500)
plt.savefig("non5.eps")

values = [876, 964, 926, 462, 396, 970, 528, 528, 528, 396] #t10

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color='skyblue')

for bar, value in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 100,
        f'{value}',
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Total Packet Lengths - Non-Storing (10s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
ax.set_ylabel("Bytes", fontsize=14, color='black')
ax.set_xlabel("Sensors", fontsize=14, color='black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.label.set_color('black')
ax.xaxis.label.set_color('black')
ax.title.set_color('black')

plt.ylim(0,2500)
plt.savefig("non10.eps")

labels = ["Root", "Sensor 1", "Sensor 2", "Sensor 5"]
values = [1458, 2000, 2440, 2244] #t5

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color='skyblue')

for bar, value in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 100,
        f'{value}',
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Total Packet Lengths - Storing (5s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
ax.set_ylabel("Bytes", fontsize=14, color='black')
ax.set_xlabel("Sensors", fontsize=14, color='black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.label.set_color('black')
ax.xaxis.label.set_color('black')
ax.title.set_color('black')

plt.ylim(0,2500)
plt.savefig("5.eps")


values = [906, 1112, 1246, 1206] #t10

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color='skyblue')

for bar, value in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 100,
        f'{value}',
        ha='center',
        va='bottom',
        fontsize=10,
        color='black'
    )

ax.set_title("Total Packet Lengths - Storing (10s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
ax.set_ylabel("Bytes", fontsize=14, color='black')
ax.set_xlabel("Sensors", fontsize=14, color='black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.label.set_color('black')
ax.xaxis.label.set_color('black')
ax.title.set_color('black')

plt.ylim(0,2500)
plt.savefig("10.eps")
