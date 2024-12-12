import matplotlib.pyplot as plt
import numpy as np

# Dados do gráfico
labels = [
    "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5",
    "Sensor 6", "Sensor 7", "Sensor 8", "Sensor 9"
]

values = [1508, 1476, 792, 726, 1486, 858, 924, 924, 660] #t5

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
plt.ylim(0,3000)
plt.savefig("assets/images/non5.eps")

values = [970, 920, 462, 396, 964, 528, 528, 528, 396] #t10

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

plt.ylim(0,3000)
plt.savefig("assets/images/non10.eps")

labels = ["Sensor 1", "Sensor 2", "Sensor 5"]
values = [1814, 2206, 2052] #t5

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

plt.ylim(0,3000)
plt.savefig("assets/images/5.eps")


values = [1154, 1300, 1284] #t10

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

plt.ylim(0,3000)
plt.savefig("assets/images/10.eps")
