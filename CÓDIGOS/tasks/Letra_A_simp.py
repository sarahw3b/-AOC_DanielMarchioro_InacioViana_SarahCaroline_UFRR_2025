from z3 import *
import itertools

x, y, z = Bools('x y z')
F = Or(Not(y), And(x, Not(z)))

print(f"{'x':<7} | {'y':<7} | {'z':<7} | {'Status':<10} | {'Resultado'}")
print("-" * 55)

for combinacao in itertools.product([True, False], repeat=3):
    val_x, val_y, val_z = combinacao
    
    s = Solver()

    s.add(F)

    s.add(x == val_x)
    s.add(y == val_y)
    s.add(z == val_z)
    
    check = s.check()
    status = "SAT" if check == sat else "UNSAT"
    
    resultado = (check == sat)
    
    print(f"{str(val_x):<7} | {str(val_y):<7} | {str(val_z):<7} | {status:<10} | {resultado}")
