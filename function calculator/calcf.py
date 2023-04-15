import math

# f(x)=(A(x))**2+B(x)+C

A2 = int(input('Digite o valor de A:'))
B2 = int(input('Digite o valor de B:'))
C2 = int(input('Digite o valor de C:'))


# valor do delta B^2-4.a.c
delta = (pow(B2,2)-(4*A2*C2))

# formúla de bhaskara x = (-b+-√delta)/2a

x1 = ((B2*-1)+math.sqrt(delta))/2*A2
x2 = ((B2*-1)-math.sqrt(delta))/2*A2

# Vértice 

vx = (B2*-1)/22*A2 # Vértice de X

vy = (delta*-1)/4*A2 # Vértice de Y

# raízes da função

print(f'As raízes que zeram a função:({x1:.1f},{x2:.1f})')
print(f'Vértice da parabola: ({vx:.1f},{vy:.1f})')



