from discord import Game
from discord.ext.commands import Bot, when_mentioned_or


from logger.bot_log import Log, Disconnecting
from utils.login import Tokens
from utils.cogs_manager import load_cogs


class bot(Bot):
    def __init__(self, prefix, status_name):

        super().__init__(
            command_prefix=when_mentioned_or(prefix),
            activity=Game(name=status_name),
        )

    @property
    def bot_log(self):
        return Log()

    @property
    def bot_disconnect(self):
        return Disconnecting


sur = bot('!', '!help -- para ayuda')


if __name__ == '__main__':
    load_cogs(sur)
    sur.run(Tokens.nhbot)

    if sur.is_closed():
        try:
            sur.bot_disconnect.disconnect(sur)
        except Exception as e:
            print(e)
        finally:
            exit()
