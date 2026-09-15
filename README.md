# 🌤️ Weather App

Uma aplicação desktop simples e elegante para consulta de clima em tempo real, construída em Python usando **PyQt5** para a interface gráfica e a API do **OpenWeatherMap**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt-5-green.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)

---

## 📌 Funcionalidades

* 🌡️ **Temperatura em tempo real:** Exibe a temperatura atual em graus Celsius (`°C`).
* 🎨 **Interface Intuitiva:** Layout moderno estilizado com CSS no PyQt5.
* 🌈 **Visual Dinâmico:** Emojis indicativos baseados no código do clima retornado pela API.
* 🔐 **Segurança de Credenciais:** Uso de variáveis de ambiente com `python-dotenv` para proteger a chave de API.
* 🛡️ **Tratamento de Erros:** Mensagens amigáveis para erros de conexão, cidade não encontrada ou chave de API inválida.

---

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/) - Interface Gráfica (GUI)
* [Requests](https://pypi.org/project/requests/) - Requisições HTTP
* [python-dotenv](https://pypi.org/project/python-dotenv/) - Gerenciamento de Variáveis de Ambiente
* [OpenWeatherMap API](https://openweathermap.org/api) - Provedor de Dados Meteorológicos

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Antes de começar, você precisará ter o **Python 3.10+** e o **Git** instalados em sua máquina, além de uma conta gratuita no [OpenWeatherMap](https://openweathermap.org/) para obter sua API Key.

### 1. Clonar o repositório

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

### 2. Criar e ativar um ambiente virtual (Opcional)

#### No Linux/macOS

```
python3 -m venv venv
source venv/bin/activate
```

#### No Windows
```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```
OPENWEATHER_API_KEY=sua_chave_api_aqui
```

### 5. Executar a aplicação

```
python main.py
```

# 📂 Estrutura do Projeto

```
.
├── .env.example          # Modelo de arquivo para variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git (incluindo o .env)
├── main.py               # Ponto de entrada da aplicação
├── requirements.txt      # Dependências necessárias para executar o programa
├── ui.py                 # Interface gráfica construída em PyQt5
├── weather_service.py    # Comunicação com a API e tratamento de exceções
└── README.md             # Documentação do projeto
```

# 📄 Licença
Este projeto está sob a licença MIT.