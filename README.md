# Ezan Vakti ve İftar Hesaplama Aracı
Bu Python betiği, verilen bir şehir için ezan vaktini ve iftar zamanını hesaplamak için kullanılır. Ayrıca, çalışma saatlerinin sonuna kalan süreyi de hesaplayabilir.

## Kurulum
Bu betiği kullanabilmek için öncelikle Python 3 ve gerekli paketlerin kurulu olması gerekmektedir. Gerekli paketler aşağıdaki gibi yüklenir:

``
pip install requests colorama
``
## Kullanım
Betik, konsol üzerinden çalıştırılır ve bazı komut satırı argümanları alır. Temel kullanım şu şekildedir:

`python ezan_vakti_iftar.py --city <şehir_adı> --end-hour <iş_bitiş_saati> [-j] [-i]`


--city: Ezan vakitlerini ve iftar zamanlarını almak istediğiniz şehrin adı.

--end-hour: Çalışma saatlerinin sonunu belirten saati belirtir. Format: HH:MM

-j: Çalışma saatlerinin sonuna kalan süreyi gösterir.

-i: İftara kalan süreyi gösterir.

Örneğin:

`
python ezan_vakti_iftar.py --city Ankara --end-hour 18:00 -j -i
`

Bu komut, Ankara'da iş bitiş saatini 18:00 olarak alır ve hem iş bitimine kalan süreyi hem de iftar vaktine kalan süreyi ekrana yazdırır.

Örnekler
### Ankara için Ezan Vakti ve İftar Hesaplama
`
python ezan_vakti_iftar.py --city Ankara --end-hour 18:00 -j -i`

### İstanbul için Ezan Vakti ve İftar Hesaplama

`python ezan_vakti_iftar.py --city Istanbul --end-hour 17:30 -i`





# Prayer Time and Iftar Calculation Tool
This Python script is used to calculate the prayer time and iftar time for a given city. Additionally, it can also calculate the remaining time until the end of working hours.

## Installation
To use this script, you need to have Python 3 and the required packages installed. You can install the required packages as follows:
`
pip install requests colorama`

The script is run from the command line and takes some command-line arguments. The basic usage is as follows:

`python ezan_vakti_iftar.py --city <city_name> --end-hour <end_of_work_hour> [-j] [-i] `

--city: Specifies the name of the city for which you want to get the prayer times and iftar times.

--end-hour: Specifies the end of working hours in HH:MM format.

-j: Shows the remaining time until the end of working hours.

-i: Shows the remaining time until iftar.

For example:



`python ezan_vakti_iftar.py --city Ankara --end-hour 18:00 -j -i `

This command takes the end of working hours as 18:00 in Ankara and prints both the remaining time until the end of working hours and the remaining time until iftar.

Examples
### Prayer Time and Iftar Calculation for Ankara

`python ezan_vakti_iftar.py --city Ankara --end-hour 18:00 -j -i `
### Prayer Time and Iftar Calculation for Istanbul


`python ezan_vakti_iftar.py --city Istanbul --end-hour 17:30 -i `


