# Programa para Pesquisa de Termos em um Arquivo txt da Bíblia com Leiaute Predefinido 

## Objetivo

- [x] Testar e ajudar a fixar os conhecimentos em python para a manipulação de texto e aperfeiçoar a utilização de uma janela básica para um programa.
- Já havia construído um programa similar com Java, más como passei a utilizar o Python e não mais o Java para o tratamento	de arquivos de texto (csv, txt, json, xml, html) para análise de dados, este problema permite testar diversos dos principais conteúdos necessários.
- [x] Com isso nesse problema proposto deve-se apenas utilizar arquivos no formato texto.
- [ ] Depois de concluído seria bom ter o mesmo problema resolvido levando o texto de Bíblia.txt para um banco de dados no sqlite3 e inclusive permitir que sejam associados a determinados versículos imagens. Más isso não é do problema proposto atualmente.
- [x] O sistema de busca foi pensado de forma a explorar recursos como lista e alguns comandos básicos ou list comprehension. Testar os conhecimentos de como transformar uma arquivo texto em um data frame ou um conjunto de dados que possam ser trabalhados, dá mesma forma que posso precisar quando manipulo relatórios extraídos de diversos sistemas de automação comercial para apresentar relatórios Gerenciais.
- [ ] Em uma versão mais para frente ver a possibilidade de testar algum tipo de script para ordenamento de dados.

## Problema Proposto

__Problema proposto__: Escrever um programa executável em pc que permita fazer a pesquisa de uma palavra ou uma frase (chamada de termo) na Bíblia.
- [x] Cada versículo que contenha o termo deve ser mostrado na tela e deve-se criar um arquivo html com essa mesma saída.
- [x] No versículo mostrado na tela e no arquivo html o termo deve aparecer em cor diferente do restante do texto.
- [x] Fazer a busca de uma palavra inteira exatamente como foi digitada.
- Exemplo: se a palavra for "casa" não deve mostrar: Casa, casar, casal, casamento acasalamento, etc. Então essa busca é de uma palavra inteira distinguindo maiúscula de minúscula.
- [x] Fazer a busca de uma palavra inteira independentemente de como foi digitada.
- Exemplo: se a palavra for "casa" ou "Casa" deve mostrar casa e Casa, más não casar, Casar, casal, casamento, etc. Então essa busca é de uma palavra inteira sem distinguir maiúscula de minúscula.
- [x] Fazer a busca de um termo único como ele foi digitado e mostrando todas as suas ocorrências.
- Exemplo: se o termo for "casa" deve mostrar casa, casar, casal, casamento, acasalamento, etc.	Então essa busca é de um termo que pode ou não ter como resultado uma palavra inteira distinguindo maiúscula de minúscula.
- [x] Fazer a busca de um termo único independentemente de como ele foi digitado e mostrando todas as suas ocorrências.
- Exemplo: se o termo for "casa" ou "Casa" deve mostrar Casa, casa, casar, Casar, casal, casamento, acasalamento, etc. Então essa busca é de um termo que pode ou não ter como resultado uma palavra inteira sem distinguindo maiúscula de minúscula.
- [x] Fazer a busca por uma frase. E deve ser caracterizado como sendo o termo em que o usuário digitou pelo menos um espaço em branco.
- Exemplo: se o termo for "casa " ou "a casa de Maria" deve mostrar o texto exatamente como digitado distinguindo maiúscula de minúscula. Isso não mostraria "Casa " ou "A casa de Maria".
- [x] Fazer a busca por uma frase. E deve ser caracterizado como sendo o termo em que o usuário digitou pelo menos um espaço em branco.
- Exemplo: se o termo for "casa " ou "a casa de Maria" deve mostrar o texto independentemente de  como digitado, ou seja, sem distinguindo maiúscula de minúscula. Isso mostraria "Casa " ou "A casa de Maria".
- [x] Fazer a busca informando o nome do livro ou o nome do livro e do capítulo ou o nome do livro, do capítulo e do versículo.
- Utilizando a seguinte notação: |NOME DO LIVRO|NÚMERO DO CAPÍTULO|NÚMERO DO VERSÍCULO
- O caractere `|` (__pipe__) é o delimitador padrão.
- Exemplo: Se desejar ver todos os versículos do livro de Mateus deve-se digitar apenas "`|Mateus|`" ou "`|MATEUS|`"
- Se desejar ver todos os versículos do capítulo 1 de Mateus deve-se digitar "`|Mateus|1|`", se digitar "`|Mateus|1`" deve mostrar do livro de Mateus os capítulos 1 e do 10 ao 19, ou seja, todos que iniciam com 1.
- Se desejar ver um versículo específico, por exemplo: Capítulo 18, versículo 20 de Mateus deve-se digitar: `|Mateus|18|20|`

## Funcionalidades que o programa deve ter

