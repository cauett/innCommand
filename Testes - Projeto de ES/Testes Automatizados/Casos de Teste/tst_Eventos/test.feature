Feature: Rolagem na página de eventos

  Como um usuário do sistema,
  Quero acessar a página local e rolar pela seção de eventos,
  Para visualizar o conteúdo completo da página.

  Scenario: Rolar a página de eventos até o fim

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da seção de eventos é visível
    When eu clico na seção de eventos
      And eu pressiono a tecla Down por '2' segundos
    Then a página deve rolar até o final
      And o conteúdo da página deve estar visível
