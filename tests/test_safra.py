"""Testes automatizados do módulo de safra."""

import unittest

from src.safra import custo_por_hectare, produtividade_kg_ha, sacas_por_hectare


class TestProdutividade(unittest.TestCase):
    def test_calcula_media_kg_por_hectare(self):
        self.assertEqual(produtividade_kg_ha(87500, 12.5), 7000.0)

    def test_arredonda_em_duas_casas(self):
        self.assertEqual(produtividade_kg_ha(1000, 3), 333.33)

    def test_area_invalida_levanta_erro(self):
        with self.assertRaises(ValueError):
            produtividade_kg_ha(1000, 0)


class TestSacas(unittest.TestCase):
    def test_converte_para_sacas_de_60kg(self):
        self.assertEqual(sacas_por_hectare(6000, 1), 100.0)


class TestCusto(unittest.TestCase):
    def test_custo_por_hectare(self):
        self.assertEqual(custo_por_hectare(45000, 12.5), 3600.0)


if __name__ == "__main__":
    unittest.main()
