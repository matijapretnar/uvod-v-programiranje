import random


def razbij_na_zloge(beseda):
    '''Besedo razdeli na zloge (deli ob vsakem samoglasniku).'''
    zlogi = []
    zlog = ''
    for znak in beseda:
        if znak.lower() in 'aeiou':
            zlogi.append(zlog + znak)
            zlog = ''
        else:
            zlog += znak
    if zlog:
        zlogi.append(zlog)
    return zlogi


def prehodi_med_zlogi(besedilo):
    prehodi = {None: {}}
    for beseda in besedilo.split():
        zlogi = razbij_na_zloge(beseda)
        for prejsnji, naslednji in zip([None] + zlogi, zlogi + [None]):
            if prejsnji not in prehodi:
                prehodi[prejsnji] = {}
            prehodi[prejsnji][naslednji] = prehodi[prejsnji].get(naslednji, 0) + 1
    return prehodi


def prehodi_med_besedami(besedilo):
    prehodi = {None: {}}
    besede = besedilo.split()
    for prejsnja, naslednja in zip([None] + besede, besede + [None]):
        if prejsnja not in prehodi:
            prehodi[prejsnja] = {}
        prehodi[prejsnja][naslednja] = prehodi[prejsnja].get(naslednja, 0) + 1
    return prehodi


def izberi_nakljucnega(pogostost):
    skupaj = sum(pogostost.values())
    izbira = random.randint(0, skupaj - 1)
    meja = 0
    for element, pojavitve in pogostost.items():
        meja += pojavitve
        if meja > izbira:
            return element


def naredi_nakljucno_besedo(prehodi):
    beseda = ''
    zlog = izberi_nakljucnega(prehodi[None])
    while zlog is not None:
        beseda += zlog
        zlog = izberi_nakljucnega(prehodi[zlog])
    return beseda

def naredi_nakljucen_stavek(prehodi):
    stavek = []
    beseda = random.choice(list(prehodi.keys()))
    for i in range(100):
        stavek.append(beseda)
        beseda = izberi_nakljucnega(prehodi[beseda])
    return " ".join(stavek)

def naredi_nakljucen_stavek2(prehodi):
    return " ".join(random.sample(list(prehodi.keys()), 100))

