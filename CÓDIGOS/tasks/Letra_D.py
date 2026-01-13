from z3 import *
import itertools

a, b, c, d = Bools('a b c d')
variaveis = [a, b, c, d]

# Expressão booleana do circuito.
F = Or(And(a, b, c, d), And(a, b, Not(c), d), And(a, b, Not(c), Not(d)), And(a, Not(b), c , d), And(Not(a), b, c, d), And(Not(a), b, c, Not(d)), And(Not(a), b, Not(c), d), And(Not(a), Not(b), Not(c), d))
 
print(f"{'a':<7} | {'b':<7} | {'c':<7} | {'d':<7} |{'F (Resultado)':<12}")
print("-" * 55)

# Gerar todas as combinações possíveis (True/False).
for combinacao in itertools.product([False, True], repeat=4):
    val_a, val_b, val_c, val_d = combinacao
    
    resultado = simplify(substitute(F, (a, BoolVal(val_a)), (b, BoolVal(val_b)), (c, BoolVal(val_c)),(d, BoolVal(val_d))))
    
    # Imprimir a linha da tabela
    print(f"{str(val_a):<7} | {str(val_b):<7} | {str(val_c):<7} | {str(val_d):<7} | {str(resultado):<12}")