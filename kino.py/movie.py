class Movie:
    __title: str
    __duration: int
    __age_limit: int

    def __init__(self, title: str, duration: int, age_limit: int) -> None:
        self.__title = title
        self.__duration = duration
        self.__age_limit = age_limit

    def get_info(self) -> str:
        return f"{self.__title} ({self.__duration} min, {self.__age_limit}+)"

    def __str__(self) -> str:
        return self.get_info()