# besedilo = '''People have voted in the Philippines, where an outspoken mayor, Rodrigo "Digong" Duterte, is the favourite to win the presidential elections. Five candidates are running but Mr Duterte led polls ahead of voting, despite controversial comments while campaigning and a hardline stance. The campaign was driven by fears about the economy, inequality and corruption. Voting was extended for an hour in some areas after glitches with vote-counting machines. More than 100,000 police officers were on duty amid violence ahead of the election. On Monday, seven people were shot dead in an ambush by unknown gunmen in the town of Rosario, in Cavite province, south of the capital, Manila. The region had been considered an area of concern because of its political rivalries, said local media. On Saturday, a mayoral candidate was murdered in the south of the country. In pictures: Crowds and queues as Filipinos vote Who are the candidates in the Philippines' elections? Cards Against Corruption: A game about the Philippines Philippine presidential candidates (left to right) Vice-President Jejomar Binay, Senator Miriam Santiago, Davao city mayor Rodrigo Image copyrightReuters President Benigno "Noynoy" Aquino is standing down as the constitution limits presidents to one six-year term. Filipinos will also pick a vice-president and local officials. The election campaign has focused on reforming the economy, infrastructure, tackling corruption and crime and on the territorial disputes with China in the South China Sea. Mr Duterte has run a campaign focused on law and order issues, but made many controversial statements, including saying that he would butcher criminals. A former state prosecutor nicknamed "The Punisher", he has been mayor of the southern city of Davao for more than 22 years. He recently joked that, as mayor, he should have been first to rape an Australian missionary murdered in a prison riot, but he later apologised. At the scene: Jonathan Head, BBC South East Asia correspondent Jump media playerMedia player helpOut of media player. Press enter to return or tab to continue. Media captionOutspoken mayor Rodrigo "Digong" Duterte holds a considerable lead over his rivals, as Jonathan Head reports Elections here are a cheerful, communal affair with large family groups or neighbours walking into the polling stations to vote together. The constant crowds coming in and out of the elementary school in Manila's Tondo district looked hard to manage. But election officials are well-practised, and voters well-informed. Plenty of officials were on hand to help voters manage the formidable ballot sheets, listing in this constituency dozens of candidates for the various local and national posts. The enthusiasm across the age and class spectrum for Mr Duterte in this campaign has exposed the weariness of Filipinos with the familiar political faces, who have delivered some economic improvements but little real change in the levels of poverty and corruption. Mr Duterte has suggested he will disregard democratic checks and balances if they get in the way of fixing the country's problems. It's a message that has excited and attracted people. Yet the numbers coming to vote here, and the positive and relaxed atmosphere, show that the faith in the familiar rituals of democracy is still as strong here as anywhere in Asia. Populism, celebrity and ugly realities Mr Duterte's closest rivals in the opinion polls are Grace Poe, a former schoolteacher and first-term senator, and Mar Roxas, a former investment banker and the grandson of the first president of the Philippine Republic. President Benigno Aquino has been leading attempts to bring together other candidates in an effort to defeat Mr Duterte. He warned that if Mr Duterte were to be elected, it could mean a return to dictatorship. Benigno AquinoImage copyrightAFP Image caption Current President Benigno Aquino can only serve one presidential term In a final rally on Saturday, Mr Aquino appealed to voters: "I need your help to stop the return of terror in our land. I cannot do it alone."However the other four candidates, also including Jejomar Binay and Miriam Defensor-Santiago, refused to step aside. An alternative look at the election campaign #BBCPH2016Image copyrightGoh Wei Choon and Jiahui Wee Image caption Love Snapchat? Follow our official BBC News account Traffic jams and Duterte fans in Manila Filipino boxing youth and politician Pacquiao Election issues through emojis The fizzy drink and bun presidential poll Cards Against Corruption: A game about the Philippines A vice-president, senators and about 18,000 local officials including mayors will also be elected. Among the candidates for the vice-presidency is "Bongbong" Marcos Jr, the son of late dictator Ferdinand Marcos. More than 54 million people are registered to vote across the archipelago of 7,000 islands.'''
besedilo = '''Il cancelliere austriaco Werner Faymann ha annunciato le sue dimissioni. Lo riportano i media locali. Faymann ha annunciato le sue dimissioni in un intervento televisivo trasmesso in diretta sul sito della cancelleria federale. "Mi sto dimettendo dal mio ruolo di capo del partito e di cancelliere federale", ha detto Faymann. Faymann lascia dopo la sconfitta alle elezioni presidenziali.  Nei giorni scorsi Faymann aveva ricevuto pressioni da parte dei sindacati e dall'ala giovanile del partito, l'Spo, per le sue posizioni sulle leggi in materia di asilo e per la sconfitta del partito durante le presidenziali di due settimane fa in cui ha trionfato l'ultranazionalista Norbert Hofer. "Avere la maggioranza del partito non è sufficiente", ha fatto sapere il portavoce di Faymann citando lo stesso cancelliere durante una conferenza stampa convocata in fretta. - See more at: http://rai.it/dl/rainews/articoli/Austria-Feymann-Presidenziali-177d0481-f43f-44b9-ab2b-56d7dc995ba0.html'''

# with open('../09-datoteke/klasiki/martin-krpan.txt') as f:
#     prehodi = prehodi_med_zlogi(f.read())
# for i in range(100):
#     print(naredi_nakljucno_besedo(prehodi))

with open('../09-datoteke/klasiki/hlapec-jernej.txt') as f:
    prehodi = prehodi_med_zlogi(f.read())
for i in range(100):
    print(naredi_nakljucno_besedo(prehodi))

# def nakljucni_zlog():
#     soglasnik = random.choice('bcčdfghjklmnprsštvzž')
#     samoglasnik = random.choice('aeiou')
#     return soglasnik + samoglasnik

# for i in range(100):
