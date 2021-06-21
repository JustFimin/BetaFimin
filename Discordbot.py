import asyncio
import discord
from gtts import gTTS
from pydub import AudioSegment
import random
import pytz
import datetime

intents = discord.Intents().all()
client = discord.Client(prefix='', intents=intents)


@client.event
async def on_ready():
    print(client.user.id)
    print("Ready!")
    while True:
        await client.change_presence(activity=discord.Streaming(name=",도움 을 입력하는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming(name=";TTS 를 말하는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Streaming(name=":TTS 를 말하는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Streaming(name=",룰렛 을 돌리는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming(name=",가위 ,바위 ,보 를 하는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming(name=",타이머 를 설정하는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming(name=",주사위 를 굴리는 ", url="https://www.twitch.tv/betafimin_discordbot"))
        await asyncio.sleep(10)


@client.event
async def on_message(message):
    msg = str(message.content)

# ===================================== 채팅인식 =====================================

    if msg.count(" » ") > 0:
        msg = str(message.content.split(" » ")[1])

# ===================================== 음성연결 =====================================

    try:
        if msg == ",들어와" or msg == ",ㄷㄹㅇ":
            connected = message.author.voice
            if connected:
                await message.author.voice.channel.connect()
                await message.channel.send("봇 들어감")
            else:
                await message.channel.send("네가 통화방에 없는데 어디로 들어가라는 거야")

    except discord.errors.ClientException:
        await message.channel.send("이미 통화방에 들어와 있어")

    if msg == ",나가" or msg == ",ㄴㄱ":
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
                connected = message.author.voice
                if connected:
                    await voice.disconnect()
                    await message.channel.send("봇 나감")
                else:
                    await message.channel.send(message.author.mention + "  네가 이 통화방에 없으면 날 내보낼 수 없어")

    if msg == ",들낙" or msg == ",ㄷㄴ":
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
                connected = message.author.voice
                if connected:
                    await voice.disconnect()
                    await message.author.voice.channel.connect()
                    await message.channel.send("봇 새로고침됨")
                else:
                    await message.channel.send(message.author.mention + "  들낙할 통화방을 찾지 못했어")

# ===================================== TTS KR =====================================

    if msg.startswith(";"):
        if msg.startswith(";;"):
            print("Fredboat Command")
        else:
            for vc in client.voice_clients:
                if vc.guild == message.guild:
                    voice = vc
                    tts = str(msg.split(";")[1])

                    tts = gTTS(text=tts, lang="ko")
                    tts.save('TTS.mp3')
                    print(tts)

                    letter_sound = AudioSegment.from_mp3('TTS.mp3')

                    raw = letter_sound.raw_data[5000:-5000]

                    octaves = 1.1
                    frame_rate = int(letter_sound.frame_rate * octaves)

                    new_sound = letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})
                    new_sound = new_sound.set_frame_rate(44100)

                    new_sound.export('TTS.mp3')

                    voice.play(discord.FFmpegPCMAudio("TTS.mp3"))

# ===================================== TTS EN =====================================

    if msg.startswith(":"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
                tts = str(msg.split(":")[1])

                tts = gTTS(text=tts, lang="en")
                tts.save('TTS.mp3')
                print(tts)

                letter_sound = AudioSegment.from_mp3('TTS.mp3')

                raw = letter_sound.raw_data[5000:-5000]

                octaves = 1
                frame_rate = int(letter_sound.frame_rate * octaves)

                new_sound = letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})
                new_sound = new_sound.set_frame_rate(44100)

                new_sound.export('TTS.mp3')

                voice.play(discord.FFmpegPCMAudio("TTS.mp3"))

