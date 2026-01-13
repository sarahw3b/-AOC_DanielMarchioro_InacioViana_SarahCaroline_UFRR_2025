from z3 import *

def ula_original(a, b, sel):
    return If(sel == 0, a - b,
           If(sel == 1, a ^ b,
           If(sel == 2, ~(a & b),
           If(sel == 3, ~(a | b),
           If(sel == 4, a << 2, BitVecVal(0, 8))))))

def ula_simplificada(a, b, sel):
    # Modelo usando as simplificações de hardware
    nand_hw = ~a | ~b
    nor_hw = ~a & ~b
    sub_hw = a + (~b + 1)
    return If(sel == 0, sub_hw,
           If(sel == 1, a ^ b,
           If(sel == 2, nand_hw,
           If(sel == 3, nor_hw,
           If(sel == 4, a << 2, BitVecVal(0, 8))))))

# Variáveis simbólicas para os testes.
a, b = BitVecs('a b', 8)
sel = BitVec('sel', 3)

print("--- [TESTE 1] VALIDAÇÃO DE SAÍDA (Amostra Específica) ---")
s_val = Solver()

resultado_teste = ula_original(BitVecVal(10, 8), BitVecVal(12, 8), BitVecVal(1, 3))
s_val.add(resultado_teste != BitVecVal(6, 8))

if s_val.check() == unsat:
    print("Resultado: A saída atende às especificações (1010 XOR 1100 = 0110).")
else:
    print("Resultado: A especificação falhou.")

print("\n--- [TESTE 2] VERIFICAÇÃO DE REDUNDÂNCIA (Equivalência) ---")
s_red = Solver()
# Procura por falhas, onde a original é diferente da simplificada.
s_red.add(ula_original(a, b, sel) != ula_simplificada(a, b, sel))

if s_red.check() == unsat:
    print("Resultado: Os circuitos são equivalentes. Redundância confirmada!")
else:
    print("Resultado: Os circuitos NÃO são equivalentes.")