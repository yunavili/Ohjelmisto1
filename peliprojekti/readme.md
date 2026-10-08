Tässä on käännös korjattuna siten, että pelin sisäiset toiminnot, valikkokohdat, muuttujat ja mekaaniset termit on jätetty englanniksi:

---

Westerosi Traveler -Peli

Tekstipohjainen seikkailupeli, joka sijoittuu Westerosin maailmaan.

Tekijä: Yuliia Ivanska eli yunaiv (mun nickname)

THE IDEA

Westerosi Traveler on terminaalissa pelattava roolipeli, joka on saanut inspiraationsa Dungeons & Dragons -pöytäroolipelistä. "Winter is coming": pelaaja on matkailija, joka on jäänyt loukkuun Westerosin karuihin maihin, missä vaara väijyy jokaisessa huoneessa. Pelimaailma koostuu viidestä huoneesta, joita yhdistää hämärä käytävä. Pelaaja tutkii huoneita, kerää esineitä, keskustelee NPC-hahmojen kanssa ja taistelee White Walkereita vastaan noppaa heittämällä.

Peliä pelataan kokonaan numeroidun main menun kautta: pelaaja kirjoittaa sen toiminnon numeron, jonka hän haluaa suorittaa, ja peli vastaa tulostetulla tekstillä. Täsmälleen kuten erittäin vanhan koulukunnan tekstiseikkailussa!

THE GOAL

Pelaaja aloittaa Hallwaysta ja löytää tavoitteensa sieltä. Pelissä on kolme erilaista endingiä:

1. Death – pelaajan HP putoaa nollaan fightissa.
2. A New Alliance – pelaaja tapaa Jon Snown Guard postissa ja päättää lähteä Westerosista yhdessä hänen kanssaan. Travelling ei ollut koskaan tarkoitettu solo adventureksi.
3. The Survivor – pelaaja voittaa jokaisen enemyn (Night Walker Hallwayssa ja White Walker Mystical vaultissa) ja selviää kaikkien odotusten vastaisesti.

Pelin läpäisyyn ei ole yhtä ainoaa "oikeaa" tapaa – pelaaja valitsee, taisteleeko hän tiensä läpi, etsiikö alliancea vai perishää yrittäessään.

OPERATING PRINCIPLES

Peli on kirjoitettu Pythonilla käyttäen vain vakiokirjastoa. Se käynnistetään 'peliprojekti'-kansansiosta komennolla python main.py -file

Käynnistyksen yhteydessä peli kirjoittaa ja näyttää intro.txt- ja ohjeet.txt-tiedostot. Jos save file 'saves.json' on olemassa, peli lataa sen, muuten peli kysyy pelaajan nimeä ja ikää. Alle 12-vuotiaat eivät saa pelata.

Pelin sydän on turn-based game loop src/game.py:

1. Check käydäänkö jokin kolmesta endingistä läpi tiedostossa src/endings.py.
2. Show main menu.
3. Read pelaajan choice ja run sitä vastaava action.
4. Repeat kunnes ending tapahtuu tai pelaaja exitöi.

MODULES

'main.py' - Entry point: kirjoittaa intro-tiedostot, sets up playerin, käynnistää game loopin
'src/game.py' - Main menu, player setup ja game loop
'src/world.py' - Builds koko game worldin: items, characters, rooms, enemies ja dice
'src/characters.py' - 'Character' base class sekä 'Player'-, 'Enemy'- ja 'NPC'-subclassit
'src/items.py' - 'Item'-, 'HealingPotion'- ja 'Dice'-classit
'src/rooms.py' - 'Room'-class: items, enemies, NPCs, descriptions ja interactions
'src/combat.py' - Turn-based fighting: attack, take damage, escape
'src/endings.py' - Checks pelin kolme end conditionia
'src/save_manager.py' - Saving ja loading pelille 'saves.json'-tiedostoon/tiedostosta (JSON format)
'src/intro.py' - Intro ja instruction tekstit, jotka näytetään startupissa

KEY MECHANICS

* Dice rolls DND-style: pelaajan attack damage on roll kuusisivuisella nopalla 'Dice.roll', ja menu tarjoaa myös free d20 rollin. 'Dice'-class tukee mitä tahansa sivumäärää, multiple dicejä, modifiereita sekä advantage/disadvantage rolleja.
* Combat: fightissa pelaaja valitsee 'Attack' tai 'Run' jokaisella turnilla. Enemies counterattackaavat fixed attack powerilla (Night Walker 5, White Walker 4). Defeated enemy poistetaan roomistaan. Dying ei enää endaa koko peliä välittömästi – ending check käsittelee sen seuraavalla loopilla.
* Inventory weight limitillä: jokaisella itemillä on weight, ja pelaaja voi kantaa enintään 100 unitia. Itemit, jotka ovat too heavy, ei voi pickata up, ja thrown-away itemit ovat gone forever.
* Rooms ja interactions: jokaisella roomilla on description ja siellä voi olla item, enemy, NPC ja special interactions (esimerkiksi "inspect shackles" tai "touch runes").
* Saving: game state (player, room, inventory, room items, enemy HP) tallennetaan human-readable JSON fileen.

FUNCTIONALITIES

Main menu tarjoaa seuraavat actionit:

1. Roll a dice (d20)
2. Stats – name, age, HP ja health status (Full Health / Injured / Critical / Dead)
3. Move – travel mihin tahansa viidestä roomista (Dungeon Cell, Ancient library, Mystical vault, Guard post, Hallway)
4. Rest – fully restore HP
5. Exit the game
6. Show inventory
7. Throw an item out (destroys permanently ja frees up weightiä)
8. Take the item lying in the current room
9. Check HP
10. Inspect the current room
11. Interact with the room e.g. search the table Guard postissa, mikä voi johtaa Ending 2:teen
12. Save game
13. Load game
14. Fight the enemy in the current room

Lisätiedot:
Siirtyminen huoneeseen, jossa on vihollinen, tarjoaa automaattisesti taistelua.
Pelaaja voi aina 'Juosta' (Run) pois taistelusta.
Tunnettu rajoitus: parannusjuoma (healing potion) on olemassa esineenä, mutta sen käyttöä ei ole vielä yhdistetty valikkoon – HP palautetaan tällä hetkellä vain lepäämällä.

KESTÄVÄ KEHITYS

Kestävä kehitys on otettu huomioon useilla tavoilla:
Ekologinen: Toimii kevyellä tekstillä ilman grafiikkaa tai verkkoyhteyden tarvetta, mikä säästää energiaa.
Sosiaalinen: Ikäraja 12+, ja tarjoaa rauhanomaisia voittoehtoja ilman väkivallan ihannointia.
Taloudellinen: Nollabudjetin lisenssi- tai ylläpitokustannukset, koska ulkoisia riippuvuuksia ei ole.
Tekninen: Modulaarinen rakenne, selkeät docstring-dokumentaatiot ja yksinkertainen koodi.
Tietovastuu: Säilyttää pelaajan nimen, iän ja edistymisen tiukasti paikallisesti standardissa JSON-muodossa.