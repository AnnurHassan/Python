def f_to_c(f_temp):
    temp = (f_temp - 32) * 5 / 9
    return temp


def c_to_f(c_temp):
    temp = c_temp * (9 / 5) + 32
    return temp


def get_force(mass, acc):
    return mass * acc


def get_energy(mass, c):
    return mass * pow(c, 2)


def get_work(mass, acc, dist):
    return get_force(mass, acc) * dist