# ===================================== 가위바위보 =====================================

    if msg == ",가위":
        r = random.randrange(1, 4)
        if r == 1:
            await message.channel.send(message.author.mention+": :v: ***VS*** "+" 베타피민: :v:")
            await message.channel.send("***비김!***")
        elif r == 2:
            await message.channel.send(message.author.mention+": :v: ***VS*** "+" 베타피민: :fist:")
            await message.channel.send("***베타피민 승리!***")
        else:
            await message.channel.send(message.author.mention+": :v: ***VS*** "+" 베타피민: :hand_splayed:")
            await message.channel.send("***"+message.author.mention+" 승리!***")

    if msg == ",바위":
        r = random.randrange(1, 4)
        if r == 1:
            await message.channel.send(message.author.mention+": :fist: ***VS*** "+" 베타피민: :v:")
            await message.channel.send("***"+message.author.mention+" 승리!***")
        elif r == 2:
            await message.channel.send(message.author.mention+": :fist: ***VS*** "+" 베타피민: :fist:")
            await message.channel.send("***비김!***")
        else:
            await message.channel.send(message.author.mention+": :fist: ***VS*** "+" 베타피민: :hand_splayed:")
            await message.channel.send("***베타피민 승리!***")

    if msg == ",보":
        r = random.randrange(1, 4)
        if r == 1:
            await message.channel.send(message.author.mention+": :hand_splayed: ***VS*** "+" 베타피민: :v:")
            await message.channel.send("***베타피민 승리!***")
        elif r == 2:
            await message.channel.send(message.author.mention+": :hand_splayed: ***VS*** "+" 베타피민: :fist:")
            await message.channel.send("***"+message.author.mention+" 승리!***")
        else:
            await message.channel.send(message.author.mention+": :hand_splayed: ***VS*** "+" 베타피민: :hand_splayed:")
            await message.channel.send("***비김!***")

# ===================================== 룰렛 =====================================

    if msg == ",룰렛":
        r = random.randrange(1, 101)
        print("룰렛:")
        print(r)
        if r <= 70:
            await message.channel.send("***꽝!*** ``(70%)``")
        elif 70 < r <= 85:
            await message.channel.send("***동메달에 당첨됨!*** ``(15%)``")
        elif 85 < r <= 95:
            await message.channel.send("***은메달에 당첨됨!*** ``(10%)``")
        elif 95 < r <= 99:
            await message.channel.send("***금메달에 당첨됨!*** ``(4%)``")
        else:
            await message.channel.send("***다이아몬드메달에 당첨됨!*** ``(1%)``")

# ===================================== 프로필 =====================================

    if msg == ",도움":
        embed = discord.Embed(title="베타피민봇은 이렇게 써줘:",
                              description="{} 피민봇은 잡다한 기능이 많은 봇이야\n\n".format(message.author.mention)
                                          + "`,도움`   » 명령어들을 알려줘\n"
                                          + "`,들어와` `,ㄷㄹㅇ`   » 베타피민이 통화방에 들어가\n"
                                          + "`,나가` `,ㄴㄱ`   » 베타피민이 통화방을 나가\n"
                                          + "`,들낙` `,ㄷㄴ`   » 통화방에 있는 베타피민을 새로고침해\n"
                                          + "`;{문장}`   » {문장}을 통화방에서 한국어로 말해줘\n"
                                          + "`:{문장}`   » {문장}을 통화방에서 영어로 말해줘\n"
                                          + "`,가위` `,바위` `,보`   » 베타피민과 가위바위보를 할 수 있어\n"
                                          + "`,룰렛`   » 베타피민이 뽑기를 해줘\n"
                                          + "`,타이머 {자연수}`   » {자연수}초의 타이머를 시작해 (최대 300초)\n"
                                          + "`,지워 {메시지수}`   » {메시지수}만큼의 메시지를 삭제해\n"
                                          + "`,주사위 {자연수}`   » 1부터 {자연수}의 수 중에 랜덤으로 하나를 뽑아줘\n"
                                          + "`,정보`   » 이 서버의 정보를 보여줘",
                              color=0xff7757)
        embed.set_author(name="Just_Fimin", url="https://cdn.discordapp.com/attachments/768828056147853312/850256767665176576/profile7_-_point.jpg", icon_url="https://cdn.discordapp.com/attachments/768828056147853312/850256767665176576/profile7_-_point.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/768828056147853312/850256493126877184/BongocatFimin_-_point.png")
        embed.set_footer(text="made by Just_Fimin\n" + "special thanks to chang06")
        await message.channel.send(embed=embed)

