if __name__ == "__main__":
    from decouple import config
    from core import bot

    bot.run(config("TOKEN"))
