from abc import ABC, abstractmethod


class Translator(ABC):
    def __init__(self, dest_lang: str) -> None:
        self.__dest_lang = ""

    @property
    def dest_language(self) -> str:
        return self.__dest_lang

    @abstractmethod
    def translate(self, src_text: str) -> str:
        raise NotImplementedError


class GoogleTranslator(Translator):
    pass


class DeepLTranslator(Translator):
    pass
