from matrix import Matrix
from matrix import Vector

m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
m3 = Matrix((3, 3))
m4 = Matrix([[1.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))
m5 = Matrix([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0], [2.0, 2.0, 2.0]], (3, 3))
m6 = Matrix([[1.0, 2.0]])
m7 = Matrix((3, 4))
v1 = Vector([2.0, 3.0])
print("size m1:", m1.shape)
print("size m2:", m2.shape)
print("size m3:", m3.shape)
print("size m4:", m4.shape)
print("size m5:", m5.shape)
print("size m6:", m6.shape)
print("size m7:", m7.shape)


print("SIZE m1:", m1.shape, "==>", m1)
print("SIZE m2:", m2.shape, "==>", m2)
print("SIZE m3:", m3.shape, "==>", m3)
print("SIZE m4:", m4.shape, "==>", m4)

print("m3+m4=", m3 + m4)
print("m4+m5=", m4 + m5)
print("m3+1=", m3 + 1)
print("1+m3=", 1 + m3)
print("m4-m5=", m4 - m5)
print("m4-1=", m4 - 1)
print("m4-1=", 1 - m4)
print("m4/1=", m4 / 1)
print("1/m4=", 1 / m4)
print("size m6:", m6.shape, "size v1", v1.size)
print("m6+v1", m6 + v1)
print("m6+v1", m6 - v1)
print("m6+v1", v1 - m6)
m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
print("size m1:", m1.shape, "size m2", m2.shape)
print(m1)
print(m2)
print("resultat -----------")
print("m1", m1)
print("m2", m2)
print("m1 * m2 =", m1 * m2)
print("m2 * m1 =", m2 * m1)
m2 = Matrix([[0.0, 1.0], [2.0, 3.0]])
print("v1 * m2 =", v1 * m2)
print("m2 * v1 =", m2 * v1)
print("5 * m2 =", 5 * m2)
print("v1 * m1 =", v1 * m1)
