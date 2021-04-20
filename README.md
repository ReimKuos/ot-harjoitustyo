# Avaruus peli

Sovellus on peli, jossa lennetään avaruudessa, väistelään vihollisia ja kerätään pisteitä tuhoamalla niitä.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.8.5`

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```


