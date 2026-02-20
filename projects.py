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

def find_game_by_name(games, name):
    for i in range(len(games)):
        if name.lower() in games[i].name.lower():
            return i
    return -1

def find_game_by_id(games, game_id):
    for i in range(len(games)):
        if games[i].id == game_id:
            return i
    return -1

def sort_games_by_player_rating(games):
    for i in range(len(games)):
        for j in range(len(games) - 1):
            if games[j].player_rating < games[j + 1].player_rating:
                games[j], games[j + 1] = games[j + 1], games[j]
    return games


def sort_games_by_name(games):
    for i in range(len(games)):
        for j in range(len(games) - 1):
            if games[j].name > games[j + 1].name:
                games[j], games[j + 1] = games[j + 1], games[j]
    return games


def apply_discount_by_genre(games, genre, discount_percentage):
    for game in games:
        if game.genre.lower() == genre.lower():
            game.price = int(game.price * (1 - discount_percentage / 100))
            

def calculate_average_price(games):
    if len(games) == 0:
        return 0

    total = 0
    for game in games:
        total += game.price

    return total / len(games)


def find_highest_rated_game(games):
    if len(games) == 0:
        return None

    highest_rated_game = games[0]
    for game in games:
        if game.player_rating > highest_rated_game.player_rating:
            highest_rated_game = game

    return highest_rated_game


def mark_hits(games):
    for game in games:
        if game.player_rating >= 8.5:
            game.status = "Хит"

def remove_out_of_stock_games(games):
    result = []
    for game in games:
        if game.copies != 0:
            result.append(game)
    return result

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
        
# . подсчитать общее количество копий всех игр
def calculate_total_copies(games):
    total_copies = 0
    for game in games:
        total_copies += game.copies
    return total_copies

# 2. вывести список игр дешевле указанной суммы
def find_games_cheaper_than(games, price):
    result = []
    for game in games:
        if game.price < price:
            result.append(game)
    return result

# 3. увеличить возрастной рейтинг игры по ИД
def increase_age_rating_by_id(games, game_id, increment):
    for game in games:
        if game.id == game_id:
            game.age_rating += increment
            return True
    return False

# 4. вывести все уникальные жанры, присутствующие в списке
def get_unique_genres(games):
    genres = set()
    for game in games:
        genres.add(game.genre)
    return genres

# 5. проверить, есть ли игры со статусом «хит»
def has_hits(games):
    for game in games:
        if game.status.lower() == "хит":
            return True
    return False

def add_game_to_list(games, game):
    global GLOBAL_VIDEO_GAME_ID
    GLOBAL_VIDEO_GAME_ID += 1
    game.id = GLOBAL_VIDEO_GAME_ID
    games.append(game)



games = []

add_game_to_list(
        games, VideoGame(1, "Game1", "Action", "PC", 16, 1500, 8.9, "Хит", 12)
    )
add_game_to_list(
        games, VideoGame(2, "Game2", "RPG", "PS5", 18, 3500, 7.6, "Обычный", 5)
    )

print_games(games)
