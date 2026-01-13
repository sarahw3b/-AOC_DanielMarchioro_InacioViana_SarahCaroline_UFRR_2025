from z3 import *
import itertools

a, b, c, d = Bools('a b c d')
variaveis = [a, b, c, d]

# Expressão booleana do circuito.
F = Or(And(a, c, d), And(a, b, Not(c)), And(b, c, Not(a)), And(d, Not(a), Not(c)))
print(f"{'a':<7} | {'b':<7} | {'c':<7} | {'d':<7} |{'F (Resultado)':<12}")
print("-" * 55)

# Gerar todas as combinações possíveis (True/False).
for combinacao in itertools.product([False, True], repeat=4):
    val_a, val_b, val_c, val_d = combinacao
    
    resultado = simplify(substitute(F, (a, BoolVal(val_a)), (b, BoolVal(val_b)), (c, BoolVal(val_c)), (d, BoolVal(val_d))))
    
    print(f"{str(val_a):<7} | {str(val_b):<7} | {str(val_c):<7} | {str(val_d):<7} | {str(resultado):<12}")