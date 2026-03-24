from movie import Movie


class Session:
    __movie: Movie
    __time: str
    __ticket_price: float
    __count_of_seats: int
    __occupied_places: list[int]

    def __init__(self, movie: Movie, time: str, ticket_price: float, count_of_seats: int) -> None:
        self.__movie = movie
        self.__time = time
        self.__ticket_price = ticket_price
        self.__count_of_seats = count_of_seats
        self.__occupied_places = []

    def show_free_seats(self) -> None:
        free = [i for i in range(1, self.__count_of_seats + 1) if i not in self.__occupied_places]
        print("Свободные места:", free)

    def book_seat(self, seat_number: int) -> bool:
        if seat_number < 1 or seat_number > self.__count_of_seats:
            print("Неверный номер места.")
            return False

        if seat_number in self.__occupied_places:
            print("Место уже занято.")
            return False

        self.__occupied_places.append(seat_number)
        print(f"Место {seat_number} успешно забронировано.")
        return True

    def cancel_booking(self, seat_number: int) -> bool:
        if seat_number in self.__occupied_places:
            self.__occupied_places.remove(seat_number)
            print(f"Бронирование места {seat_number} успешно отменено.")
            return True

        print("Место не было забронировано.")
        return False

    def is_seat_free(self, seat_number: int) -> bool:
        if seat_number < 1 or seat_number > self.__count_of_seats:
            print("Неверный номер места.")
            return False

        return seat_number not in self.__occupied_places

    def get_info(self) -> str:
        occupied_count = len(self.__occupied_places)
        free_count = self.__count_of_seats - occupied_count

        return (
            f"Фильм: {self.__movie}\n"
            f"Время сеанса: {self.__time}\n"
            f"Цена билета: {self.__ticket_price}\n"
            f"Всего мест: {self.__count_of_seats}\n"
            f"Свободных мест: {free_count}\n"
            f"Занятых мест: {occupied_count}"
        )
