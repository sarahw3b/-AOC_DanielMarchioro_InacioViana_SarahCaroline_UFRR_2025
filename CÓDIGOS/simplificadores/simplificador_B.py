from z3 import *
from sympy import sympify, simplify_logic

def z3_to_sympy_str(expr):
    s = str(expr)
    return s

def full_adder_basic_gates(a_str, b_str, cin_str):
    """
    Define a lógica do Full Adder usando apenas AND, OR, NOT.
    Xor(a, b) -> Or(And(a, Not(b)), And(Not(a), b))
    """
    # Xor(a, b) expandido
    xor_ab = f"Or(And({a_str}, Not({b_str})), And(Not({a_str}), {b_str}))"
    
    # Soma = Xor(xor_ab, cin) expandido
    soma = f"Or(And({xor_ab}, Not({cin_str})), And(Not({xor_ab}), {cin_str}))"
    
    # Cout = (a And b) Or (cin And xor_ab)
    cout = f"Or(And({a_str}, {b_str}), And({cin_str}, {xor_ab}))"
    
    return soma, cout

def simplificar_circuito(formula_str):
    expressao = sympify(formula_str)
    expressao_simplificada = simplify_logic(expressao, form='dnf') # dnf para Soma de Produtos
    
    resultado = str(expressao_simplificada)
    resultado_bonito = resultado.replace("|", " ∨ ").replace("&", " ʌ ").replace("~", "¬")
    return resultado, resultado_bonito


# Entradas: a0, b0, cin
soma_str, cout_str = full_adder_basic_gates("a0", "b0", "cin")

print("--- Simplificação da Saída SOMA (Bit 0) ---") 
simplificada_s, bonita_s = simplificar_circuito(soma_str)
print(f"Original: {soma_str}")
print(f"Simplificada: {bonita_s}\n")

print("--- Simplificação da Saída CARRY OUT (Bit 0) ---")
simplificada_c, bonita_c = simplificar_circuito(cout_str)
print(f"Original: {cout_str}")
print(f"Simplificada: {bonita_c}")