# ===================================== 타이머 =====================================

    if msg == ",타이머":
        await message.channel.send("```사용법 : ,타이머 {숫자}```\n``{숫자}초 타이머가 시작돼``")

    if msg.startswith(",타이머 "):
        try:
            t = int(msg.split(",타이머 ")[1])
            print("타이머:")
            print(t)
            if 300 >= t > 0:
                t2 = 1
                await message.channel.send(str(message.author.mention) + "``" + str(t) + "``초 타이머가 시작됬어")
                await asyncio.sleep(1)
                t3 = await message.channel.send("``" + str(t2) + "``초 경과")
                for i in range(1, t):
                    t2 = t2 + 1
                    await asyncio.sleep(1)
                    await t3.edit(content="``" + str(t2) + "``초 경과")

                await asyncio.sleep(1)
                await t3.edit(content=str(message.author.mention) + "``" + str(t) + "``초가 지났어")

            elif t <= 0:
                await message.channel.send("``타이머는 자연수로 적어줘``")

            elif t > 300:
                await message.channel.send("``타이머는 300초 이하로 적어줘``")
        except ValueError:
            await message.channel.send("``타이머는 자연수인 숫자로 적어줘``")

    if msg.startswith(",더월드 "):
        try:
            t = int(msg.split(",더월드 ")[1])
            print("타이머:")
            print(t)
            if 60 >= t > 0:
                t2 = 1
                await message.channel.send("***더월드! 시간이여 멈추어라!!! ``" + str(t) + "``초동안 멈출 수 있다!!!***")
                await asyncio.sleep(1)
                t3 = await message.channel.send("***``" + str(t2) + "``초 경과!***")
                for i in range(1, t):
                    t2 = t2 + 1
                    await asyncio.sleep(1)
                    await t3.edit(content="***``" + str(t2) + "``초 경과!***")

                await asyncio.sleep(1)
                await t3.edit(content="***```diff\n-Zero....```***")

            elif t <= 0:
                await message.channel.send("``0초 이하동안 시간을 멈추는건 의미가 없다...``")

            elif t > 60:
                await message.channel.send("``아직 시간을 60초 넘게 멈추긴 무리다...``")

        except ValueError:
            await message.channel.send("``시간을 멈추려면 수치가 필요하다...``")

# ===================================== 주사위 =====================================

    if msg == ",주사위":
        await message.channel.send("```사용법 : ,주사위 {숫자}```\n``1부터 {숫자}만큼의 수 중 랜덤으로 하나를 뽑아``")

    if msg.startswith(",주사위 "):
        try:
            d = int(msg.split(",주사위 ")[1])
            if d > 1:
                r = random.randrange(1, int(d + 1))
                d2 = await message.channel.send("***``주사위를 굴리는중``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중.``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중..``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중...``***")
                await asyncio.sleep(1)
                await d2.edit(content="***주사위에서  ``" + str(r) + "``(이)가 나왔어***")

            elif 0 < d <= 1:
                d2 = await message.channel.send("***``주사위를 굴리는중``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중.``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중..``***")
                await asyncio.sleep(0.5)
                await d2.edit(content="***``주사위를 굴리는중...``***")
                await asyncio.sleep(1)
                await d2.edit(content="***주사위에서  ``1``.... 밖에 안나오지 않나.....?***")

            elif d <= 0:
                await message.channel.send("``주사위는 자연수로 적어줘``")

        except ValueError:
            await message.channel.send("``주사위는 자연수인 숫자로 적어줘``")

# ===================================== 청소 =====================================

    if msg.startswith(",지워 "):
        d = message.author.guild_permissions.administrator

        if d is True:
            amount = int(msg.split(",지워 ")[1])
            if 50 > amount > 0:
                await message.delete()
                await message.channel.purge(limit=amount)
                await message.channel.send("``"+str(amount)+"``개의 메시지를 삭제했어")
                await asyncio.sleep(2)
                await message.channel.purge(limit=1)
            if amount <= 0:
                await message.delete()
                await message.channel.purge(limit=amount)
                await message.channel.send("``"+str(amount)+"``개(?)의 메시지를 삭제했어")
                await asyncio.sleep(2)
                await message.channel.purge(limit=1)
            if amount >= 50:
                await message.channel.send("`,지워`는 위험성이 있어서 `50`개 이상의 메시지는 한번에 삭제할 수 없어")
        else:
            await message.channel.send(message.author.mention + "너는 메시지를 지울 권한이 없어")

