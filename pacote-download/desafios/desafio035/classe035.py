from abc import ABC,abstractmethod
class Arquivo(ABC):
    def __init__(self, nome:str,ext:str, tam:int = 0):
        self.nome = nome
        self.tamanho = tam
        self._extencao = None
        self.extencao = ext
    @property
    def extencao(self):
        return self._extencao
    @extencao.setter
    def extencao(self, ext:str):
        format = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in format:
            self._extencao = ext
        else:
            raise AttributeError("O Arquivo está em um formato não suportado")
    @abstractmethod
    def abrir(self):
        pass
    @property
    def nome_completo(self):
        return f'"{self.nome}.{self.extencao}"({self.tamanho/1_000_000}MB)'
class DOC(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome,'docx',tam )


    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft World")

class PDF(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome,'pdf', tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

def abrir_arquivo(objeto):
    objeto.abrir()