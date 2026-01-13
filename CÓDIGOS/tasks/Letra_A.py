from z3 import *
import itertools

# 1. Definir variáveis booleanas
x, y, z = Bools('x y z')
variaveis = [x, y, z]

# 2. Expressão booleana do circuito
F = Or(And(x, Not(And(y, z))), And(Or(Not(x), y), Not(Or(y, And(Not(z), x)))))
 
# 3. Cabeçalho da tabela
print(f"{'x':<7} | {'y':<7} | {'z':<7} | {'F (Resultado)':<12}")
print("-" * 45)

# 4. Gerar todas as combinações possíveis (True/False)
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


