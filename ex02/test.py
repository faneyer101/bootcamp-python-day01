from vector import Vector

test = Vector(5)
test = Vector((5, 10))
test = Vector((10, 5))
test = Vector([0.0, 1.0, 2.0, 3.0])
v1 = Vector(2)
v2 = Vector([2.0, 3.0])
v3 = Vector((4, 6))
print("----------------------")
print("v1+v2=", v1 + v2)
print("v1+3=", v1 + 3)
print("3+v1=", 3 + v1)
print("v1-v2=", v1 - v2)
print("v1-3=", v1 - 3)
print("3-v1=", 3 - v1)
print("v1*v2=", v1 * v2)
print("v1*3=", v1 * 3)
print("3*v2=", 3 * v2)
print("v1/3=", v1 / 3)
print("3/v1=", 3 / v1)
print("v1+v2+v3=", v1 + v2 + v3)
print("v1+v2+v3=", v1 - v2 - v3)
print("v1*v2*v3=", v1 * v2 * v3)
print("v1+v2-v3*v2=", v1 + v2 - v3 * v2)
