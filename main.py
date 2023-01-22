from playwright.sync_api import sync_playwright
import json
from datetime import datetime



def guardarPremio(premio):
    with open("premios.json", "r") as json_file:
        premios = json.load(json_file)
    dia = str(datetime.now().strftime("%d-%m")
)
    premios.append({"fecha": dia, "premio": premio})
    with open("premios.json", "w") as json_file:
        json.dump(premios, json_file)
    

with sync_playwright() as p:
    
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.loteriasyapuestas.es/es/resultados/euromillones/comprobar")
    
    #numeros
    page.click('div#qa_comprobador-introduceCombinacion-numero-EMIL-4')
    page.click('div#qa_comprobador-introduceCombinacion-numero-EMIL-17')
    page.click('div#qa_comprobador-introduceCombinacion-numero-EMIL-23')
    page.click('div#qa_comprobador-introduceCombinacion-numero-EMIL-28')
    page.click('div#qa_comprobador-introduceCombinacion-numero-EMIL-37')

    #estrellas
    page.click('div#qa_comprobador-introduceCombinacion-reintegro-EMIL-7')
    page.click('div#qa_comprobador-introduceCombinacion-reintegro-EMIL-11')

    #comprobar 
    page.click('a#qa_comprobador-formulario-botonComprobar-EMIL')
    page.click('button#CybotCookiebotDialogBodyButtonDecline')
    

    #resultado 
    
    dia = str(datetime.now())
    if( page.inner_html("#qa_comprobador-tusAciertos-literalPremiada-EMIL") == "No Premiada" ):
        guardarPremio("No premiada")
        
    else:
        premio = page.inner_text("#qa_comprobador-cantidadPremio-EMIL-1")
        guardarPremio(premio)

    
    

