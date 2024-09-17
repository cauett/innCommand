# -*- coding: utf-8 -*-
import time


def main():
    startBrowser("http://localhost:3000")
    
    
    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 8.5:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    mouseClick(waitForImage("zoom"))
    
    
    mouseClick(waitForImage("galeria"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 2:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")


    mouseClick(waitForImage("quartos"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 5:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    
    mouseClick(waitForImage("lazer"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 2:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    
    mouseClick(waitForImage("restaurante"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 2:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    
    mouseClick(waitForImage("eventos"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 2:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    
    mouseClick(waitForImage("contatos"))
    snooze(0.5)  # Pausa antes do scrolldown para garantir que a página esteja carregada

    # Pressiona a tecla "Down" por 3 segundos para rolar até o fim da página
    start_time = time.time()
    while time.time() - start_time < 1.9:  # Pressiona por 3 segundos
        keyPress("<Down>")
        snooze(0.1)  # Pequena pausa entre as pressões para simular o movimento contínuo
    keyRelease("<Down>")
    
    mouseClick(waitForImage("nome"))
    # Simula a digitação do nome letra por letra
    nome = "Carlos Cauet Ferreira Costa"
    for char in nome:
        keyPress(char)
        
    mouseClick(waitForImage("telefone"))
    telefone = "881234567"
    for char in telefone:
        keyPress(char)
    
    mouseClick(waitForImage("email"))
    email = "teste.com"
    for char in email:
        keyPress(char)
    
    mouseClick(waitForImage("mensagem"))
    mensagem = "incommand é o melhor"
    for char in mensagem:
        keyPress(char)
    
    mouseClick(waitForImage("enviar"))
    
    
    mouseClick(waitForImage("reservar"))
    snooze(0.5)
    
    keyPress("<Tab>")
    checkin = "31122024"
    for char in checkin:
        keyPress(char)
    keyPress("<Tab>")
    checkout = "05012025"
    for char in checkout:
        keyPress(char)
        
    keyPress("<Tab>")
    keyPress("<Tab>")
    keyPress("<Return>")
    keyPress("<Tab>")
    keyPress("<Return>")
    keyPress("<Down>")
    keyPress("<Down>")
    keyPress("<Return>")
    keyPress("<Tab>")
    nome = "Carlos Cauet Ferreira Costa"
    for char in nome:
        keyPress(char)
        
    keyPress("<Tab>")
    email = "teste.com"
    for char in email:
        keyPress(char)
    
    keyPress("<Tab>")
    telefone = "881234567"
    for char in telefone:
        keyPress(char)
    
    keyPress("<Tab>")
    keyPress("<Return>")
