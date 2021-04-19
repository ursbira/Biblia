import os
from typing import Sized
import PySimpleGUI as sg
import Biblia_Tools
# import keyboard

cp = sg.cprint

# Pega o nome da pasta atual
pasta_atual = os.getcwd()
# Variáveis de caminho e usuário
USERNAME = os.environ.get('USERNAME')
VERSION = '1.0_11mar_2021'
TITULO1 = 'Pesquisar na Bíblia (urs.bira) - Selecionar'
TITULO2 = 'Pesquisar na Bíblia (urs.bira) - Pesquisar'
TEXTO_S = 'Pesquisar na Bíblia (urs.bira) - (' + VERSION + ') | Usuário: '
AVISO1 = 'Se digitar espaço na pesquisa não pode ser Pesquisa Palavra' +\
          ' Inteira. Será Pesquisa de FRASE!'
textStatus = str(TEXTO_S) + str(USERNAME)

# Definindo os arquivos de trabalho
biblia_em_txt = 'Biblia.txt'
biblia_versiculo_txt = 'Biblia_versiculo.txt'
biblia_ler = os.path.join(pasta_atual, biblia_em_txt)
biblia_gravar = os.path.join(pasta_atual, biblia_versiculo_txt)

# Variáveis parar tratar o texto
testamento = ''
livro_atual = ''
livro_cap_atual = ''
termo_digitado = ''
palavra_inteira = False
dif_mai_min = False
qtde_livro = 0
qtde_capitulo = 0
qtde_versiculo = 0
conta_linha = 0
total_linha = 0
separador = '|'
pointing = ['!', ',', '.', ':', '?', ';']
tp_pesquisa = 0
# win2_active  = False
# Verifica se o arquivo de pesquisa existe
if os.path.isfile(biblia_versiculo_txt):
    pesquisa_liberada = True
else:
    pesquisa_liberada = False

# Lista de Tuplas com 10 campos com dados sobre os livros da Bíblia
# com o seguinte leiaute: Número, Abreviatura, AT ou NT, Quantidade 
# Versículos, Pentatêuco (True), Evangelhos (True), Coluna ainda não
# usada (False), Outra Coluna ainda não usada (False), Nome do Livro,
# e Código inventado para o livro
livros_lista = [
(1 , '  ', 'AT', 0, True , False, False, False, 'GÊNESIS', '_l01'),
(2 , '  ', 'AT', 0, True , False, False, False, 'ÊXODO', '_l02'),
(3 , '  ', 'AT', 0, True , False, False, False, 'LEVÍTICO', '_l03'),
(4 , '  ', 'AT', 0, True , False, False, False, 'NÚMEROS', '_l04'),
(5 , '  ', 'AT', 0, True , False, False, False, 'DEUTERONÔMIO', '_l05'),
(6 , '  ', 'AT', 0, False, False, False, False, 'JOSUÉ', '_l06'),
(7 , '  ', 'AT', 0, False, False, False, False, 'JUÍZES', '_l07'),
(8 , '  ', 'AT', 0, False, False, False, False, 'RUTE', '_l08'),
(9 , '  ', 'AT', 0, False, False, False, False, 'I SAMUEL', '_l09'),
(10, '  ', 'AT', 0, False, False, False, False, 'II SAMUEL', '_l10'),
(11, '  ', 'AT', 0, False, False, False, False, 'I REIS', '_l11'),
(12, '  ', 'AT', 0, False, False, False, False, 'II REIS', '_l12'),
(13, '  ', 'AT', 0, False, False, False, False, 'I CRÔNICAS', '_l13'),
(14, '  ', 'AT', 0, False, False, False, False, 'II CRÔNICAS', '_l14'),
(15, '  ', 'AT', 0, False, False, False, False, 'ESDRAS', '_l15'),
(16, '  ', 'AT', 0, False, False, False, False, 'NEEMIAS', '_l16'),
(17, '  ', 'AT', 0, False, False, False, False, 'ESTER', '_l17'),
(18, '  ', 'AT', 0, False, False, False, False, 'JÓ', '_l18'),
(19, '  ', 'AT', 0, False, False, False, False, 'SALMOS', '_l19'),
(20, '  ', 'AT', 0, False, False, False, False, 'PROVÉRBIOS', '_l20'),
(21, '  ', 'AT', 0, False, False, False, False, 'ECLESIASTES', '_l21'),
(22, '  ', 'AT', 0, False, False, False, False, 'CÂNTICO DOS CÂNTICOS', '_l22'),
(23, '  ', 'AT', 0, False, False, False, False, 'ISAÍAS', '_l23'),
(24, '  ', 'AT', 0, False, False, False, False, 'JEREMIAS', '_l24'),
(25, '  ', 'AT', 0, False, False, False, False, 'LAMENTAÇÕES DE JEREMIAS', '_l25'),
(26, '  ', 'AT', 0, False, False, False, False, 'EZEQUIEL', '_l26'),
(27, '  ', 'AT', 0, False, False, False, False, 'DANIEL', '_l27'),
(28, '  ', 'AT', 0, False, False, False, False, 'OSÉIAS', '_l28'),
(29, '  ', 'AT', 0, False, False, False, False, 'JOEL', '_l29'),
(30, '  ', 'AT', 0, False, False, False, False, 'AMÓS', '_l30'),
(31, '  ', 'AT', 0, False, False, False, False, 'OBADIAS', '_l31'),
(32, '  ', 'AT', 0, False, False, False, False, 'JONAS', '_l32'),
(33, '  ', 'AT', 0, False, False, False, False, 'MIQUÉIAS', '_l33'),
(34, '  ', 'AT', 0, False, False, False, False, 'NAUM', '_l34'),
(35, '  ', 'AT', 0, False, False, False, False, 'HABACUQUE', '_l35'),
(36, '  ', 'AT', 0, False, False, False, False, 'SOFONIAS', '_l36'),
(37, '  ', 'AT', 0, False, False, False, False, 'AGEU', '_l37'),
(38, '  ', 'AT', 0, False, False, False, False, 'ZACARIAS', '_l38'),
(39, '  ', 'AT', 0, False, False, False, False, 'MALAQUIAS', '_l39'),
(40, '  ', 'NT', 0, False, True , False, False, 'MATEUS', '_l40'),
(41, '  ', 'NT', 0, False, True , False, False, 'MARCOS', '_l41'),
(42, '  ', 'NT', 0, False, True , False, False, 'LUCAS', '_l42'),
(43, '  ', 'NT', 0, False, True , False, False, 'JOÃO', '_l43'),
(44, '  ', 'NT', 0, False, False, False, False, 'ATOS', '_l44'),
(45, '  ', 'NT', 0, False, False, False, False, 'ROMANOS', '_l45'),
(46, '  ', 'NT', 0, False, False, False, False, 'I CORÍNTIOS', '_l46'),
(47, '  ', 'NT', 0, False, False, False, False, 'II CORÍNTIOS', '_l47'),
(48, '  ', 'NT', 0, False, False, False, False, 'GÁLATAS', '_l48'),
(49, '  ', 'NT', 0, False, False, False, False, 'EFÉSIOS', '_l49'),
(50, '  ', 'NT', 0, False, False, False, False, 'FILIPENSES', '_l50'),
(51, '  ', 'NT', 0, False, False, False, False, 'COLOSSENSES', '_l51'),
(52, '  ', 'NT', 0, False, False, False, False, 'I TESSALONICENSES', '_l52'),
(53, '  ', 'NT', 0, False, False, False, False, 'II TESSALONICENSES', '_l53'),
(54, '  ', 'NT', 0, False, False, False, False, 'I TIMÓTEO', '_l54'),
(55, '  ', 'NT', 0, False, False, False, False, 'II TIMÓTEO', '_l55'),
(56, '  ', 'NT', 0, False, False, False, False, 'TITO', '_l56'),
(57, '  ', 'NT', 0, False, False, False, False, 'FILEMOM', '_l57'),
(58, '  ', 'NT', 0, False, False, False, False, 'HEBREUS', '_l58'),
(59, '  ', 'NT', 0, False, False, False, False, 'TIAGO', '_l59'),
(60, '  ', 'NT', 0, False, False, False, False, 'I PEDRO', '_l60'),
(61, '  ', 'NT', 0, False, False, False, False, 'II PEDRO', '_l61'),
(62, '  ', 'NT', 0, False, False, False, False, 'I JOÃO', '_l62'),
(63, '  ', 'NT', 0, False, False, False, False, 'II JOÃO', '_l63'),
(64, '  ', 'NT', 0, False, False, False, False, 'III JOÃO', '_l64'),
(65, '  ', 'NT', 0, False, False, False, False, 'JUDAS', '_l65'),
(66, '  ', 'NT', 0, False, False, False, False, 'APOCALIPSE', '_l66')]

