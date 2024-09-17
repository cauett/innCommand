Feature: Preenchimento do formulário de contato

  Como um usuário do sistema,
  Quero acessar a página local, rolar até o final da página,
  E preencher o formulário de contatos,
  Para enviar meus dados para a empresa.

  Scenario: Preencher e enviar o formulário de contatos

    Given que a página 'http://localhost:3000' está aberta no navegador
      And a imagem da seção de contatos é visível
    When eu clico na seção de contatos
      And eu pressiono a tecla Down por '1.9' segundos
      And eu clico no campo nome
      And eu digito 'Carlos Cauet Ferreira Costa' no campo nome
      And eu clico no campo telefone
      And eu digito '881234567' no campo telefone
      And eu clico no campo email
      And eu digito 'teste.com' no campo email
      And eu clico no campo mensagem
      And eu digito 'incommand é o melhor' no campo mensagem
    Then eu clico no botão de enviar
      And o formulário deve ser enviado com sucesso