# ===================================== 임시 =====================================

    if msg == ",자가진단":
        r = random.randrange(1, 3)
        if r <= 1:
            embed = discord.Embed(title="자가진단 사이트:",
                                  description="https://hcs.eduro.go.kr/#/main",
                                  color=0x00eaff)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/845329851388133386/852166284162367488/cKIPifwuWHrwrYg2A-fTj2hzQypTfVXFU4SYGZzvx-nGvCpJTDNkrlUfuGCNZwlAXA.png")
            await message.channel.send(embed=embed)
        if r >= 2:
            embed = discord.Embed(title="작아진 단 사이트:",
                                  description="https://hcs.eduro.go.kr/#/main",
                                  color=0x00eaff)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/848862233537675285/851828753238982656/20200729032701.1236751.jpg")
            await message.channel.send(embed=embed)

# ===================================== with 베타창공 =====================================

    if msg == "[ㄷㄹㅇ":
        connected = message.author.voice
        if connected:
            await message.author.voice.channel.connect()
            await message.channel.send("[들어와")

    if msg == "[ㄴㄱ":
        connected = message.author.voice
        if connected:
            await message.author.voice.channel.connect()
            await message.channel.send("[나가")

    if msg == "[ㄷㄴ":
        connected = message.author.voice
        if connected:
            await message.author.voice.channel.connect()
            await message.channel.send("[들낙")

# ===================================== 멤버수 =====================================

    if msg == ",정보":
        u = 0
        for _ in message.guild.roles[1].members:
            u = u + 1
        b = 0
        for _ in message.guild.roles[2].members:
            b = b + 1
        u2 = str("**유저 수 : `" + str(u) + "명`**\n")
        for member in message.guild.roles[1].members:
            u2 = u2 + "  `" + str(member.name) + "`  "
        u2 = u2 + "\n⠀"
        b2 = str("**봇 수 : `" + str(b) + "명`**\n")
        for bot in message.guild.roles[2].members:
            b2 = b2 + "  `" + str(bot.name) + "`  "
        b2 = b2 + "\n⠀"
        tc = 0
        for _ in message.guild.text_channels:
            tc = tc + 1
        voc = 0
        for _ in message.guild.voice_channels:
            voc = voc + 1
        embed = discord.Embed(title="**〈 `" + str(message.guild.name) + "` 의 정보 〉**",
                              description="⠀\n"
                                            + "**서버 지역 : `" + str(message.guild.region) + "`**\n"
                                            + "**서버 주인 : " + message.guild.owner.mention + "**\n"
                                            + "\n**채팅 채널 : `" + str(tc) + "개`**\n"
                                            + "**음성 채널 : `" + str(voc) + "개`**\n"
                                            + "\n**총 멤버 수 : `" + str(message.guild.member_count) + "명`**\n⠀"
                                            + "\n" + str(u2) + "\n"
                                            + str(b2)
                                            + "\n ",
                              color=0xff7757)
        embed.set_thumbnail(
            url=str(message.guild.icon_url))
        await message.channel.send(embed=embed)

