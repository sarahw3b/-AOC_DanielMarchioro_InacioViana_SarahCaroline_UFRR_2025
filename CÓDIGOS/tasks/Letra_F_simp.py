from z3 import *

RegDst = Bool('RegDst')
ALUSrc = Bool('ALUSrc')
MemtoReg = Bool('MemtoReg')
RegWrite = Bool('RegWrite')
MemRead = Bool('MemRead')
MemWrite = Bool('MemWrite')

# F representa a ativação correta do caminho de dados para Tipo R
fluxo_tipo_R_simp = And(RegDst, Not(ALUSrc), Not(MemtoReg), RegWrite, Not(MemRead), Not(MemWrite))

solver = Solver()
solver.add(fluxo_tipo_R_simp)

if solver.check() == sat:
    print("O fluxo da instrução Tipo R é logicamente possível.")
    print("Exemplo de estado:", solver.model())
else:
    print("O fluxo configurado é impossível (conflito de sinais).")