from discordbbcbot.settings import ApplicationSettingsHandler

handler = ApplicationSettingsHandler()
settings = handler.load()
print(settings.discord_token)
