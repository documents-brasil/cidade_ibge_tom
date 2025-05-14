# cidade_ibge_tom
[![PyPI](https://img.shields.io/pypi/v/cidade_ibge_tom)](https://pypi.org/project/cidade_ibge_tom/) ![pyversions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue) ![https://github.com/leogregianin/cidade_ibge_tom/actions](https://github.com/leogregianin/cidade_ibge_tom/workflows/CI/badge.svg?branch=main)


## Cidade IBGE TOM

Biblioteca Python para consulta de informações das cidades brasileiras pelos códigos IBGE ou TOM.

### O que são esses códigos?

* `Código IBGE` é um padrão de código das Cidades brasileiras, que é composto por 7 dígitos, sendo os 2 primeiros o código do Estado.

* `Código TOM` é um padrão de código das Cidades brasileiras utilizado por sistemas, por exemplo, [SIAFI](https://siafi.tesouro.gov.br/) - Sistema Integrado de Administração Financeira do Governo Federal, que é composto por 4 dígitos. A tabela completa dos códigos pode ser obtida [aqui](https://www.tesourotransparente.gov.br/ckan/dataset/lista-de-municipios-do-siafi/resource/eebb3bc6-9eea-4496-8bcf-304f33155282).

[![asciicast](https://asciinema.org/a/519647.svg)](https://asciinema.org/a/519647)

## Instalação

```bash
pip install cidade_ibge_tom
```

Ou com poetry:

```bash
poetry add cidade_ibge_tom
```

## Utilização

### Exemplo básico

```python
from cidade_ibge_tom import info_cidade

# Busca pelo código IBGE
resultado = info_cidade(codigo='5300108')
print(resultado)
# Saída: {'ibge': '5300108', 'tom': '9701', 'nome': 'Brasília-DF'}

# Busca pelo código TOM
resultado = info_cidade(codigo='7107')
print(resultado)
# Saída: {'ibge': '3550308', 'tom': '7107', 'nome': 'São Paulo-SP'}

# Caso o código não seja encontrado
resultado = info_cidade(codigo='9999999')
print(resultado)
# Saída: {}
```

### Exemplos de uso em sistemas

```python
from cidade_ibge_tom import info_cidade

# Verificação se um código existe
codigo_ibge = '5300108'
cidade = info_cidade(codigo=codigo_ibge)
if cidade:
    print(f"Cidade encontrada: {cidade['nome']}")
else:
    print(f"Código {codigo_ibge} não encontrado")

# Extraindo código TOM a partir do IBGE
codigo_ibge = '3550308'
cidade = info_cidade(codigo=codigo_ibge)
codigo_tom = cidade.get('tom')
print(f"O código TOM de São Paulo é: {codigo_tom}")
```

## Desempenho

A biblioteca foi otimizada para busca rápida, usando índices para acessar rapidamente os códigos IBGE e TOM, o que garante uma performance constante O(1) independentemente do tamanho da base de dados.


### Comandos úteis

```bash
# Verificar estilo de código
make lint

# Verificar tipagem estática
make mypy

# Executar testes
make test

# Verificar cobertura de código
make cov
```

## Licença

MIT License
