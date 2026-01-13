from z3 import *

# Fórmula 1 original.
def full_adder_v1(a, b, cin):
    xor_ab = Or(And(a, Not(b)), And(Not(a), b))
    s = Or(And(xor_ab, Not(cin)), And(Not(xor_ab), cin))
    cout = Or(And(a, b), And(cin, xor_ab))
    return s, cout

# Fórmula 2 simplificada.
def full_adder_v2(a, b, cin):
    xor_ab_manual = Or(And(a, Not(b)), And(Not(a), b))
    s = Or(And(xor_ab_manual, Not(cin)), And(Not(xor_ab_manual), cin))
    cout = Or(And(a, b), And(cin, xor_ab_manual))
    return s, cout

# Configuração dos inputs de 8 bits
A = [Bool(f'a{i}') for i in range(8)] 
B = [Bool(f'b{i}') for i in range(8)]
Cin = Bool('cin')

soma_v1, soma_v2 = [], []
carry_v1, carry_v2 = Cin, Cin

for i in range(8):
    s1, carry_v1 = full_adder_v1(A[i], B[i], carry_v1)
    s2, carry_v2 = full_adder_v2(A[i], B[i], carry_v2)
    soma_v1.append(s1)
    soma_v2.append(s2)

Cout_v1 = carry_v1
Cout_v2 = carry_v2

# Solver para comparação.
solver = Solver()
desvios = []
for i in range(8):
    desvios.append(soma_v1[i] != soma_v2[i])
desvios.append(Cout_v1 != Cout_v2)

solver.add(Or(desvios))

if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes.")