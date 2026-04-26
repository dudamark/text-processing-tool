# 📄 Processamento de Texto com Python (Sprint 1)

## 📌 Visão Geral

Este projeto foi desenvolvido como parte da **Sprint 1 — Fundamentos de Python**, com o objetivo de aplicar conceitos essenciais da linguagem na construção de uma ferramenta completa de processamento de texto.

A aplicação é **100% baseada em bibliotecas nativas do Python**, sem dependências externas, e realiza:

- Extração de e-mails com regex
- Validação de IDs de funcionários
- Limpeza e normalização de texto
- Leitura segura de arquivos
- Contagem de frequência de palavras

---

## 📁 Estrutura do Projeto

processamento_texto/  
│  
├── main.py          # Script principal que orquestra o fluxo  
├── utils.py         # Funções de extração, validação e contagem  
├── cleaner.py       # Classe responsável pela limpeza do texto  
├── file_reader.py   # Leitor de arquivos com tratamento de erros  
└── exemplo.txt      # Arquivo de entrada para testes  

---

## ⚙️ Tecnologias Utilizadas

Apenas bibliotecas nativas do Python:

- re → Expressões regulares  
- collections → Contador de palavras  

---

## 🚀 Funcionalidades

### 1. 📧 Extração de E-mails

Função que identifica e retorna e-mails válidos a partir de um texto.

Critérios:
- Deve conter @  
- Deve terminar com: .com, .org, .net ou .br  

Retorno:  
Lista de e-mails válidos encontrados

---

### 2. 🆔 Validação de IDs

Formato esperado:

AAA-1234

Regras:
- AAA → 3 letras maiúsculas  
- 1234 → 4 dígitos  

Retorno:
- Lista de IDs válidos  
- Lista de IDs inválidos  

---

### 3. 🧹 Classe TextCleaner

Responsável pela limpeza do texto.

Atributo:
- original_text

Métodos:
- remove_extra_spaces() → remove espaços duplicados  
- remove_special_characters() → mantém apenas letras, números, espaços, pontos e vírgulas  
- to_lowercase() → converte para minúsculas  

Saída:
Texto limpo e padronizado

---

### 4. 📂 Leitura de Arquivos

Função que lê arquivos .txt com tratamento de erros.

Tratamento:
- Arquivo não encontrado  
- Problemas de encoding  

Retorno:
- Conteúdo do arquivo  
- OU mensagem de erro (sem crash)

---

### 5. 📊 Frequência de Palavras

Conta quantas vezes cada palavra aparece.

Regras:
- Ignora maiúsculas/minúsculas  
- Ignora pontuação  

Retorno:
Dicionário no formato: { palavra: quantidade }

---

## 🔄 Fluxo do Sistema

1. Lê o arquivo exemplo.txt  
2. Limpa o texto  
3. Extrai e-mails  
4. Valida IDs  
5. Conta frequência de palavras  
6. Exibe resultados  

---

## 📝 Exemplo de Entrada

Olá equipe,  
Por favor, entrem em contato com maria.silva@example.com ou com o RH em hr@company.com.br.  
IDs de funcionários pendentes de validação: ABC-1234, AB1-2345, XYZ-9999.  
Obrigado!  

---

## 📤 Saída Esperada

E-mails:
['maria.silva@example.com', 'hr@company.com.br']

IDs:
Válidos → ['ABC-1234', 'XYZ-9999']  
Inválidos → ['AB1-2345']

Texto limpo:
ola equipe por favor entrem em contato com maria.silva@example.com ou com o rh em hr@company.com.br ids de funcionarios pendentes de validacao abc-1234 ab1-2345 xyz-9999 obrigado

Frequência (exemplo):
{ 'ola': 1, 'equipe': 1, 'em': 2 }

---

## ▶️ Como Executar

1. Acesse a pasta:
cd processamento_texto

2. Execute:
python main.py

---

## ✅ Requisitos Atendidos

- Uso de funções  
- Uso de classes  
- Regex  
- Tratamento de erros  
- Manipulação de arquivos  
- Código modular  

---

## 📌 Observações

Projeto focado exclusivamente nos fundamentos de Python, sem uso de bibliotecas externas.
