Feature: Rolagem na página do restaurante

  Como um usuário do sistema,
  Quero acessar a página local e rolar pela seção de restaurante,
  Para visualizar o conteúdo completo da página.

  Scenario: Rolar a página do restaurante até o fim

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da seção de restaurante é visível
    When eu clico na seção de restaurante
      And eu pressiono a tecla Down por '2' segundos
    Then a página deve rolar até o final
      And o conteúdo da página deve estar visível
