def find_force(m1, m2, r, g=9.8):
    force = (m1*m2*g) / (r ** 2)
    return force

result = find_force(12, 13, 14)
print(result)