- [x] Ter um local para digitar o termo de busca.
- [x] Marcar se será busca por palavra inteira ou não.
- [x] Marcar se a busca distingue ou não maiúscula de minúsculas.
- [ ] Ter um limite de versículos a mostrar. Se informar 0 mostra todos os que forem encontrados se informar 100 mostra os primeiros 100.
- [ ] Ter uma opção para escolher quantos versículos adjacentes serão mostrados com a seguinte regra:
- [ ] Se a pesquisa retornar apenas um versículo mostra os X versículos antes e X depois.
- Se informar 0 só mostra o versículo se informar 5 mostra os 5 antes e os 5 depois

- [x] Quando pressionado o botão de iniciar a busca deve-se mostrar na tela quais as opções de busca foi selecionada.
- [x] Ter uma barra de progresso.
- [x] Se escolher busca por palavra inteira e o termo de busca contiver um espaço em branco ou o caractere | esta opção deve ser desmarcada automaticamente e avisado ao usuário de que a opção foi alterada por que se tiver espaço em branco será uma busca por uma frase  e si tiver o caractere | será uma busca por livro.
- [ ] Se não digitar nada no termo de busca e iniciar a busca deve mostrar uma tela com uma ajuda de como fazer a pesquisa. Para isso deve ler do arquivo Biblia.txt as linhas que iniciarem com ## que são o texto de ajuda.

## Sobre o arquivo texto da Bíblia.txt:

- O arquivo Biblia.txt foi baixado do site: site: [umsocorpo.com.br](www.umsocorpo.com.br), como isso tem muito tempo não lembro por que escolhi este. Esta informação consta na última linha do arquivo.
- Um dos objetivos é substituir integralmente este texto original até que ele fique exatamente igual à versão de João Ferreira de Almeida Edição Revista e Corrigida que tenho aqui em casa (É a Bíblia que Zé Bira utilizou em seus estudos e nela fez várias anotações). Comecei a fazer isso muito, muito lentamente, com paradas longas e retomadas demoradas, é algo que desejo fazer sem nenhuma pressa.
- Do arquivo original baixado fiz várias adaptações para que no próprio arquivo já haja as condições de atender a vários das determinações estabelecidas acima, estas adaptações estão descritas nas primeiras linhas do arquivo.
- Estas primeiras linhas descrevem como inventei um leiaute, por exemplo se a linha começar com # é uma linha de comentário, o programa não vai ler esta linha, se começa com ## é um texto para ser mostrado no botão de ajuda.
	
### Alguns tratamentos feitos no arquivo Biblia.txt foram por exemplo:

- [x] No caso dos parenteses no texto deixei eles sempre com um espaço em branco entre eles e as palavras para facilitar na hora de procurar por uma palavra inteira então por exemplo o trecho:
- "A casa de Maria (filha de Ana)." deixei no texto "A casa de Maria ( filha de Ana ).". Com isso na hora de procurar pela palavra "filha" ou "Ana" não há o que se preocupar com os parenteses. Ficando apenas os sinais de pontuação para serem tratados: '.', ',', ';', ':', '!', '?'. No caso so hifem ele é considerado como parte da palavra.
- [x] No caso dos nomes dos livros da Bíblia que tem mais de uma palavra ou que tem algarismo romanos em seu nome como por exemplo: "LAMENTAÇÕES DE JEREMIAS" no arquivo Bíblia.txt está como LAMENTAÇÕES=DE=JEREMIAS e "I CORÍNTIOS" está I=CORÍNTIOS, etc.

### Leiaute criado dentro do arquivo Bíblia.txt

- [x] As linhas que iniciam com:

- \# É uma linha de comentário o programa não deve ler
- \## é uma linha com texto que deve ser exibido na tela de ajuda do programa. (Não implementado ainda no código). 
- @ São dados sobre a versão da Bíblia e sua tradução
- % Indica onde começa o Antigo e o Novo Testamento
- | É um texto que na versão de João Ferreira de Almeida Edição Revista e Corrigida aparece antes de alguns versículos com informações sobre aquela passagem, por exemplo: Antes do versículo 1 do Capítulo I de Gênesis tem: "A criação do céu e da terra e de tudo o que se contem." Esse texto refere-se aos eventos que vão do versículo 1 até o 23 do capítulo I, e ele sempre aparece imediatamente antes do versículo que inicia o que ele se refere e nele consta até que versículo vai. Com isso a idéia é que sempre uma busca retornar o primeiro versículo deste comentário esta linha seria mostrada. Más, no texto original que baixei não tem isso, isso eu fui digitando depois lendo direto do texto de João Ferreira de Almeida que eu tenho em casa, eu não coloquei em tudo, apenas nos capítulos iniciais da Gênesis.
- espaço em branco:  Quando a linha inicia com um espaço em branco significa que é a identificação do LIVRO E CAPÍTULO.
1.   Para Livros em que haja numeração Romana como em "I SAMUEL" o sinal de = separa o algarismo romano do nome ficando "I=SAMUEL".
2.   Para Livros em que haja nome composto como em "CÂNTICO DOS CÂNTICOS" o sinal de = separa as palavras do nome ficando "CÂNTICO=DOS=CÂNTICOS"
- Quando o primeiro caractere for:
- a) uma Letra é por que é o nome do livro da Bíblia, exemplo: começa com GÊNESIS ou ÊXODO ou DEUTERONÔMIO, etc.
- b) um número indica que é o número do versículo capítulo do livro designado em uma das linhas que a precede.
- A numeração do versículo se reinicia a cada capítulo.

