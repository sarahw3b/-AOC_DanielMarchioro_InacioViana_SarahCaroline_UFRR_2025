from sympy import sympify, simplify_logic

def simplificar_sinal(nome_sinal, formula_str):
    expressao = sympify(formula_str)
    simplificada = simplify_logic(expressao)
    
    saida_bool = str(simplificada).replace("|", "∨").replace("&", "∧").replace("~", "¬")
    
    print(f"Sinal: {nome_sinal:<10}")
    print(f"Original:    {formula_str}")
    print(f"Simplificada: {saida_bool}")
    print("-" * 50)

formulas = {
    "Jump": "And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), op1, Not(op0))",
    
    "ALUOp0": "And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0))",
    
    "Branch": "And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0))",
    
    "ALUOp1": "And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0))",
    
    "RegDst": "And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0))",
    
    "MemWrite": "And(Not(s2), Not(s1), s0, op5, Not(op4), op3, Not(op2), op1, op0)",
    
    "MemRead": "Or(And(Not(s2), Not(s1), Not(s0)), And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0))",
    
    "MemtoReg": "And(Not(s2), Not(s1), s0, Not(op5), Not(op4), Not(op3), op2, op1, op0)",
    
    "RegWrite": "And(s2, Not(s1), Not(s0), Or(And(Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)), And(Not(op5), Not(op4), Not(op3), op2, op1, op0), And(Not(op5), Not(op4), op3, Not(op2), Not(op1), Not(op0))))",
    
    "ALUSrc": "And(Not(s2), s1, Not(s0), Or(And(Not(op5), Not(op4), Not(op3), op2, op1, op0), And(Not(op5), Not(op4), op3, Not(op2), op1, op0)))"
}

print("=== SIMPLIFICAÇÃO DE SINAIS DE CONTROLE MIPS ===\n")

for sinal, formula in formulas.items():
    simplificar_sinal(sinal, formula)