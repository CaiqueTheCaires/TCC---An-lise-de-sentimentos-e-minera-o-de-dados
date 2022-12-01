<?php
set_time_limit(10000); //

	if(($_SERVER['REQUEST_METHOD'] == 'POST') && (isset($_POST['Botao']))) {	
	$item= $_POST['textaao'];
    $email = $_POST['e-mail'];
    $coleta = $_POST['Coleta'];
    $quantidade = $_POST['Quantidade'];
    $de = $_POST['DataDe'];
    $ate = $_POST['DataAte'];
    $run = exec("TCC_Snscrape.py $coleta $quantidade");
    echo $run;
    $blob = exec("TCC_TextBlob_GoogleTrans.py");
    $azure = exec("TCC_Azure.py");
    $flair = exec("TCC_Flair_AnalySenti.py");
    echo $flair;
    $mail = exec("TCC_Email.py $item $email $quantidade");
    header("location: ?");
}

?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel='icon' href='Doge.png' type='image/ico'>
    <title> Feelings Analyzer </title>

    <!-- CSS -->
    <link rel="stylesheet" href="form-1.css">

    <!-- BoxIcons CSS -->
    <link href='https://unpkg.com/boxicons@2.1.2/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="container">
        
        <div class="box">

                </section>

                <p class="topic">1. Primeiro, informe alguns dados que serão necessários para fazer a análise.</p>

                <section class="section-1">
                        <span class="titulo">Dados Pessoais</span>
                        
                        <div class="input">
                            <div class="campo-entrada">
                                <label>Nome Completo</label>
                                <form method='post'> <input type="text" name ="textaao" placeholder="Digite seu nome" required>
                            </div>

                            <div class="campo-entrada">
                                <label>E-mail</label>
                                <form method='post'> <input type="text" name = 'e-mail' placeholder="Digite seu e-mail" required>
                            </div> 

                        </div>
                    
                </section>

                <p class="topic">2. Em seguida, você fornecerá informaçãoes específicas para filtragem de comentários.</p>

                <section class="section-2">
                    <div class="input">
                        <div class="idioma">
                            <span class="titulo">Idioma</span>
                                
                            <label>Selecione o idioma dos comentários:</label>
                            <div class="radio-buttons">
                                    
                                <label class="custom-radio">
                                    <input type="radio" name="radio">
                                    
                                    <div class="radio-btn">
                                        <div class="country-img">
                                            <img src="flag-brasil.svg"/>
                                            <label class="titulo">Português</label>
                                        </div>

                                        <span class="check-icon">
                                            <span class="icon"></span>
                                        </span>
                                    </div>  
                                </label>

                                <label class="custom-radio">
                                    <input type="radio" name="radio">

                                    <div class="radio-btn">                                            
                                        <div class="country-img">
                                            <img src="flag-eua.svg">
                                            <label class="titulo">Inglês</label>
                                        </div>

                                        <span class="check-icon">
                                            <span class="icon"></span>                                                
                                        </span>
                                    </div>  
                                </label>

                            </div>

                        </div>

                        <div class="data">                              
                            <span class="titulo">Data</span>

                            <label>Período dos comentários citados.</label>

                            <div class="periodo">
                                <div class="input-data">
                                    <label>De</label>
                                    <input type="date" required>
                                </div>

                                <div class="input-data">
                                    <label>Até</label>
                                    <input type="date" required>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>  
                
                <p class="topic">3. Por final, nossa ferramenta fará a busca destes comentários através de uma palavra ou pessoa (usuário) específica, logo a baixo na caixa de busca .</p>

                <section class="section-3">
                    <div class="input-busca">
                        <label>Digite uma palavra ou um usuário do Twitter:</label>
                            <div class="campo-entrada">
                                <form method='post'> <input type="text" name= "Coleta" placeholder="Pesquisar" required> <br>

                                <form method='post'> <input type="text" name= "Quantidade" placeholder="Comentarios" required>
                            </div>
                            


                            <button class="button" type='submit' name='Botao'>
                                    Enviar
                            </button>
                            </form>
                    </div>
                </section>
            
        </div>

            
    </div>
        <script src="/Site/JS/main.js"></script>        
</body>
</html>