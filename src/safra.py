"""Cálculos de safra do AgroGestor.

Concentra as regras de negócio de produtividade e de custo por hectare,
conforme o documento de requisitos (RF03, RN01 e RN02).
"""

from __future__ import annotations

KG_POR_SACA = 60.0


def produtividade_kg_ha(producao_kg: float, area_ha: float) -> float:
    """Calcula a produtividade em kg por hectare (RN01 e RN02)."""
    if area_ha <= 0:
        raise ValueError("A área do talhão deve ser maior que zero.")
    return round(producao_kg / area_ha, 2)


def sacas_por_hectare(
    producao_kg: float, area_ha: float, kg_por_saca: float = KG_POR_SACA
) -> float:
    """Converte a produtividade para sacas por hectare."""
    if kg_por_saca <= 0:
        raise ValueError("O peso da saca deve ser maior que zero.")
    return round(produtividade_kg_ha(producao_kg, area_ha) / kg_por_saca, 2)


def custo_por_hectare(custo_total: float, area_ha: float) -> float:
    """Calcula o custo de produção por hectare, em reais."""
    if area_ha <= 0:
        raise ValueError("A área do talhão deve ser maior que zero.")
    return round(custo_total / area_ha, 2)
