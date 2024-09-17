# -*- coding: utf-8 -*-
import time


#####Galeria
@Given("que a página '|any|' está aberta no navegador")
def step_impl(context, url):
    startBrowser(url)

@Given("a imagem da galeria é visível")
def step_impl(context):
    waitForImage("galeria")

@When("eu clico na galeria")
def step_impl(context):
    mouseClick(waitForImage("galeria"))

@When("eu pressiono a tecla Down por '|any|' segundos")
def step_impl(context, duration):
    start_time = time.time()
    while time.time() - start_time < float(duration):
        keyPress("<Down>")
        snooze(0.1)
    keyRelease("<Down>")

@Then("a página deve rolar até o final")
def step_impl(context):
    # Aqui podemos incluir uma validação, como verificar se chegamos ao final da página
    pass

@Then("o conteúdo da página deve estar visível")
def step_impl(context):
    # Incluir verificação de visibilidade de elementos no final da página
    pass


#####Quartos
@Given("a imagem da seção de quartos é visível")
def step_impl(context):
    waitForImage("quartos")

@When("eu clico na seção de quartos")
def step_impl(context):
    mouseClick(waitForImage("quartos"))


#####Lazer
@Given("a imagem da seção de lazer é visível")
def step_impl(context):
    waitForImage("lazer")

@When("eu clico na seção de lazer")
def step_impl(context):
    mouseClick(waitForImage("lazer"))


#####Restaurante
@Given("a imagem da seção de restaurante é visível")
def step_impl(context):
    waitForImage("restaurante")

@When("eu clico na seção de restaurante")
def step_impl(context):
    mouseClick(waitForImage("restaurante"))


#####Eventos
@Given("a imagem da seção de eventos é visível")
def step_impl(context):
    waitForImage("eventos")

@When("eu clico na seção de eventos")
def step_impl(context):
    mouseClick(waitForImage("eventos"))


#####Mapa
@When("eu clico no botão de zoom")
def step_impl(context):
    mouseClick(waitForImage("zoom"))

@Then("o conteúdo da página com zoom deve estar visível")
def step_impl(context):
    # Incluir verificação de visibilidade de elementos no zoom
    pass


#####Contatos
@Given("a imagem da seção de contatos é visível")
def step_impl(context):
    waitForImage("contatos")

@When("eu clico na seção de contatos")
def step_impl(context):
    mouseClick(waitForImage("contatos"))

@When("eu clico no campo nome")
def step_impl(context):
    mouseClick(waitForImage("nome"))

@When("eu digito '|any|' no campo nome")
def step_impl(context, nome):
    for char in nome:
        keyPress(char)

@When("eu clico no campo telefone")
def step_impl(context):
    mouseClick(waitForImage("telefone"))

@When("eu digito '|any|' no campo telefone")
def step_impl(context, telefone):
    for char in telefone:
        keyPress(char)

@When("eu clico no campo email")
def step_impl(context):
    mouseClick(waitForImage("email"))

@When("eu digito '|any|' no campo email")
def step_impl(context, email):
    for char in email:
        keyPress(char)

@When("eu clico no campo mensagem")
def step_impl(context):
    mouseClick(waitForImage("mensagem"))

@When("eu digito '|any|' no campo mensagem")
def step_impl(context, mensagem):
    for char in mensagem:
        keyPress(char)

@Then("eu clico no botão de enviar")
def step_impl(context):
    mouseClick(waitForImage("enviar"))

@Then("o formulário deve ser enviado com sucesso")
def step_impl(context):
    pass


#####Reserva
@When("eu clico no botão de reservar")
def step_impl(context):
    mouseClick(waitForImage("reservar"))

@When("eu preencho a data de check-in com '|any|'")
def step_impl(context, checkin):
    keyPress("<Tab>")
    for char in checkin:
        keyPress(char)

@When("eu preencho a data de check-out com '|any|'")
def step_impl(context, checkout):
    keyPress("<Tab>")
    for char in checkout:
        keyPress(char)

@When("eu seleciono o número de hóspedes")
def step_impl(context):
    keyPress("<Tab>")
    keyPress("<Tab>")
    keyPress("<Return>")

@When("eu seleciono o quarto")
def step_impl(context):
    keyPress("<Tab>")
    keyPress("<Return>")
    keyPress("<Down>")
    keyPress("<Down>")
    keyPress("<Return>")

@When("eu preencho o nome com '|any|'")
def step_impl(context, nome):
    keyPress("<Tab>")
    for char in nome:
        keyPress(char)

@When("eu preencho o email com '|any|'")
def step_impl(context, email):
    keyPress("<Tab>")
    for char in email:
        keyPress(char)

@When("eu preencho o telefone com '|any|'")
def step_impl(context, telefone):
    keyPress("<Tab>")
    for char in telefone:
        keyPress(char)

@Then("eu confirmo a reserva")
def step_impl(context):
    keyPress("<Tab>")
    keyPress("<Return>")

@Then("o formulário de reserva deve ser enviado")
def step_impl(context):
    pass

