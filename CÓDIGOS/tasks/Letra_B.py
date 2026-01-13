from z3 import *
import itertools
import random

def full_adder(a, b, cin):
    # s = (a ^ b) ^ cin
    xor_ab = Or(And(a, Not(b)), And(Not(a), b))
    s = Or(And(xor_ab, Not(cin)), And(Not(xor_ab), cin))
    # cout = (a & b) | (cin & (a ^ b))
    cout = Or(And(a, b), And(cin, xor_ab))
    return s, cout

A = [Bool(f'a{i}') for i in range(8)]
B = [Bool(f'b{i}') for i in range(8)]
Cin = Bool('cin')

soma_bits = []
carry_atual = Cin
for i in range(8):
    s, carry_atual = full_adder(A[i], B[i], carry_atual)
    soma_bits.append(s)
Cout = carry_atual

def bits_to_str(bits):
    return "".join(['1' if b else '0' for b in reversed(bits)])

print(f"Verificando 10 exemplos aleatórios com Z3 Solver...\n")
print(f"{'A (bin)':<10} | {'B (bin)':<10} | {'Cin':<3} | {'Cout':<4} | {'Soma (bin)':<10} | {'Status'}")
print("-" * 75)

for _ in range(10):
    va = [random.choice([True, False]) for _ in range(8)]
    vb = [random.choice([True, False]) for _ in range(8)]
    vcin = random.choice([True, False])
    
    s = Solver()
    
    s.add(Cin == vcin)
    for i in range(8):
        s.add(A[i] == va[i])
        s.add(B[i] == vb[i])
    
    if s.check() == sat:
        m = s.model()
        # Avaliar as expressões de saída baseadas no modelo encontrado
        res_soma = [is_true(m.evaluate(sb)) for sb in soma_bits]
        res_cout = is_true(m.evaluate(Cout))
        status = "SAT"
    else:
        status = "UNSAT"
        res_soma = [False]*8
        res_cout = False

    print(f"{bits_to_str(va):<10} | {bits_to_str(vb):<10} | {int(vcin):<3} | {int(res_cout):<4} | {bits_to_str(res_soma)} | {status}")

print(f"\nGerando arquivo 'tabela_verdade_8bits.txt'...")
print("Isso pode levar alguns segundos devido às 131.072 combinações...")

with open("tabela_verdade_8bits.txt", "w") as f:
    f.write("A(7-0) B(7-0) Cin | Cout Soma(7-0)\n")
    f.write("-" * 40 + "\n")
    

    for combo in itertools.product([False, True], repeat=17):
        va = combo[0:8]
        vb = combo[8:16]
        vcin = combo[16]
        
        # Lógica do somador aplicada à linha
        c = vcin
        res_soma = []
        for i in range(8):
            s = va[i] ^ vb[i] ^ c
            c = (va[i] & vb[i]) | (c & (va[i] ^ vb[i]))
            res_soma.append(s)
        res_cout = c
        
        # Escrever no arquivo (1 para True, 0 para False)
        line = f"{bits_to_str(va)} {bits_to_str(vb)} {int(vcin)} | {int(res_cout)} {bits_to_str(res_soma)}\n"
        f.write(line)

print("Concluído! O arquivo 'tabela_verdade_8bits.txt' foi criado com sucesso.")