# ===================================== 영어 수행 =====================================

    if msg == ",영어수행":
        r = random.randrange(1, 17)
        if r <= 1:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**1-1** (사진을 클릭하여 확대)\n\n"
                                                + "T : I like Spanish food\n"
                                                + "Y : ||Have you ever had Spanish food before?||\n"
                                                + "T : No, I haven’t. Have you?\n"
                                                + "Y : ||Yes, I have. I hope you can try It something.||\n"
                                                + "T : I will.",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856473683866550272/document_0012.jpg"))
            await message.channel.send(embed=embed)

        if 1 < r <= 2:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**1-2** (사진을 클릭하여 확대)\n\n"
                                                + "T : I like travel\n"
                                                + "Y : ||Have you ever visited another country?||\n"
                                                + "T : No, I haven’t. Have you?\n"
                                                + "Y : ||Yes, I have. I hope you can travel to another country sometime.||\n"
                                                + "T : I will.",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856473787242381332/document_0012.jpg"))
            await message.channel.send(embed=embed)

        if 2 < r <= 3:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**1-3** (사진을 클릭하여 확대)\n\n"
                                                + "Y : ||You should read this book about the moon. It’s really interesting||\n"
                                                + "T : I know. I’ve already read it\n"
                                                + "Y : ||You did? How about the movie? Have you also seen the movie about the book?||\n"
                                                + "T : No, I haven’t.\n"
                                                + "Y : ||Well, it’s even better than the book. I hope you can see the movie soon.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856473900560023572/document_0012.jpg"))
            await message.channel.send(embed=embed)

        if 3 < r <= 4:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**1-4** (사진을 클릭하여 확대)\n\n"
                                                + "T : I’m going to buy this CD. I love listening to piano music.\n"
                                                + "Y : ||Me, too. I also enjoy playing the piano.||\n"
                                                + "T : Really? So you can play the piano?\n"
                                                + "Y : ||Yes. How about you?||\n"
                                                + "T : Well, I’ve never learned how to play.\n"
                                                + "Y : ||It’s fun. I hope you’ll have a chance to learn.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856473900560023572/document_0012.jpg"))
            await message.channel.send(embed=embed)

        if 4 < r <= 5:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**2-1** (사진을 클릭하여 확대)\n\n"
                                                + "T : Welcome to Italian Food. What would you like to order?\n"
                                                + "Y : ||I want to order a mushroom pizza.||\n"
                                                + "T : Would you like anything else?\n"
                                                + "Y : ||No, thank you.||\n"
                                                + "T : Will it be for here or to go?\n"
                                                + "Y : ||For here, please.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474014578245642/document_0030.jpg"))
            await message.channel.send(embed=embed)

        if 5 < r <= 6:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**2-2** (사진을 클릭하여 확대)\n\n"
                                                + "T : What would you like to order?\n"
                                                + "Y : ||I want to order a piece of cake||\n"
                                                + "T : Would you like anything else?\n"
                                                + "Y : ||No.||\n"
                                                + "T : Will it be for here or to go?\n"
                                                + "Y : ||To go, please, Thank you.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474062636580864/document_0030.jpg"))
            await message.channel.send(embed=embed)

        if 6 < r <= 7:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**2-3** (사진을 클릭하여 확대)\n\n"
                                                + "T : What would you like to order?\n"
                                                + "Y : ||I want to order Mandoguk||\n"
                                                + "T : Would you like anything else?\n"
                                                + "Y : ||No, thank you.||\n"
                                                + "T : Will it be for here or to go?\n"
                                                + "Y : ||It’s to go, please.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474127929049109/document_0030.jpg"))
            await message.channel.send(embed=embed)

        if 7 < r <= 8:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**2-4** (사진을 클릭하여 확대)\n\n"
                                                + "T : What would you like to order?\n"
                                                + "Y : ||I want to order a hot dog and one milk, please.||\n"
                                                + "T : Would you like anything else?\n"
                                                + "Y : ||No.||\n"
                                                + "T : Will it be for here or to go?\n"
                                                + "Y : ||To go, please, Thank you.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474184971583528/document_0030.jpg"))
            await message.channel.send(embed=embed)

        if 8 < r <= 9:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**3-1** (사진을 클릭하여 확대)\n\n"
                                                + "Y : ||It’s raining cats and dogs.||\n"
                                                + "T : Can you say that again?\n"
                                                + "Y : ||I said, “It’s raining cats and dogs.”||\n"
                                                + "T : What does that mean?\n"
                                                + "Y : ||It means “It’s raining a lot.”||\n"
                                                + "T : Oh, I see.",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474263356047360/document_0048.jpg"))
            await message.channel.send(embed=embed)

        if 9 < r <= 10:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**3-2** (사진을 클릭하여 확대)\n\n"
                                                + "Y : ||This juice is on me.||\n"
                                                + "T : Can you say that again?\n"
                                                + "Y : ||I said, “This juice is on me.”||\n"
                                                + "T : What does that mean?\n"
                                                + "Y : ||It means “I’ll pay for the juice.”||\n"
                                                + "T : Oh, I see.",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474445048709120/document_0048.jpg"))
            await message.channel.send(embed=embed)

        if 10 < r <= 11:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**3-3** (사진을 클릭하여 확대)\n\n"
                                                + "~~Y : ||Everything looks delicious.||~~\n"
                                                + "~~T : Yes, Would you like some of my spaghetti?~~\n"
                                                + "Y : ||No, thanks. Spaghetti is not my cup of tea.||\n"
                                                + "T : Can you say that again?\n"
                                                + "Y : ||I said, “Spaghetti is not my cup of tea.”||\n"
                                                + "T : What does that mean?\n"
                                                + "Y : ||It means “I don’t like spaghetti.”||\n"
                                                + "T : Oh, I see.",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474406519832586/document_0048.jpg"))
            await message.channel.send(embed=embed)

        if 11 < r <= 12:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**3-4** (사진을 클릭하여 확대)\n\n"
                                                + "Y : ||I feel under the weather.||\n"
                                                + "T : Can you say that again?\n"
                                                + "Y : ||I said, “I feel under the weather.”||\n"
                                                + "T : What does that mean?\n"
                                                + "Y : ||It means “I don’t feel well.” I think I have a cold.”||\n"
                                                + "T : Oh. Why don’t you by some medicine before you get on the plane? You can get medicine at the store over there.\n"
                                                + "Y : ||I guess I should.||",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474362278314004/document_0048.jpg"))
            await message.channel.send(embed=embed)

        if 12 < r <= 13:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**4-1** (사진을 클릭하여 확대)\n\n"
                                                + "T : Hello. May I help you?\n"
                                                + "Y : ||Yes, please. I’d like to get a refund for this watch.||\n"
                                                + "T : OK. Was there anything wrong with it?\n"
                                                + "Y : ||No, I just changed my mind. Can I get my money back?||\n"
                                                + "T : Let’s see. Do you have the receipt with you?\n"
                                                + "Y : ||Here it is. I bought it three days ago.||\n"
                                                + "T : Oh, then it’s possible",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474513508401162/document_0066.jpg"))
            await message.channel.send(embed=embed)

        if 13 < r <= 14:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**4-2** (사진을 클릭하여 확대)\n\n"
                                                + "T : Hello. May I help you?\n"
                                                + "Y : ||Yes, please. I’d like to get a refund for this smartphone.||\n"
                                                + "T : OK. Was there anything wrong with it?\n"
                                                + "Y : ||No, I just changed my mind. Can I get my money back?||\n"
                                                + "T : Let’s see. Do you have the receipt with you?\n"
                                                + "Y : ||Here it is. I bought it three days ago.||\n"
                                                + "T : Oh, then it’s possible",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474604548784148/document_0066.jpg"))
            await message.channel.send(embed=embed)

        if 14 < r <= 15:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**4-3** (사진을 클릭하여 확대)\n\n"
                                                + "T : Hello. May I help you?\n"
                                                + "Y : ||Yes, please. I’d like to get a refund for this T-shirt.||\n"
                                                + "T : OK. Was there anything wrong with it?\n"
                                                + "Y : ||It’s too small. Can I get my money back?||\n"
                                                + "T : Let’s see. Do you have the receipt with you?\n"
                                                + "Y : ||Here it is. I bought it three days ago.||\n"
                                                + "T : Oh, then it’s possible",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474553438175302/document_0066.jpg"))
            await message.channel.send(embed=embed)

        if 15 < r <= 16:
            embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                                  description="**4-4** (사진을 클릭하여 확대)\n\n"
                                                + "T : Hello. May I help you?\n"
                                                + "Y : ||Yes, please. I’d like to get a refund for this black umbrella.||\n"
                                                + "T : OK. Was there anything wrong with it?\n"
                                                + "Y : ||No, I just changed my mind. Can I get my money back?||\n"
                                                + "T : Let’s see. Do you have the receipt with you?\n"
                                                + "Y : ||Here it is. I bought it three days ago.||\n"
                                                + "T : Oh, then it’s possible",
                                  color=0xff7757)
            embed.set_thumbnail(
                url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474656847298610/document_0066.jpg"))
            await message.channel.send(embed=embed)

    if msg == ",음악수행 1":
        embed = discord.Embed(title="영어 수행 중 하나를 랜덤으로 보여드립니다(출처 : 두클래스)",
                              description="**4-4** (사진을 클릭하여 확대)\n\n"
                                          + "T : Hello. May I help you?\n"
                                          + "Y : Yes, please. I’d like to get a refund for ______________\n"
                                          + "T : OK. Was there anything wrong with it?\n"
                                          + "Y : ||No, I just changed my mind. Can I get my money back?||\n"
                                          + "T : Let’s see. Do you have the receipt with you?\n"
                                          + "Y : ||Here it is. I bought it three days ago.||\n"
                                          + "T : Oh, then it’s possible",
                              color=0xff7757)
        embed.set_thumbnail(
            url=str("https://cdn.discordapp.com/attachments/821951856245866497/856474656847298610/document_0066.jpg"))
        await message.channel.send(embed=embed)

# ===================================== print =====================================

    if msg == ",print":
        await message.channel.send("_`printing!`_")

        
access_token = os.environ['BOT_TOKEN']
client.run("access_token")