# Definição das dimensões da Janela
WIN_W = 1250
WIN_H = 650
BAR_H = int(WIN_W/10*.7) # Dimensão da barra de progresso
STA_H = int(WIN_W/10*.82) # Dimensão da barra de status
OUT_H1 = int(WIN_W/10*1.3) # Dimensão da janela output 1
OUT_V1 = int(WIN_W/10*.03) # Dimensão da janela output 1
OUT_H2 = int(WIN_W/10*1.3) # Dimensão da janela output 2
OUT_V2 = int(WIN_W/10*.9) # Dimensão da janela output 2

# Definir se mostra ou não o frame que contém os livros a selecionar
frame_selecionar = True
# Definir se mostra ou não os elementos da janela
ocultar_elementos_da_janela = True

def mostrar_ajuda() -> None:
    """ Mostra o texto de ajuda.
    """
    print('Tela de ajuda.')


def mostrar_variaveis() -> None:
    print('Nome Usuário :', USERNAME)
    print('Texto S      :', TEXTO_S)
    print('Texto Status :', textStatus)
    print('Pasta Atual         :', pasta_atual)
    print('Biblia Lida         :', biblia_em_txt)
    print('Biblia Gravada      :', biblia_versiculo_txt)
    print('Local Biblia Lida   :', biblia_ler)
    print('Local Biblia Gravada:', biblia_gravar)
    print('Caractere Separador  :', separador)

