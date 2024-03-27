import matplotlib.pyplot as plt


x_coordinates = []
with open('x_coordinates.txt', 'r') as f:
    for line in f:
        x_coordinates.append(int(line.strip()))


y_coordinates = []
with open('y_coordinates.txt', 'r') as f:
    for line in f:
        y_coordinates.append(int(line.strip()))


plt.figure(figsize=(8, 6))
plt.hexbin(x_coordinates, y_coordinates, gridsize=30, cmap='Blues', alpha=0.7)
plt.colorbar(label='Counts')
plt.title('Heatmap of Locations')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
