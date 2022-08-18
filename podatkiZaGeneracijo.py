import random
imenaPostaj = ["'Ljubljana'", "'Celje'", "'Kranj'", "'Koper'", 
                    "'Velenje'", "'Novo_mesto'", "'Ptuj'", "'Trbovlje'", 
                    "'Kamnik'", "'Nova_Gorica'", "'Jesenice'", "'Domžale'", 
                    "'Škofja_Loka'", "'Izola'", "'Murska_Sobota'", "'Postojna'", 
                    "'Logatec'", "'Vrhnika'", "'Kočevje'"]

proga1 = ["'Jesenice'", "'Kranj'", "'Škofja_Loka'", "'Ljubljana'"]
razdalja1 = [35, 12, 23]

proga2 = ["'Koper'", "'Postojna'", "'Logatec'","'Vrhnika'", "'Ljubljana'"]
razdalja2 = [60, 27,10,32]

proga3 = ["'Murska_Sobota'", "'Ptuj'", "'Celje'", "'Trbovlje'", "'Ljubljana'"]
razdalja3 = [5, 7, 7, 8]

proga4 = ["'Domžale'", "'Kočevje'", "'Novo_mesto'", "'Ljubljana'"]
razdalja4 = [75, 47, 70]

proga5 = ["'Velenje'", "'Kamnik'", "'Ljubljana'", "'Nova_Gorica'", "'Izola'"]
razdalja5 = [57, 23, 106, 81]



proge = [proga1, proga2, proga3, proga4, proga5]
razdalje = [razdalja1, razdalja2, razdalja3, razdalja4, razdalja5]

imena = ["'Franc'",
"'Marija'",
"'Janez'",
"'Ana'",
"'Marko'",
"'Maja'",
"'Ivan'",
"'Irena'",
"'Anton'",
"'Mojca'",
"'Andrej'",
"'Mateja'",
"'Jožef'",
"'Nina'",
"'Jože'",
"'Nataša'",
"'Luka'",
"'Andreja'",
"'Peter'",
"'Barbara'",
"'Marjan'",
"'Jožica'",
"'Matej'",
"'Petra'",
"'Tomaž'",
"'Eva'",
"'Milan'",
"'Anja'",
"'Aleš'",
"'Katja'",
"'Branko'",
"'Sara'"]

priimki = ["'Novak'",
"'Horvat'",
"'Kovačič'",
"'Krajnc'",
"'Zupančič'",
"'Potočnik'",
"'Kovač'",
"'Mlakar'",
"'Vidmar'",
"'Kos'",
"'Golob'",
"'Turk'",
"'Kralj'",
"'Božič'",
"'Korošec'",
"'Bizjak'",
"'Zupan'",
"'Hribar'",
"'Kotnik'",
"'Rozman'",
"'Kavčič'",
"'Kastelic'",
"'Oblak'",
"'Hočevar'",
"'Petek'",
"'Kolar'",
"'Žagar'",
"'Košir'",
"'Koren'",
"'Klemenčič'"]

nazivi = ["'strojnik'", "'strojevodja'", "'prometnik'"]

