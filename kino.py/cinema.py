from session import Session


class Cinema:
    __name_cinema: str
    __list_of_sessions: list[Session]

    def __init__(self, name_cinema: str) -> None:
        self.__name_cinema = name_cinema
        self.__list_of_sessions = []

    def add_session(self, session: Session) -> None:
        self.__list_of_sessions.append(session)

    def show_all_sessions(self) -> None:
        if len(self.__list_of_sessions) == 0:
            print("Сеансы отсутствуют.")
            return

        print(f"Кинотеатр: {self.__name_cinema}")
        for i, session in enumerate(self.__list_of_sessions, start=1):
            print(f"\nСеанс №{i}")
            print(session.get_info())

    def show_sessions(self, movie_title: str) -> None:
        print(f"Сеансы фильма '{movie_title}':")
        found = False
        for session in self.__list_of_sessions:
            if movie_title in session.get_info():
                print(session.get_info())
                found = True

        if not found:
            print("Сеансы не найдены.")

    def find_session_by_number(self, index: int) -> Session | None:
        if 0 <= index < len(self.__list_of_sessions):
            return self.__list_of_sessions[index]

        print("Сеанс не найден.")
        return None

    def get_sessions_count(self) -> int:
        return len(self.__list_of_sessions)

    def book_ticket(self, session_index: int, seat_number: int) -> None:
        session = self.find_session_by_number(session_index)
        if session != None:
            session.book_seat(seat_number)

    def cancel_ticket(self, session_index: int, seat_number: int) -> None:
        session = self.find_session_by_number(session_index)
        if session != None:
            session.cancel_booking(seat_number)
