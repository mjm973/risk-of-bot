# RiskOfBot.py

import os
import discord
from discord.ext import commands
import random
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

survivors = [
    'Commando',
    'Huntress',
    'Bandit',
    'MUL-T',
    'Engineer',
    'Artificer',
    'Mercenary',
    'REX',
    'Loader',
    'Acrid',
    'Captain',
    'Heretic'
]

common = [
    'Armor-Piercing Rounds',
    'Backup Magazine',
    'Bison Steak',
    'Bundle of Fireworks',
    'Bustling Fungus',
    'Cautious Slug',
    'Crowbar',
    'Energy Drink',
    'Focus Crystal',
    'Gasoline',
    'Lens-Maker\'s Glasses',
    'Medkit',
    'Monster Tooth',
    'Paul\'s Goat Hoof',
    'Personal Shield Generator',
    'Repulsion Armor Plate',
    'Rusted Key',
    'Soldier\'s Syringe',
    'Sticky Bomb',
    'Stun Grenade',
    'Topaz Brooch',
    'Tougher Times',
    'Tri-Tip Dagger',
    'Warbanner'
]

uncommon = [
    'AtG Missile Mk. 1',
    'Bandolier',
    'Berzerker\'s Pauldron',
    'Chronobauble',
    'Death Mark (Harry Potter vuelve a Hogwarts)',
    'Fuel Cell',
    'Ghor\'s Tome',
    'Harverster\'s Scythe',
    'Hopoo Feather',
    'Infusion',
    'Kjaro\'s Band',
    'Leeching Seed',
    'Lepton Daisy',
    'Old Guillotine',
    'Old War Stealthkit',
    'Predatory Instincts',
    'Razorwire',
    'Red Whip',
    'Rose Buckler',
    'Runald\'s Band',
    'Squid Polyp',
    'Ukulele',
    'War Horn',
    'Wax Quail',
    'Will-o\'-the-Wisp'
]

legendary = [ 
    '57 Leaf Clover',
    'Aegis',
    'Alien Head',
    'Brainstalks',
    'Brilliant Behemoth',
    'Ceremonial Dagger',
    'Defensive Mircobots',
    'Dio\'s Friendo',
    'Frost Relic',
    'H3AD-5T v2',
    'Happiest Mask',
    'Hardlight Afterburner',
    'Interstelar Desk Plant',
    'N\'kuhana\'s Opinion',
    'Rejuvenation Rack',
    'Resonance Disc',
    'Sentient Meat Hook',
    'Shattering Justice',
    'Soulbound Catalyst',
    'Unstable Tesla Coil',
    'Wake of Vultres'
]

equipment = [
    'Blast Shower',
    'Disposable Missile Launcher',
    'Eccentric Vase',
    'Foreign Fruit',
    'Forgive Me Please',
    'Gnarled Woodsprite',
    'Gorag\'s Opus',
    'Jade Elephant',
    'Milky Chrysalis',
    'Ocular HUD',
    'Preon Accumulator',
    'Primordial Cube',
    'Radar Scanner',
    'Recycler',
    'Royal Capacitor',
    'Sawmerang',
    'Super Massive Leech',
    'The Back-up',
    'The Crowdfunder',
    'Volcanic Egg',
    'Effigy of Grief',
    'Glowing Meteorite',
    'Helfire Tincture',
    'Spinel Tonic'
]

lunar = [ 
    'Beads of Fealty',
    'Brittle Crown',
    'Corpsebloom',
    'Defian Gouge',
    'Essence of Heresy',
    'Focused Convergence',
    'Gesture of the Drowned',
    'Hooks of Heresy',
    'Mercurial Rachis',
    'Purity',
    'Shaped Glass',
    'Strides of Heresy',
    'Transcendence',
    'Visions of Heresy'
]

last_user = None
last_survivor = None 
last_commmon = None
last_uncommon = None 
last_legendary = None
last_equipment = None 
last_lunar = None

bot = commands.Bot(command_prefix="!")

@bot.command(name="test", help=":)")
async def test_command(ctx):
    await ctx.send("The answer is 42")

def build_run_string(username = "User"):
    global last_survivor
    global last_commmon
    global last_uncommon
    global last_legendary
    global last_equipment
    global last_lunar

    template = "*{6}*, your survivor is **{0}**!\nCommon: **{1}**\nUncommon: **{2}**\nLegendary: **{3}**\nEquipment: **{4}**\nLunar: **{5}**"

    return template.format(last_survivor,
        last_commmon, 
        last_uncommon,
        last_legendary,
        last_equipment,
        last_lunar,
        username)

@bot.command(name="randomrun", help="Generates a random loadout for a locked randomized run")
@commands.guild_only()
async def random_run_command(ctx):
    global survivors
    global last_survivor
    global common 
    global last_commmon
    global uncommon
    global last_uncommon
    global legendary
    global last_legendary
    global equipment
    global last_equipment
    global lunar
    global last_lunar

    tag = ctx.author.nick or ctx.author.name

    last_user = tag
    last_survivor = random.choice(survivors)
    last_commmon = random.choice(common)
    last_uncommon = random.choice(uncommon)
    last_legendary = random.choice(legendary)
    last_equipment = random.choice(equipment)
    last_lunar = random.choice(lunar)

    await ctx.send(build_run_string(last_user))

@bot.command(name="reroll", help="Rerolls the last loadout. Takes 'common' or 'uncommon' as a parameter")
@commands.guild_only()
async def reroll_run_command(ctx, rarity):
    global last_user
    global last_survivor
    global common 
    global last_commmon
    global uncommon
    global last_uncommon
    global last_legendary
    global last_equipment
    global last_lunar

    def reroll_common():
        global common
        global last_commmon

        last_commmon = random.choice(common)
        return True

    def reroll_uncommon():
        global uncommon
        global last_uncommon

        last_uncommon = random.choice(uncommon)
        return True


    reroll_table = {
        "common" : reroll_common,
        "uncommon" : reroll_uncommon
    }

    reroll = reroll_table.get(rarity, lambda : False)
    if reroll():
        await ctx.send(build_run_string(last_user))
    else:
        await ctx.send("Can't reroll that, yo!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected!')

bot.run(TOKEN)