def criar_versiculo(linha_o: str) -> str:
    """Monta a linha para ficar com 5 campos separados pelo
       valor da variável separador ficando com uma numeração
       sequencial de versículo, AT ou NT, Nome do Livro,
       número do Capítulo, número do versículo e seu texto

    Args:
        linha_o (str): Linha com o versículo original.

    Returns:
        str: Retorna o Versículo com o formato por exemplo:
             0001|AT|GÊNESIS|1|Texto do versículo|
    """
    global testamento, livro_atual, livro_cap_atual, qtde_livro,\
           qtde_capitulo, qtde_versiculo
    versiculo = ''
    # linha = linha_o.replace('\n', separador + '\n')
    caractere = linha_o[0:1]
    if linha_o.startswith('%ANTIGO TESTAMENTO'):
        testamento = 'AT'
    if linha_o.startswith('%NOVO TESTAMENTO'):
        testamento = 'NT'
    if caractere.isalpha():
        # No leiaute do arquivo Biblia.txt quando a linha começa com
        # uma letra significa que é a linha que contém o nome do Livro.
        # Aqui conta a quantidade de Livros
        qtde_livro += 1
        livro_atual = linha_o.replace('\n', '')
    if caractere.isspace():
        # As linhas que inicial com espaço no arquivo txt original são
        # as que contém o nome do Livro e seu capítulo, então aqui conta
        # a quantidade total de capítulos da Bíblia. 
        qtde_capitulo += 1
        livro_cap_atual = linha_o.replace('\n', separador).replace(' ',
         separador)
        # Nomes de Livros com mais de uma palavra e aqueles que contém
        # algarismo romano em seu nome tem o sinal de = separando os 
        # termos, por isso, agora substitui o = por espaço.
        livro_cap_atual = livro_cap_atual.replace('=', ' ')
    if caractere.isdecimal():
        # As linhas que iniciam com números são as que contêm os
        # versículos propriamente ditos e elas inicial com o número do
        # versículo naquele capítulo separado por um espaço e em 
        # seguida o texto do versículo.
        # Aqui conta o total de versículos da Bíblia.
        qtde_versiculo += 1
        # Pega do início da linha até o primeiro espaço em branco
        num_versiculo = linha_o[:linha_o.index(' ')]
        # Pega do primeiro espaço em branco +1 até o último caractere
        txt_versiculo = linha_o[linha_o.index(' ')+1:-1]
        versiculo = (str(qtde_versiculo).zfill(5) + separador + testamento +\
            livro_cap_atual + str(num_versiculo) + separador + txt_versiculo+\
            separador + '\n')
    return versiculo


def gravar_versiculos() -> None:
    global total_linha, conta_linha
    conta_linha = 0
    total_linha = 0
    # Abrir o arquivo txt da Bíblia para convertê-lo
    with open(biblia_ler, 'r', encoding="utf8") as biblia_lida:
        # Apura a quantidade de linhas do arquivo
        total_linha =  sum(1 for _ in biblia_lida)
        # Retorna o ponteiro para o início do arquivo
        biblia_lida.seek(0)
        window.Element('_progressbar').UpdateBar(0, max = total_linha)
        # Gravar a Bíblia salvando em cada linha somente os versículos
        with open(biblia_gravar, 'w', encoding="utf8", newline='') as biblia_versiculo:
            for linha in biblia_lida:
                conta_linha += 1
                versiculo_criado = criar_versiculo(linha)
                biblia_versiculo.write(versiculo_criado)
                window.Element('_progressbar').UpdateBar(conta_linha)


def ocultar_elementos_janela() -> None:
    global ocultar_elementos_da_janela
    if ocultar_elementos_da_janela:
        ocultar_elementos_da_janela = False
        window.Element('_frame_livros_biblia').Update(visible=False)
        window.Element('_frame_botoes_selecionar').Update(visible=False)
        window.Element('_monitor').Update(visible=True)
    else:
        ocultar_elementos_da_janela = True
        window.Element('_frame_livros_biblia').Update(visible=True)
        window.Element('_frame_botoes_selecionar').Update(visible=True)
        window.Element('_monitor').Update(visible=True)


def marcar_livro(livro: str) -> None:
    window.Element(livro).Update(True, disabled=False,
        visible=True, text_color='red')


def desmarcar_livro(livro: str) -> None:
    window.Element(livro).Update(False, disabled=False,
        visible=True, text_color='gray')


def selecionar_grupo_livros(grupo: str) -> None:
    checar_livros = 0
    contar_livros_selecionados = 0
    for abreviar in livros_lista:
        checar_livros += 1
        if grupo == 'Antigo Testamento':
            if checar_livros < 40:
                contar_livros_selecionados += 1
                marcar_livro(abreviar[9])
            else:
                desmarcar_livro(abreviar[9])
        elif grupo == 'Novo Testamento':
            if checar_livros > 39:
                contar_livros_selecionados += 1
                marcar_livro(abreviar[9])
            else:
                desmarcar_livro(abreviar[9])
        elif grupo == 'Pentateuco':
            if checar_livros < 6:
                contar_livros_selecionados += 1
                marcar_livro(abreviar[9])
            else:
                desmarcar_livro(abreviar[9])
        elif grupo == 'Evangelhos':
            if (checar_livros > 39 and checar_livros < 44):
                contar_livros_selecionados += 1
                marcar_livro(abreviar[9])
            else:
                desmarcar_livro(abreviar[9])
        elif grupo == 'Limpar':
                desmarcar_livro(abreviar[9])
        elif grupo == 'Todos':
                contar_livros_selecionados += 1
                marcar_livro(abreviar[9])
    window.Element('_output').Update('')
    print(str(contar_livros_selecionados),
        'Livros Selecionados [', grupo, ']')

def pesquisar_apos_5pipe(linha: str) -> str:
    """ Separa da linha informada o texto que inicia após o 5º\
        caractere | (pipe) localizado na linha fornecida e retorna a\
        linha contendo apenas o texto que refere-se ao versículo\
        propriamente dito.

    Args:
        linha (str): Linha original para ser tratada

    Returns:
        str: Retorna a Linha somente com o texto do versículo.
    """
    achar = 0
    contar = 0
    linha_pura = linha
    for x in linha:
        contar += 1
        if x == separador:
            achar += 1
        if achar == 5:
            linha_pura = (linha[contar:])
            linha_inicio = (linha[:contar])
            break
    linha_pura = linha_pura.replace('|','')
    return linha_pura, linha_inicio

