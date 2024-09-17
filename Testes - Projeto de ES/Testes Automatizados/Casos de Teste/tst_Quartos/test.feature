Feature: Rolagem na página de quartos

  Como um usuário do sistema,
  Quero acessar a página local e rolar pela seção de quartos,
  Para visualizar o conteúdo completo da página.

  Scenario: Rolar a página de quartos até o fim

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da seção de quartos é visível
    When eu clico na seção de quartos
      And eu pressiono a tecla Down por '5' segundos
    Then a página deve rolar até o final
      And o conteúdo da página deve estar visível
