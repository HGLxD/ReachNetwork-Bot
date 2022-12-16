import disnake
import os

from colorama import Fore
from Database import Database
from disnake.ext import commands

from Config import JsonExtractor as JE

__import__("colorama").init(autoreset = True)

class ReachNetwork(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = JE.prefix,
            intents = disnake.Intents.all(),
            help_command = None
        )
    async def on_ready(self):
        await Database.create_tables()
        for filename in os.listdir("./Cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"Cogs.{filename[:-3]}")

        print(f"{Fore.LIGHTWHITE_EX}! {Fore.LIGHTRED_EX}Вошел как: {self.user}({self.user.id})")

    async def on_slash_command_error(self, interaction,error):
        print(error)

bot = ReachNetwork()

if __name__ == "__main__":
    bot.run(JE.token)