def atual_status_tp_pesq_janela2() -> None:
    # Atualiza o status dos tipos de pesquisa na janela 2
    if win2_active:
        win2.Element('_tipo_pesquisa').Update(str(tp_pesquisa))

        if palavra_inteira:
            win2.Element('_palavra_inteira_status').Update(
                'Palavra Inteira: Sim')
        else:
            win2.Element('_palavra_inteira_status').Update(
                'Palavra Inteira: Não')

        if dif_mai_min:
            win2.Element('_dif_mai_min_status').Update(
                'Diferencia Maiúscula/Minúscula: Sim')
        else:
            win2.Element('_dif_mai_min_status').Update(
                'Diferencia Maiúscula/Minúscula: Não')


def definir_tipo_pesquisa(t_pesquisa: str, td_mai_min: bool,
    tp_inteira: bool) -> int:
    global tp_pesquisa, separador, palavra_inteira

    # São 7 tipos de pesquisa que formam 5 grupos
    # 1 usa a linha original como lista
    # 2 e 5 usa a linha original como string
    # 3 usa a linha minúscula como lista
    # 4 e 6 usa a linha minúscula como string
    # 7 usa a linha original mostra a linha toda não procura palavra

    if td_mai_min ==True and tp_inteira == True:
        # Ao pesquisar casa não considera casas, casar, casamento
        tipo_pesquisa = 1
    if td_mai_min ==True and tp_inteira == False:
        # Ao pesquisar casa considera casas, casar, casamento
        tipo_pesquisa = 2
    if td_mai_min ==False and tp_inteira == True:
        # Ao pesquisar casa não considera casas, casar, casamento
        tipo_pesquisa = 3
    if td_mai_min ==False and tp_inteira == False:
        # Ao pesquisar casa considera casas, casar, casamento
        tipo_pesquisa = 4
    if ' ' in t_pesquisa and td_mai_min ==True:
        # Pesquisa por frase distinguindo maiúsc de minúsc.
        tipo_pesquisa = 5
        window.Element('_palavra_inteira').Update(False)
        palavra_inteira = False
    if ' ' in t_pesquisa and td_mai_min ==False:
        # Pesquisa por frase não distinguindo maiúsc de minúsc.
        tipo_pesquisa = 6
        window.Element('_palavra_inteira').Update(False)
        palavra_inteira = False
    if separador in t_pesquisa:
        # Pesquisa pelo nome do Livro
        tipo_pesquisa = 7
        window.Element('_palavra_inteira').Update(False)
        palavra_inteira = False

    # Atualiza a variável global do tipo da
    tp_pesquisa = tipo_pesquisa

    # Atualiza o status dos tipos de pesquisa na janela 2
    atual_status_tp_pesq_janela2()
    # return tipo_pesquisa


def mapear_linha(linha: str, termo:str) -> list:
    """ Faz o mapeamento da linha indicando a posição inicial de cada
        termo localizado

    Args:
        linha (str): Linha a ser analisada
        termo (str): termo a ser localizado

    Returns:
        list: Retorna uma lista com as posições de cada termo localizado
              na linha
    """
    linha_split = linha.split()
    mapa_x = []
    for x in linha_split:
        if x == termo:
            mapa_x

    comecar_em = -1
    qtde = linha.count(termo)
    # Criar uma lista com a posição onde começa as palavras localizadas
    mapa = []
    for _ in range(qtde):
        comecar_em = (linha.find(termo, comecar_em + 1))
        mapa.append(comecar_em)
    
    return mapa


def unir_listas(lista_de_busca: list, lista_original: list) -> list:
    """ Cria uma lista de tuplas com termos das duas listas fornecidas.
        Independentemente de como o termo foi digitado ele será sempre
        mostrado na forma como se encontra na linha original.

    Args:
        lista_de_busca (list): Lista onde está sendo efetuada a busca
                               que pode estar igual a original ou
                               totalmente em minúsculo.
        lista_original (list): Lista original.

    Returns:
        list: Retorna uma lista de tuplas com todos os termos das listas
              e seus respectivos indices:
              (indice, termo_lista_de_busca, termo_lista_original)
    """
    listas_unidas = []
    for i, x in enumerate(lista_de_busca):
        listas_unidas.append((i, x,lista_original[i]))
    return listas_unidas


