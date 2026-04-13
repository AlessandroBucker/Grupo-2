-- ==============================================================================
-- SCRIPT DE CRIAÇÃO DO BANCO DE DADOS - PROPÓSITO PARTNERS (POSTGRESQL)
-- Versão: 5.0 (Adoção do Modelo RBAC - Permissões Granulares)
-- Responsável: Gabriel Rodrigo Marques Duglokinski
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. TABELAS BASE (Sem dependências / Sem FKs)
-- ------------------------------------------------------------------------------

-- O "Crachá" do usuário
CREATE TABLE tipo_usuario (
    id_tipo_usuario SERIAL PRIMARY KEY,
    tipo_usuario VARCHAR(50) NOT NULL -- Ex: 'ADMIN', 'USUARIO'
);

-- As "Salas" do sistema
CREATE TABLE modulo (
    id_modulo SERIAL PRIMARY KEY,
    nome_modulo VARCHAR(50) NOT NULL -- Ex: 'EMPRESA', 'DOCUMENTO', 'RELATORIO'
);

-- O que o usuário pode fazer nas salas
CREATE TABLE tipo_permissao (
    id_tipo_permissao SERIAL PRIMARY KEY,
    tipo_permissao VARCHAR(50) NOT NULL -- Ex: 'CONSULTAR', 'ALTERAR', 'EXCLUIR'
);

CREATE TABLE periodo_contabil (
    id_periodo SERIAL PRIMARY KEY,
    mes_referente VARCHAR(20) NOT NULL, -- Ex: '01/2026'
    abertura DATE,
    fechamento DATE,
    status VARCHAR(20) DEFAULT 'Aberto'
);

-- ------------------------------------------------------------------------------
-- 2. TABELAS PRINCIPAIS (Com dependências / Com FKs)
-- ------------------------------------------------------------------------------

CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20), 
    id_tipo_usuario INT NOT NULL, -- FK apontando para tipo_usuario
    cpf VARCHAR(14) UNIQUE, 
    crc VARCHAR(20), 
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_acesso TIMESTAMP,
    CONSTRAINT fk_usuario_tipo FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario)
);

CREATE TABLE empresa (
    id_empresa SERIAL PRIMARY KEY,
    razao_social VARCHAR(200) NOT NULL,
    nome_fantasia VARCHAR(200),
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    representante_legal INT, 
    segmento VARCHAR(100),
    status VARCHAR(20) DEFAULT 'Ativa',
    data_cadastro DATE DEFAULT CURRENT_DATE,
    CONSTRAINT fk_empresa_representante FOREIGN KEY (representante_legal) REFERENCES usuario(id_usuario)
);

-- ------------------------------------------------------------------------------
-- 3. TABELAS ASSOCIATIVAS E DE NEGÓCIO
-- ------------------------------------------------------------------------------

-- Tabela mestre de permissões (Cruzamento RBAC)
CREATE TABLE permissoes (
    id_permissoes SERIAL PRIMARY KEY,
    id_modulo INT NOT NULL,
    id_usuario INT NOT NULL,
    id_tipo_permissao INT NOT NULL,
    CONSTRAINT fk_perm_modulo FOREIGN KEY (id_modulo) REFERENCES modulo(id_modulo),
    CONSTRAINT fk_perm_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_perm_tipo FOREIGN KEY (id_tipo_permissao) REFERENCES tipo_permissao(id_tipo_permissao)
);

