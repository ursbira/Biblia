import Biblia

def selecionar_antigo_testamento2() -> None:
            for abreviar in Biblia.livros_abrev:
                window.Element(abreviar).Update(True, disabled=False, visible=True)

def selecionar_novo_testamento2() -> None:
            for abreviar in Biblia.livros_abrev:
                window.Element(abreviar).Update(False, disabled=False, visible=True)