import math
import numpy as np

class Point:
    
    def __init__(self, pos):
        points = pos.strip().split(",")
        self.x = int(points[0])
        self.y = int(points[1])
        self.z = int(points[2])
        self.circuit = -1
        
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2 +
            (self.z - other.z)**2
        )
        
    def same_circuit(self, other):
        return self.circuit == other.circuit and self.circuit != -1
    
    def __repr__(self):
        return f"{self.x};{self.y};{self.z}:{self.circuit}"

points = []

with open("input2.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        #print(line)
        points.append(Point(line))



grid = np.zeros((len(points), len(points)), dtype=int)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        grid[i][j] = points[i].distance(points[j])


number_of_circuits = 0
last_minimum_distance = 0
i = 0

while i < 1000:
    positive = grid[grid > last_minimum_distance]
    smallest = positive.min()
    last_minimum_distance = smallest
    
    firsts_index, seconds_index = np.where(grid == smallest)
        
    for j in range(len(firsts_index)):
    
        first = points[firsts_index[j]]
        second = points[seconds_index[j]]
        i += 1
        #print("first", first.circuit, "second", second.circuit)
        
        if (not first.same_circuit(second)):
            if first.circuit != -1:
                if second.circuit != -1:
                    circuit_to_change = second.circuit
                    for point in points:
                        if point.circuit == circuit_to_change:
                            point.circuit = first.circuit
                else:
                    second.circuit = first.circuit
            elif second.circuit != -1:
                first.circuit = second.circuit
            else:
                first.circuit = number_of_circuits
                second.circuit = number_of_circuits
                number_of_circuits += 1
            
    
circuits = [0] * number_of_circuits

for point in points:
    if point.circuit != -1:
        circuits[point.circuit] += 1
        
circuits = sorted(circuits, reverse=True)

print(circuits[0] * circuits[1] * circuits[2])


print(circuits)
#for point in points:
#    print(point)
    
    
#print(grid)
#print("smallest", smallest, "grid", row, col)