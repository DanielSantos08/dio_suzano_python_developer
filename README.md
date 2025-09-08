# 🐍 Suzano Python Developer - DIO Bootcamp

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![DIO](https://img.shields.io/badge/DIO-Bootcamp-orange.svg)](https://www.dio.me/bootcamp/suzano-python-developer)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)]()

## 📋 Sobre o Projeto

Este repositório contém os projetos desenvolvidos durante o **Bootcamp Suzano Python Developer** da [Digital Innovation One (DIO)](https://www.dio.me/). Atualmente estou na primeira etapa do bootcamp, focando nos fundamentos da linguagem Python e desenvolvimento do primeiro projeto prático.

## 🎯 Objetivo Atual

Desenvolver um **Sistema Bancário** completo em Python que implementa as operações básicas de:
- 💰 **Depósito**: Valores positivos com validação
- 💸 **Saque**: Limite de 3 saques diários, máximo R$ 500,00 por operação
- 📊 **Extrato**: Histórico completo de transações com formatação R$ xxx.xx

## 🏢 Sobre a Suzano

A Suzano é a maior produtora mundial de celulose e uma das principais fabricantes de papel da América Latina. Com mais de 100 anos de história, a empresa é referência em sustentabilidade e inovação, desenvolvendo soluções sustentáveis a partir de matérias-primas renováveis.

## 📚 Módulo Atual: Sintaxe Básica com Python

### ✅ Conteúdos Estudados
- Tipos de operadores em Python
- Estruturas condicionais e de repetição
- Manipulação de strings
- Funções em Python
- Tratamento de erros e validações

### 🎯 Projeto Implementado: Sistema Bancário V1

**Funcionalidades:**
- ✅ Menu interativo com opções claras
- ✅ Operação de depósito com validação de valores positivos
- ✅ Operação de saque com múltiplas validações:
  - Limite de 3 saques por dia
  - Valor máximo de R$ 500,00 por saque
  - Verificação de saldo suficiente
- ✅ Extrato detalhado com formatação monetária
- ✅ Tratamento de erros para entradas inválidas
- ✅ Mensagens informativas para o usuário

## 📁 Estrutura Atual do Repositório

```
dio_suzano_python_developer/
├── v1_sistema_bancario/          # Sistema bancário versão 1
│   └── desafio.py               # Implementação principal
├── desafio_data_e_hora/          # Desafio: Data e Hora
│   └── desafio_v1.py            # Sistema bancário POO com data/hora
├── otimizando_sistema_bancario/  # Sistema bancário otimizado
│   └── desafio.py               # Sistema modularizado com funções
└── README.md                    # Este arquivo
```

## 🚀 Como Executar o Sistema Bancário

### Pré-requisitos
- Python 3.10 ou superior instalado
- Terminal ou prompt de comando

### Executando o Sistema
```bash
# Clone o repositório
git clone https://github.com/DanielSantos08/dio_suzano_python_developer.git

# Navegue até o diretório do projeto
cd dio_suzano_python_developer/v1_sistema_bancario

# Execute o sistema bancário
python3 desafio.py
```

### Exemplo de Uso
```
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> d
Informe o valor do depósito: R$ 1500.45

=== Depósito realizado com sucesso! ===
Valor depositado: R$ 1500.45
Saldo atual: R$ 1500.45
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**: Linguagem principal
- **Estruturas de controle**: if/else, while, for
- **Funções**: Modularização do código
- **Tratamento de exceções**: try/except para validações
- **Formatação de strings**: f-strings para saída formatada

## 🎯 Desafios Implementados

### 📅 Desafio: Data e Hora
**Localização**: `desafio_data_e_hora/desafio_v1.py`

**Funcionalidades Implementadas:**
- ✅ **Limite de 10 transações diárias** por conta
- ✅ **Registro de data e hora** em todas as transações
- ✅ **Validação de transações por dia** - impede operações após atingir o limite
- ✅ **Extrato com timestamp** - mostra quando cada transação foi realizada
- ✅ **Sistema orientado a objetos** completo com classes Cliente, Conta, Transação
- ✅ **Controle de saques diários** baseado na data atual

**Principais Melhorias:**
- Controle rigoroso de transações por dia usando `datetime`
- Histórico detalhado com data/hora de cada operação
- Validações que consideram apenas transações do dia atual
- Interface que informa quantas transações restam no dia

**Como usar:**
```bash
cd desafio_data_e_hora
python3 desafio_v1.py

# Fluxo necessário:
# 1. [nu] Criar novo usuário
# 2. [nc] Criar nova conta para o usuário
# 3. [d/s] Realizar depósitos/saques
# 4. [e] Visualizar extrato com data/hora
```

**Tecnologias:**
- `datetime` e `date` para manipulação de data/hora
- Programação Orientada a Objetos (POO)
- Decorators para logging de transações

### 🔧 Desafio: Sistema Bancário Otimizado
**Localização**: `otimizando_sistema_bancario/desafio.py`

**Funcionalidades Implementadas:**
- ✅ **Sistema totalmente modularizado** com funções específicas
- ✅ **Função depositar()** - argumentos apenas por posição (`/`)
- ✅ **Função sacar()** - argumentos apenas por nome (`*`)
- ✅ **Função exibir_extrato()** - argumentos mistos (posição + nome)
- ✅ **Gestão de usuários** - cadastro com validação de CPF único
- ✅ **Gestão de contas** - vinculação usuário-conta com agência fixa
- ✅ **Múltiplas contas por usuário** - um usuário pode ter várias contas
- ✅ **Listagem de contas** - visualização organizada de todas as contas

**Principais Melhorias:**
- Código completamente modularizado em funções específicas
- Diferentes tipos de passagem de argumentos (posicional, nomeado, misto)
- Sistema de usuários com dados completos (nome, CPF, endereço, data nascimento)
- Contas numeradas sequencialmente com agência fixa "0001"
- Validações robustas e tratamento de erros aprimorado
- Interface mais completa com novas opções de menu

**Como usar:**
```bash
cd otimizando_sistema_bancario
python3 desafio.py

# Fluxo recomendado:
# 1. [nu] Criar novo usuário (nome, CPF, endereço, data nascimento)
# 2. [nc] Criar nova conta para o usuário (informar CPF)
# 3. [lc] Listar contas cadastradas
# 4. [d/s] Realizar depósitos/saques
# 5. [e] Visualizar extrato
```

## 📞 Contato

- **LinkedIn**: [Daniel Santos](https://www.linkedin.com/in/danielsantos10/)
- **GitHub**: [DanielSantos08](https://github.com/DanielSantos08)
- **Email**: danfergatthi@gmail.com

## 🙏 Agradecimentos

- **[Digital Innovation One (DIO)](https://www.dio.me/)** pela plataforma de ensino
- **[Suzano](https://www.suzano.com.br/)** pela parceria e oportunidade
- **Comunidade DIO** pelo suporte e conhecimento compartilhado

---

⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐

*Desenvolvido com 💚 durante o Bootcamp Suzano Python Developer - DIO 2024*
