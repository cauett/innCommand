Feature: Rolagem e interação com o botão de zoom

  Como um usuário do sistema,
  Quero acessar a página local, rolar até o final da página,
  E clicar no botão de zoom,
  Para interagir com o conteúdo da página.

  Scenario: Rolar a página até o fim e clicar no botão de zoom

    Given que a página 'http://localhost:3000' está aberta no navegador
    When eu pressiono a tecla Down por '8.5' segundos
    Then a página deve rolar até o final
    When eu clico no botão de zoom
    Then o conteúdo da página com zoom deve estar visível
