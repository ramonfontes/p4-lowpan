import matplotlib.pyplot as plt
import numpy as np

# Dados do gráfico
labels = [
    "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5",
    "Sensor 6", "Sensor 7", "Sensor 8", "Sensor 9", "Sensor 10"
]

values = [1578, 1576, 1520, 858, 792, 1636, 924, 924, 924, 792] #t5

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

ax.set_title("Total Packet Lengths - Non-Storage (5s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
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

values = [888, 916, 932, 462, 396, 976, 528, 528, 528, 396] #t10

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

ax.set_title("Total Packet Lengths - Non-Storage (10s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
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

labels = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 6"]
values = [2056, 2110, 1980, 2130] #t5

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

ax.set_title("Total Packet Lengths - Storage (5s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
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


values = [1356, 1042, 1074, 1194] #t10

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

ax.set_title("Total Packet Lengths - Storage (10s)", fontsize=16, color='black', pad=20, fontdict=dict(weight='bold'))
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
