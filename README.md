# Verificação Formal de Circuitos Digitais utilizando Lógica Booleana e o Solver Z3

Este repositório contém os materiais desenvolvidos para o projeto final da disciplina de Arquitetura e Organização de Computadores da Universidade Federal de Roraima, ministrada pelo Prof. Herbert Rocha. **“Verificação Formal de Circuitos Digitais utilizando Lógica Booleana e o Solver Z3”**, submetido no formato de artigo acadêmico conforme os padrões da Sociedade Brasileira de Computação (SBC).

O projeto explora a aplicação de técnicas de verificação formal para garantir a correção funcional, identificar redundâncias lógicas e validar simplificações em circuitos digitais, utilizando lógica booleana, manipulação simbólica e prova automática de teoremas.

---

## Resumo

Este trabalho apresenta uma metodologia de verificação formal de circuitos digitais utilizando lógica booleana e o prover de teoremas Z3. Seis circuitos foram analisados: (A) um circuito combinacional, (B) um somador completo de 8 bits, (C) uma unidade de controle por máquina de estados finitos para um processador MIPS multiciclo, (D) uma expressão booleana complexa, (E) uma Unidade Lógica e Aritmética de 8 bits com múltiplas funções, e (F) o fluxo de execução de uma instrução tipo R no MIPS. Cada circuito foi convertido em fórmulas booleanas, que foram então verificadas usando Z3 quanto à correção da saída, redundância de componentes e equivalência lógica. Os resultados demonstram a eficácia da verificação automatizada na identificação de redundâncias e garantia da correção dos circuitos, com aplicações potenciais em projeto e otimização digital.

---

## Introdução

O projeto de sistemas computacionais eficientes exige a eliminação de redundâncias em suas bases lógicas. Neste contexto, este trabalho explora a simplificação estruturada de expressões booleanas utilizando Python, aplicando bibliotecas como SymPy para a manipulação simbólica dos termos e o Z3 para certificar que a lógica original é preservada.

A redução da complexidade lógica possibilita a criação de circuitos digitais mais eficientes, mantendo a fidelidade funcional às especificações originais.

---

## Metodologia

O processo de modelagem, análise, simplificação e verificação segue os mesmos passos para todos os circuitos analisados:

1. O circuito é analisado e convertido em sua fórmula booleana equivalente.
2. A fórmula é modelada em Python utilizando a biblioteca Z3 para simulação e verificação formal.
3. A expressão é submetida à biblioteca SymPy para tentativa de simplificação simbólica.
4. A fórmula simplificada é novamente validada com o Z3 para verificar seu comportamento funcional.
5. As versões original e simplificada são comparadas utilizando Z3 para comprovar formalmente sua equivalência lógica.

---

## Tecnologias Utilizadas

- Python 3  
- Z3 Solver  
- SymPy  

---

## Conclusão

Os resultados indicam que a integração entre verificação formal e manipulação simbólica é eficaz para garantir a correção e a otimização de circuitos digitais. A prova automática de equivalência lógica contribui para aumentar a confiabilidade de transformações aplicadas durante o projeto de sistemas digitais.

## Autores

- Daniel Marchioro.
- Inácio Lopes Da Silva Viana.
- Sarah Caroline Amaral Pereira.