def pesquisar_na_biblia(termo_pesquisa: str, tp_pesq) -> None:
    global total_linha, conta_linha, pointing, separador
    termo = termo_pesquisa
    tam_termo = len(termo)
    termo_min = termo.lower()

    # Não precisou colocar os parêntesis nesta lista por que no texto
    # tomou-se o cuidado de todos sos parêntesis abrindo ou fechando
    # estarem separados por espaços em brancos.
    lista_termo = [termo]
    lista_termo_min = [termo_min]
    for sinal in pointing:
        lista_termo.append(termo + sinal)
        lista_termo_min.append(termo_min + sinal)

    conta_linha = 0
    total_linha = 0
    contar_versiculo_localizado = 0
    contar_termo_localizado = 0
    win2.Element('_versiculo_localizado').Update(str(contar_versiculo_localizado))
    win2.Element('_termo_localizado').Update(str(contar_termo_localizado))

    # Abrir o arquivo convertido no formato com versículos
    # para a pesquisa
    with open(biblia_gravar, 'r', encoding="utf8") as biblia_versiculo:
        # Apura a quantidade de linhas do arquivo
        total_linha =  sum(1 for _ in biblia_versiculo)
        # Retorna o ponteiro para o início do arquivo
        biblia_versiculo.seek(0)
        # Deixa a barra de progresso pronta
        win2.Element('_progresso_pesquisa').UpdateBar(0, max = total_linha)
        conta_progresso_pesquisa = 0

        # Inicia a busca do termo pesquisado
        for linha_o in biblia_versiculo:
            linha_o_min = linha_o.lower()
            linha_separada = pesquisar_apos_5pipe(linha_o)
            # linha contém apenas o versículo propriamente dito
            # sem a parte inicial da linha que identifica o livro,
            # capítulo, número do versículos, exemplo abaixo:
            # 00538|AT|GÊNESIS|21|24|Respondeu Abraão: Eu jurarei.|
            # Seria somente o trecho "Respondeu Abraão: Eu jurarei."
            linha = linha_separada[0]
            linha_inicio = linha_separada[1]
            conta_progresso_pesquisa += 1
            # Atualiza a barra de progresso
            win2.Element('_progresso_pesquisa').UpdateBar(conta_progresso_pesquisa)
            # Cria uma linha toda minúscula para ser usada quando não
            # quer diferenciar a busca entre maiúsc/minúsc
            linha_min = linha.lower()
            linha_lista = linha.split()

            # Remove os simbolos de pontuação da linha com list
            # comprehension. No final não precisou utilizar a linha 
            # sem pontuação, más mantive aqui para utilizar depois
            # em outro exemplo
            # linha_sem_pont = ''.join(simbolo for simbolo in linha if simbolo not in pointing)

            win2.Element('_versiculo_localizado').Update(str(contar_versiculo_localizado))
            win2.Element('_termo_localizado').Update(str(contar_termo_localizado))

            # Definir como e onde será a busca de acordo com o tp_pesq
            if tp_pesq == 1:
                # 1 usa a linha original como lista
                # Utilizando a linha original e o termo original 
                # digitado faz com que a busca faça distinção entre
                # maiúsculo de minúsculo.
                # Buscar em uma lista é uma busca por palavra inteira.
                linha_atual = linha.split()
                termo_atual = lista_termo
                lista_termo_atual = lista_termo
                linha_unida_lista = unir_listas(linha_atual, linha_lista)

            if tp_pesq == 3:
                # 3 usa a linha minúscula como lista
                # Utiliza o termo minúsculo e a lista minúscula, isso
                # quer dizer que a busca não distingue maiúsculo de
                # minúsculo. Buscar em uma lista é uma busca por 
                # palavra inteira.
                linha_atual = linha_min.split()
                termo_atual = lista_termo_min
                lista_termo_atual = lista_termo_min
                linha_unida_lista = unir_listas(linha_atual, linha_lista)

            if tp_pesq == 2 or tp_pesq == 5:
                # 2 e 5 usa a linha original como string
                linha_atual = linha
                termo_atual = termo

            if tp_pesq == 4 or tp_pesq == 6:
                # 4 e 6 usa a linha minúscula como string
                linha_atual= linha_min
                termo_atual = termo_min

            # Aqui o Tipo da Busca já foi definido.
            # Fazer a busca e mostrar a linha destacando o termo
            # pesquisado
            if tp_pesq == 1 or tp_pesq == 3:
                # Conta quantos testes foram feitos para comparar
                # com a quantidade de itens em mapa e saber que 
                # terminou para ao final acrescentar uma quebra de linha 
                contar_testes = 0
                palavra_encontrada = False
                for verificar in linha_atual:
                    for t_vez in lista_termo_atual:
                        if verificar == t_vez:
                            palavra_encontrada = True
                            contar_versiculo_localizado += 1
                            break
                    if palavra_encontrada:
                        break

                if palavra_encontrada:
                    mapa = []
                    for j, parte in enumerate(linha_atual):
                        achou = False
                        for termo_vez in lista_termo_atual:
                            if parte == termo_vez:
                                achou = True
                                break
                            else:
                                achou = False

                        if achou:
                            # True indica que é o termo procurado
                            mapa.append((True, linha_unida_lista[j][2]))
                            contar_termo_localizado += 1
                        else:
                            # False indica que é uma palavra comum
                            mapa.append((False, linha_unida_lista[j][2]))

                    # Mostra o início da linha
                    cp(f'{linha_inicio} ', colors='blue on floralwhite',
                       end='', window=win2)

                    # Juntas as palavras e mostrar a linha completa
                    for montar in mapa:
                        contar_testes += 1
                        if montar[0]:
                            # Mostra a palavra com formatação diferente
                            cp(f'{montar[1]} ', colors='red on yellow', 
                               end='', window=win2)
                        else:
                            # Mostra a palavra normalmente
                            cp(f'{montar[1]} ', colors='black on floralwhite',
                               end='', window=win2)
                        
                        if contar_testes == len(mapa):
                            # apesar de não imprimir nada, más força
                            # passar para a próxima linha.
                           print('')
 
            # FIXME: Preciso Resolver estes problemas

            # Testar com as palavras: montanha

            # * Falta colocar para gravar um arquivo HTML com a lista
            # * dos versículos que foram localizados
            # ! Falta passar a obedecer o filtro de só pesquisar nos
            # ! livros que foram selecionados
            # * Falta colocar a ação de mostrar a ajuda se iniciar a
            # * pesquisa sem digitar nenhuma palavra
            # ? Definir se vai colocar um limite de só pesquisar uma
            # ? palavra como no mínimo Y letras, ou se vai criar uma 
            # ? lista de palavras como: [ um, uma, seu, sua, etc.] que
            # ? nunca são pesquisadas.
            # ! Falta colocar uma opção para informar só mostrar os 
            # ! primeiros X versículos, se informar ZERO mostra tudo.
            # * Ivan sugeriu fazer a pesquisa independentemente de ter
            # * digitado a palavra com ou sem acento.
            # ! Colocar uma opção para caso o resultado da pesquisa
            # ! retorne apenas uma linha, possa mostrar também, as K
            # ! linhas anteriores e K posteriores.

            # TODO: Falta colocar uma opção para ler do arquivo txt
            # TODO  as linhas que descrevem ao que vai se referir os
            # TODO  versículos subsequentes. Neste caso, ainda falta
            # TODO  gravar também estas linhas no arquivo 
            # TODO  Biblia_versiculo.txt. Elas já constam no arquivo
            # TODO  Biblia.txt

            # TODO: Falta colocar para trazer as observações sobre
            # TODO  um versículo se ele for consultado sozinho e
            # TODO  colocar para trazer a tradução se houver.
            # TODO  No arquivo Biblia_versiculo.txt não tem ainda
            # TODO  gravando nem observações sobre os versículos
            # TODO  nem o versículo em inglês e também a leitura
            # TODO  do versículo como é feita atualmente considera
            # TODO  que não há nenhum texto depois dele, então se
            # TODO  passar a ter observações ou traduções depois
            # TODO  dele, com certeza, vai ter que alterar a forma
            # TODO  como considera o fim do versículo utilizando
            # TODO  como delimitador de campo o caractere | (pipe) .
            
            if tp_pesq == 2 or tp_pesq == 5 or\
               tp_pesq == 4 or tp_pesq == 6:
                # 2 e 5 usa a linha original como string
                mapa_da_linha = mapear_linha(linha_atual, termo_atual)
                qtde = linha_atual.count(termo_atual)
                # ? tam_termo = len(termo_atual)   REPETIDO NÃO PRECISA?
                if qtde > 0:
                    contar_versiculo_localizado += 1
                    cp(f'{linha_inicio} ', colors='blue on floralwhite',
                       end='', window=win2)
                    # Mostrar os trechos da linha distinguindo-os do
                    # termo localizado
                    for pos in range(qtde):
                        contar_termo_localizado += 1
                        if pos == 0:
                            # Quando o termo localizado inicia a linha
                            palavra_linha = linha[0:tam_termo]
                            if mapa_da_linha[pos] == 0:
                                # cp(f'{termo}', colors='red on yellow',
                                cp(f'{palavra_linha}', colors='red on yellow',
                                   end='', window=win2)

                            else:
                                # Quando a palavra localizada não esta
                                # no início da linha
                                palavra_linha = linha[mapa_da_linha[pos]:mapa_da_linha[pos]+tam_termo]
                                trecho = linha[:mapa_da_linha[pos]]
                                cp(f'{trecho}', colors='black on floralwhite',
                                   end='', window=win2)
                                # cp(f'{termo}', colors='red on yellow', end='',
                                cp(f'{palavra_linha}', colors='red on yellow',
                                   end='', window=win2)
                        else:
                            # Demais partes da linha
                            # trecho separa o trecho entre as palavras
                            palavra_linha = linha[mapa_da_linha[pos]:mapa_da_linha[pos]+tam_termo]
                            trecho = linha[mapa_da_linha[pos-1]+\
                                tam_termo:mapa_da_linha[pos]]
                            cp(f'{trecho}', colors='black on floralwhite',
                               end='', window=win2)
                            # cp(f'{termo}', colors='red on yellow', end='',
                            cp(f'{palavra_linha}', colors='red on yellow',
                               end='', window=win2)

                    # Se tiver texto após a última palavra localizada
                    trecho = linha[mapa_da_linha[pos]+tam_termo:]
                    cp(f'{trecho}', colors='black on floralwhite',
                     end='', window=win2)

            if tp_pesq == 7:
                # 7 usa a linha original mostra a linha toda
                # verifica se o termo inicia o versículo
                # optei por verificar se o termo consta no início da
                # linha sem considerar os 7 caracteres inicias que são
                # o número geral do versículo e a identificação AT/NT
                if linha_o_min[8:].startswith(termo_min):
                    contar_versiculo_localizado += 1
                    cp(f'{linha_o}', colors='black on floralwhite',
                        end='', window=win2)

            # Se digitar espaço em branco na busca a busca vai ser por
            # frase e não por uma palavra iteira, então a opção
            # "palavra inteira" deve ficar False. Outro exemplo:
            # Se ele digitar o caractere pipe | por exemplo para
            # pesquisa por |RUTE|2| que vai mostrar todo o capítulo
            # 2 do livro de RUTE também não é uma busca por 
            # palavra inteira.
            ainda_utilizando = False
            if ainda_utilizando:
                window.Element('_palavra_inteira').Update(False)
                win2.Element('_palavra_inteira_status').Update(
                    'Palavra Inteira: Não')


