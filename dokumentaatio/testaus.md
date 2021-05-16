# Testausdokumentti

Ohjelmaa on tetsattu automatisoiduilla luokka testeillä sekä manuallisilla järjestelmätason testeillä

## Luokka testaus

### Sovellus loggikan testit

`Player`-luokka sekä eri vihollis- ja panos- luokat on testattu osittain, muuten testit ovat puutteellisia

### Testauskattavuus

Testattavien asioiden testuskattavuus on 44%

![kattavuus][pic]

# Järjestelmä testaus

Manuaalisina testeinä on testattu kahta asiaa

## Asennus

Sovelluksen asennus on testattu ohjeiden mukaisesti Linux- ymäristössä

## Toiminnallisuudet

Sovellusta on testattu käytännössä määrittely dokumetin toimintojen mukaisesti, on myös testattu satunnaisilla syötteillä, mutta rajoittuneen syöte mahdollisuuden takia, mitään vikoja ei ole löytynyt

## Laatuongelmia

 - sovellus ei anna tialnteeseen sopivia virheilmoituksia, sillä niitä ei ole määritelty
 - Follower- tyypin viholliset välillä jäävät jumiin yhdelle linjalle, jossa ne liikkuvat vain ylös alas suunnassa

[pic]:./coveragePic.png
