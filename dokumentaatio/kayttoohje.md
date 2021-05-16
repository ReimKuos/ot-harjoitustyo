# Asennus ja Käyttöohje

## Asennus

### Tarvittavat kirjastot

Standardi kirjastojen lisäksi sovellus hyödyntää pygame- kirjastoa tämän saa asennettua komennolla:

```bash
pip install pygame
```

### Ohjelmiston asennus

Riippuvuudet saadaan asennettua komennolla:

```bash
poetry install
```

Ja peli saadaan tämän jälkeen Käynnistettyä komennolla:

```bash
poetry run invoke start
```

## Yleistä
- Pelin voi sulkea aina ESC-näppäimellä tai ruudun yläkulmasta

## Alkunäyttö
- Toiminnot
    - Ylös- ja alas-näppäimillä voi siirtyä eri valintojen kohdalle
    - SPACE valitsee valitun kohdan
    - EXIT-kohta sulkee pelin
    - START-kohta aloittaa pelin
    - SCORE- kohta siirtyy score näytölle mistä näkee kymmenen parasta tulosta (SPACE-näppäin paluttaa käyttäjän aloitusnäytölle)

- Puuttellisuudet
    - Tällä hetkellä osoitin on hiemmä planeetta oikean kuvan puutteetn takia

## Pelissä

- Alus liikkuu WASD-näppäimillä tai nuolinäppäimillä
- Alus ampuu SPACE-näppäimellä

- Näytölle ilmestyy vihollisa, joita voi tuhota ampumalla niitä, jolloin ne antavat pisteitä
- Jos vihollinen tai sen panos koskettaa pelaajaa tuhoutuu pelaaja automaattisesti, tällöin uuden pelin voi aloitta R-näppäimellä ja T-näppäimellä voi siirtyä aloitusnäytölle

## Muut komentolinjan komennot

Testien suoritus tapahtuu komennolla 

```bash
poetry run invoke test
```

Tetsikattavuus saadaan komennolla (hakemistona _htmlcov_)

```bash
poetry run invoke test
```

Pylint- tarkistus

```bash
poetry run invoke lint
```

