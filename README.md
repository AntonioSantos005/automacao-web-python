
# Estrutura de Automação de Testes com Behave e Selenium (Python)

Este projeto implementa uma estrutura básica de automação de testes em Python utilizando **Behave** (Cucumber para Python) com **Selenium WebDriver**, seguindo o padrão Page Object Model.

## 🧪 Funcionalidades Automatizadas

- Teste de login em sistema fictício
- Interações com o site do Google

## 🔧 Tecnologias Utilizadas

- Python 3.9+
- Behave (BDD com Gherkin)
- Selenium WebDriver
- Page Object Model (POM)

## 📁 Estrutura do Projeto

```
.
├── features/             # Arquivos .feature com os cenários
├── steps/                # Implementações dos passos em Python
├── pages/                # Page Objects
├── browser.py            # Setup do navegador
├── environment.py        # Hooks do Behave
├── requirements.txt      # Dependências do projeto
```

## 🚀 Como Executar os Testes

1. Clone o repositório:

```bash
git clone https://github.com/AntonioSantos005/automacao-web-python.git
cd automacao-web-python
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os testes:

```bash
behave
```

## 📝 Observações

- Projeto desenvolvido em 2020 para uma demonstração de selenium webdriver com python
- O projeto é modularizado e segue boas práticas de automação com BDD.
- Para executar testes com interface gráfica, é necessário ter um driver de navegador (ex: chromedriver) no PATH.

## 👤 Autor

Antônio de Sousa – [LinkedIn](https://www.linkedin.com/in/antoniosousas/)
