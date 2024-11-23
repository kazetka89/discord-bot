import discord
import requests

TOKEN = ''
ESP_IP = 'http://192.168.0.235'

# Inicjalizacja klienta Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Funkcja do wysyłania żądania HTTP do ESP32
# def send_command(gpio, state):
#     try:
#         url = f"{ESP_IP}/{gpio}/{state}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             return f"GPIO {gpio} ustawione na {state.upper()}"
#         else:
#             return f"Nie udało się wysłać polecenia do GPIO {gpio}."
#     except Exception as e:
#         return f"Błąd połączenia z ESP32: {str(e)}"
def send_command(gpio, state):
    try:
        url = f"{ESP_IP}/gpio/{gpio}/{state}"
        print(f"Wysyłanie żądania do URL: {url}")  # Debug
        response = requests.get(url)
        print(f"Odpowiedź HTTP: {response.status_code}")  # Debug
        if response.status_code == 200:
            return f"GPIO {gpio} ustawione na {state.upper()}"
        else:
            return f"Nie udało się wysłać polecenia do GPIO {gpio}. Status: {response.status_code}"
    except Exception as e:
        return f"Błąd połączenia z ESP32: {str(e)}"


@client.event
async def on_ready():
    print(f'Bot {client.user} jest włączony!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!gpio'):
        # Przykład komendy: !gpio 5 on
        try:
            _, gpio, state = message.content.split()
            response = send_command(gpio, state)
            await message.channel.send(response)
        except ValueError:
            await message.channel.send("Użycie: !gpio [nr GPIO] [on/off]")

client.run(TOKEN)