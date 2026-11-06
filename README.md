# projeto2026_SCM_AGRO

Repositório de artefatos do **AgroGestor**, aplicativo de gestão agrícola para produtores
rurais. Este projeto é usado como estudo de caso da disciplina de **Projeto de Software**
(U4 — A1: Gerenciamento de Configuração).

## Objetivo

Manter um **repositório único e remoto** com a última versão de todos os artefatos do projeto,
permitindo que os membros do time:

- obtenham os artefatos atualizados no computador local (`git clone` / `git pull`);
- isolem o desenvolvimento em *branches* (`feature/*`);
- registrem cada mudança com mensagem rastreável (`git commit`);
- integrem o trabalho ao repositório remoto (`git push`).

## Estrutura

```
projeto2026_SCM_AGRO/
├── docs/
│   └── requisitos.md      # requisitos funcionais do módulo de safra
├── src/
│   ├── __init__.py
│   ├── app.py             # ponto de entrada da aplicação
│   └── safra.py           # cálculos de produtividade
├── tests/
│   └── test_safra.py      # testes automatizados
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar

```bash
git clone https://github.com/<usuario>/projeto2026_SCM_AGRO.git
cd projeto2026_SCM_AGRO
python -m src.app
python -m unittest discover -s tests -v
```

## Fluxo de trabalho adotado

| Etapa | Comando | Finalidade |
|---|---|---|
| Atualizar | `git pull` | Trazer a última versão do remoto |
| Isolar | `git checkout -b feature/nome` | Criar a linha de desenvolvimento |
| Verificar | `git status` | Ver o que mudou |
| Preparar | `git add .` | Colocar as mudanças na *staging area* |
| Registrar | `git commit -m "..."` | Gravar a mudança com mensagem |
| Publicar | `git push` | Enviar para o GitHub |
| Integrar | Pull Request + `git merge` | Revisar e juntar ao ramo principal |

## Equipe

| Integrante | Responsabilidade |
|---|---|
| Juliano Vieira | Gerente de configuração / backend |
| Mariana Alves | Product Owner |
| Ana Souza | Design e documentação |
| Rafael Lima | Backend |
| Carlos Menezes | Frontend |

## Licença

Uso acadêmico.
