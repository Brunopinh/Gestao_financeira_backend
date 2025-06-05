# Gestao_financeira_backend
Esse projeto será um sistema web para controle financeiro e fluxo de caixa feito com python e fast api.

# Estrutura das pasta e organizado
app/
├── api/         # Endpoints (rotas) organizados por versão
├── core/        # Configurações globais (ex: settings, segurança)
├── crud/        # Funções que acessam o banco de dados (Create, Read, Update, Delete)
├── db/          # Sessão com o banco, modelos SQLAlchemy, inicialização
├── service/     # Lógica de negócio (validações, regras do sistema)
├── main.py      # Inicializa a FastAPI

# Exemplo de como será a extrutura
Gestao_financeira_backend/
├── app/
│   ├── api/                  # Rotas organizadas por versão e domínio
│   │   └── v1/
│   │       ├── auth/
│   │       │   ├── login.py
│   │       │   ├── register.py
│   │       └── usuarios.py   # (opcional) endpoints gerais de usuário
│   │       └── financeiro.py # entradas, saídas, contas, etc.
│   │
│   ├── core/                 # Configurações e utilitários principais
│   │   └── config.py         # Variáveis de ambiente, CORS, JWT, etc.
│   │
│   ├── crud/                 # Operações diretas com o banco
│   │   ├── user_crud.py
│   │   └── financeiro_crud.py
│   │
│   ├── db/                   # Banco de dados
│   │   ├── database.py       # Conexão com PostgreSQL
│   │   └── models.py         # (opcional) definindo as tabelas, se quiser usar ORM
│   │
│   ├── schemas/              # Modelos Pydantic para validação
│   │   ├── usuario.py        # UsuarioCreate, UsuarioLogin, UsuarioOut, etc.
│   │   └── financeiro.py     # EntradaCreate, ContaOut, etc.
│   │
│   ├── service/              # Regras de negócio
│   │   ├── usuario_service.py
│   │   └── financeiro_service.py
│   │
│   └── main.py               # Ponto de entrada da aplicação
│
├── .env                      # Variáveis de ambiente
├── requirements.txt
└── README.md
