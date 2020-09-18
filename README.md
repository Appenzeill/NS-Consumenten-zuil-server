# NS-Consumenten zuil

Simple overview of use/purpose.

## Beschrijving

An in-depth paragraph about your project and overview of use.

## Aanleiding
De Nederlandse Spoorwegen vinden het erg belangrijk dat zij goed kunnen communiceren met hun klanten én van hun klanten goede of minder goede ervaringen horen. Daarom houden ze van tijd tot tijd een enquête onder de reizigers. Het nadeel van een enquête is dat het lang duurt voordat je de resultaten krijgt. De NS heeft gemerkt dat Twitter veel sneller werkt. Het lijkt de directie daarom een goed plan dat klanten hun opmerkingen/complimenten via een computer, aanwezig op elk het station, kunnen invoeren en dat deze opmerkingen dan zichtbaar worden in die stationshal.

De directie is echter ook wel een beetje bang voor Twitter, want men heeft gemerkt dat het ook gebruikt kan worden als uitlaatklep voor ontevreden reizigers. Daarom is het belangrijk dat de inhoud van de Tweets worden gelezen voordat ze worden gepost op Twitter en zichtbaar worden in de stationshal. Op deze manier kunnen respectloze uitingen en bijvoorbeeld schuttingstaal eruit gefilterd worden.

## Opdracht
De opdracht die jij krijg om dit uit te werken, luidt: ontwerp en bouw een systeem met behulp van Twitter waarbij de mening van klanten zichtbaar wordt voor andere reizigers.

Hiervoor gelden onderstaande eisen:

## Eisen voor het systeem
Om dit idee concreet te maken, denkt men aan de volgende systeemeisen (requirements):

1. Op een computerzuil  (module 1) op een willekeurig NS-station kunnen mensen hun berichtje (hun Tweet) van maximaal 140 karakters invoeren. Dit bericht wordt in een database opgeslagen met de datum en een eventuele naam. Als deze leeg is wordt de naam "anoniem" ingevuld.

2. Daarna krijgt een moderator van de NS het berichtje te zien en diegene kan kiezen voor “accept” of “reject”. Bij “reject” wordt een opmerking samen met datum en tijd aan het bericht in de database toegevoegd. De moderator werkt eerst aan het oudste bericht. Bij de NS zijn verschillende moderators. We willen bij een bericht opslaan welke moderator het bericht heeft beoordeeld.

3. Bij “accept” wordt het berichtje op Twitter geplaatst via een twitteraccount. Het account bevat het woord “test” in de naam, want het gaat nu nog om een Proof-of-Concept (PoC).

4. Op een ander scherm worden een aantal van de meest recente Tweets van het account getoond in de stationshal (module 3). Het is belangrijk dat deze Tweets er goed uitzien.

5. Het kan zijn dat er tijdelijk geen Tweets geplaatst worden,  bijvoorbeeld als niemand gedurende een bepaalde tijd een Tweet heeft geplaatst. Zorg ervoor dat je dan het weerbericht laat zien op het scherm in de stationshal.

6. De moderator moet een overzicht kunnen krijgen van de afgekeurde Tweets (module 2)

Uiteindelijk zul je 3 modules en een database gebouwd hebben.

## Eisen aan het ontwerp
Het ontwerp omvat een BPMN-model en Use Case diagram met twee volledig uitgewerkte  Use Cases. Daarnaast is een conceptueel datamodel vereist. Dit model wordt verder uitgewerkt in een logisch en fysiek datamodel.

## Tips voor de realisatie
Maak het bovengenoemde systeem met behulp van Python. Het gebruik van Tkinter kan mooie resultaten opleveren, maar is niet verplicht. Je mag ook gebruik maken van een andere Python GUI library.

Let op: de Twitter-API levert geen XML, maar JSON!

## Technische hulpbronnen
Technische hulpbronnen

Onderstaande technische kennis wordt niet in de lessen MOD en PROG aangeboden. Je zult dit zelf moeten aanleren met de volgende tutorials of handleidingen.

        Voor de database: Python DB koppeling
        Voor het opzetten van een koppeling met Twitter: Twitter API
        Voor een koppeling met het weerbericht, Weer API

### Dependencies

* Pipenv
* Twitter API
* Flask

### Installing



### Executing program

* Activeer pipenv omgeving 
```
pipenv shell
```
* Activeer applicatie
```
python3 app.py
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Auteurs

Contributors names and contact info

[Daan Roth](https://github.com/Appenzeill)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the GPL-3.0 License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
