from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_automobiliaidb import AutomobiliaiDb
from class_autopard import AutoPard
import datetime
sie_metai = datetime.date.today().year


engine = create_engine('sqlite:///automobiliaidb.db')
Session = sessionmaker(bind=engine)
session = Session()
engine2 = create_engine('sqlite:///automobiliai_pardavimui.db')
Session2 = sessionmaker(bind=engine2)
session2 = Session2()

while True:
    prisijungimas = int(input("Pasirinkite veiksmą: \n"
                             "1 - Darbuotojo prisijungimas \n"
                             "2 - Vartotojo prisijungimas \n"))
    if prisijungimas == 1:
        pasirinkimas = int(input("Pasirinkite veiksmą: \n"
                             "--------Automobilių duomenų bazė--------------------\n" 
                             "1 - Įrašyti automobilio duomenis į duomenų bazę \n" 
                             "2 - Peržiūrėti automobilių sąrašą iš duomenų bazės\n"
                             "3 - Ištrinti įrašą iš duomenų bazės\n"
                             "\n--------Parduodamų automobilių parkas--------------------\n"
                             "4 - Pridėti automobilį į parduodamų automobilių parką\n"
                             "5 - Peržiūrėti automobilių parką\n"
                             "6 - Ištrinti parduotą automobilį\n"
                                 ))
        if pasirinkimas == 1:
            marke = input("Įveskite automobilio markę: ")
            modelis = input("Įveskite modelį: ")
            kebulas = input("Įveskite kėbulo tipą (sedanas/kupė/universalas/visureigis): ")
            rida = int(input("Įveskite ridą: "))
            if 150000 >= rida:
                nuvertejimas_rida = 1.5
            elif 150000 < rida <= 250000:
                nuvertejimas_rida = 1.25
            elif rida > 250000:
                nuvertejimas_rida = 1
            variklio_turis = float(input("Įveskite variklio tūrį: "))
            gamybos_metai = int(input("Įveskite gamybos metus: "))
            kuro_tipas = input("Įveskite kuro tipą (benzinas/dyzelinas/elektra): ")
            pavaru_deze = input("Įveskite pavarų dėžės tipą (mechaninė/automatinė): ")
            trukumai = input("Nurodykite automobilio trūkumus (variklio defektas/kėbulo defektai/nėra): ")
            if trukumai == "variklio defektas" and gamybos_metai >= 2015:
                trukumu_verte = 3000
            elif trukumai == "variklio defektas" and gamybos_metai < 2015:
                trukumu_verte = 1500
            elif trukumai == "kėbulo defektai" or trukumai == "kebulo defektai":
                trukumu_verte = 500
            elif trukumai == "nėra" or trukumai == "nera":
                trukumu_verte = 0
            kaina = int(input("Įveskite modelio kainą pagal katalogą: "))
            rinkos_verte = round(kaina * (0.78 * (0.85**(sie_metai - gamybos_metai - 1)))) * \
                           nuvertejimas_rida - trukumu_verte
            automobilis = AutomobiliaiDb(marke, modelis, kebulas, rida, variklio_turis, gamybos_metai, kuro_tipas,
                                  pavaru_deze, trukumai, kaina, rinkos_verte)
            session.add(automobilis)
            session.commit()
            print("--------------")

        if pasirinkimas == 2:
            automobiliai = session.query(AutomobiliaiDb).all()
            print("--------------")
            for automobilis in automobiliai:
                print(automobilis)
            print("--------------")

        if pasirinkimas == 3:
            automobiliai = session.query(AutomobiliaiDb).all()
            print("--------------")
            for automobilis in automobiliai:
                print(automobilis)
            print("--------------")
            auto_id = int(input("Pasirinkite norimą ištrinti ID: "))
            trinamas_id = session.query(AutomobiliaiDb).get(auto_id)
            session.delete(trinamas_id)
            session.commit()

        if pasirinkimas == 4:
            marke = input("Įveskite automobilio markę: ")
            modelis = input("Įveskite modelį: ")
            kebulas = input("Įveskite kėbulo tipą (sedanas/kupė/universalas/visureigis): ")
            rida = int(input("Įveskite ridą: "))
            if 150000 >= rida:
                nuvertejimas_rida = 1.5
            elif 150000 < rida <= 250000:
                nuvertejimas_rida = 1.25
            elif rida > 250000:
                nuvertejimas_rida = 1
            variklio_turis = float(input("Įveskite variklio tūrį: "))
            gamybos_metai = int(input("Įveskite gamybos metus: "))
            kuro_tipas = input("Įveskite kuro tipą (benzinas/dyzelinas/elektra): ")
            pavaru_deze = input("Įveskite pavarų dėžės tipą (mechaninė/automatinė): ")
            trukumai = input("Nurodykite automobilio trūkumus (variklio defektas/kėbulo defektai/nėra): ")
            if trukumai == "variklio defektas" and gamybos_metai >= 2015:
                trukumu_verte = 3000
            elif trukumai == "variklio defektas" and gamybos_metai < 2015:
                trukumu_verte = 1500
            elif trukumai == "kėbulo defektai" or trukumai == "kebulo defektai":
                trukumu_verte = 500
            elif trukumai == "nėra" or trukumai == "nera":
                trukumu_verte = 0
            kaina = int(input("Įveskite modelio kainą pagal katalogą: "))
            rinkos_verte = round(kaina * (0.76 * (0.85**(sie_metai - gamybos_metai - 1)))) * \
                           nuvertejimas_rida - trukumu_verte
            automobiliai_pardavimui = AutoPard(marke, modelis, kebulas, rida, variklio_turis, gamybos_metai, kuro_tipas,
                                  pavaru_deze, trukumai, kaina, rinkos_verte)
            session2.add(automobiliai_pardavimui)
            session2.commit()
            print("--------------")

        if pasirinkimas == 5:
            automobiliai_pardavimui = session2.query(AutoPard).all()
            print("--------------")
            for automobilis in automobiliai_pardavimui:
                print(automobilis)
            print("--------------")

        if pasirinkimas == 6:
            automobiliai_pardavimui = session2.query(AutoPard).all()
            print("--------------")
            for automobilis in automobiliai_pardavimui:
                print(automobilis)
            print("--------------")
            auto_id = int(input("Pasirinkite norimą ištrinti ID: "))
            trinamas_id = session2.query(AutoPard).get(auto_id)
            session2.delete(trinamas_id)
            session2.commit()

    if prisijungimas == 2:
        pasirinkimas = int(input("Pasirinkite veiksmą: \n"
                             "1 - Noriu parduoti automobilį \n" 
                             "2 - Peržiūrėti automobilių sąrašą \n"
                             "3 - Noriu gauti paskolą automobiliui \n"))
        if pasirinkimas == 1:
            marke = input("Įveskite automobilio markę: ")
            modelis = input("Įveskite modelį: ")
            kebulas = input("Įveskite kėbulo tipą: ")
            rida = int(input("Įveskite ridą: "))
            variklio_turis = float(input("Įveskite variklio tūrį: "))
            gamybos_metai = int(input("Įveskite gamybos metus: "))
            kuro_tipas = input("Įveskite kuro tipą (benzinas/dyzelinas/elektra): ")
            pavaru_deze = input("Įveskite pavarų dėžės tipą (mechaninė/automatinė): ")
            trukumai = input("Nurodykite automobilio trūkumus (variklio defektas/kėbulo defektai/nėra): ")
            paieska = session.query(AutomobiliaiDb).filter(AutomobiliaiDb.marke.ilike(marke),
                                                      AutomobiliaiDb.modelis.ilike(modelis),
                                                      AutomobiliaiDb.kebulas.ilike(kebulas),
                                                      AutomobiliaiDb.variklio_turis == variklio_turis,
                                                      AutomobiliaiDb.gamybos_metai.ilike(gamybos_metai),
                                                      AutomobiliaiDb.kuro_tipas.ilike(kuro_tipas),
                                                      AutomobiliaiDb.pavaru_deze.ilike(pavaru_deze))
            for vartotojo_automobilis in paieska:
                kaina = vartotojo_automobilis.kaina
                if trukumai == "variklio defektas" and gamybos_metai >= 2015:
                    trukumu_verte = 3000
                elif trukumai == "variklio defektas" and gamybos_metai < 2015:
                    trukumu_verte = 1500
                elif trukumai == "kėbulo defektai" or trukumai == "kebulo defektai":
                    trukumu_verte = 500
                elif trukumai == "nėra" or trukumai == "nera":
                    trukumu_verte = 0
                if 150000 >= rida:
                    nuvertejimas_rida = 1.5
                elif 150000 < rida <= 250000:
                    nuvertejimas_rida = 1.25
                elif rida > 250000:
                    nuvertejimas_rida = 1
                rinkos_verte = round(kaina * (0.76 * (0.85 ** (sie_metai - gamybos_metai - 1)))) * \
                               nuvertejimas_rida - trukumu_verte
                print(f"\nJūsų automobilis {marke} {modelis} šiai dienai vertas {rinkos_verte} EUR\n")

        if pasirinkimas == 2:
            automobiliai_pardavimui = session2.query(AutoPard).all()
            print("--------------")
            for automobilis in automobiliai_pardavimui:
                print(automobilis)
            print("--------------")

        if pasirinkimas == 3:
            while True:
                paskolos_suma = int(input("Įveskite paskolos sumą: "))
                paskolos_terminas = int(input("Įveskite paskolos terminą (mėnesiais): "))
                darbo_trukme = input("Ar šiuo metu esate dirbantis ir dabartinėje darbovietėje dirbate ilgiau nei 4 "
                                     "mėnesius?(Taip/Ne): ")
                if darbo_trukme == "Ne":
                    print("Jūsų darbo stažas neatitinka paskolos suteikimui keliamų reikalavimų! "
                          "Privalote išdirbti ne mažiau kaip 4 mėn. toje pačioje darbovietėje. \n")
                    break
                pajamos = int(input("Nurodykite savo mėnesinių pajamų dydį: "))
                islaidos = int(input("Nurodyktie savo mėnesinių išlaidų dydį: "))
                paskolos_terminas_metais = float(paskolos_terminas / 12)
                metine_palukanu_norma = (paskolos_suma * 0.06) * paskolos_terminas_metais
                sutarties_sudarymo_mokestis = paskolos_suma * 0.04
                menesinis_administravimo_mokestis = (paskolos_suma * 0.004) * paskolos_terminas
                grazintina_suma = paskolos_suma + metine_palukanu_norma + sutarties_sudarymo_mokestis \
                                  + menesinis_administravimo_mokestis
                menesio_imokos_dydis = grazintina_suma / paskolos_terminas
                ar_virsija_pajamas = pajamos * 0.4
                print("--------------")
                if ar_virsija_pajamas < islaidos + menesio_imokos_dydis:
                    print("\nJūsų turimų įsipareigojimų dydis viršija nustatytą normą (40% visų pajamų) "
                          "ir paskola Jums negali būti suteikta!\n")
                    break
                elif ar_virsija_pajamas > islaidos + menesio_imokos_dydis:
                    print(f"\nSveikiname! Jums gali būti suteikta {paskolos_suma} EUR paskolos suma {paskolos_terminas}"
                          f" mėn. terminui. Bendra grąžintina paskolos suma: {grazintina_suma} EUR, "
                          f"mėnesinių įmokų dydis: {round(menesio_imokos_dydis, 2)} EUR/mėn.\n")
                    break
