from z3 import *

x, y, z = Bools('x y z')

F_original = Or(And(x, Not(And(y, z))), And(Or(Not(x), y), Not(Or(y, And(Not(z), x)))))
F_simplificado = Or(Not(y), And(x, Not(z)))


solver = Solver()

solver.add(F_original != F_simplificado)

if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")

    