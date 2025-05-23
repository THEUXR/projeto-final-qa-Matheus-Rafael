# projeto-final-qa-Matheus-Rafael

📄 Estrutura do README.md (Obrigatória)
1. Apresentação
Nome completo


Curso e semestre


Um parágrafo com uma breve descrição da sua experiência com a disciplina


2. O que é Quality Assurance (QA)?
Explique com suas palavras o conceito de QA e sua importância no desenvolvimento de software


Use uma linguagem simples e acessível, como se estivesse explicando para alguém leigo


3. Conceitos Aprendidos Durante o Semestre
Escreva um parágrafo explicando o que você aprendeu sobre:
Qualidade em software e cultura de qualidade


Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório)


Planejamento de testes (critérios de aceitação, planos e casos de teste)


Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.)


Automação de testes e integração com CI/CD


Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade)


4. Ferramentas e Sites Utilizados
Liste todos os sites e ferramentas que você usou durante o curso, por exemplo:
https://reqres.in/


https://colab.research.google.com/ 


https://github.com/


https://uptimerobot.com/


(outros que desejar incluir)


5. Explicação dos Testes Entregues
Para cada um dos três testes obrigatórios entregues na pasta /testes, responda:
Nome do teste


Objetivo


Qual biblioteca Python foi utilizada


Qual resultado esperado


Link para o arquivo (ex: testes/teste_01.py)


Exemplo de formatação:

✅ Teste 01 – Verificação de status da API ReqRes
Biblioteca: Requests


Objetivo: Verificar se o endpoint retorna status HTTP 200


Resultado esperado: Teste passa com sucesso se o status for 200


Arquivo: testes/teste_01.py



6. Conclusão Final
Escreva um parágrafo com sua reflexão pessoal, respondendo:
O que você aprendeu de mais importante?


Como você enxerga a área de QA no seu futuro profissional?


Qual ferramenta ou tema mais chamou sua atenção e por quê?


TESTE 01 TESTE DE REGRESSÃO

Objetivo	Garantir que a função formatar_preco mantenha seu comportamento histórico, mesmo após futuras modificações no código.
Biblioteca	Python padrão (sem bibliotecas externas).
Resultado Esperado	Todos os casos de teste devem passar, mostrando a mensagem: ✅ Regressão: Nenhuma mudança inesperada detectada
O resultado saiu como o esperado e sem nenhum erro.

TESTE 02 TESTDE DE INTEGRASSÃO

Objetivo	Verificar se os módulos de estoque e vendas trabalham corretamente juntos, atualizando o estoque conforme as vendas são processadas.
Biblioteca	Python padrão (sem bibliotecas externas).
Resultado Esperado	O estoque deve ser atualizado corretamente (lápis: 98, caneta: 49), e a mensagem ✅ Integração: Fluxo de venda funcionando
O resultado saiu como o esperado e sem nenhum erro.

TESTE 03 TESDE UNITARIO

Objetivo	Validar a função calcular_desconto de forma isolada, garantindo que:
• Calcula descontos corretamente
• Rejeita porcentagens inválidas (ex: 110%).
Biblioteca	unittest (biblioteca padrão do Python).
Resultado Esperado	Saída no console mostrando que os 3 testes passaram (OK).
O resultado saiu como o esperado e sem nenhum erro.
