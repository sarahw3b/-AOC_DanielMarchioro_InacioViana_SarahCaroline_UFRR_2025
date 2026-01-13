from z3 import *

a, b, c, d = Bools('a b c d')

F_original = Or(And(a, b, c, d), And(a, b, Not(c), d), And(a, b, Not(c), Not(d)), And(a, Not(b), c , d), And(Not(a), b, c, d), And(Not(a), b, c, Not(d)), And(Not(a), b, Not(c), d), And(Not(a), Not(b), Not(c), d)) 
F_simplificado = Or(And(a, c, d), And(a, b, Not(c)), And(b, c, Not(a)), And(d, Not(a), Not(c)))


solver = Solver()

solver.add(F_original != F_simplificado)

if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")