import discord_cfg
import logging
logging.basicConfig(level=logging.INFO)
client = discord_cfg.Client("ex.cfg")
permissions = discord_cfg.Client("per.cfg")
client.run()
exit()