## Como o programa deve proceder:
- [x] Deve ter um botão para importar o arquivo Biblia.txt que deve ser fornecido com o executável para o usuário e à partir dele deve criar o arquivo biblia_versiculo.txt com o seguinte leiaute:
- A|B|C|D|E|F|G|I|J|K|L|M|N|O|P|
- Sendo que na versão deste problema proposto deve considerar somente até a letra G.
- [x] A = Número sequencial de 00001 a 31096 que é a quantidade de versículos que consta no arquivo Bíblia.txt (Sempre 5 caracteres)
- [x] B = A indicação de AT (Antigo Testamento) ou NT (Novo Testamento) (Sempre 2 caracteres)
- [x] C = Nome do Livro totalmente em maiúsculo
- [x] D = Número do Capítulo do Livro
- [x] E = Número do Versículo do Livro
- [x] F = Texto do Versículo em Português
- [ ] G = Texto do Versículo em Inglês. Ainda não tem.
- [ ] H = Texto do Versículo em Esperanto. Ainda não tem.
- [ ] I = Texto do Versículo em Espanhol. Ainda não tem.
- [ ] J = Texto do Versículo em Francês. Ainda não tem.
- [ ] K = Texto do Versículo em Italiano. Ainda não tem.
- [ ] L = Observação 1 sobre o versículo, algum detalhe ou curiosidade sobre o versículo
- [ ] M = Observação 2 sobre o versículo, ou detalhe sobre algo do versículo em relação a personagens, a cidade, o país, o idioma
- [ ] N = Observação 3 sobre o versículo, ou algo importante sobre seu contexto, a tradução ou outras traduções
- [ ] O = Observação 4 sobre o versículo, de O em diante seriam comentários com relação ao Evangelho Segundo o Espiritismo
- [ ] P = Observação 5 sobre o versículo, onde é citado no Evangelho Segundo o Espiritismo e outras obras Espiritas
		
- No caso do G se depois do F só tiver o | sem texto subsequente não deve mostrar, pois no arquivo Bíblia.txt não tem o texto em inglês ainda, a ideia seria depois que tiver uma versão 1.0 pronta vou procurar um texto da Holly Bible em Inglês e atualizar na posição G. Más inicialmente o programa deve prever que se tiver algo digitado em G deve mostrar sempre que solicitado.
- Pode por exemplo ter uma opção para marcar se mostra ou não o idioma inglês, ou se mostra em inglês sempre que a busca retornar apenas um versículo.

## O que ainda esta em fase de desenvolvimento
- [ ] Falta colocar para gravar um arquivo HTML com a lista dos versículos que foram localizados
- [ ] Falta passar a obedecer o filtro de só pesquisar nos livros que foram selecionados
- [ ] Falta colocar a ação de mostrar a ajuda se iniciar a pesquisa sem digitar nenhuma palavra
- [ ] Definir se vai colocar um limite de só pesquisar uma palavra como no mínimo Y letras
- [ ] Ou se vai criar uma lista de palavras como: [ um, uma, seu, sua, etc.] que nunca são pesquisadas.
- [ ] Falta colocar uma opção para informar só mostrar os primeiros X versículos, se informar ZERO mostra tudo.
- [ ] Ivan sugeriu fazer a pesquisa independentemente de ter digitado a palavra com ou sem acento. Essa é legal.
- [ ] Colocar uma opção para caso o resultado da pesquisa retorne apenas uma linha, possa mostrar também, as K linhas anteriores e K posteriores.
- [ ] Falta colocar uma opção para ler do arquivo txt as linhas que descrevem ao que vai se referir os versículos subsequentes.
- Neste caso, ainda falta gravar também estas linhas no arquivo Biblia_versiculo.txt.
- Elas já constam no arquivo Biblia.txt, pelo menos nos na parte inicial de Gênesis.
- [ ] Falta colocar para trazer as observações sobre um versículo se ele for consultado sozinho e colocar para trazer a tradução se houver.
- No arquivo Biblia_versiculo.txt não tem ainda gravando nem observações sobre os versículos nem o versículo em inglês e também a leitura do versículo como é feita atualmente considera que não há nenhum texto depois dele, então se passar a ter observações ou traduções depois dele, com certeza, vai ter que alterar a forma como considera o fim do versículo utilizando como delimitador de campo o caractere | (pipe) .

## Propostas para depois que for liberada a versão 1.0

1.	Tratar o leiaute depois do campo G, prevendo se há ou não texto neles.
2.	Uma versão para banco de dados sqlite3
3.	Uma versão para Web?
4.	Uma versão para smartphone?

## Versão e Alterações

Salvador, Pernambués, 23 de março de 2021 3:17

Última Alteração: 19 de abril de 2021 12:43