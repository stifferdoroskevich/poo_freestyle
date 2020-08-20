from poo import Point

p1=Point()
p2=Point()

p1.reset()
print(p1.x, p1.y)

p2.move(3,7)
print(p2.x, p2.y)

try:
    p3=Point()
    print(p3.x, p3.y)
    p4=Point(8,10)
    print(p4.x, p4.y)
except Exception as e:
    print(e)
finally:
    print(p2.x)


