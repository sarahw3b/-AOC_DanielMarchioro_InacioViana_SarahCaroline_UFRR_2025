from z3 import *
import itertools

s2, s1, s0 = Bools('s2 s1 s0')
op5, op4, op3, op2, op1, op0 = Bools('op5 op4 op3 op2 op1 op0')

# Jump: Estado 2 (010) e OpCode 000010
jump_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), op1, Not(op0))

# ALUOp0 e Branch: Estado 2 (010) e OpCode 000100 (BEQ)
aluop0_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0))

branch_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), op2, Not(op1), Not(op0))

# ALUOp1 e RegDst: Estado 2 (010) e OpCode 000000 (R-Type)
aluop1_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0))

regdst_expr = And(Not(s2), s1, Not(s0), Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0))

# MemWrite: Estado 1 (001) e OpCode 101011 (SW)
memwrite_expr = And(Not(s2), Not(s1), s0, op5, Not(op4), op3, Not(op2), op1, op0)

# MemRead: Estado 0 (000) OU [Estado 1 (001) e OpCode 100011 (LW)]
memread_expr = Or(And(Not(s2), Not(s1), Not(s0)), And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0))

# MemtoReg: Estado 1 (001) e OpCode 100011 (LW)
memtoreg_expr = And(Not(s2), Not(s1), s0, op5, Not(op4), Not(op3), Not(op2), op1, op0)

# RegWrite: Estado 4 (100) para R-Type, LW e SW (conforme a lógica da imagem)
regwrite_expr = And(s2, Not(s1), Not(s0), Or(And(Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0)), And(Not(op5), Not(op4), Not(op3), op2, op1, op0), And(Not(op5), Not(op4), op3, Not(op2), Not(op1), Not(op0))))

# ALUSrc: Estado 2 (010) e (LW OU SW)
alusrc_expr = And(Not(s2), s1, Not(s0), Or(And(op5, Not(op4), Not(op3), Not(op2), op1, op0), And(op5, Not(op4), op3, Not(op2), op1, op0)))

sinais = {
    "Jump": jump_expr,
    "ALUOp0": aluop0_expr,
    "Branch": branch_expr,
    "MemWrite": memwrite_expr,
    "MemRead": memread_expr,
    "RegWrite": regwrite_expr,
    "ALUSrc": alusrc_expr
}

opcodes_teste = {
    "R-Type (000000)": (False, False, False, False, False, False),
    "Jump   (000010)": (False, False, False, False, True, False),
    "BEQ    (000100)": (False, False, False, True, False, False),
    "LW     (100011)": (True, False, False, False, True, True),
    "SW     (101011)": (True, False, True, False, True, True)
}

print(f"{'Estado':<8} | {'Instrução (OpCode)':<20} | {'Sinal Ativo':<12} | {'Z3 Status'}")
print("-" * 65)

# Testando nos estados principais S0, S1, S2 e S4
for v_s2, v_s1, v_s0 in [(False,False,False), (False,False,True), (False,True,False), (True,False,False)]:
    for nome_inst, v_ops in opcodes_teste.items():
        v_op5, v_op4, v_op3, v_op2, v_op1, v_op0 = v_ops
        
        for nome_sinal, expr in sinais.items():
            s = Solver()
            s.add(expr)
            # Adiciona as restrições do cenário atual
            s.add(s2 == v_s2, s1 == v_s1, s0 == v_s0)
            s.add(op5 == v_op5, op4 == v_op4, op3 == v_op3, op2 == v_op2, op1 == v_op1, op0 == v_op0)
            
            if s.check() == sat:
                est_str = f"S{int(v_s2)*4 + int(v_s1)*2 + int(v_s0)}"
                print(f"{est_str:<8} | {nome_inst:<20} | {nome_sinal:<12} | SAT (Ativo)")