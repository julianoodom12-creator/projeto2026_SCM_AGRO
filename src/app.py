"""AgroGestor — ponto de entrada da aplicação.

Lista os talhões cadastrados e apresenta os indicadores de produtividade.
"""

from __future__ import annotations

TALHOES: list[dict] = [
    {"id": 1, "nome": "Talhão Norte", "area_ha": 12.5, "producao_kg": 87500.0},
    {"id": 2, "nome": "Talhão Sul", "area_ha": 8.0, "producao_kg": 52800.0},
    {"id": 3, "nome": "Talhão Leste", "area_ha": 15.2, "producao_kg": 95000.0},
]


def listar_talhoes() -> None:
    """Imprime a relação de talhões com a respectiva área."""
    print("AgroGestor — talhões cadastrados")
    print("-" * 44)
    print(f"{'ID':>3}  {'Talhão':<16}{'Área (ha)':>10}")
    for talhao in TALHOES:
        print(f"{talhao['id']:>3}  {talhao['nome']:<16}{talhao['area_ha']:>10.1f}")
    print("-" * 44)
    print(f"Total de área: {sum(t['area_ha'] for t in TALHOES):.1f} ha")


def main() -> None:
    listar_talhoes()


if __name__ == "__main__":
    main()
