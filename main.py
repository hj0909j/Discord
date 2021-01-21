# -*- coding:utf-8 -*- 
import discord, asyncio, urllib # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다. token = "my_token"
# 아까 메모해 둔 토큰을 입력합니다 client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.

token ="NjI2OTE0NTI5NDg1MjU4ODA1.XY1Bpw.3maJBBUhrMHIIZFHERYGLRfOsLk"
client = discord.Client()

#when started bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("send ;command"))
    print("I'm start")
    print(client.user.name)
    print(client.user.id)
    
    #Shoreline map 
    # urllib.request.urlretrieve("https://i.imgur.com/O3pBFyc.jpg", "ShorelineHidden.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/vAjHVMK.jpg", "ShorelineMap.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/JWzR9LD.jpeg", "ShorelineResort.jpg")
    # print("Shoreline maps loaded")

    # #Customs map
    # urllib.request.urlretrieve("https://i.imgur.com/fHXD7eJ.jpg", "CustomsHidden.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/2N8hFtM.png", "CustomsEscape.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/ZneuHRn.jpeg", "CustomsDorm.jpg")
    # print("Customs maps loaded")
    
    # urllib.request.urlretrieve("https://i.imgur.com/q37ZLmj.jpg", "InterchangeHidden.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/BB42i7B.jpg", "InterchangeMap.jpg")
    # print("Interchange maps loaded")

    # urllib.request.urlretrieve("https://i.imgur.com/ScEyqoC.png", "ReserveKey.jpg")
    # urllib.request.urlretrieve("https://i.imgur.com/vXRHlGd.png", "ReserveBunker.jpg")
    # print("Reserve maps loaded")
    
    # urllib.request.urlretrieve("https://i.imgur.com/1HgDFzf.jpg", "FactoryMap.jpg")
    # print("Factory map loaded")
    
    # urllib.request.urlretrieve("https://i.imgur.com/zMwDUfI.png", "LabMap.png")
    # print("Lab map loaded")


@client.event

#when message by bot ignoring the message
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == ";command":
        await message.channel.send("```;Customs, ;Shoreline, ;Interchange...\n;quest\nDeveloper : !Truck#7166\n```")

    if message.content == ";quest":
        await message.channel.send(";qpra, ;qthe, ;qfen, ;qpea, ;qmec, ;qrag, ;qjae")

#Map Load
    if message.content == ";Customs":
        channel = message.channel

        # 이미지를 지정한 URL에서 다운로드하여 저장
        # 디스코드에 올릴 파일을 지정하고, attachment에서 사용할 이름을 지정
        CustomsHidden = discord.File("CustomsHidden.jpg", filename="CustomsHidden.jpg")
        CustomsEscape = discord.File("CustomsEscape.jpg", filename="CustomsEscape.jpg")
        CustomsDorm = discord.File("CustomsDorm.jpg",   filename="CustomsDorm.jpg")

        await channel.send(file = CustomsHidden)
        await channel.send(file = CustomsEscape)
        await channel.send(file = CustomsDorm)
        
    if message.content == ";Shoreline":
        channel = message.channel
        
        ShorelineHidden = discord.File("ShorelineHidden.jpg", filename="ShorelineHidden.jpg")
        ShorelineMap = discord.File("ShorelineMap.jpg", filename="ShorelineMap.jpg")
        ShorelineResort = discord.File("ShorelineResort.jpg", filename="ShorelineResort.jpg")
        
        await channel.send(file = ShorelineHidden)
        await channel.send(file = ShorelineMap)
        await channel.send(file = ShorelineResort)

    if message.content == ";Interchange":
        channel = message.channel
        
        InterchangeHidden = discord.File("InterchangeHidden.jpg", filename="InterchangeHidden.jpg")
        InterchangeMap = discord.File("InterchangeMap.jpg", filename="InterchangeMap.jpg")

        await channel.send(file = InterchangeHidden)
        await channel.send(file = InterchangeMap)

    if message.content == ";Reserve":
        channel = message.channel

        ReserveKey = discord.File("ReserveKey.jpg", filename = "ReserveKey.jpg")
        ReserveBunker = discord.File("ReserveBunker.jpg", filename = "ReserveBunker.jpg")

        await channel.send(file = ReserveKey)
        await channel.send(file = ReserveBunker)

    if message.content == ";Factory":
        channel = message.channel

        FactoryMap = discord.File("FactoryMap.jpg", filename = "FactoryMap.jpg")

        await channel.send(file = FactoryMap)

    if message.content == ";The Lab":
        channel = message.channel
        LabMap = discord.File("LabMap.png", filename = "LabMap.png")
        
        await channel.send(file = LabMap)


