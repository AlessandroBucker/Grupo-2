# 🏗️ ARQUITETURA DO PROJETO

> **Propósito Partners** | Análise Financeira Automatizada com Inteligência Artificial

---

## 📌 Sumário

1. [Nome e Objetivo do Sistema](#1-nome-e-objetivo-do-sistema)
2. [Tecnologias Utilizadas](#2-tecnologias-utilizadas)
3. [Estrutura de Pastas](#3-estrutura-de-pastas)
4. [Organização da Arquitetura](#4-organização-da-arquitetura)
5. [Responsabilidade de Cada Parte](#5-responsabilidade-de-cada-parte)
6. [Perfis de Usuário e Controle de Acesso](#6-perfis-de-usuário-e-controle-de-acesso)
7. [Telas e Rotas da Aplicação](#7-telas-e-rotas-da-aplicação)
8. [Fluxo Principal da Aplicação](#8-fluxo-principal-da-aplicação)
9. [Design System — "Precision Finance"](#9-design-system--precision-finance)
10. [Como Rodar o Projeto](#10-como-rodar-o-projeto)

---

## 1. Nome e Objetivo do Sistema

**Nome:** A definir
**Cliente:** Propósito Partners (escritório de contabilidade e consultoria financeira)  
**Deploy:** https://finanwire-wqtpetfe.manus.space

### Objetivo

É uma plataforma web inteligente que automatiza a extração, análise e geração de relatórios de documentos financeiros empresariais. O sistema recebe arquivos como **DRE (Demonstração de Resultado do Exercício)**, **Balanço Patrimonial** e **Balancete de Verificação**, processa-os via **OCR** e **IA**, calcula indicadores financeiros automaticamente e gera relatórios em PDF — reduzindo o tempo de análise manual de **2 dias** para **poucas horas**. Este projeto tem como objetivo o desenvolvimento de um sistema web inteligente de análise financeira automatizada, capaz de auxiliar empresas na interpretação de dados financeiros a partir de documentos enviados pelos usuários.

A aplicação foi estruturada utilizando uma arquitetura modular, separando as camadas de backend, frontend e banco de dados. Essa organização permite maior escalabilidade, manutenção facilitada e melhor divisão de responsabilidades entre os componentes do sistema.

O sistema irá utilizar tecnologias modernas de desenvolvimento web e bibliotecas de análise de dados para processar informações financeiras, gerar indicadores e produzir relatórios automatizados que auxiliem na tomada de decisão empresarial.

### Problema que resolve

| Antes (manual) | Depois (FinanceIA) |
|---|---|
| Analista lê PDF manualmente | OCR extrai dados automaticamente |
| Cálculo de indicadores em planilha | Cálculo automático com validação |
| Relatórios feitos no Word/Excel | Geração de PDF padronizado |
| Sem controle de versão de docs | Histórico centralizado por empresa |
| Sem alertas de prazo | Notificações automáticas por perfil |

---

## 2. Tecnologias Utilizadas  
O sistema é construído sobre uma base sólida de Python para processamento de dados e uma interface moderna em React.

### Front-end (`/projeto/frontend`)

| Tecnologia | Versão | Finalidade |
|---|---|---|
| **React** | 19 | Framework principal de UI |
| **TypeScript** | 5+ | Tipagem estática |
| **Vite** | 7 | Bundler e servidor de desenvolvimento |
| **Wouter** | 3.7 | Roteamento client-side (leve, sem React Router) |
| **Tailwind CSS** | 4 | Estilização utilitária |
| **shadcn/ui** | latest | Componentes base acessíveis (Radix UI) |
| **Recharts** | latest | Gráficos financeiros |
| **React Hook Form** | latest | Gerenciamento de formulários |
| **Zod** | latest | Validação de schemas |
| **Framer Motion** | latest | Animações de UI |
| **Lucide React** | latest | Biblioteca de ícones |

### Back-end BFF (`/projeto/backend`)

| Tecnologia | Versão | Finalidade |
|---|---|---|
| **Node.js** | ≥ 18 | Runtime do servidor |
| **Express** | 4 | Framework HTTP |
| **TypeScript** | 5+ | Tipagem no servidor |

### Back-end Principal (`/backend` — Django)

| Tecnologia | Finalidade |
|---|---|
| **Python 3** | Linguagem principal |
| **Django** | Framework web |
| **PostgreSQL** | Banco de dados relacional |
| **Tesseract OCR** | Extração de texto de PDFs escaneados |
| **pdfplumber** | Extração de texto de PDFs digitais |
| **ReportLab** | Geração de relatórios em PDF |

### Ferramentas de desenvolvimento

| Ferramenta | Uso |
|---|---|
| **pnpm** | Gerenciador de pacotes (front-end) |
| **Prettier** | Formatação automática de código |
| **Git** | Controle de versão |

---

## 3. Estrutura de Pastas

A estrutura do projeto foi organizada seguindo uma arquitetura modular, com separação clara entre frontend, backend, banco de dados e documentação. 
Separando em cinco elementos principais na raiz do projeto: 

```
analise-finaceira-ia-proposito-partners/
│
├── backend/                          # Back-end Django (Python)
│   ├── apps/
│   │   ├── usuarios/                 # App: gestão de usuários
│   │   │   └── models.py
│   │   ├── empresas/                 # App: gestão de empresas
│   │   │   └── models.py
│   │   ├── documentos/               # App: upload e controle de docs
│   │   │   └── models.py
│   │   ├── analise_financeira/       # App: motor de cálculo de KPIs
│   │   │   └── indicadores.py
│   │   └── relatorios/               # App: geração de PDF
│   │       └── pdf_generator.py
│   └── config/
│       └── settings_example.py       # Exemplo de configuração Django
│
├── database/
│   └── scripts_sql/
│       ├── init.sql                  # Script de inicialização
│       └── script_banco_proposito.sql # Schema completo
│
├── docs/
│   ├── arquitetura.md                # Visão arquitetural original
│   └── wireframes/
│       └── upload_wireframe.txt
│
├── frontend/                         # Protótipo HTML/CSS simples (descontinuado)
│   ├── pages/home.html
│   ├── components/navbar.html
│   └── services/api.js  
│   └── mvc-projeto/                  # ✅ PROJETO PRINCIPAL EM PRODUÇÃO
│
├── ARQUITETURA.md                    # ← Este arquivo
└── README.md                         # README raiz do repositório
```

---

## 4. Organização da Arquitetura

O projeto adota o padrão **MVC (Model-View-Controller)** no front-end React, com uma camada de **Service** para comunicação com a API e **Context API** para estado global.

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONT-END (React)                         │
│                                                                   │
│  ┌──────────┐    dispara     ┌────────────┐    chama    ┌──────┐ │
│  │   VIEW   │ ─────────────▶ │ CONTROLLER │ ──────────▶ │ API  │ │
│  │ (React   │                │ (.ts fns)  │             │ SVC  │ │
│  │  pages/  │ ◀─────────────  │            │ ◀──────────  │      │ │
│  │  components)  renderiza   └─────┬──────┘  retorna   └──────┘ │
│  └──────────┘                      │                             │
│       ▲                            │ lê/escreve                  │
│       │ provê estado               ▼                             │
│  ┌────┴──────────────┐      ┌────────────┐                       │
│  │  CONTEXT API      │      │   MODEL    │                       │
│  │  AuthContext      │      │ (interfaces│                       │
│  │  NotifContext     │      │  TypeScript│                       │
│  │  ThemeContext     │      │  puras)    │                       │
│  └───────────────────┘      └────────────┘                       │
└─────────────────────────────────────────────────────────────────┘
         │ HTTP (fetch)
         ▼
┌─────────────────┐
│  BFF — Node.js  │  (serve SPA + proxy futuro para Django)
│  Express server │
└────────┬────────┘
         │ (integração futura)
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACK-END Django (Python)                       │
│   usuarios │ empresas │ documentos │ analise_financeira │ relatorios │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────┐
│ PostgreSQL  │
└─────────────┘
```

### Camadas e seus papéis

| Camada | Localização | Papel |
|---|---|---|
| **Model** | `client/src/models/` | Define as formas (tipos/interfaces) das entidades. Sem lógica. |
| **Controller** | `client/src/controllers/` | Orquestra a lógica de negócio. Chama Services. Não renderiza nada. |
| **View** | `client/src/views/` | Renderiza a UI. Dispara ações nos Controllers. Sem lógica de negócio. |
| **Service** | `client/src/services/` | Camada de comunicação HTTP. Abstraí fetch/axios. |
| **Context** | `client/src/contexts/` | Estado global compartilhado entre Views via React Context API. |
| **BFF Server** | `server/` | Serve a SPA em produção. Futuro: proxy para Django. |
| **Shared** | `shared/` | Tipos e utilitários usados tanto no client quanto no server. |

---

## 5. Responsabilidade de Cada Parte

### Models (`/client/src/models/`)

São interfaces TypeScript puras — **sem lógica**, apenas contratos de dados.

| Arquivo | Entidade | Atributos principais |
|---|---|---|
| `User.ts` | Usuário do sistema | `id`, `name`, `email`, `role: UserRole`, `empresaId` |
| `Empresa.ts` | Empresa-cliente | `id`, `razaoSocial`, `cnpj`, `status`, `analistaId` |
| `Documento.ts` | Documento financeiro | `id`, `nome`, `tipo`, `status: DocumentoStatus`, `empresaId` |

**Tipos derivados importantes:**
- `UserRole = "ADM" | "ANALISTA" | "CLIENTE"` — controla o acesso por perfil (RF04)
- `DocumentoStatus = "pendente" | "processando" | "processado" | "erro"` — rastreia o OCR

---

### Controllers (`/client/src/controllers/`)

São funções assíncronas puras — **sem JSX**, sem estado React.

| Arquivo | Funções | Requisitos |
|---|---|---|
| `AuthController.ts` | `loginController()`, `logoutController()`, `getSessionController()` | RF01, RF03, RNF01 |
| `DashboardController.ts` | `fetchDashboardData(role)`, `fetchKPIs(role)` | RF04, RF25, RF26 |
| `UploadController.ts` | `uploadDocumento(file, empresaId)`, `fetchDocumentos(empresaId)` | RF12–RF19 |

---

### Views / Pages (`/client/src/views/pages/`)

| Componente | Rota | Funcionalidades implementadas |
|---|---|---|
| `Login.tsx` | `/login` | Formulário login, recuperação de senha (RF03), bloqueio 5 tentativas (RNF01), consentimento LGPD (RF23), modo demonstração 3 perfis (RF04) |
| `Dashboard.tsx` | `/dashboard` | 4 KPIs por perfil, tabela de processos com filtros, alertas, gráfico receita/despesa, gráfico indicadores (RF04, RF10, RF20–RF22, RF25–RF27) |
| `Upload.tsx` | `/upload` | Drag-and-drop, fila OCR assíncrona, revisão de campos com baixa confiança (<75%), confirmação (RF12–RF19) |
| `Cadastro.tsx` | `/cadastro` | Multi-step: empresa (4 passos) e usuário (3 passos), com validação e LGPD (RF01, RF06, RF07, RF11) |
| `Listagem.tsx` | `/empresas`, `/usuarios`, `/relatorios` | Tabela com busca, filtros, paginação, ações inline (RF08–RF10, RF31) |
| `Home.tsx` | `/` | Página de entrada / splash screen |
| `NotFound.tsx` | `*` | Página 404 |

---

### Componentes de Layout (`/client/src/views/components/layout/`)

| Componente | Responsabilidade |
|---|---|
| `AppLayout.tsx` | Wrapper de todas as telas autenticadas: navbar superior, breadcrumbs, área de conteúdo, integração com `NotificationBell` |
| `ErrorBoundary.tsx` | Captura erros de renderização em toda a árvore React, exibindo fallback amigável |

---

### Contexts (`/client/src/contexts/`)

| Contexto | Estado que gerencia | Expõe |
|---|---|---|
| `AuthContext.tsx` | Sessão do usuário logado | `user`, `isAuthenticated`, `loginDemo(perfil)`, `logout()` |
| `NotificationContext.tsx` | Alertas e notificações do sistema | `obterNotificacoesPorPerfil(perfil)` |
| `ThemeContext.tsx` | Tema da interface (claro/escuro) | `theme`, `setTheme()` |

---

### Services (`/client/src/services/`)

| Arquivo | Métodos | Características |
|---|---|---|
| `ApiService.ts` | `get<T>()`, `post<T>()`, `put<T>()`, `delete<T>()` | Base URL via `VITE_API_URL`, headers automáticos, `credentials: include`, tratamento de erros HTTP |

---

### Shared (`/shared/`)

| Arquivo | O que contém |
|---|---|
| `shared/utils/formatters.ts` | `formatCNPJ()`, `formatCurrency()`, `formatDate()` — usadas em client e server |
| `shared/constants/const.ts` | Constantes globais compartilhadas |

---

### Back-end Django (`/backend/`)

| App | Responsabilidade |
|---|---|
| `usuarios/` | CRUD de usuários, autenticação JWT, controle de perfis |
| `empresas/` | CRUD de empresas, vinculação analista-empresa |
| `documentos/` | Upload, armazenamento e rastreamento de status de documentos |
| `analise_financeira/` | Motor de cálculo: liquidez, EBITDA, endividamento, rentabilidade |
| `relatorios/` | Geração de relatórios em PDF com ReportLab |

---

## 6. Perfis de Usuário e Controle de Acesso

O controle de acesso (RF04) é baseado em **perfis**, diferenciando dados e permissões em toda a aplicação.

| Perfil | `UserRole` | Acesso | Empresas |
|---|---|---|---|
| Administrador | `ADM` | Total — gerencia usuários, empresas e configurações | Todas (ex: 34) |
| Analista | `ANALISTA` | Processa documentos, gera relatórios | Atribuídas (ex: 8) |
| Contador/Cliente | `CLIENTE` | Consulta somente-leitura, download de relatórios | Próprias (ex: 3) |

O perfil é armazenado no `AuthContext` e consumido pelas Views para renderizar dados diferenciados. **Não há redirecionamento por perfil ainda** — isso deve ser implementado na integração com o back-end.

---

## 7. Telas e Rotas da Aplicação

Rotas definidas em `App.tsx` usando **wouter**:

| Rota | Componente | Auth? | Observação |
|---|---|---|---|
| `/` | `Home` | Não | Splash screen inicial |
| `/login` | `Login` | Não | Entrada principal com modo demo |
| `/dashboard` | `Dashboard` | Sim | Tela principal — dados por perfil |
| `/cadastro` | `Cadastro` | Sim | Multi-step empresa e usuário |
| `/empresas` | `Listagem` | Sim | Tab padrão: Empresas |
| `/usuarios` | `Listagem` | Sim | Tab padrão: Usuários |
| `/relatorios` | `Listagem` | Sim | Tab padrão: Relatórios |
| `/upload` | `Upload` | Sim | Fluxo OCR completo |
| `/configuracoes` | `Dashboard` | Sim | Placeholder (a implementar) |
| `*` | `NotFound` | — | 404 |

> ⚠️ **Atenção:** As rotas "Auth?" marcadas como Sim **não possuem guard de rota implementado ainda**. O `AuthContext` está pronto, mas o redirecionamento automático para `/login` deve ser adicionado.

---

## 8. Fluxo Principal da Aplicação

```
Usuário acessa /login
      │
      ├─▶ Modo Demo → loginDemo(perfil) → AuthContext
      │
      └─▶ Formulário → AuthController.loginController() → API
                │
                ▼
          AuthContext.user = { id, nome, perfil, empresas }
                │
                ▼
          /dashboard ──▶ DashboardController.fetchDashboardData(role)
                │              └─▶ dados filtrados por perfil
                │
                ├─▶ Clique em empresa ──▶ /upload
                │         │
                │         ▼
                │   UploadController.uploadDocumento()
                │         │
                │         ▼
                │   OCR assíncrono → confiança < 75% → revisão manual
                │         │
                │         ▼
                │   confirmação → status "processado"
                │         │
                │         └─▶ /relatorios (geração de PDF)
                │
                └─▶ /cadastro / /empresas / /usuarios (CRUD)
```

---

## 9. Design System — "Precision Finance"

Estilo **Corporate Minimalism** com acento técnico, inspirado em ferramentas financeiras profissionais.

### Paleta de cores

| Token | Valor hex | Uso |
|---|---|---|
| Azul-Marinho | `#0F1C2E` | Fundo do painel lateral (login) |
| Branco-Gelo | `#F7F9FC` | Fundo principal do conteúdo |
| Azul-Cobalto | `#1A56DB` | Ação primária, links, destaques |
| Verde-Esmeralda | `#059669` | Indicadores positivos, status "Concluído" |
| Vermelho-Coral | `#DC2626` | Erros, alertas críticos |
| Âmbar | `#D97706` | Avisos, pendências, OCR baixa confiança |
| Roxo | `#7C3AED` | Indicadores secundários (EBITDA, relatórios) |

### Tipografia

- **Interface:** IBM Plex Sans (pesos: 400, 500, 600, 700)
- **Valores numéricos/financeiros:** IBM Plex Mono (para KPIs, CNPJs, valores monetários)

### Componentes base

Todos os componentes de UI são do **shadcn/ui** (Radix UI + Tailwind). Para adicionar novos componentes:

```bash
# Na pasta mvc-projeto/
npx shadcn@latest add [nome-do-componente]
```

---

## 10. Como Rodar o Projeto

### Pré-requisitos

- [Visual studio Code](https://code.visualstudio.com/)  
- [pip](https://pypi.org/)  

### Instalação

```bash
# Clone o repositório
git clone https://github.com/propósito-partners/analise-finaceira-ia-propósito-partners.git

# Acesse a pasta do projeto principal
cd analise-finaceira-ia-proposito-partners/projeto/

# Instale as dependências
PyPI install
```

### Desenvolvimento (modo local)

```bash
PyPI dev
```

Acesse em: **http://localhost:3000**

O servidor de desenvolvimento (Vite) inicia o front-end React com HMR (hot reload) e o BFF Node.js em paralelo.

### Build para produção

```bash
PyPI build
PyPI start
```

### Modo Demonstração (sem back-end)

A aplicação funciona completamente **sem back-end** usando o modo demo. Na tela de Login, clique em um dos 3 perfis disponíveis (ADM, ANALISTA ou CONTADOR) para acessar com dados simulados.

---

### 🧪 Testes

Ainda não há cobertura de testes automatizados. A prioridade para a próxima entrega é:

1. **Testes unitários** nos Controllers (funções puras — fáceis de testar)
2. **Testes de integração** nos Services (mock de fetch)
3. **Testes de componente** nas Views principais (Login, Dashboard)


### 👥 Equipe do projeto

| Nome | GitHub |
|---|---|
| Alessandro Werner Bucker | — |
| Gabriel Rodrigo Marques Duglokinski | — |
| Marlon Pires Mendes | — |
| Samara Malta de Faria da Silva | — |
| Tessália Pomocena dos Santos | — |

---

*Última atualização: Março/2026 — Propósito Partners © 2026*
