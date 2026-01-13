from sympy import sympify, simplify_logic

def simplificar_string_booleana(formula_str):
    expressao = sympify(formula_str)
    
    expressao_simplificada = simplify_logic(expressao)
    
    return str(expressao_simplificada)

entrada = "Or(And(a, b, c, d), And(a, b, Not(c), d), And(a, b, Not(c), Not(d)), And(a, Not(b), c , d), And(Not(a), b, c, d), And(Not(a), b, c, Not(d)), And(Not(a), b, Not(c), d), And(Not(a), Not(b), Not(c), d))"
saida = simplificar_string_booleana(entrada)

saida_bool = saida.replace("|", " ∨").replace("&", "∧").replace("~", "¬")

print(f"Fórmula original: {entrada}")
print(f"Fórmula simplificada:   {saida_bool}")