#task

    #EFT wiki URL
    url = "https://escapefromtarkov.gamepedia.com/"

    #Prapor
    qpra1 = ["Debut", "Checking", "Search_mission","Shootout_picnic", "Delivery_from_the_past", "BP_deport", "The_bunker_-_Part_1","The_bunker_-_Part_2","Bad_rep_evidence", "Ice_cream_cones", "Postman_Pat_-_Part_1",
                                 "Shaking_up_teller", "The_Punisher_-_Part_1", "The_Punisher_-_Part_2", "The_Punisher_-_Part_3", "The_Punisher_-_Part_4", "The_Punisher_-_Part_5", "The_Punisher_-_Part_6"
                                 ,"Anesthesia","Polikhim_hobo","Grenadier","Insomnia", "Big_customer", "No_offence", "Grenadier"]
    qpra2 = [ "Perfect_mediator", "Insomnia","Test_drive_-_Part_1","Regulated_materials"]
    
    #Theraphist
    qthe1 = ["Shortage","Operation_Aquarius_-_Part_1","Operation_Aquarius_-_Part_1", "Sanitary_Standards_-_Part_1", "Sanitary_Standards_-_Part_2"
                        ,"Pharmacist", "Painkiller","Car repair","Hippocratic_Vow", "Supply_plans","Health_Care_Privacy_-_Part_1", "Health_Care_Privacy_-_Part_2", "Health_Care_Privacy_-_Part_3"
                        ,"An_apple_a_day_-_keeps_the_doctor_away", "Health_Care_Privacy_-_Part_4","Athlete", "Private_clinic", "Health_Care_Privacy_-_Part_5"
                        ,"Decontamination_service","General_wares","Colleahues_-_Part_1","Colleahues_-_Part_2","Colleahues_-_Part_3", "Postman_Pat_-_Part_2", "Out_of_curiosity"]
    qthe2 = ["Trust_regain"]

    #Fenc
    qfen = ["Collector"]

    #Skier
    qski = ["Supplier", "The_Extortionist", "Stirrup","What%27s_on_the_flash_drive%3F", "Golden_swag", "Chemical_-_Part_1", "Chemical_-_Part_2", "Chemical_-_Part_3", "Chemical_-_Part_4",
                        "Loyalty_buyout", "Vitamins_-_Part_1", "Vitamins_-_Part_2", "Friend_from_the_West_-_Part_1","Friend_from_the_West_-_Part_2","Lend_lease_-_Part_1", "Informed_means_armed", "Chumming", "Kind_of_sabotage", "Slient_caliber", "Flint", "Bullshit", "Setup","Rigged_game" ]
    
    #Peacekeeper
    qpea1 = ["Fishing_Gear", "Tigri_Safari", "Scrap_Metal", "Eagle_Eye", "Humanitarian_Supplies", "The_Cult_-_Part_1","The_Cult_-_Part_2", "Spa_Tour_-_Part_1","Spa_Tour_-_Part_2","Spa_Tour_-_Part_3",
                        "Spa_Tour_-_Part_4", "Spa_Tour_-_Part_5", "Spa_Tour_-_Part_6", "Spa_Tour_-_Part_7", "Cargo_X_-_Part_1", "Cargo_X_-_Part_2", "Cargo_X_-_Part_3", "Lend_lease_-_Part_2", "Wet_Job_-_Part_1", "Wet_Job_-_Part_2",
                        "Wet_Job_-_Part_3", "Wet_Job_-_Part_4", "Wet_Job_-_Part_5","Wet_Job_-_Part_6","Mentor"]
    qpea2 = ["The_guide", "Samples","TerraGroup_employee", "Peacekeeping_mission" ]

    #Mechanic
    qmec1 = ["Gunsmith_-_Part_1","Gunsmith_-_Part_2", "Gunsmith_-_Part_3" , "Gunsmith_-_Part_4" , "Gunsmith_-_Part_5" ,"Gunsmith_-_Part_6", "Gunsmith_-_Part_7", "Gunsmith_-_Part_8",
                                  "Gunsmith_-_Part_9","Gunsmith_-_Part_10","Gunsmith_-_Part_11","Gunsmith_-_Part_12","Gunsmith_-_Part_13","Gunsmith_-_Part_14","Gunsmith_-_Part_15","Gunsmith_-_Part_16"]
    qmec2 = ["Introduction", "Farming_-_Part_1", "Farming_-_Part_2", "Farming_-_Part_3", "Farming_-_Part_4","Signal_-_Part_1", "Signal_-_Part_2", "Signal_-_Part_3", "Signal_-_Part_4", "Bad_habit",
                                  "Scout", "Insider", "Psycho_Sniper", "Import", "Fertilizers", "A_Shooter_Born_in_Heaven", "Introduction"]

    #Ragman
    qrag1 = ["Only_business", "Make_Ultra_Great_Again", "Big_sale", "The_Blood_of_War_-_Part_1","The_Blood_of_War_-_Part_2","The_Blood_of_War_-_Part_3", "Dressed_to_kill", "Gratitude", "Sales_Night", "Hot_delivery", "Database_-_Part_1","Database_-_Part_2",
                        "Minibus", "Sew_it_good_-_Part_1", "Sew_it_good_-_Part_2", "Sew_it_good_-_Part_3", "Sew_it_good_-_Part_4", "The_key_to_success","he_Blood_of_War_-_Part_2", "he_Blood_of_War_-_Part_3", "The_key_to_success", "Living_high_is_not_a_crime_-_Part_1",
                        "Living_high_is_not_a_crime_-_Part_2","" "Charisma_brings_success", "No_fuss_needed"]
    qrag2 = [ "Supervisor", "Scavanger", "Textile_-_Part_1","Textile_-_Part_2"]

    #Jaeger
    qjae1 = ["Acquaintance", "The_survivalist_path_-_Unprotected,_but_dangerous", "The_survivalist_path_-_Thrifty", "The_survivalist_path_-_Zhivchik", "The_survivalist_path_-_Wounded_beast", "The_survivalist_path_-_Tough_guy",
                        "The_survivalist_path_-_Cold_blooded", "The_survivalist_path_-_Junkie", "The_survivalist_path_-_Zatoichi", "The_survivalist_path_-_Eagle-owl", "The_survivalist_path_-_Combat_medic", "Huntsman_path_-_Secured_perimeter", "Huntsman_path_-_The_trophy",
                        "Huntsman_path_-_Woods_cleaning", "Huntsman_path_-_Controller", "Huntsman_path_-_Sell-out", "Huntsman_path_-_Woods_keeper", "Huntsman_path_-_Justice", "Huntsman_path_-_Evil_watchman","Huntsman_path_-_Eraser","Huntsman_path_-_Eraser_-_Part_2",
                        "Ambulance", "Shady_business", "Nostalgia", "Fishing_place" ]
    qjae2 = ["Countesy_visit", "Hunting_trip", "Reserv", "The_Tarkov_shooter_-_Part_1","The_Tarkov_shooter_-_Part_2","The_Tarkov_shooter_-_Part_3","The_Tarkov_shooter_-_Part_4",
                        "The_Tarkov_shooter_-_Part_5","The_Tarkov_shooter_-_Part_6","The_Tarkov_shooter_-_Part_7","The_Tarkov_shooter_-_Part_8", "Shady_business", "Huntsman_path_-_Sadist","Hunter"]

    if message.content == ";qski":
        channel = message.channel
        
        embed = discord.Embed(title="Skier Task", color=0x00ff56)
        for i in range(0,len(qski)):
            embed.add_field(name=qski[i], value=url+qski[i], inline=True)
        
        await channel.send(embed=embed)

   
    if message.content == ";qpra":
        channel = message.channel

        embed = discord.Embed(title="Prapor Task", color=0x00ff56)
        for i in range(0,len(qpra1)):
            embed.add_field(name=qpra1[i], value=url+qpra1[i], inline=True)
        await channel.send(embed=embed)
        
        embed = discord.Embed(title="Prapor Task", color=0x00ff56)
        for i in range(0,len(qpra2)):
            embed.add_field(name=qpra2[i], value=url+qpra2[i], inline=True)
        
        await channel.send(embed=embed)
    
    if message.content == ";qthe":
        channel = message.channel
        embed = discord.Embed(title="Theraphist Task", color=0x00ff56)
        for i in range(0,len(qthe1)):
            embed.add_field(name=qthe1[i], value=url+qthe1[i], inline=True)
        await channel.send(embed=embed)

        embed = discord.Embed(title="Theraphist Task", color=0x00ff56)
        for i in range(0,len(qthe2)):
            embed.add_field(name=qthe2[i], value=url+qthe2[i], inline=True)
        await channel.send(embed=embed)


    if message.content == ";qfen":
        channel = message.channel
        embed = discord.Embed(title="Fence Task", color=0x00ff56)
        for i in range(0,len(qfen)):
            embed.add_field(name=qfen[i], value=url+qfen[i], inline=True)
        await channel.send(embed=embed)

    if message.content == ";qpea":
        channel = message.channel
        embed = discord.Embed(title="Peacekeeper Task", color=0x00ff56)
        for i in range(0,len(qpea1)):
            embed.add_field(name=qpea1[i], value=url+qpea1[i], inline=True)
        await channel.send(embed=embed)
        
        embed = discord.Embed(title="Peacekeeper Task", color=0x00ff56)
        for i in range(0,len(qpea2)):
            embed.add_field(name=qpea2[i], value=url+qpea2[i], inline=True)
        await channel.send(embed=embed)

    if message.content == ";qmec":
        channel = message.channel
        embed = discord.Embed(title="Mechanic Task", color=0x00ff56)
        for i in range(0,len(qmec1)):
            embed.add_field(name=qmec1[i], value=url+qmec1[i], inline=True)
        await channel.send(embed=embed)
        
        embed = discord.Embed(title="Mechanic Task", color=0x00ff56)
        for i in range(0,len(qmec2)):
            embed.add_field(name=qmec2[i], value=url+qmec2[i], inline=True)
        await channel.send(embed=embed)

    if message.content == ";qrag":
        channel = message.channel
        embed = discord.Embed(title="Ragman Task", color=0x00ff56)
        for i in range(0,len(qrag1)):
            embed.add_field(name=qrag1[i], value=url+qrag1[i], inline=True)
        await channel.send(embed=embed)
        
        embed = discord.Embed(title="Ragman Task", color=0x00ff56)
        for i in range(0,len(qrag2)):
            embed.add_field(name=qrag2[i], value=url+qrag2[i], inline=True)
        await channel.send(embed=embed)
    
    if message.content == ";qjae":
        channel = message.channel
        embed = discord.Embed(title="Jaeger Task", color=0x00ff56)
        for i in range(0,len(qjae1)):
            embed.add_field(name=qjae1[i], value=url+qjae1[i], inline=True)
        await channel.send(embed=embed)
        
        embed = discord.Embed(title="Jaeger Task", color=0x00ff56)
        for i in range(0,len(qjae2)):
            embed.add_field(name=qjae2[i], value=url+qjae2[i], inline=True)
        await channel.send(embed=embed)
client.run(token) # token