from dataclasses import dataclass


@dataclass
class VideoGame:
    id: int
    name: str
    genre: str
    platform: str
    age_rating: int
    price: int
    player_rating: float
    status: str
    copies: int

GLOBAL_VIDEO_GAME_ID = 0


def search_games_by_name(games, substring):
    return [game for game in games if substring.lower() in game.name.lower()]


def find_game_by_id(games, game_id):
    for i in range(len(games)):
        if games[i].id == game_id:
            return i
    return -1


def filter_games_by_age_rating(games, age_rating):
    return [game for game in games if game.age_rating == age_rating]


def sort_games_by_name(games):
    return sorted(games, key=lambda game: game.name)


def apply_discount_by_genre(games, genre, discount_percentage):
    for game in games:
        if game.genre.lower() == genre.lower():
            game.price = int(game.price * (1 - discount_percentage / 100))


def calculate_average_price(games):
    if not games:
        return 0
    total_price = sum(game.price for game in games)
    return total_price / len(games)


def find_highest_rated_game(games):
    if not games:
        return None
    return max(games, key=lambda game: game.player_rating)


def mark_hits(games):
    for game in games:
        if game.player_rating >= 8.5:
            game.status = "Хит"


def remove_out_of_stock_games(games):
    return [game for game in games if game.copies > 0]


def print_games(games):
    print(
        f"{'ID':<6}{'Название':<20}{'Жанр':<12}{'Платформа':<12}"
        f"{'Возраст':<10}{'Цена':<8}{'Рейтинг':<10}{'Статус':<10}{'Копии':<8}"
    )
    for g in games:
        print(
            f"{g.id:<6}{g.name:<20}{g.genre:<12}{g.platform:<12}"
            f"{g.age_rating:<10}{g.price:<8}{g.player_rating:<10.1f}{g.status:<10}{g.copies:<8}"
        )


def add_game_to_list(games, game):
    global GLOBAL_VIDEO_GAME_ID
    GLOBAL_VIDEO_GAME_ID += 1
    game.id = GLOBAL_VIDEO_GAME_ID
    games.append(game)


if __name__ == "__main__":
    games = []

    add_game_to_list(
        games, VideoGame(1, "Game1", "Action", "PC", 16, 1500, 8.9, "Хит", 12)
    )
    add_game_to_list(
        games, VideoGame(2, "Game2", "RPG", "PS5", 18, 3500, 7.6, "Обычный", 5)
    )

    print_games(games)
