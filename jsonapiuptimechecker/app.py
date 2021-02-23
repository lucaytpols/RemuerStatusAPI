import time
import requests

from discord_webhook import DiscordWebhook, DiscordEmbed


try:
    # this is not the exact source code, i changed a few things, also the webhook updates every 5 minute.
    
    url1 = requests.get("site")

    if url1.status_code == 200:
        json_api_response_1 = "OK, running without issues!"
    else:
        url1 = "Error: site is having a issue right now, please check later."

except:
    json_api_response_1 = "Offline, please check again later!"
    json_api_response_2 = "Offline, please check again later!"
    json_api_response_3 = "Offline, please check again later!"

while True:

    # json-api

    webhook = DiscordWebhook(url='discord_webhook_url')

    embed = DiscordEmbed(
        title="(user) Status", color=343434
    )
    embed.set_author(
        name="Status changes every 5 minutes."
    )

    embed.set_footer(text="Bot made by © (user)")
    embed.set_timestamp()

    embed.add_embed_field(name="Main page:", value=f"The status is: {json_api_response_1}", inline=True)

    webhook.add_embed(embed)
    response = webhook.execute()

    time.sleep(300)
    webhook.delete(response)
