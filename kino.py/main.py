from cinema import Cinema
from movie import Movie
from session import Session


def read_int(prompt: str) -> int:
    return int(input(prompt).strip())


def create_demo_cinema() -> Cinema:
    cinema = Cinema("Кинотеатр 'Премьер'")

    movie1 = Movie("Дюна", 155, 12)
    movie2 = Movie("Интерстеллар", 169, 12)
    movie3 = Movie("Джокер", 122, 18)

    cinema.add_session(Session(movie1, "10:00", 350.0, 20))
    cinema.add_session(Session(movie2, "14:00", 400.0, 20))
    cinema.add_session(Session(movie3, "19:00", 450.0, 20))

    return cinema


def show_menu() -> None:
    print("\nМеню:")
    print("1. Показать все сеансы")
    print("2. Посмотреть свободные места на сеансе")
    print("3. Забронировать место")
    print("4. Отменить бронь")
    print("5. Выход")


def main() -> None:
    cinema = create_demo_cinema()

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            cinema.show_all_sessions()

        elif choice == "2":
            session_number = read_int("Введите номер сеанса: ")
            session = cinema.find_session_by_number(session_number - 1)
            if session != None:
                session.show_free_seats()

        elif choice == "3":
            session_number = read_int("Введите номер сеанса: ")
            seat_number = read_int("Введите номер места: ")
            cinema.book_ticket(session_number - 1, seat_number)

        elif choice == "4":
            session_number = read_int("Введите номер сеанса: ")
            seat_number = read_int("Введите номер места: ")
            cinema.cancel_ticket(session_number - 1, seat_number)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт. Выберите число от 1 до 5.")


if __name__ == "__main__":
    main()

