Feature: Rolagem na página de lazer

  Como um usuário do sistema,
  Quero acessar a página local e rolar pela seção de lazer,
  Para visualizar o conteúdo completo da página.

  Scenario: Rolar a página de lazer até o fim

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da seção de lazer é visível
    When eu clico na seção de lazer
      And eu pressiono a tecla Down por '2' segundos
    Then a página deve rolar até o final
      And o conteúdo da página deve estar visível