if __name__ == '__main__':
    # Definir o Tema da janela
    sg.theme('Tan')  #DarkAmber
    # sg.SetOptions(element_padding=(0,5))

    livros_def = {'default':True, 'disabled':True,
        'visible':True, 'font':'Arial 9'}
    # Definindo os checkbox com list comprehension
    livros_a = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] <12)
    livros_b = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] >11 and x[0]<23)
    livros_c = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] >22 and x[0]<34)
    livros_d = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] >33 and x[0]<45)
    livros_e = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] >44 and x[0]<56)
    livros_f = ((sg.Checkbox(x[8], **livros_def, key=x[9]),)
        for x in livros_lista if x[0] >55 and x[0]<67)
    frame_livros_a = [*livros_a]
    frame_livros_b = [*livros_b]
    frame_livros_c = [*livros_c]
    frame_livros_d = [*livros_d]
    frame_livros_e = [*livros_e]
    frame_livros_f = [*livros_f]

    # Configuração da barra de status
    st_bar = {'size':(STA_H, 1), 'relief':'sunken',
        'font':('Helvetica', 14), 'text_color':'black',
        'background_color':'aquamarine', 'justification':'left'}
    
    # Configuração dos botões de pesquisa dos livros
    bt_lvr = {'button_color':('aliceblue','teal'), 'font':'bold'}

    # Configuração dos frames dos livros
    fr_lvr = {'font':'Arial 10', 'title_color':'turquoise'}

    # Frame Selecionar Livros
    frame_botoes_selecionar = [[sg.Button('Limpar', **bt_lvr),
        sg.Button('Todos', **bt_lvr),
        sg.Button('Ocultar', **bt_lvr),
        sg.Button('Antigo Testamento', **bt_lvr),
        sg.Button('Novo Testamento', **bt_lvr),
        sg.Button('Pentateuco', **bt_lvr),
        sg.Button('Evangelhos', **bt_lvr),
        sg.Button('Importar', button_color=('darkblue', 'bisque'),
            tooltip=' Criar arq 1ª vez! ', font='bold', key='_importar'),
        sg.Button('Sair', button_color=('linen','orangered'),
            font='bold')],
        [sg.Checkbox('Palavra inteira', default=True, font='bold', 
            key='_palavra_inteira'),
        sg.Checkbox('Diferenciar Maiúscula/Minúscula', font='bold',
            key='_dif_mai_min'),
        sg.Text('Pesquisar por:', font='bold'),
        sg.InputText(background_color='pink', text_color='blue',
            key='_palavra_pesq', focus=True),
        sg.Button('Pesquisar', button_color=('linen','olivedrab'),
            font='bold')],
        [sg.ProgressBar(1000, orientation='h', size=(BAR_H, 20),
            key='_progressbar')]]

    # Definir o output
    frame_monitor = [[
    sg.Output(size=(OUT_H1, OUT_V1), text_color='crimson',
        background_color='palegoldenrod', key='_output')]]

    #Testando incluir um item na tela atribuindo-o a uma variável
    text_elem = sg.Text(size=(18, 1))
    text_elem1 = sg.Text('BÍBLIA SAGRADA - Tradução: João Ferreira'+\
        'de Almeida - Edição Revista e Corrigida - '+\
        '(na grafia simplificada) - 43ª impressão - ' +\
        'Imprensa Bíblica Brasileira', size=(218, 1))

    # Frame com os Checkbox dos nomes dos Livros
    frame_livros_biblia = [[
    sg.Frame('(A)', frame_livros_a, **fr_lvr, key='_grupo1'),
    sg.Frame('(B)', frame_livros_b, **fr_lvr, key='_grupo2'),
    sg.Frame('(C)', frame_livros_c, **fr_lvr, key='_grupo3'),
    sg.Frame('(D)', frame_livros_d, **fr_lvr, key='_grupo4'),
    sg.Frame('(E)', frame_livros_e, **fr_lvr, key='_grupo5'),
    sg.Frame('(F)', frame_livros_f, **fr_lvr, key='_grupo6')]]

    # Leiaute da janela
    layout = [
        [text_elem, text_elem1],
        [sg.Frame('Livros da Bíblia ', frame_livros_biblia,
            font='Arial 10', title_color='blue',
            key='_frame_livros_biblia')],
        [sg.Frame(' Escolhas ', frame_botoes_selecionar,
            font='Arial 10', title_color='green',
            key='_frame_botoes_selecionar')],
        [sg.Frame(' Monitor ', frame_monitor,
            font='Arial 10', title_color='blue', key='_monitor')],
        [sg.StatusBar(textStatus, **st_bar, key='_textStatus'),
        sg.Button('Redefinir')]]

    # Criar a janela
    window = sg.Window(TITULO1, layout=layout, margins=(5, 0),
            resizable=True, return_keyboard_events=True,
            size=(WIN_W,WIN_H), location=(5, 5))

    # Loop para os eventos
    win2_active = False
    while True:
        event, values = window.read(timeout=500)
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

        if os.path.isfile(biblia_versiculo_txt):
            window.Element('Pesquisar').Update(disabled=False)
        else:
            window.Element('Pesquisar').Update(disabled=True)

        if event == 'Limpar':
            selecionar_grupo_livros('Limpar')

        if event == 'Todos':
            selecionar_grupo_livros('Todos')

        if event == 'Antigo Testamento':
            selecionar_grupo_livros('Antigo Testamento')
            
        if event == 'Novo Testamento':
            selecionar_grupo_livros('Novo Testamento')

        if event == 'Pentateuco':
            selecionar_grupo_livros('Pentateuco')

        if event == 'Evangelhos':
            selecionar_grupo_livros('Evangelhos')

        if event == 'Ocultar':
            if frame_selecionar:
                frame_selecionar = False
                window.Element('_frame_livros_biblia').Update(visible=False)
                window.Element('Ocultar').Update('Reexibir')
            else:
                frame_selecionar = True
                window.Element('_frame_livros_biblia').Update(visible=True)
                window.Element('Ocultar').Update('Ocultar ')

        if event == 'Redefinir':
            ocultar_elementos_janela()
        
        if values['_palavra_inteira'] == True:
            window.Element('_palavra_inteira').Update(text_color='red')
            palavra_inteira = True
        else:
            window.Element('_palavra_inteira').Update(text_color='gray')
            palavra_inteira = False

        if values['_dif_mai_min'] == True:
            window.Element('_dif_mai_min').Update(text_color='red')
            dif_mai_min = True
        else:
            window.Element('_dif_mai_min').Update(text_color='gray')
            dif_mai_min = False

        for meus_checkbox in livros_lista:
            if values[meus_checkbox[9]] == True:
                window.Element(meus_checkbox[9]).Update(text_color='red')
            else:
                window.Element(meus_checkbox[9]).Update(text_color='gray')

        if event == '_importar':
            window.Element('_importar').Update(disabled=True)
            window.Element('_importar').Update('Aguarde!')
            window.Element('_frame_livros_biblia').Update(visible=False)

            mostrar_variaveis()
            gravar_versiculos()
            print('Importação concluída com sucesso!')
            # print(livros_biblia)
            window.Element('_importar').Update(disabled=False)
            window.Element('_importar').Update('Importar')
            window.Element('_frame_livros_biblia').Update(visible=True)

        # 'Control_L:17' é a tecla CONTROL Esquerda
        if not win2_active and (event == 'Pesquisar' or event == 'Control_L:17'):
            # Prevenir se remover o arquivo de pesquisa depois que
            # entra no programa
            if os.path.isfile(biblia_versiculo_txt):
                # Preparar palavra a pesquisar
                termo_digitado = window.Element('_palavra_pesq').Get()
                definir_tipo_pesquisa(termo_digitado,
                 dif_mai_min, palavra_inteira)
                # Ativa a janela 2 somente depois de definir o tipo
                # da pesquisa
                win2_active = True
                window.Hide()
                pesquisa_liberada = True

                # Aqui começa o leiaute da segunda janela
                frame_monitor2 = [[
                sg.Multiline(size=(OUT_H2, OUT_V2), key='_output2',
                 autoscroll=True, reroute_stdout=True, write_only=False,
                 reroute_cprint=True, background_color='floralwhite',
                 font='Arial 12')]]

                layout2 = [[
                    sg.Text('Pesquisar por:', font='bold'),
                    # sg.Text('Pesquisando por:[' + termo_digitado + ']'),
                sg.InputText(background_color='pink', text_color='blue',
                    key='_palavra_pesq2', focus=True),
                sg.Text('Palavra Inteira: Não', 
                    key='_palavra_inteira_status'),
                sg.Text('Diferencia Maiúscula/Minúscula: Não',
                    key='_dif_mai_min_status'),
                sg.Text('T:'), sg.Text('.', key='_tipo_pesquisa'),
                sg.Text('Qtde Versículos:'), sg.Text('.......', 
                    key='_versiculo_localizado'),
                sg.Text('Qtde termo:'), sg.Text('.......', 
                    key='_termo_localizado'),],
                [sg.Button('Voltar'),
                sg.Button('Iniciar'),
                sg.ProgressBar(1000, orientation='h', size=(BAR_H, 20),
                key='_progresso_pesquisa')],
                [sg.Frame(' Monitor 2 ', frame_monitor2,
                font='Arial 10', title_color='blue', key='_monitor2')]]

                win2 = sg.Window(TITULO2, size=(WIN_W,WIN_H),
                       location=(5, 5), layout=layout2)

            else:
                # Como não achou o arquivo de pesquisa desabilita botão
                window.Element('Pesquisar').Update(disabled=False)

        if win2_active:
            ev2, values2 = win2.read(timeout=500)
            if ev2 == sg.WIN_CLOSED or ev2 == 'Voltar':
                win2_active  = False
                window.UnHide()
                win2.close()

            # Atualiza o status dos tipos de pesquisa
            atual_status_tp_pesq_janela2()

            if ev2 == 'Iniciar':
                # Prevenir se remover o arquivo de pesquisa depois
                # que entra no programa
                if os.path.isfile(biblia_versiculo_txt):
                    win2.Element('_output2').Update('')
                    termo_digitado = win2.Element('_palavra_pesq2').Get()
                    window.Element('_palavra_pesq').Update(termo_digitado)
                    definir_tipo_pesquisa(termo_digitado, dif_mai_min, palavra_inteira)
                    pesquisar_na_biblia(termo_digitado, tp_pesquisa)
                else:
                    # Como não achou o arquivo de pesquisa desabilita
                    # o botão das duas janelas
                    window.Element('Pesquisar').Update(disabled=False)
                    win2.Element('Iniciar').Update(disabled=False)

            if pesquisa_liberada:
                # Quando clica em Pesquisar na primeira janela já entra
                # na segunda janela iniciando a pesquisa
                win2.Element('_palavra_pesq2').Update(termo_digitado)
                definir_tipo_pesquisa(termo_digitado, dif_mai_min, palavra_inteira)
                pesquisar_na_biblia(termo_digitado, tp_pesquisa)
                pesquisa_liberada = False

        # Atuando sobre teclas que forem pressionadas
        if event == '@':
            text_elem.update('[' + event + ' - ' + VERSION + ']')

        if event == ' ' or event == separador:
            # Ao digitar no termo de pesquisa um espaço ou o 
            # caractere da variável separador que inicialmente
            # é um | (pipe) desmarca a opção palavra inteira
            # e avisa que o tipo de pesquisa mudou, será uma
            # pesquisa por frase ou pelo nome do
            # livro/capítulo/versículo.
            window.Element('_palavra_inteira').Update(False)
            window.Element('_textStatus').Update(AVISO1)
            window.Element('_textStatus').Update(background_color="tomato")

        if event == '%':
            mostrar_ajuda()

    window.close()