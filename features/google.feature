# language: pt

Funcionalidade: realizar pesquisa no Google

  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar pagina de teste
    Dado que acesso a pagina do Google

  Cenario: acessar pagina do Google e realizar pesquisa
    Dado que preencho o campo de pesquisa com Python
    Quando clico no botao de pesquisar
    Entao devo visualizar os resultados