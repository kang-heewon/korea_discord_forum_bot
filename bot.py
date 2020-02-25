import discord
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 681130615529144326:
        guild = client.get_guild(681090066512347146)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == "c_":
            name = "C"
        elif payload.emoji.name == "cpp":
            name = "C++"
        elif payload.emoji.name == "cs":
            name = "C#"
        elif payload.emoji.name == "go":
            name = "Go"
        elif payload.emoji.name == "java":
            name = "Java"
        elif payload.emoji.name == "js":
            name = "JavaScript"
        elif payload.emoji.name == "kotlin":
            name = "Kotlin"
        elif payload.emoji.name == "php":
            name = "PHP"
        elif payload.emoji.name == "python":
            name = "Python"
        elif payload.emoji.name == "ruby":
            name = "Ruby"
        elif payload.emoji.name == "rust":
            name = "Rust"
        elif payload.emoji.name == "swift":
            name = "Swift"
        role = discord.utils.get(guild.roles, name="🔧" + name)
        await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 681130615529144326:
        guild = client.get_guild(681090066512347146)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == "c_":
            name = "C"
        elif payload.emoji.name == "cpp":
            name = "C++"
        elif payload.emoji.name == "cs":
            name = "C#"
        elif payload.emoji.name == "go":
            name = "Go"
        elif payload.emoji.name == "java":
            name = "Java"
        elif payload.emoji.name == "js":
            name = "JavaScript"
        elif payload.emoji.name == "kotlin":
            name = "Kotlin"
        elif payload.emoji.name == "php":
            name = "PHP"
        elif payload.emoji.name == "python":
            name = "Python"
        elif payload.emoji.name == "ruby":
            name = "Ruby"
        elif payload.emoji.name == "rust":
            name = "Rust"
        elif payload.emoji.name == "swift":
            name = "Swift"
        role = discord.utils.get(guild.roles, name="🔧" + name)
        await member.remove_roles(role)


client.run(os.environ.get("BOT_TOKEN"))

