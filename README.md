# Verificação Formal de Circuitos Digitais usando Z3

## Descrição
Implementação da metodologia de verificação formal de circuitos digitais utilizando lógica booleana e o prover de teoremas Z3.

## Circuitos Analisados
1. **A**: Circuito combinacional
2. **B**: Somador completo de 8 bits
3. **C**: Unidade de controle por máquina de estados finitos para processador MIPS multiciclo
4. **D**: Expressão booleana complexa
5. **E**: Unidade Lógica e Aritmética (ULA) de 8 bits
6. **F**: Fluxo de execução de instrução tipo R no MIPS

## Metodologia
1. Extração da fórmula booleana do circuito
2. Verificação com Z3 para correção da saída
3. Simplificação com SymPy
4. Comparação de equivalência com Z3
5. Análise de redundâncias

## Requisitos
- Python 3.8+
- Z3-solver
- SymPy
- Jupyter (para notebooks)
