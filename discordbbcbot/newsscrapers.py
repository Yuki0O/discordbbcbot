from abc import ABC, abstractmethod


class NewsScraper(ABC):
    def __init__(self, target_url: str) -> None:
        self.__target_url = ""

    @property
    def target_url(self) -> str:
        return self.__target_url

    @abstractmethod
    def scrape(self) -> list[str]:
        raise NotImplementedError


class BBCNewsScraper(NewsScraper):
    pass


class JSTNewsScraper(NewsScraper):
    pass


class NGGNewsScraper(NewsScraper):
    pass
