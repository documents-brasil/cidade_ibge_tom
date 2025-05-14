from typing import Dict, Tuple, Optional
from .cidade import cidade


# Índices para busca mais rápida
_indice_ibge: Dict[str, Tuple[str, str, str]] = {}
_indice_tom: Dict[str, Tuple[str, str, str]] = {}


def _inicializar_indices() -> None:
    """
    Inicializa os índices para busca mais eficiente.
    Esta função é chamada apenas uma vez quando o módulo é importado.
    """
    for (codigo_ibge, codigo_tom), nome_cidade in cidade.items():
        _indice_ibge[codigo_ibge] = (codigo_ibge, codigo_tom, nome_cidade)
        _indice_tom[codigo_tom] = (codigo_ibge, codigo_tom, nome_cidade)


def info_cidade(codigo: str = "") -> Dict[str, str]:
    """
    Busca informações da cidade por código IBGE ou TOM.

    Args:
        codigo: Código IBGE (7 dígitos) ou código TOM (4 dígitos)

    Returns:
        Dicionário com as informações da cidade ou dicionário vazio se não encontrado
    """
    if not codigo:
        return {}
        
    if not _indice_ibge:  # Verifica se os índices já foram inicializados
        _inicializar_indices()

    # Primeiro tenta buscar pelo código IBGE
    resultado = _indice_ibge.get(codigo)

    # Se não encontrou, tenta pelo código TOM
    if not resultado:
        resultado = _indice_tom.get(codigo)

    # Se encontrou algum resultado, retorna como dicionário
    if resultado:
        codigo_ibge, codigo_tom, nome_cidade = resultado
        return {
            'ibge': codigo_ibge,
            'tom': codigo_tom,
            'nome': nome_cidade
        }

    return {}


# Inicializa os índices na importação do módulo
_inicializar_indices() 