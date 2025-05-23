# projeto-final-qa-Matheus-Rafael

📄 Estrutura do README.md (Obrigatória)
1. Apresentação
Nome completo: MATHEUS RAFAEL DAMASCENO GOMES


GTI e 5NA


Foi bem dificil no inicio mas comecei a pegar o jeito


2. O que é Quality Assurance (QA)?

é o processo de garantir que um produto ou serviço atenda a padrões de qualidade. No caso de software, por exemplo, envolve testar e revisar para evitar erros antes do lançamento. O objetivo é entregar algo funcional e confiável, prevenindo problemas antes que cheguem ao usuário.



3. Conceitos Aprendidos Durante o Semestre
Escreva um parágrafo explicando o que você aprendeu sobre:
Qualidade em software e cultura de qualidade

Eu entendi que a qualidade em software significa garantir que ela seja confiável, eficiente e livre de falhas. A cultura de qualidade é quando toda a equipe, não só o time de QA, trabalha para prevenir problemas antes que aconteçam. Isso envolve testes contínuos, colaboração e foco na excelência desde o início do desenvolvimento.


Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório)

- Teste Unitário: Verifica se partes pequenas do código funcionam bem sozinhas.
- Teste de Integração: Checa se os módulos do sistema se comunicam corretamente.
- Teste de Sistema: Testa o software completo para garantir que tudo funciona como esperado.
- Teste de Aceitação: Confirma se o sistema atende às necessidades do usuário ou cliente.
- Teste de Regressão: Garante que mudanças no código não criem novos problemas.
- Teste Exploratório: O testador explora o sistema sem roteiro fixo para encontrar possíveis falhas.
Se quiser mais exemplos ou entender melhor como aplicá-los, é só perguntar!


Planejamento de testes (critérios de aceitação, planos e casos de teste)

- Critérios de aceitação: Regras que definem se uma funcionalidade está funcionando corretamente.
- Plano de teste: Documento que organiza como e o que será testado.
- Casos de teste: Cenários práticos para verificar se o sistema funciona como esperado.



Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.)

Eu aprendi a como ver se uma aplicação tem suas funcionalidades sem taxas de erros e com qualidade utilizando Collab, IA para fazer busca por correções de codigos e dicas entre outras ferramentas (eu não lembro do nome da maioria sincerirade)

Automação de testes e integração com CI/CD

- Automação de testes: Usa ferramentas para testar o código automaticamente, tornando o processo mais rápido e preciso.
- CI/CD: Automatiza a integração e entrega do software, garantindo lançamentos rápidos e seguros.

Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade)


- Métricas: Medem a qualidade do software, como taxa de erros e desempenho.
- Rastreamento de bugs: Ferramentas registram e acompanham erros para garantir a correção.
- Observabilidade: Ajuda a entender o comportamento do sistema por meio de logs e métricas.



4. Ferramentas e Sites Utilizados
Liste todos os sites e ferramentas que você usou durante o curso, por exemplo:

https://reqres.in/


https://colab.research.google.com/ 


https://github.com/


https://uptimerobot.com/


https://miro.com/pt/


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

-Foi analizar um codigo ou uma aplicação que tenha qualidade

Como você enxerga a área de QA no seu futuro profissional?

- bom é dificil explicar visto que eu tive um pouco de dificuldade

Qual ferramenta ou tema mais chamou sua atenção e por quê?

- foi uma ferramneta que usamos em ver os erros em um site da nasa lá (não lembro o nome)

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
