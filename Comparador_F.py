from z3 import *

RegDst = Bool('RegDst')
ALUSrc = Bool('ALUSrc')
MemtoReg = Bool('MemtoReg')
RegWrite = Bool('RegWrite')
MemRead = Bool('MemRead')
MemWrite = Bool('MemWrite')

fluxo_tipo_R = And(RegDst, Not(ALUSrc), Not(MemtoReg), RegWrite, Not(MemRead), Not(MemWrite))
fluxo_tipo_R_simp = And(RegDst, Not(ALUSrc), Not(MemtoReg), RegWrite, Not(MemRead), Not(MemWrite))


solver = Solver()

solver.add(fluxo_tipo_R != fluxo_tipo_R_simp)

if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")