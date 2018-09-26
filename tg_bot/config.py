from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID =  288167324  # my telegram ID
    OWNER_USERNAME = "psyfuck_x"  # my telegram username
    API_KEY = "652618591:AAEJS-ktVzJ8WTg0fxkZ0xpoXsyfAgs29co"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://psyfuck:123@Biren.Satan@127.0.0.1:5432/psyfuckbot'  # sample db credentials
    MESSAGE_DUMP = '-1001334334931' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [288167324]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
