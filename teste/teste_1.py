#TESTE DE REGRESSÃO
# Função que formata preços (versão estável)
def formatar_preco(valor):
    """Versão 2.1 - Formata com R$ e 2 decimais"""
    return f"R${float(valor):.2f}".replace('.', ',')

# Teste de regressão (compara com saídas conhecidas)
def test_regressao_precos():
    casos = {
        10: "R$10,00",
        5.5: "R$5,50",
        0.99: "R$0,99"
    }
    
    for entrada, saida_esperada in casos.items():
        assert formatar_preco(entrada) == saida_esperada, f"Falha em {entrada}"
    print("✅ Regressão: Nenhuma mudança inesperada detectada")

test_regressao_precos()
