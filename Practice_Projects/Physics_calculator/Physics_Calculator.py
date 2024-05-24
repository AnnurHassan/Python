import Calculator_Functions as CF

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3 * 10**8

print("========================================")
f100_in_celsius = CF.f_to_c(100)
print(f"100 Degrees Fahrenheit in Celcius: {f100_in_celsius}")

print("========================================")

c0_in_fahrenheit = CF.c_to_f(0)
print(f"0 Degeers Celcius in Fahrenheit: {c0_in_fahrenheit}")

print("========================================")

train_force = CF.get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

print("========================================")

bomb_energy = CF.get_energy(bomb_mass, c)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

print("========================================")

train_work = CF.get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules if work over {train_distance} meters.")

print("========================================")
