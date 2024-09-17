Feature: Preenchimento de formulário de reserva

  Como um usuário do sistema,
  Quero acessar a página local e preencher o formulário de reserva,
  Para reservar uma estadia com as informações fornecidas.

  Scenario: Preencher e enviar o formulário de reserva

    Given que a página 'http://localhost:3000' está aberta no navegador
    When eu clico no botão de reservar
      And eu preencho a data de check-in com '31122024'
      And eu preencho a data de check-out com '05012025'
      And eu seleciono o número de hóspedes
      And eu seleciono o quarto
      And eu preencho o nome com 'Carlos Cauet Ferreira Costa'
      And eu preencho o email com 'teste.com'
      And eu preencho o telefone com '881234567'
    Then eu confirmo a reserva
      And o formulário de reserva deve ser enviado