naselja = ["'Beričevo'",
"'Brinje'",
"'Dol pri Ljubljani'",
"'Kleče pri Dolu'",
"'Ljubljana '",
"'Allendejeva ulica'",
"'Apihova ulica'",
"'Avčinova ulica'",
"'Avšičeva cesta '",
"'Belokranjska ulica'",
"'Bevkova cesta'",
"'Bežigrad'",
"'Blasnikova ulica'",
"'Blasov breg'",
"'Borutova ulica'",
"'Brankova ulica'",
"'Bratinova ulica'",
"'Bratov Čebuljev ulica'",
"'Bratov Jakopičev ulica'",
"'Bratov Kunovarjev ulica'",
"'Bratovševa ploščad'",
"'Brnčičeva ulica'",
"'Carja Dušana ulica'",
"'Celestinova ulica'",
"'Celjska ulica'",
"'Cerkova ulica'",
"'Cesta Ceneta Štuparja'",
"'Cesta na Brod'",
"'Cesta Urške Zatlerjeve '",
"'Cesta v Pečale'",
"'Cesta v Podboršt'",
"'junija'",
"'Čolnarjeva ulica'",
"'Čargova ulica'",
"'Čemažarjeva ulica'",
"'Čerinova ulica'",
"'Črnuška cesta'",
"'Črtomirova ulica'",
"'Dajnkova ulica'",
"'Danile Kumarjeve ulica'",
"'Dečkova ulica'",
"'Dečmanova ulica'",
"'Dermotova ulica'",
"'Detelova ulica'",
"'Dimičeva ulica'",
"'Dolina'",
"'Dravska ulica'",
"'Dunajska cesta '",
"'Einspielerjeva ulica'",
"'Endliherjeva ulica'",
"'Fabianijeva ulica'",
"'Forsterjeva ulica'",
"'Franketova ulica'",
"'Funtkova ulica'",
"'Gača'",
"'Gameljska cesta'",
"'Glavarjeva ulica'",
"'Glinškova ploščad'",
"'Godeževa ulica'",
"'Gogalova ulica'",
"'Golarjeva ulica'",
"'Gorjančeva ulica'",
"'Goropečnikova ulica'",
"'Grafenauerjeva ulica'",
"'Grassellijeva ulica'",
"'Grintovška ulica'",
"'Hacquetova ulica'",
"'Herbersteinova ulica'",
"'Hlebčeva ulica'",
"'Hranilniška ulica'",
"'Hribernikova ulica'",
"'Hribovska pot'",
"'Hubadova ulica'",
"'Ilešičeva ulica'",
"'Ipavčeva ulica'",
"'Izletniška ulica'",
"'Jakšičeva ulica'",
"'Janova ulica'",
"'Janševa ulica'",
"'Jarnikova ulica'",
"'Jarše'",
"'Jarška cesta '",
"'Jazbečeva pot'",
"'Ježa'",
"'Ježica'",
"'Kadilnikova ulica'",
"'Kalingerjeva ulica'",
"'Kališnikov trg'",
"'Kamniška ulica'",
"'Katreževa pot'",
"'Kerševanova ulica'",
"'Kleče'",
"'Kočenska ulica'",
"'Kolarjeva ulica'",
"'Komanova ulica'",
"'Koroška ulica'",
"'Kosova ulica'",
"'Koželjeva ulica'",
"'Kraljeva ulica'",
"'Kranjčeva ulica'",
"'Kratka pot'",
"'K reaktorju'",
"'Kregarjeva ulica'",
"'Kržičeva ulica'",
"'Kumrovška ulica'",
"'Kurilniška ulica '",
"'Kušarjeva ulica'",
"'Kuzmičeva ulica'",
"'Lambergarjeva ulica'",
"'Lavričeva ulica'",
"'Lemeževa ulica'",
"'Likozarjeva ulica'",
"'Linhartova cesta'",
"'Linhartov podhod'",
"'Livarska ulica'",
"'Ložarjeva ulica'",
"'Luize Pesjakove ulica'",
"'Lužiško-srbska ulica'",
"'Magajnova ulica'",
"'Majaronova ulica'",
"'Mala vas'",
"'Mariborska ulica'",
"'Marice Kovačeve ulica'",
"'Maroltova ulica '",
"'Mašera-Spasičeva ulica'",
"'Matjaževa ulica'",
"'Med hmeljniki'",
"'Meškova ulica'",
"'Mire Lenardičeve ulica'",
"'Mislejeva ulica'",
"'Mlinska pot'",
"'Mucherjeva ulica'",
"'Na brežini'",
"'Nade Ovčakove ulica'",
"'Nadgoriška cesta'",
"'Na produ'",
"'Na Žalah'",
"'Neubergerjeva ulica'",
"'Novakova ulica'",
"'Novinarska ulica'",
"'Obvozna cesta'",
"'Ocvirkova ulica'",
"'Ogrinčeva ulica'",
"'Okrogarjeva ulica'",
"'Omahnova ulica'",
"'Pahorjeva ulica'",
"'Palmejeva ulica'",
"'Parmova ulica '",
"'Pasterkova pot'",
"'Pavlovčeva ulica'",
"'Pečarjeva ulica'",
"'Pečnik'",
"'Pegamova ulica'",
"'Peričeva ulica'",
"'Perkova ulica'",
"'Petkova ulica'",
"'Petričeva ulica'",
"'Pionirska pot'",
"'Planinska cesta'",
"'Pleteršnikova ulica'",
"'Pod bregom'",
"'Podgorica'",
"'Pod gričem'",
"'Pod klancem'",
"'Podmilščakova ulica'",
"'Polanškova ulica'",
"'Popovičeva ulica'",
"'Posavskega ulica'",
"'Pot Draga Jakopiča'",
"'Pot k Savi'",
"'Pot k sejmišču'",
"'Pot v Čeželj'",
"'Pot v Goričico'",
"'Pot v Hrastovec'",
"'Pot v hribec'",
"'Pot v Mlake'",
"'Pot v Smrečje'",
"'Prekmurska ulica'",
"'Preradovičeva ulica'",
"'Presetnikova ulica'",
"'Pribinova ulica'",
"'Primožičeva ulica'",
"'Pšatska pot'",
"'Ptujska ulica'",
"'hercegovske divizije)'",
"'Raičeva ulica'",
"'Ravbarjeva ulica'",
"'Reboljeva ulica'",
"'Robbova ulica'",
"'Robičeva ulica'",
"'Rodičeva ulica'",
"'Rožanska ulica'",
"'Samova ulica'",
"'Saveljska cesta '",
"'Savlje'",
"'Savska cesta '",
"'Selanova ulica'",
"'Seliškarjeva ulica'",
"'Simončičeva ulica'",
"'Slovenčeva ulica'",
"'Smoletova ulica'",
"'Soteska pot'",
"'Sovretova ulica'",
"'Stadionska ulica'",
"'Staničeva ulica'",
"'Stara Ježica'",
"'Stare Črnuče'",
"'Stolpniška ulica'",
"'Stoženska ulica'",
"'Stožice'",
"'Strmec'",
"'Strniševa cesta'",
"'Suhadolčanova ulica'",
"'Svetosavska ulica'",
"'Šarhova ulica'",
"'Šentjakob'",
"'Šerkova ulica'",
"'Šifrerjeva ulica'",
"'Šlandrova ulica'",
"'Štajerska cesta '",
"'Štebijeva cesta'",
"'Štembalova ulica'",
"'Štihova ulica'",
"'Tesovnikova ulica'",
"'Tolstojeva ulica'",
"'Tomačevo'",
"'Tomačevska cesta'",
"'Tominškova ulica'",
"'Topniška ulica'",
"'Trebinjska ulica'",
"'Triglavska ulica'",
"'Trstenjakova ulica'",
"'Turnerjeva ulica'",
"'Udvančeva ulica'",
"'Ulica aktivistov'",
"'Ulica bratov Židan'",
"'Ulica Koroškega bataljona'",
"'Ulica Majke Jugovičev'",
"'Ulica Metoda Mikuža'",
"'Ulica nadgoriških borcev'",
"'Ulica padlih borcev'",
"'Ulica Pavle Jeromnove'",
"'Ulica Pohorskega bataljona'",
"'Ulica prvoborcev'",
"'Ulica Staneta Severja'",
"'Ulica v Kokovšek'",
"'Valjhunova ulica'",
"'V dolini'",
"'Velikovška ulica'",
"'Verdnikova ulica'",
"'Vilharjeva cesta '",
"'Vodovodna cesta '",
"'Hošiminhova ulica'",
"'Vrbovec'",
"'Vurnikova ulica'",
"'V Varde'",
"'Za gasilskim domom'",
"'Zagrebška ulica'",
"'Zajčeva pot'",
"'Za partizanskim domom'",
"'Zasavska cesta'",
"'Ziljska ulica'",
"'Zupanova ulica'",
"'Žolgerjeva ulica'",
"'Žorgova ulica'"]

