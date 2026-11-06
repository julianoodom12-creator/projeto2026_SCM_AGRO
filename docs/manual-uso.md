# Manual de uso — AgroGestor

Guia rápido para executar o módulo de safra e interpretar os indicadores gerados.

## Pré-requisitos

- Python 3.11 ou superior
- Git (para obter e atualizar os artefatos do repositório)

## 1. Obter os artefatos do repositório remoto

```bash
git clone https://github.com/julianoodom12-creator/projeto2026_SCM_AGRO.git
cd projeto2026_SCM_AGRO
```

## 2. Executar a aplicação

```bash
python -m src.app
```

Saída esperada:

```
AgroGestor — talhões cadastrados
--------------------------------------------------------------------
 ID  Talhão            Área (ha)   Prod. (kg/ha)    Sacas/ha
--------------------------------------------------------------------
  1  Talhão Norte           12.5         7000.00      116.67
  2  Talhão Sul              8.0         6600.00      110.00
  3  Talhão Leste           15.2         6250.00      104.17
--------------------------------------------------------------------
Total de área: 35.7 ha
```

## 3. Executar os testes automatizados

```bash
python -m unittest discover -s tests -v
```

O resultado esperado é `OK`, com 5 testes executados.

## 4. Atualizar o projeto com a última versão

Antes de iniciar qualquer alteração, traga as mudanças do repositório remoto:

```bash
git pull
```

## 5. Enviar uma alteração

```bash
git status                 # verifica o que mudou
git add .                  # prepara os arquivos alterados
git commit -m "descrição"  # registra a alteração
git push                   # publica no GitHub
```

## Indicadores

| Indicador | Fórmula | Unidade |
|---|---|---|
| Produtividade | produção ÷ área | kg/ha |
| Sacas por hectare | produtividade ÷ 60 | sc/ha |
| Custo por hectare | custo total ÷ área | R$/ha |

> Em caso de dúvida sobre as regras de negócio, consulte `docs/requisitos.md`.
