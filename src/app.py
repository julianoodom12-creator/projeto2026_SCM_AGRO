"""AgroGestor — ponto de entrada da aplicação.

Lista os talhões cadastrados e apresenta os indicadores de produtividade.
"""

from __future__ import annotations

from src.safra import produtividade_kg_ha, sacas_por_hectare

TALHOES: list[dict] = [
    {"id": 1, "nome": "Talhão Norte", "area_ha": 12.5, "producao_kg": 87500.0},
    {"id": 2, "nome": "Talhão Sul", "area_ha": 8.0, "producao_kg": 52800.0},
    {"id": 3, "nome": "Talhão Leste", "area_ha": 15.2, "producao_kg": 95000.0},
]


def listar_talhoes() -> None:
    """Imprime a relação de talhões com os indicadores de produtividade."""
    print("AgroGestor — talhões cadastrados")
    print("-" * 68)
    print(f"{'ID':>3}  {'Talhão':<16}{'Área (ha)':>10}{'Prod. (kg/ha)':>16}{'Sacas/ha':>12}")
    print("-" * 68)
    for talhao in TALHOES:
        prod = produtividade_kg_ha(talhao["producao_kg"], talhao["area_ha"])
        sacas = sacas_por_hectare(talhao["producao_kg"], talhao["area_ha"])
        print(
            f"{talhao['id']:>3}  {talhao['nome']:<16}{talhao['area_ha']:>10.1f}"
            f"{prod:>16.2f}{sacas:>12.2f}"
        )
    print("-" * 68)
    print(f"Total de área: {sum(t['area_ha'] for t in TALHOES):.1f} ha")


def main() -> None:
    listar_talhoes()


if __name__ == "__main__":
    main()
