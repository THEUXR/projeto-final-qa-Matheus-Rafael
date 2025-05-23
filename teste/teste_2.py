#TESTE DE INTEGRAÇÃO
# Módulo de estoque
estoque = {"lápis": 100, "caneta": 50}

def vender_item(item, quantidade):
    if estoque[item] >= quantidade:
        estoque[item] -= quantidade
        return True
    return False

# Módulo de vendas
def processar_venda(itens):
    for item, qtd in itens.items():
        if not vender_item(item, qtd):
            raise ValueError(f"Estoque insuficiente: {item}")
    return True

# Teste de integração
def test_venda_completa():
    itens = {"lápis": 2, "caneta": 1}
    processar_venda(itens)
    assert estoque["lápis"] == 98, "Falha no estoque de lápis"
    assert estoque["caneta"] == 49, "Falha no estoque de caneta"
    print("✅ Integração: Fluxo de venda funcionando")

test_venda_completa()
