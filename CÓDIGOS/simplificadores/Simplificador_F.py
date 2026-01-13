from sympy import sympify, simplify_logic

def simplificar_string_booleana(formula_str):
    expressao = sympify(formula_str)
    
    expressao_simplificada = simplify_logic(expressao)

    return str(expressao_simplificada)


entrada = "And(RegDst, Not(ALUSrc), Not(MemtoReg), RegWrite, Not(MemRead), Not(MemWrite))"

saida = simplificar_string_booleana(entrada)

saida_bool = saida.replace("|", " ∨").replace("&", "ʌ").replace("~", "¬")

print(f"Fórmula original: {entrada}")
print(f"Fórmula simplificada:   {saida_bool}")