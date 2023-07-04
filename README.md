# WhatSapp - Python


# Configuração
Clone o repositório:

bash
Copy code
git clone https://github.com/Maycon355/WPP-PY.git
Baixe o ChromeDriver adequado para a versão do seu navegador Chrome e coloque-o no diretório driver do repositório clonado.

# Instale os pacotes Python necessários:

Copy code
pip install -r requirements.txt
Uso
Abra o script em Python aula.py no seu editor de texto preferido.

Personalize o script modificando os seguintes parâmetros:

Mensagem1: O parâmetro de URL usado para compor a mensagem do WhatsApp.
Mensagem3: A mensagem de texto a ser enviada juntamente com a imagem.
Numeros: Uma lista de números de telefone para enviar as mensagens.
Execute o script:

# Copy code
python aula.py
O script automatizará o processo de login no WhatsApp Web, selecionará cada contato da lista Numeros, anexará o arquivo de imagem, digitará a mensagem de texto e a enviará.

Observe que o script pode levar algum tempo para ser executado, dependendo do número de contatos e da velocidade da sua conexão com a internet.

# Observações Importantes
Certifique-se de ter uma conexão com a internet estável antes de executar o script.
O script utiliza o Selenium e o ChromeDriver para automatizar as interações na web. Portanto, é necessário ter o navegador Chrome instalado em sua máquina.
O script envia mensagens e imagens para vários contatos. Use-o de forma responsável e em conformidade com os termos de serviço do WhatsApp.
Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

# Reconhecimentos
Selenium - Ferramenta de automação web
Python - Linguagem de programação
Sinta-se à vontade para contribuir para este projeto abrindo problemas (issues) ou enviando solicitações de recebimento (pull requests).

# Pontos Positivos
Automatiza o processo de envio de mensagens e imagens no WhatsApp.
Permite personalizar a mensagem e os contatos a serem enviados.
Utiliza o Selenium, uma ferramenta de automação web amplamente usada e confiável.
Pode ser adaptado para outros casos de uso de automação web.
Permite o envio de mensagens em massa, economizando tempo e esforço.
O código é modular e fácil de entender.
Suporta o envio de imagens juntamente com as mensagens de texto.
Possui uma licença de código aberto (MIT License), permitindo o uso e a modificação livremente.
Tudo isso pensando na usabilidade e gravando o cache do navegador.
