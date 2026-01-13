from z3 import *
import itertools
import random

def full_adder(a, b, cin):
    s = Or(And(Or(And(a, Not(b)), And(Not(a), b)), Not(cin)), And(Not(Or(And(a, Not(b)), And(Not(a), b))), cin))
    cout = Or(And(a, b), And(cin, Or(And(a, Not(b)), And(Not(a), b))))
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

print(f"Gerando 10 exemplos aleatórios no console...\n")
print(f"{'A (bin)':<10} | {'B (bin)':<10} | {'Cin':<3} | {'Cout':<4} | {'Soma (bin)':<10}")
print("-" * 55)

for _ in range(10):
    # Valores aleatórios para o exemplo
    va = [random.choice([True, False]) for _ in range(8)]
    vb = [random.choice([True, False]) for _ in range(8)]
    vcin = random.choice([True, False])
    
    # Substituição no Z3
    subs = [(Cin, BoolVal(vcin))] + [(A[i], BoolVal(va[i])) for i in range(8)] + [(B[i], BoolVal(vb[i])) for i in range(8)]
    
    res_soma = [is_true(simplify(substitute(s, *subs))) for s in soma_bits]
    res_cout = is_true(simplify(substitute(Cout, *subs)))
    
    print(f"{bits_to_str(va):<10} | {bits_to_str(vb):<10} | {int(vcin):<3} | {int(res_cout):<4} | {bits_to_str(res_soma)}")

print(f"\nGerando arquivo 'tabela_verdade_8bits.txt'...")
print("Isso pode levar alguns segundos devido às 131.072 combinações...")

with open("tabela_verdade_8bits_simplficado.txt", "w") as f:
    # Cabeçalho do arquivo
    f.write("A(7-0) B(7-0) Cin | Cout Soma(7-0)\n")
    f.write("-" * 40 + "\n")
    
    # Gerar todas as 2^17 combinações
    # Nota: Para performance em 131k linhas, usamos lógica booleana direta 
    # que é idêntica à do Z3 definida acima.
    for combo in itertools.product([False, True], repeat=17):
        # combo: [a0..a7, b0..b7, cin]
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