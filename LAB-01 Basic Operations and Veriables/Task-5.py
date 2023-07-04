velocity = int(input("Enter Velocity: "))
acceleration = int(input("Enter Acceleration: "))
time = int(input("Enter Time: "))

distance_S = velocity * time + 0.5 * acceleration * time**2

print("Distance =", distance_S)
