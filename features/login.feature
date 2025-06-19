# language: pt

@now
Funcionalidade: login orange hrm

  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar pagina de teste
    Dado que acesso a pagina do Hrm

  Cenario: login com sucesso
    Quando preencher o campo user com "Admin"
    E preencher o campo senha com "admin123"
    E clicar no botao login
    Entao o sistema apresenta o usuario logado "Welcome Paul"