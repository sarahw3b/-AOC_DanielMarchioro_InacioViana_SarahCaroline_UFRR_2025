from sympy import symbols, simplify_logic, Or, And, Not, Xor

def format_expr(expr):
    if expr is False: return "0"
    if expr is True: return "1"
    if expr.is_Atom: return str(expr)
    if expr.func == Not: return "¬" + format_expr(expr.args[0])
    if expr.func == And: return " ^ ".join([format_expr(arg) for arg in expr.args])
    if expr.func == Or: return " v ".join(["(" + format_expr(arg) + ")" for arg in expr.args])
    return str(expr)

A = symbols('A0:8')
B = symbols('B0:8')

print("--- FÓRMULAS SIMPLIFICADAS DA ULA INTEIRA ---")

nand_f = simplify_logic(Not(And(A[0], B[0])), form='dnf')
nor_f = simplify_logic(Not(Or(A[0], B[0])), form='dnf')

xor_f = simplify_logic(Xor(A[0], B[0]), form='dnf')

shift_bit2 = A[0] 

print(f"NAND (Bit 0): {format_expr(nand_f)}")
print(f"NOR (Bit 0): {format_expr(nor_f)}")
print(f"XOR (Bit 0): {format_expr(xor_f)}")
print(f"SHIFT (Bit 2): {format_expr(shift_bit2)}")