CREATE TABLE termo_aceite_lgpd (
    id_termo SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    versao VARCHAR(20) NOT NULL,
    data_aceite TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_usuario VARCHAR(45) NOT NULL,
    status_consentimento BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_termo_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    id_empresa INT NOT NULL,
    cep VARCHAR(10) NOT NULL,
    rua VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    CONSTRAINT fk_endereco_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

CREATE TABLE usuario_empresa (
    id_usuario INT NOT NULL,
    id_empresa INT NOT NULL,
    cargo VARCHAR(100), 
    status_vinculo VARCHAR(20) DEFAULT 'Ativo',
    data_vinculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    validade_permissao TIMESTAMP,
    PRIMARY KEY (id_usuario, id_empresa),
    CONSTRAINT fk_ue_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_ue_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

CREATE TABLE documento (
    id_documento SERIAL PRIMARY KEY,
    id_empresa INT NOT NULL,
    id_periodo INT NOT NULL, 
    tipo VARCHAR(50) NOT NULL, 
    arquivo_path VARCHAR(255) NOT NULL, 
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    status VARCHAR(50) DEFAULT 'Pendente', 
    CONSTRAINT fk_doc_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa),
    CONSTRAINT fk_doc_periodo FOREIGN KEY (id_periodo) REFERENCES periodo_contabil(id_periodo)
);

CREATE TABLE dado_financeiro (
    id_dado SERIAL PRIMARY KEY,
    id_documento INT, -- NULO: Permite inserir na mão sem PDF!
    id_empresa INT NOT NULL, -- FK: Diz de quem é o dado mesmo se não tiver PDF
    id_periodo INT NOT NULL, -- FK: Diz o mês mesmo se não tiver PDF
    id_usuario_validador INT, 
    tipo_dado VARCHAR(50) NOT NULL, 
    categoria VARCHAR(100) NOT NULL, 
    valor_numerico DECIMAL(15, 2), 
    valor_texto VARCHAR(255),      
    score_confianca_ia DECIMAL(5, 2), 
    CONSTRAINT fk_dado_doc FOREIGN KEY (id_documento) REFERENCES documento(id_documento),
    CONSTRAINT fk_dado_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa),
    CONSTRAINT fk_dado_periodo FOREIGN KEY (id_periodo) REFERENCES periodo_contabil(id_periodo),
    CONSTRAINT fk_dado_validador FOREIGN KEY (id_usuario_validador) REFERENCES usuario(id_usuario)
);

CREATE TABLE relatorio (
    id_relatorio SERIAL PRIMARY KEY,
    id_empresa INT NOT NULL,
    link_pdf VARCHAR(255) NOT NULL,
    criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_relatorio_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

CREATE TABLE historico_notificacao (
    id_notificacao SERIAL PRIMARY KEY,
    id_destinatario INT NOT NULL,
    id_empresa INT, 
    tipo_alerta VARCHAR(50) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    recebido BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_notif_usuario FOREIGN KEY (id_destinatario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_notif_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

-- ------------------------------------------------------------------------------
-- TABELA DE AUDITORIA (Registro de Ações Críticas)
-- ------------------------------------------------------------------------------
CREATE TABLE log_auditoria (
    id_log SERIAL PRIMARY KEY,
    id_usuario INT, -- NULO se a ação for do próprio sistema
    acao VARCHAR(50) NOT NULL, -- Ex: 'UPLOAD_DOCUMENTO', 'EXCLUSAO_DADO'
    entidade_afetada VARCHAR(50) NOT NULL, -- Ex: 'DOCUMENTO', 'DADO_FINANCEIRO'
    detalhes TEXT, 
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- ------------------------------------------------------------------------------
-- 4. VIEWS E TRIGGERS 
-- ------------------------------------------------------------------------------

CREATE VIEW vw_resumo_documentos_empresa AS
SELECT 
    e.razao_social, e.cnpj, d.tipo AS tipo_documento, p.mes_referente, d.status
FROM empresa e
JOIN documento d ON e.id_empresa = d.id_empresa
JOIN periodo_contabil p ON d.id_periodo = p.id_periodo;

CREATE OR REPLACE FUNCTION fn_atualiza_data_modificacao()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_atualiza_documento
BEFORE UPDATE ON documento
FOR EACH ROW
EXECUTE FUNCTION fn_atualiza_data_modificacao();
