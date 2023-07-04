from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium import webdriver
import time
# Importar biblioteca SQLite3
import os
import pyautogui

#Parametros importantes

Mensagem1 = f'''send?phone='''
Mensagem3 = '''&text=%F0%9F%93%A2%20%5BMaycon%20Motta%5D%3A%20Domine%20a%20API%20REST%20com%20nosso%20curso%20Advpl!%20Oportunidade%20%C3%BAnica!%20%F0%9F%9A%80%0A%0A%F0%9F%8C%9F%20Potencialize%20suas%20habilidades%20em%20Advpl%20e%20se%20torne%20um%20especialista%20em%20API%20REST!%20%F0%9F%92%AA%0A%0A%F0%9F%93%9A%20Nosso%20curso%20exclusivo%20de%20Advpl%20para%20API%20REST%20%C3%A9%20a%20chave%20para%20abrir%20possibilidades%20incr%C3%ADveis.%20Aprenda%20a%20criar%20e%20gerenciar%20APIs%20REST%20com%20efici%C3%AAncia.%20Desenvolvido%20por%20especialistas%2C%20ele%20elevar%C3%A1%20seu%20conhecimento%20t%C3%A9cnico.%20%F0%9F%93%88%0A%0A%F0%9F%92%A1%20Por%20que%20escolher%20nosso%20curso%3F%0A%0A1%EF%B8%8F%E2%83%A3%20Valoriza%C3%A7%C3%A3o%20profissional%3A%20Desenvolvedores%20Advpl%20experientes%20em%20API%20REST%20est%C3%A3o%20em%20alta!%20Aproveite%20oportunidades%20de%20carreira%20impressionantes%20ao%20dominar%20essa%20tecnologia.%0A%0A2%EF%B8%8F%E2%83%A3%20Conhecimento%20atualizado%3A%20Esteja%20%C3%A0%20frente%20da%20concorr%C3%AAncia%20com%20nosso%20conte%C3%BAdo%20atualizado.%20Esteja%20preparado%20para%20qualquer%20desafio!%0A%0A3%EF%B8%8F%E2%83%A3%20Aprendizado%20pr%C3%A1tico%3A%20Aprenda%20fazendo%20e%20construa%20um%20portf%C3%B3lio%20impressionante.%20Nossa%20metodologia%20interativa%20garantir%C3%A1%20que%20voc%C3%AA%20saiba%20aplicar%20seu%20conhecimento%20em%20projetos%20reais.%0A%0A4%EF%B8%8F%E2%83%A3%20Suporte%20especializado%3A%20Nossa%20equipe%20de%20instrutores%20qualificados%20est%C3%A1%20pronta%20para%20orientar%20voc%C3%AA.%20Aprenda%20com%20os%20melhores%20e%20acelere%20seu%20crescimento%20profissional.%0A%0A%F0%9F%8E%81%20B%C3%B4nus%20exclusivo%3A%20Ao%20se%20inscrever%20agora%2C%20obtenha%20acesso%20a%20materiais%20complementares%2C%20e-books%2C%20v%C3%ADdeos%20tutoriais%20e%20exemplos%20de%20c%C3%B3digo.%0A%0A%F0%9F%94%92%20Vagas%20limitadas!%20Para%20saber%20mais%2C%20envie%20mensagem%20para%20%5Bseu%20n%C3%BAmero%20de%20contato%5D.%20Impulsione%20sua%20carreira%20agora!%0A%0A%F0%9F%8C%9F%20Invista%20no%20seu%20futuro!%20Seja%20um%20especialista%20em%20API%20REST%20com%20nosso%20curso%20de%20Advpl.%20Junte-se%20a%20n%C3%B3s!%20%F0%9F%9A%80%F0%9F%92%BC%0A%0A%5BMaycon%20Motta%5D%0AEspecialista%20em%20Advpl%20e%20API%20REST%0A%0A%F0%9F%93%B2%20Envie%20mensagem%20agora%20para%20saber%20mais!''' 

#https://api.whatsapp.com/send?phone=    5544998465693    &text=ENVIO%20TESTE%20DE%20WPP

def enviamsg():

    dir_path = os.getcwd()
    chromedriver = dir_path + "\\driver\\chromedriver.exe"
    dir_cache = dir_path + "\\cache"
    nome_arquivo = 'WhatsMsg.png'

    try:
        cache = webdriver.ChromeOptions()
        cache.add_argument(r"user-data-dir={}".format(dir_cache))
        #cache.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
        cache.add_argument('--log-level=1')
        cache.add_argument('--disable-gpu') 

        chrome = webdriver.Chrome(chromedriver, options=cache)



        #Função criada para pegar todos os número de wpp do banco
       
        Numeros = [5544998465693, 5544998465693, 5544999791488, 5544998465693, 5544998465693, 5544998465693, 5544998465693, 5544998465693, 5544998465693]

        for Numero in Numeros:


            #numero_whatsapp = Numero[0]  # Acessar o primeiro elemento da tupla (coluna 'wpp')
            chrome.get(f"https://web.whatsapp.com/{Mensagem1}{Numero}{Mensagem3}")
        
            chrome.get(f"https://web.whatsapp.com/{Mensagem1}{Numero}{Mensagem3}")

            while len(chrome.find_elements(By.ID,'side')) < 1:
                time.sleep(1)

            try:

                while len(chrome.find_elements(By.CSS_SELECTOR, "span[data-icon='clip']")) < 1:
                    time.sleep(1)

                chrome.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
                # Seleciona input
                chrome.find_element(By.CLASS_NAME,"_3fV_S").click()
                # Adiciona arquivo
                print(f"Inserindo imagem: {nome_arquivo}")

                time.sleep(1)
                pyautogui.write(nome_arquivo)
                time.sleep(1)
                pyautogui.press('enter')
                
                time.sleep(1)

                chrome.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p').click()
                time.sleep(1)
                chrome.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                print("Enviando imagem...")
                time.sleep(1)
                print("Enviando texto...")
                chrome.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()  


                time.sleep(1)


                pyautogui.press('enter')
                time.sleep(1)
  

            except Exception as e:
                print("Erro ao enviar midia", e)
                                     
    except Exception as e:
        print("Erro ao inicializar", e)


enviamsg()