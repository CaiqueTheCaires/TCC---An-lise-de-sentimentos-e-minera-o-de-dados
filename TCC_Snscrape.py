#GITHUB da solução: https://github.com/JustAnotherArchivist/snscrape
#Tutorial de utilização em canal brasileiro: https://www.youtube.com/watch?v=ZxWx0nt3rPE
#Tutorial de utilização em canal estrangeiro: https://www.youtube.com/watch?v=jtIMnmbnOFo

#Importa webscrapping snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

palavraphp = sys.argv[1]
quantidade = int(sys.argv[2])
#de = sys.argv[3]
#ate = sys.argv[4]



def Parametros_Snscrape():

    contador = 0

    #pesquisar tweet por usuario ou palavra
    condicao = 2

    if condicao == 1:
        palavra = '(from:' + input('Digite o nome do usuario para pesquisar:\n ') + ')'
    elif condicao == 2:
        palavra = palavraphp



    #selecionar idioma do tweet ou sem idioma
    condicao = ''
    condicao = 1

    if condicao == 1:
        idioma = 'lang:pt'
        contador = 1
    elif condicao == 2:
        idioma = 'lang:en'
        contador = 1

    #periodo especifico do tweet ou sem periodo
    condicao = 2

    if condicao == 1 and contador == 1:
        dt_inicio = 'since:'+input('(FORMATO YYYY-MM-DD) Digite a data de Inicio:\n ')
        dt_fim = 'until:'+input('(FORMATO YYYY-MM-DD) Digite a data de fim:\n ')
        contador = 2
    elif condicao == 1:
        dt_inicio = 'since:'+input('(FORMATO YYYY-MM-DD) Digite a data de Inicio:\n ')
        dt_fim = 'until:'+input('(FORMATO YYYY-MM-DD) Digite a data de fim:\n ')
        contador = 3

    #pesquisar palavra e idioma
    if contador == 1:
        query = palavra +" " + idioma

    #pesquisar palavra, idioma e data
    elif contador == 2:
        query = palavra +" " + idioma + " " + dt_fim + " " + dt_inicio

    #pesquisar palavra e data
    elif contador == 3:
        query = palavra +" " + dt_fim + " " + dt_inicio

    #pesquisar somente palavra
    else:
        query = palavra

    tweets = []
    limit = quantidade

    #looping do webscrapping para retirar tweets
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.user.displayname, tweet.user.username, tweet.date, tweet.content, tweet.quoteCount,tweet.likeCount,tweet.retweetCount])

    df = pd.DataFrame(tweets, columns=['Usuario', 'TagNick', 'DataPost' , 'Texto', 'Comentarios','Likes','Retweets'])

    df.to_csv("ScrapperTwitterBase.csv", sep=';', encoding='utf-8', index=False)

print("BASE EXTRAÍDA")

Parametros_Snscrape()