komentarji = ["'Še eno jutro sivo bedno'",
"'dež in megla tak kot vedno'",
"'ura glih odbila sedem je preč'",
"'Na ulicah kolone'",
"'tip v avtu živčno kolne še en dan ko čisto vsem je odveč'",
"'Medtem ko zmerjajo se s klinci'",
"'vneto mahajo z sredinci jaz z nasmehom na obrazu grem naprej'",
"'Ker dans ni službe ne opravkov'",
"'pošte'",
"'banke'",
"'ne sestankov'",
"'danes sem uzel si frej'",
"'Danes ne zanima me politika'",
"'kultura'",
"'novice'",
"'točna ura in humor'",
"'Korakam v ritmu pesmi'",
"'v levi štrik'",
"'žiletka v desni'",
"'ker danes je dan za samomor'",
"'Nič več položnic plačevanja'",
"'hipotek na stanovanja'",
"'kreditov'",
"'šefov'",
"'delovnih sobot'",
"'Ker bol kot jaz živim življenje se zdi'",
"'da ono živi mene in danes čas je da zaključim pot'",
"'Nic več mačkov in bolezni'",
"'neuslišanih ljubezni'",
"'življenskih uprašanj in dilem'",
"'Težka odločitev al naj uporabim britev ali rajši špago moj bo zadni problem'",
"'Danes me ne briga naj bo hrast ali pa lipa'",
"'kostanj'",
"'breza'",
"'oreh smreka ali bor'",
"'Da le je veja dost rejena za težo mojega življenja'",
"'ker danes je dan za samomor'",
"'Sn štrik naštimo'",
"'ga prvezo'",
"'vzel žiletko v krošnjo splezo'",
"'Se v vetru veja zamajala je da glih žilo sn sfaliu'",
"'Sn tok v afektu se razjezo'",
"'da sn z žileto štrik prerezo in prleto dol na tla polomljen'",
"'in sumljivo živ'",
"'Morda pa jutri bo uspelo'",
"'čeprav se komu lohk se zdelo'",
"'da sem nesposoben tolko kot sem nor'",
"'A če pomislim res ne vem a v meni je problem'",
"'al pa v tem da dans ni dan za samomor'"]

vozovnicaId = [1,2,3,4, 5]
vozovnicaIme = ["'Yearly'", "'Pensioner'", "'Monthly'", "'Student'", "'Dnevna'"]
vozovnicaCena = [120, 20, 30, 15, 0]
vozovnicaOpis = ["'Celoletna vozovnica. Velja po celi Sloveniji.'", "'Celoletna vozovnica. Velja po celi Sloveniji.'", "'Mesečna vozovnica. Velja po celi Sloveniji.'", "'Celoletna vozovnica. Velja po celi Sloveniji'", "'Dnevna vozovnica. Cena je odvisna od relacije.'"]
vozovnicaVelja = [365, 1000000, 30, 365, 0]


def randomInt():
    return random.randint(0, 1000)

