# NS-Consumenten-zuil-server

## Inhoudsopgave 
* [Algemene informatie](#algemene-informatie)
* [Technologieën](#technologieën)
* [Setup](#setup)
* [Handleiding](#handleiding)
* [Auteur](#auteur)
* [Licentie](#licentie)

## Algemene informatie
Dit project is een eindopdracht van periode A 2020 op de opleiding HBO ICT.

Het doel van het project is om een applicatie te schrijven er feedback kan worden gegeven, en die feedback kan worden beoordeeld.
Ook kan de feedback worden gezet op Twitter doormiddel van een API.
	
## Technologieën
Project is voornamelijk gemaakt met:
* Python
* Postgresql
* Flask
* Pipenv
  
## Setup
De applicatie gebruikt dbconfig.properties om de gevoelige data zoals keys en wachtwoorden op te slaan.
Deze moet in de root van het project.
Een voorbeeld hiervan is:

dbconfig.properties
```
 # DB Properties
 db.username=postgres
 db.password=wachtwoord
 db.host=localhost
 db.database=ns_zuil_school
 db.port=5432
 
 # Twitter Properties
 twitter.public_key=key
 twitter.secret_key=key
 twitter.acces_token=key
 twitter.secret_acces_token=key
```

De dependicies worden door Pipenv geregeld.
In de Pipfile en Pipfile.lock worden deze bijgehouden.

De debug.html file is een bestand waarmee je POST requests kan sturen naar de server. Deze worden ook ontvangen, en is makkelijker dan de Flutter programma te bouwen.

## Handleiding
Het project gebruikt Pipenv, hierdoor zijn de dependicies geregeld.
Activeer pipenv door pipenv shell uit te voeren:
```
$ pipenv shell
```

Daarna kan je het programma gebruiken
```
$ python main.py
```

Dit geeft de arguments van het programma aan.
Om een gebruiker toe te voegen moet je dit invoeren:
```
$ python main.py user
```

Om een review toe te voegen voer je het volgende in:
```
$ python main.py review
```

## Auteur 
* Daan Roth | 1782443 | [Appenzeill](https://github.com/Appenzeill) | Daanroth@protonmail.com

## Licentie

Dit project heeft de GNU General Public Licentie v3 [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
