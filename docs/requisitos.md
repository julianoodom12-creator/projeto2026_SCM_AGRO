# Requisitos — Módulo de Safra

Documento de requisitos do módulo de acompanhamento de safras do **AgroGestor**.
Versão controlada pelo Git: toda alteração neste artefato deve ser registrada em um
*commit* com mensagem descritiva.

## Requisitos funcionais

| Código | Requisito | Prioridade |
|---|---|---|
| RF01 | Cadastrar talhões com nome, área (ha) e cultura plantada. | Alta |
| RF02 | Registrar a produção (kg) de cada talhão por safra. | Alta |
| RF03 | Calcular a produtividade em kg por hectare. | Alta |
| RF04 | Emitir relatório de produtividade por período de safra. | Média |

## Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deve funcionar sem conexão e sincronizar depois. |
| RNF02 | Os cálculos devem ter precisão de duas casas decimais. |
| RNF03 | O código deve manter cobertura de testes automatizados. |

## Regras de negócio

- **RN01** — A área de um talhão deve ser maior que zero.
- **RN02** — A produtividade é calculada por `produção (kg) / área (ha)`.
- **RN03** — Cada registro de produção pertence a uma safra e a um talhão.
- **RN04** — A conversão em sacas considera sacas de 60 kg.

## Histórico de alterações

| Data | Versão | Descrição |
|---|---|---|
| 05/11/2026 | 0.1 | Criação do documento com RF01 a RF03. |
| 06/11/2026 | 0.2 | Inclusão de RF04, RN04 e do módulo `src/safra.py`. |
| 06/11/2026 | 0.3 | Inclusão do manual de uso (`docs/manual-uso.md`). |
