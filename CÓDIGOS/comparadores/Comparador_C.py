from z3 import *

s2, s1, s0 = Bools('s2 s1 s0')
op5, op4, op3, op2, op1, op0 = Bools('op5 op4 op3 op2 op1 op0')

#Originais.

jump_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), op1, Not(op0)),
aluop0_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0)),
branch_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0)),
aluop1_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)),
regdst_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)),
memwrite_expr = And(Not(s2), Not(s1), s0, op5, Not(op4), op3, Not(op2), op1, op0),
memread_expr = Or(And(Not(s2), Not(s1), Not(s0)), And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0)),
memtoreg_expr = And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0),
regwrite_expr = And(s2, Not(s1), Not(s0), Or(And(Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)), And(Not(op5), Not(op4), Not(op3), op2, op1, op0), And(Not(op5), Not(op4), op3, Not(op2), Not(op1), Not(op0)))),
alusrc_expr = And(Not(s2), s1, Not(s0), Or(And(op5, Not(op4), Not(op3), Not(op2), op1, op0),And(op5, Not(op4), op3, Not(op2), op1, op0)))

# Operações simplificadas:

jump_simp = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), op1, Not(op0)),
aluop0_simp = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0)),
branch_simp = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0)),
aluop1_simp = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)),
regdst_simp = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)),
memwrite_simp = And(Not(s2), Not(s1), s0, op5, Not(op4), op3, Not(op2), op1, op0),
memread_simp = Or(And(Not(s2), Not(s1), Not(s0)), And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0)),
memtoreg_simp = And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0),
regwrite_simp = And(s2, Not(s1), Not(s0), Or(And(Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)), And(Not(op5), Not(op4), Not(op3), op2, op1, op0), And(Not(op5), Not(op4), op3, Not(op2), Not(op1), Not(op0)))),
alusrc_simp = And(Not(s2), s1, Not(s0), Or(And(op5, Not(op4), Not(op3), Not(op2), op1, op0),And(op5, Not(op4), op3, Not(op2), op1, op0)))


UC_original = [jump_expr, aluop0_expr, branch_expr, aluop1_expr, regdst_expr, memwrite_expr, memread_expr, memtoreg_expr, regwrite_expr, alusrc_expr]
UC_simplificada = [jump_simp, aluop0_simp, branch_simp, aluop1_simp, regdst_simp, memwrite_simp, memread_simp, memtoreg_simp, regwrite_simp, alusrc_simp]

solver = Solver()

def solver_all(F_original, F_simplificado):
    
    solver.add(F_original != F_simplificado)
    if solver.check() == sat:
        print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
    else:
        print("Os circuitos são equivalentes. A redundância pode ser removida.")

for i in range (10):
    solver_all(UC_original[i], UC_simplificada[i])