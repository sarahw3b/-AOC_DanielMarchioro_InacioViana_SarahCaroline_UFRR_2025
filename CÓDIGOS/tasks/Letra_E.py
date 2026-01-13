from z3 import *
import itertools

a, b, b_in = Bools('a b b_in')

def imprimir_separador(titulo):
    print(f"\n{'='*20} {titulo} {'='*20}")

def resolver_linha(expressao, vars_map):
    """Auxiliar para verificar se a combinação é SAT ou UNSAT na expressão"""
    s = Solver()
    s.add(expressao)
    for var, val in vars_map.items():
        s.add(var == val)
    
    check = s.check()
    return "SAT" if check == sat else "UNSAT", (check == sat)

imprimir_separador("TABELA VERDADE: SUBTRAÇÃO (1 BIT)")

# Definições das expressões.
Diferenca = Xor(Xor(a, b), b_in)
Emprestimo = Or(And(Not(a), b), And(Not(Xor(a, b)), b_in))

print(f"{'A':<6} | {'B':<6} | {'Bin':<6} | {'Dif (Status)':<12} | {'Empr (Status)':<12}")
print("-" * 65)

for comb in itertools.product([True, False], repeat=3):
    v_a, v_b, v_bin = comb
    mapeamento = {a: v_a, b: v_b, b_in: v_bin}
    
    st_d, res_d = resolver_linha(Diferenca, mapeamento)
    st_e, res_e = resolver_linha(Emprestimo, mapeamento)
    
    print(f"{str(v_a):<6} | {str(v_b):<6} | {str(v_bin):<6} | {st_d:<12} | {st_e:<12}")


imprimir_separador("TABELA VERDADE: FUNÇÕES LÓGICAS")
f_xor  = Xor(a, b)
f_nand = Not(And(a, b))
f_nor  = Not(Or(a, b))

print(f"{'A':<6} | {'B':<6} | {'XOR (SAT)':<10} | {'NAND (SAT)':<10} | {'NOR (SAT)':<10}")
print("-" * 55)

for comb in itertools.product([True, False], repeat=2):
    v_a, v_b = comb
    mapeamento = {a: v_a, b: v_b}
    
    st_xor, _  = resolver_linha(f_xor, mapeamento)
    st_nand, _ = resolver_linha(f_nand, mapeamento)
    st_nor, _  = resolver_linha(f_nor, mapeamento)
    
    print(f"{str(v_a):<6} | {str(v_b):<6} | {st_xor:<10} | {st_nand:<10} | {st_nor:<10}")


imprimir_separador("MAPEAMENTO DE HARDWARE: SHIFT LEFT 2")
print(f"{'Posição Saída':<15} | {'Origem do Dado':<20}")
print("-" * 40)

for i in range(8):
    origem = "Fixo em 0 (GND)" if i < 2 else f"Vem do Bit {i-2} de entrada"
    print(f"Bit {i:<11} | {origem}")