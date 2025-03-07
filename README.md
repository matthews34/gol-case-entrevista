# Projeto Técnico - Gol

Este projeto foi desenvolvido como parte do processo seletivo da empresa Gol. O objetivo é demonstrar habilidades técnicas na construção de uma aplicação web utilizando tecnologias modernas e boas práticas de desenvolvimento.

## Arquitetura do Projeto

O projeto segue uma arquitetura simples e modular, permitindo fácil expansão e manutenção. Abaixo estão as principais tecnologias utilizadas:

- **Framework:** Escrito em Python utilizando o framework Flask ([Flask](https://flask.palletsprojects.com/))
- **Banco de Dados:** SQLite ([SQLite](https://www.sqlite.org/index.html))
- **Containerização:** Utiliza Docker para garantir ambiente padronizado ([Docker](https://www.docker.com/))
- **Ambiente de Desenvolvimento:** VSCode com DevContainer para um setup de desenvolvimento mais eficiente ([DevContainers](https://code.visualstudio.com/docs/devcontainers/containers))
- **Gerenciamento de Dependências:** Poetry para facilitar a gestão de pacotes e dependências ([Poetry](https://python-poetry.org/))
- **Deploy:** Realizado na plataforma Railway ([Railway](https://railway.app/))

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/matthews34/gol-case-entrevista.git
   cd gol-case-entrevista
   ```
2. Execute a aplicação.
   1. No VSCode, abra o projeto utilizando a extensão Dev Container e execute a aplicação:
   ```bash
   flask run --debug
   ```
   2. Alternativamente, construa a imagem do container a partir do Dockerfile e execute a imagem
3. A aplicação estará disponível em `http://localhost:5000`.

## Possíveis Melhorias

Para aprimorar o projeto e garantir maior robustez, mantenabilidade e permitir novas funcionalidades, algumas melhorias poderiam ser implementadas:

- **Usar um ORM:** Utilizar um ORM como SQLAlchemy para melhor manipulação do banco de dados.
- **Usar um banco de dados mais robusto:** Trocar o SQLite por PostgreSQL ou MySQL para maior escalabilidade.
- **Testes:** Criar testes unitários e de integração para garantir a qualidade do código.
- **Atualizar o banco periodicamente:** Implementar um mecanismo para atualização periódica do banco de dados conforme atualização dos dados pela ANAC.
- **Pre-commit hooks:** Configurar pre-commit hooks para garantir padronização de estilo e boas práticas no código.
- **CI/CD mais robusto:** Configurar pipelines de CI/CD mais completos que incluam, por exemplo, verificação de pre-commit hooks e execução de testes.
- **Separar front-end e back-end:** Utilizar um framework de front-end como React, Vue ou Angular para maior flexibilidade na interface web.

