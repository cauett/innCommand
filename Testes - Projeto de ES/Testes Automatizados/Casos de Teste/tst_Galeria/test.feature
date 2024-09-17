Feature: Rolagem na galeria de imagens

  Como um usuário do sistema,
  Quero acessar a página local e rolar pela galeria de imagens,
  Para visualizar o conteúdo completo da página.

  Scenario: Rolar a página da galeria até o fim

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da galeria é visível
    When eu clico na galeria
      And eu pressiono a tecla Down por '2' segundos
    Then a página deve rolar até o final
      And o conteúdo da página deve estar visível
