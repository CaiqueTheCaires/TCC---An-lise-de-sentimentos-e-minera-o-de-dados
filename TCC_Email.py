import win32com.client as win32
import pandas as pd
import sys
# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

Nome = sys.argv[1]
emaile = sys.argv[2]
qtd = sys.argv[3]


# configurar as informações do seu e-mail
email.To = emaile
email.Subject = "Analise de Sentimentos do Twitter - Doge Feel's"
email.HTMLBody = f"""
<td align="right" class="esd-block-image" style="font-size: 0px;"><a target="_blank"><img class="adapt-img" src="https://zcoxrf.stripocdn.email/content/guids/CABINET_de226f0a0c003fcfd4c22796db21b057/images/imagem1.png" alt style="display: block;" width="32"></a></td>
<td align="left" class="esd-block-text">
    <p><strong>
            <font style="vertical-align: inherit;">
                <font style="vertical-align: inherit;">
                    <font style="vertical-align: inherit;">
                        <font style="vertical-align: inherit; color: #ffffff;">
                            <font style="vertical-align: inherit;">
                                <font style="vertical-align: inherit;">Doge Feel's</font>
                            </font>
                        </font>
                    </font>
                </font>
            </font>
        </strong></p>
</td>
<p> Olá {Nome}, a extração dos tweets foi finalizada com sucesso; </p>
<p> Foi extraído um total de {qtd} Tweets. </p>
<p> A análise de sentimentos foi feita em cada um dos tweets, e seus resultados podem ser encontrados abaixo e no arquivo em anexo. </p>
<p> Caso queira uma outra visão, acesse o link abaixo e insira o csv em anexo neste e-mail. </p>
<p><a href="https://gustavo2309-streamlitapp-tela-graficos-jia7ia.streamlitapp.com/" class="esd-frame-element esd-hover-element esdev-disable-select">
        <font style="vertical-align: inherit;">
            <font style="vertical-align: inherit;">Indicadores Análise de sentimentos</font>
        </font>
    </a></p>

"""

anexo = "C://xampp/htdocs/dashboard/Analise_Sentimentos_Base.csv"
email.Attachments.Add(anexo)

print("E-MAIL ENVIADO =)")

email.Send()