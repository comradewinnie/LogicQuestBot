import asyncio
from app.database.models import async_main 
import app.database.requests as rq

async def main():
    await async_main()

    # для 7 класса
    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv='Kādai vecai kundzei ļoti patika suņi un kaķi. Kopumā viņai bija <b>desmit</b> mājdzīvnieki.\n\nKādu dienu viņa nolēma viņus visus pabarot ar konfektēm un iedeva 56 gabaliņus. Turklāt mēs zinām, ka viņa <b>katram kaķim iedeva piecus</b> saldumus, bet <b>katram sunim sešus</b>.\n\nCik suņu un cik kaķu viņai bija?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti tādā formā: "<b>2 un 5</b>", ja atbilde ir 2 suņi un 5 kaķi.</i>',
        text_en='An old lady loved dogs and cats. She had <b>ten</b> pets in total.\n\nOne day she decided to feed them all candy and gave them 56 pieces. Furthermore, we know that she gave <b>five</b> sweets to each cat, and <b>six</b> sweets to each dog.\n\nHow many dogs and how many cats did she have?\n\n<i><b>Warning</b></i><i>: Write your answer in the form: "<b>2 and 5</b>", if the answer is 2 dogs and 5 cats.</i>',
        text_ru='Одна старая леди очень любила собак и кошек. Всего у нее было <b>десять</b> питомцев.\n\nОднажды она решила накормить их всех конфетами, и раздала им 56 штук. При этом мы знаем, что каждой кошке она давала по <b>пять</b> конфет, а каждой собаке — по <b>шесть</b>.\n\nСколько у нее было собак и сколько кошек?\n\n<i><b>Важно</b></i><i>: Ответ пиши в такой форме: "<b>2 и 5</b>", если ответ - 2 собаки и 5 кошек.</i>',
        answer_lv="6 un 4",
        answer_en="6 and 4",
        answer_ru="6 и 4",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=6,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Ir trīs istabas. Uz katras no tām durvīm kaut kas rakstīts:\n\nUz pirmās istabas durvīm: <b>"Šajā istabā ir pūķis."</b>\nUz otrās istabas durvīm: <b>"Šajā istabā ir princese."</b>\nUz trešās istabas durvīm: <b>"Pūķis sēž otrajā istabā."</b>\n\nUzrakstītais <b>var būt</b> patiess un <b>var nebūt</b> patiess; tomēr zināms, ka <b>tikai viens</b> no tiem ir patiess.\n\nMēs arī zinām, ka princese ir tikai vienā no istabām, bet <b>pārējās divās ir pūķi</b>.\n\nKurā istabā tad princese sēž?',
        text_en='There are three rooms, and on the door of each of them there is a sign. And this is what is written on the signs:\n\nOn the first: <b>"There is a dragon in this room."</b>\nOn the second: <b>"There is a princess in this room."</b>\nOn the third: <b>"The dragon is in the second room."</b>\n\nWhat is written on these signs <b>may be</b> true, or <b>may not</b>; however, it is known that <b>only one</b> of them is true.\n\nWe also know that the princess is only in one of the rooms, and <b>the other two have dragons</b>.\n\nSo where is the princess?',
        text_ru='Есть три комнаты, на двери каждой из них — табличка. А написано на табличках вот что:\n\nНа первой: <b>«В этой комнате сидит дракон».</b>\nНа второй: <b>«В этой комнате — принцесса».</b>\nНа третьей: <b>«Дракон сидит во второй комнате».</b>\n\nНаписанное на этих табличках <b>может</b> оказаться правдой, а <b>может и нет</b>; известно, однако, что <b>только на одной</b> из них — правда.\n\nА еще мы знаем, что принцесса — лишь в одной из комнат, а <b>в двух других — драконы</b>.\n\nТак в какой же комнате сидит принцесса?',
        answer_lv="1. istabā",
        answer_en="In room 1",
        answer_ru="В 1 комнате",
        choices_lv=["1. istabā", "2. istabā", "3. istabā"],
        choices_en=["In room 1", "In room 2", "In room 3"],
        choices_ru=["В 1 комнате", "Во 2 комнате", "В 3 комнате"],
        points=10,
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv='Es izdomāju divciparu skaitli, lielāku par 10, tad tā ciparu summu sadalīju uz pusēm un paņēmu veselu daļu. Kreisajā pusē tai pierakstīju 20, tad pieskaitīju 59. Pēc tam, izsvītrojot pēdējo ciparu, atkal aprēķināju iegūtā skaitļa ciparu summu. Cik man sanāca?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai vienu ciparu!</i>',
        text_en='I thought of a two-digit number, greater than 10, then divided the sum of its digits in half and took the whole part. I attributed 20 to the left side, then added 59, then crossed out the last digit and again calculated the sum of the digits of the resulting number. What number did I get?\n\n<i><b>Warning</b></i><i>: Write only one number in the answer!</i>',
        text_ru='Я задумал двузначное число, больше, чем 10, потом сумму его цифр поделил пополам и взял целую часть. К ней я приписал слева 20, потом прибавил 59, после чего, вычеркнув последнюю цифру, вновь посчитал сумму цифр полученного числа. Сколько у меня получилось?\n\n<i><b>Важно</b></i><i>: В ответе пиши только одну цифру!</i>',
        answer_lv="8",
        answer_en="8",
        answer_ru="8",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=7,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Miegainajā valstībā visi iedzīvotāji ir sadalīti dienas un nakts ciltīs.\n\nViss, kam tic dienas ciltij piederošie, ir patiesība, ja tajā brīdī viņi ir nomodā; ja viņi guļ, visi viņu uzskati ir nepatiesi. Ar nakts cilti ir otrādi.\n\nTātad, viens miegainās karaļvalsts iedzīvotājs nolēma, ka viņš guļ un pieder dienas ciltij. Ko tad īsti par viņu var pateikt?',
        text_en='In the sleepy kingdom, all the inhabitants are divided into day and night tribes.\n\nEverything that those belonging to the day tribe believe in is true if they are awake at that moment; if they are asleep, all their beliefs are false. With the night tribe, everything is the other way around.\n\nSo, one inhabitant of the sleepy kingdom decided that he was asleep and belonged to the day tribe. But what can be said about him in reality?',
        text_ru='В сонном царстве все жители делятся на дневное и ночное племена.\n\nВсё, во что верят принадлежащие к дневному племени — правда, если в этот момент они бодрствуют; если же они спят, все их убеждения ложны. С ночным племенем всё наоборот.\n\nТак вот, один житель сонного царства решил, будто он спит и принадлежит к дневному племени. А что можно сказать о нем на самом деле?',
        answer_lv="Viņš ir nakts ciltī un neguļ",
        answer_en="He is in the night tribe and doesn't sleep",
        answer_ru="Он в ночном племени и не спит",
        choices_lv=["Viņš ir nakts ciltī un guļ", "Viņš ir dienas ciltī un neguļ", "Viņš ir dienas ciltī un guļ", "Viņš ir nakts ciltī un neguļ"],
        choices_en=["He is in the night tribe and sleeps", "He is in the day tribe and doesn't sleep", "He is in the day tribe and sleeps", "He is in the night tribe and doesn't sleep"],
        choices_ru=["Он в ночном племени и спит", "Он в дневном племени и не спит", "Он в дневном племени и спит", "Он в ночном племени и не спит"],
        points=12,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Ir trīs apgalvojumi:\n\n1) 2. un 3. apgalvojums ir nepatiess.\n2) 1. un 3. apgalvojums ir nepatiess.\n3) 1. un 2. apgalvojums ir nepatiess.\n\nVai vismaz VIENS no tiem var būt patiess?',
        text_en='There are three statements:\n\n1. Statements 2 and 3 are false.\n2. Statements 1 and 3 are false.\n3. Statements 1 and 2 are false.\n\nCan any ONE of them be true?',
        text_ru='Есть три утверждения:\n\n1. Утверждения 2 и 3 ложны.\n2. Утверждения 1 и 3 ложны.\n3. Утверждения 1 и 2 ложны.\n\nМожет ли хотя бы ОДНО из них быть истинным?',
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=4,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Ir trīs apgalvojumi:\n\n1) 2. un 3. apgalvojums ir nepatiess.\n2) 1. un 3. apgalvojums ir nepatiess.\n3) 1. un 2. apgalvojums ir nepatiess.\n\nVai DIVI no tiem var būt patiesi?',
        text_en='There are three statements:\n\n1. Statements 2 and 3 are false.\n2. Statements 1 and 3 are false.\n3. Statements 1 and 2 are false.\n\nCan TWO of them be true?',
        text_ru='Есть три утверждения:\n\n1. Утверждения 2 и 3 ложны.\n2. Утверждения 1 и 3 ложны.\n3. Утверждения 1 и 2 ложны.\n\nМогут ли ДВА из них быть истинными?',
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=8,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Ir trīs apgalvojumi:\n\n1) 2. un 3. apgalvojums ir nepatiess.\n2) 1. un 3. apgalvojums ir nepatiess.\n3) 1. un 2. apgalvojums ir nepatiess.\n\nVai VISI uzreiz var būt patiesi?',
        text_en='There are three statements:\n\n1. Statements 2 and 3 are false.\n2. Statements 1 and 3 are false.\n3. Statements 1 and 2 are false.\n\nCan ALL be true at once?',
        text_ru='Есть три утверждения:\n\n1. Утверждения 2 и 3 ложны.\n2. Утверждения 1 и 3 ложны.\n3. Утверждения 1 и 2 ложны.\n\nМогут ли ВСЕ сразу быть истинными?',
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=10,
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Vai vesela skaitļa kvadrāts var būt pāra, bet nedalāms ar četri?",
        text_en="Can the square of an integer be even but not divisible by four?",
        text_ru="Может ли квадрат целого числа быть чётным, но не делиться на четыре?",
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Es paņēmu nepāra skaitli un kāpināju to kvadrātā. Ja no iegūtā skaitļa atņemšu 1, vai tas dalīsies ar 4?",
        text_en="I took an odd number and squared it. If I subtract 1 from the resulting number, will it be divisible by 4?",
        text_ru="Я взял нечетное число и возвел в квадрат. Если я вычту из полученного числа 1, будет ли оно делиться на 4?",
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Kāds kungs, rādot draugam mākslinieka gleznotu portretu, teica:\nMan nav ne māsu, ne brāļu, bet šī cilvēka tēvs bija mana tēva dēls.\nKas bija attēlots portretā?",
        text_en="A gentleman, showing his friend a portrait painted for him by an artist, said: \nI have neither sisters nor brothers, but this man's father was my father's son.\nWho was depicted in the portrait?",
        text_ru="Один джентльмен, показывая своему другу портрет, нарисованный по его заказу одним художником, сказал:\nУ меня нет ни сестер, ни братьев, но отец этого человека был сыном моего отца.\nКто был изображен на портрете?",
        answer_lv="Šī kunga dēls",
        answer_en="This gentleman's son",
        answer_ru="Сын этого джентльмена",
        choices_lv=["Šī kunga vecvectēvs", "Šī kunga dēls", "Šī kunga vectēvs", "Šī kunga tēvs"],
        choices_en=["This gentleman's great-grandfather", "This gentleman's son", "This gentleman's grandfather", "This gentleman's father"],
        choices_ru=["Прадед этого джентльмена", "Сын этого джентльмена", "Дед этого джентльмена", "Отец этого джентльмена"],
        points=10
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Aizvakar Mašai bija 17 gadi. Nākamgad viņai būs 20 gadi. Kad ir Mašas dzimšanas diena?\n\n<i><b>Atbildes piemērs</b></i><i>: 23. aprīlī</i>",
        text_en="The day before yesterday Masha was 17 years old. Next year she will be 20 years old. When is Masha's birthday?\n\n<i><b>Answer example</b></i><i>: April 23</i>",
        text_ru="Позавчера Маше было 17 лет. В следующем году ей будет 20 лет. Когда у Маши день рождения?\n\n<i><b>Пример ответа</b></i><i>: 23 апреля</i>",
        answer_lv="31. decembrī",
        answer_en="December 31",
        answer_ru="31 декабря",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Tiesas priekšā stāv trīs cilvēki, no kuriem katrs var būt aborigēns vai citplanētietis.\nTiesnesis zina, ka aborigēni vienmēr atbild uz jautājumiem patiesi, bet citplanētieši vienmēr melo. Taču tiesnesis nezina, kurš no viņiem ir aborigēns un kurš citplanētietis.\nViņš jautāja pirmajam, bet viņa atbildi nedzirdēja. Tāpēc viņš vispirms jautā otrajam, bet pēc tam trešajam par to, ko atbildēja pirmais.\n\nOtrais saka, ka pirmais sevi sauca par aborigēnu, trešais - ka pirmais sevi sauca par citplanētieti.\n\nKas bija otrais un trešais apsūdzētie?",
        text_en="Three men stand before a judge, each of whom could be either an aborigine or an alien.\nThe judge knows that aborigines always answer questions truthfully, and aliens always lie. However, the judge does not know which of them is an aborigine and which is an alien.\nHe asked the first one, but did not hear his answer. So he asks first the second, and then the third, what the first one answered.\n\nThe second one says that the first one said he was an aborigine, and the third one says that the first one said he was an alien.\n\nWho were the second and third defendants?",
        text_ru="Перед судом стоят три человека, из которых каждый может быть либо аборигеном, либо пришельцем.\nСудья знает, что аборигены всегда отвечают на вопросы правдиво, а пришельцы всегда лгут. Однако судья не знает, кто из них абориген, а кто — пришелец.\nОн сначала спросил первого, но не расслышал его ответа. Поэтому он спрашивает сначала второго, а потом третьего о том, что ответил первый.\n\nВторой говорит, что первый назвался аборигеном, третий — что первый назвался пришельцем.\n\nКем были второй и третий подсудимые?",
        answer_lv="Otrais ir aborigēns, trešais ir citplanētietis",
        answer_en="The second is an aborigine, the third is an alien",
        answer_ru="Второй - абориген, третий - пришелец",
        choices_lv=["Otrais ir aborigēns, trešais ir citplanētietis", "Otrais ir citplanētietis, trešais ir aborigēns", "Otrais un trešais ir aborigēni", "Otrais un trešais ir citplanētieši"],
        choices_en=["The second is an aborigine, the third is an alien", "The second is an alien, the third is an aborigine", "The second and third are natives", "The second and third are aborigines"],
        choices_ru=["Второй - абориген, третий - пришелец", "Второй - пришелец, третий - абориген", "Второй и третий - аборигены", "Второй и третий - пришельцы"],
        points=12
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Kad trīs draudzenes - Jana, Nastja un Maša - izgāja ārā pastaigāties, viņas bija ģērbušās baltā, sarkanā un zilā kleitās.\n\nViņu kurpes bija tās pašas trīs krāsas, bet tikai Janas <b>kurpju un kleitas krāsas ir vienādas</b>. Tajā pašā laikā Nastjas kleita un kurpes <b>nebija zilas</b>, bet Mašai bija <b>sarkanas kurpes</b>.\n\nNosaki <b>JANAS</b> kurpju un kleitas krāsas.",
        text_en="When three friends - Yana, Nastya and Masha - went out for a walk, they were wearing white, red and blue dresses.\n\nTheir shoes were the same three colors, but only Yana's shoes and dress <b>matched</b>. At the same time, neither Nastya's dress nor shoes <b>were blue</b>, and Masha was <b>wearing red shoes</b>.\n\nDetermine the colors of <b>YANA's</b> shoes and dress.",
        text_ru="Когда три подруги — Яна, Настя и Маша — вышли гулять, на них были белое, красное и синее платья.\n\nТуфли их были тех же трёх цветов, но только у Яны цвета туфель и платья <b>совпадали</b>. При этом у Насти ни платье, ни туфли <b>не были синими</b>, а Маша была <b>в красных туфлях</b>.\n\nОпредели цвета туфель и платья <b>ЯНЫ</b>.",
        answer_lv="Zilas kurpes un zila kleita",
        answer_en="Blue shoes and a blue dress",
        answer_ru="Синие туфли и синее платье",
        choices_lv=["Sarkanas kurpes un sarkana kleita", "Zilas kurpes un zila kleita", "Baltas kurpes un balta kleita"],
        choices_en=["Red shoes and a red dress", "Blue shoes and a blue dress", "White shoes and a white dress"],
        choices_ru=["Красные туфли и красное платье", "Синие туфли и синее платье", "Белые туфли и белое платье"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Kad trīs draudzenes - Jana, Nastja un Maša - izgāja ārā pastaigāties, viņas bija ģērbušās baltā, sarkanā un zilā kleitās.\n\nViņu kurpes bija tās pašas trīs krāsas, bet tikai Janas <b>kurpju un kleitas krāsas ir vienādas</b>. Tajā pašā laikā Nastjas kleita un kurpes <b>nebija zilas</b>, bet Mašai bija <b>sarkanas kurpes</b>.\n\nNosaki <b>NASTJAS</b> kurpju un kleitas krāsas.",
        text_en="When three friends - Yana, Nastya and Masha - went out for a walk, they were wearing white, red and blue dresses.\n\nTheir shoes were the same three colors, but only Yana's shoes and dress <b>matched</b>. At the same time, neither Nastya's dress nor shoes <b>were blue</b>, and Masha was <b>wearing red shoes</b>.\n\nDetermine the colors of <b>NASTYA's</b> shoes and dress.",
        text_ru="Когда три подруги — Яна, Настя и Маша — вышли гулять, на них были белое, красное и синее платья.\n\nТуфли их были тех же трёх цветов, но только у Яны цвета туфель и платья <b>совпадали</b>. При этом у Насти ни платье, ни туфли <b>не были синими</b>, а Маша была <b>в красных туфлях</b>.\n\nОпредели цвета туфель и платья <b>НАСТИ</b>.",
        answer_lv="Baltas kurpes un sarkana kleita",
        answer_en="White shoes and a red dress",
        answer_ru="Белые туфли и красное платье",
        choices_lv=["Sarkanas kurpes un balta kleita", "Baltas kurpes un sarkana kleita"],
        choices_en=["Red shoes and a white dress", "White shoes and a red dress"],
        choices_ru=["Красные туфли и белое платье", "Белые туфли и красное платье"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Kad trīs draudzenes - Jana, Nastja un Maša - izgāja ārā pastaigāties, viņas bija ģērbušās baltā, sarkanā un zilā kleitās.\n\nViņu kurpes bija tās pašas trīs krāsas, bet tikai Janas <b>kurpju un kleitas krāsas ir vienādas</b>. Tajā pašā laikā Nastjas kleita un kurpes <b>nebija zilas</b>, bet Mašai bija <b>sarkanas kurpes</b>.\n\nNosaki <b>MAŠAS</b> kurpju un kleitas krāsas.",
        text_en="When three friends - Yana, Nastya and Masha - went out for a walk, they were wearing white, red and blue dresses.\n\nTheir shoes were the same three colors, but only Yana's shoes and dress <b>matched</b>. At the same time, neither Nastya's dress nor shoes <b>were blue</b>, and Masha was <b>wearing red shoes</b>.\n\nDetermine the colors of <b>MASHA's</b> shoes and dress.",
        text_ru="Когда три подруги — Яна, Настя и Маша — вышли гулять, на них были белое, красное и синее платья.\n\nТуфли их были тех же трёх цветов, но только у Яны цвета туфель и платья <b>совпадали</b>. При этом у Насти ни платье, ни туфли <b>не были синими</b>, а Маша была <b>в красных туфлях</b>.\n\nОпредели цвета туфель и платья <b>МАШИ</b>.",
        answer_lv="Sarkanas kurpes un balta kleita",
        answer_en="Red shoes and a white dress",
        answer_ru="Красные туфли и белое платье",
        choices_lv=["Sarkanas kurpes un balta kleita", "Sarkanas kurpes un zila kleita"],
        choices_en=["Red shoes and a white dress", "Red shoes and a blue dress"],
        choices_ru=["Красные туфли и белое платье", "Красные туфли и синее платье"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Rindā pie skolas kafejnīcas ir Vika, Sofija, Boriss, Deniss un Alla.\n\nVika ir priekšā Sofijai, bet aiz Allas; Boriss un Alla nestāv viens otram blakus; Deniss nav blakus Allai, Vikai vai Borisam.\n\nKādā secībā skolēni stāv?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti ar komatiem, ar atstarpēm, bez punkta beigās!</i>\n<i><b>Atbildes piemērs</b></i><i>: Deniss, Vika, Alla, Sofija, Boriss</i>",
        text_en="Vika, Sonya, Borya, Denis and Alla are standing in line at the school cafeteria.\n\nVika is in front of Sonya, but after Alla; Borya and Alla are not standing next to each other; Denis is not next to Alla, Vika or Borya.\n\nIn what order are the children standing?\n\n<i><b>Warning</b></i><i>: Write your answer separated by commas, with spaces, without a full stop at the end!</i>\n<i><b>Answer example</b></i><i>: Denis, Vika, Alla, Sonya, Borya</i>",
        text_ru="В очереди в школьный буфет стоят Вика, Соня, Боря, Денис и Алла.\n\nВика стоит впереди Сони, но после Аллы; Боря и Алла не стоят рядом; Денис не находится рядом ни с Аллой, ни с Викой, ни с Борей.\n\nВ каком порядке стоят ребята?\n\n<i><b>Важно</b></i><i>: Ответ пиши через запятую, с пробелами, без точки в конце!</i>\n<i><b>Пример ответа</b></i><i>: Денис, Вика, Алла, Соня, Боря</i>",
        answer_lv="Alla, Vika, Boriss, Sofija, Deniss",
        answer_en="Alla, Vika, Borya, Sonya, Denis",
        answer_ru="Алла, Вика, Боря, Соня, Денис",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz salas dzīvo bruņinieki un meļi. Bruņinieki vienmēr saka patiesību, meļi vienmēr melo. Daži iedzīvotāji teica, ka uz salas ir pāra skaits bruņinieku, bet citi teica, ka uz salas ir nepāra skaits meļu. Vai salas iedzīvotāju skaits var būt nepāra?",
        text_en="There are knights and liars on an island. Knights always tell the truth, liars always lie. Some of the inhabitants said that there was an even number of knights on the island, and the rest said that there was an odd number of liars on the island. Can the number of inhabitants on an island be odd?",
        text_ru="На острове живут рыцари и лжецы. Рыцари всегда говорят правду, лжецы всегда лгут. Некоторые жители заявили, что на острове чётное число рыцарей, а остальные заявили, что на острове нечётное число лжецов. Может ли число жителей острова быть нечётным?",
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz galda ir piecas monētas rindā: vidējā ir ar ģerboni uz augšu, bet pārējās ir ar ciparu uz augšu. Ir atļauts vienlaikus apgriezt trīs blakus esošās monētas. Vai ar vairāku šādu apgriezienu palīdzību ir iespējams visas piecas monētas nolikt ar ģerboni uz augšu?",
        text_en="There are five coins in a row on the table: the middle one is heads up, and the rest are tails up. It is allowed to turn over three adjacent coins at the same time. Is it possible to turn all five coins heads up using several such turns?",
        text_ru="На столе лежат в ряд пять монет: средняя — вверх орлом, а остальные — вверх решкой. Разрешается одновременно перевернуть три рядом лежащие монеты. Можно ли при помощи нескольких таких переворачиваний все пять монет положить вверх орлом?",
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=4
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Skolā notika skrējiens, kurā piedalījās 5 sportisti, un katrs ieņēma dažādas vietas (no pirmās līdz piektajai). Kad nākamajā dienā katram jautāja, kuru vietu viņš ieņēma, katrs nosauca vienu skaitli no 1 līdz 5, un visu piecu atbilžu summa bija vienāda ar 22. Kāds bija mazākais meļu skaits, kāds varēja būt starp šiem sportistiem?",
        text_en="There was a race at school with 5 athletes, and they all took different places (from first to fifth). When each of them was asked the next day what place they took, each gave one number from 1 to 5, and the sum of all five answers was 22. What is the smallest number of liars that could have been among these athletes?",
        text_ru="В школе прошёл забег с участием 5 спортсменов, и все заняли разные места (с первого по пятое). Когда на следующий день каждого из них спросили, какое место он занял, каждый назвал одно число от 1 до 5, причём сумма всех пяти ответов оказалась равна 22. Какое наименьшее количество врунишек могло быть среди этих спортсменов?",
        answer_lv="2",
        answer_en="2",
        answer_ru="2",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Divi slēpotāji sacensības uzsāka labā trasē ar ātrumu 12 kilometri stundā. Sākās grūts posms, kurā ātrums nokritās līdz 8 kilometriem stundā. Kad abi slēpotāji iebrauca šajā zonā, attālums starp viņiem bija par 300 metriem mazāks nekā sākumā. Kāds bija attālums starp slēpotājiem sākumā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="Two skiers started a race on a good track at a speed of 12 kilometers per hour. A difficult section began, where the speed dropped to 8 kilometers per hour. When both skiers entered this section, the distance between them was 300 meters less than the initial one. What was the distance between the skiers at the beginning?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="Двое лыжников начали гонку по хорошей лыжне со скоростью 12 километров в час. Начался трудный участок, на котором скорость упала до 8 километров в час. Когда оба лыжника вошли на этот участок, расстояние между ними оказалось на 300 метров меньше первоначального. Каково расстояние между лыжниками было вначале?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="900",
        answer_en="900",
        answer_ru="900",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Abababab cilts alfabētā ir tikai divi burti, un katrs vārds sastāv no astoņiem burtiem. Cik vārdu var būt šīs cilts valodā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="The Abababab tribe's alphabet has only two letters, and each word consists of eight letters. How many words can there be in the language of this tribe?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="В алфавите племени Абабабаб всего две буквы, а каждое слово состоит за восьми букв. Сколько слов может быть в языке этого племени?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="256",
        answer_en="256",
        answer_ru="256",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz galda ir četras kārtis, uz kurām virsū ir rakstīts: “A”, “B”, “4”, “5”. Nav zināms, kas rakstīts kartīšu pretējās pusēs.\n\n<b>Vai ir jāapgriež PIRMĀ kartīte</b>, lai pārbaudītu apgalvojuma “Ja vienā kartītes pusē ir uzrakstīts pāra skaitlis, tad otrā patskaņis” patiesumu?",
        text_en='There are four cards on the table with the following written on the top: "A", "B", "4", "5". What is written on the opposite sides of the cards is unknown.\n\n<b>Should the FIRST card be turned over</b> to check the truth of the statement: "If an even number is written on one side of the card, then a vowel is on the other"?',
        text_ru="На столе лежат четыре карточки, на которых сверху написано: «А», «Б», «4», «5». Что написано на противоположных сторонах карточек, неизвестно.\n\n<b>Нужно ли перевернуть ПЕРВУЮ карточку</b>, чтобы проверить истинность утверждения: «Если на одной стороне карточки написано чётное число, то на другой — гласная буква»?",
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz galda ir četras kārtis, uz kurām virsū ir rakstīts: “A”, “B”, “4”, “5”. Nav zināms, kas rakstīts kartīšu pretējās pusēs.\n\n<b>Vai ir jāapgriež OTRĀ kartīte</b>, lai pārbaudītu apgalvojuma “Ja vienā kartītes pusē ir uzrakstīts pāra skaitlis, tad otrā patskaņis” patiesumu?",
        text_en='There are four cards on the table with the following written on the top: "A", "B", "4", "5". What is written on the opposite sides of the cards is unknown.\n\n<b>Should the SECOND card be turned over</b> to check the truth of the statement: "If an even number is written on one side of the card, then a vowel is on the other"?',
        text_ru="На столе лежат четыре карточки, на которых сверху написано: «А», «Б», «4», «5». Что написано на противоположных сторонах карточек, неизвестно.\n\n<b>Нужно ли перевернуть ВТОРУЮ карточку</b>, чтобы проверить истинность утверждения: «Если на одной стороне карточки написано чётное число, то на другой — гласная буква»?",
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz galda ir četras kārtis, uz kurām virsū ir rakstīts: “A”, “B”, “4”, “5”. Nav zināms, kas rakstīts kartīšu pretējās pusēs.\n\n<b>Vai ir jāapgriež TREŠĀ kartīte</b>, lai pārbaudītu apgalvojuma “Ja vienā kartītes pusē ir uzrakstīts pāra skaitlis, tad otrā patskaņis” patiesumu?",
        text_en='There are four cards on the table with the following written on the top: "A", "B", "4", "5". What is written on the opposite sides of the cards is unknown.\n\n<b>Should the THIRD card be turned over</b> to check the truth of the statement: "If an even number is written on one side of the card, then a vowel is on the other"?',
        text_ru="На столе лежат четыре карточки, на которых сверху написано: «А», «Б», «4», «5». Что написано на противоположных сторонах карточек, неизвестно.\n\n<b>Нужно ли перевернуть ТРЕТЬЮ карточку</b>, чтобы проверить истинность утверждения: «Если на одной стороне карточки написано чётное число, то на другой — гласная буква»?",
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Uz galda ir četras kārtis, uz kurām virsū ir rakstīts: “A”, “B”, “4”, “5”. Nav zināms, kas rakstīts kartīšu pretējās pusēs.\n\n<b>Vai ir jāapgriež CETURTĀ kartīte</b>, lai pārbaudītu apgalvojuma “Ja vienā kartītes pusē ir uzrakstīts pāra skaitlis, tad otrā patskaņis” patiesumu?",
        text_en='There are four cards on the table with the following written on the top: "A", "B", "4", "5". What is written on the opposite sides of the cards is unknown.\n\n<b>Should the FOURTH card be turned over</b> to check the truth of the statement: "If an even number is written on one side of the card, then a vowel is on the other"?',
        text_ru="На столе лежат четыре карточки, на которых сверху написано: «А», «Б», «4», «5». Что написано на противоположных сторонах карточек, неизвестно.\n\n<b>Нужно ли перевернуть ЧЕТВЁРТУЮ карточку</b>, чтобы проверить истинность утверждения: «Если на одной стороне карточки написано чётное число, то на другой — гласная буква»?",
        answer_lv="Jā",
        answer_en="Yes",
        answer_ru="Да",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="378",
        answer_en="378",
        answer_ru="378",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>ötszáz tizenhét</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>ötszáz tizenhét</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>ötszáz tizenhét</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="517",
        answer_en="517",
        answer_ru="517",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>ezer hatszáz tíz</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>ezer hatszáz tíz</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>ezer hatszáz tíz</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="1610",
        answer_en="1610",
        answer_ru="1610",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nUzraksti skaitli <b>306</b> ungāru valodā!\n\n<i><b>Svarīgi</b></i><i>: Obligāti raksti atbildi ar unikālām ungāru burtu rakstzīmēm. Kopē, ja tie nav uz tavas tastatūras.</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWrite the number <b>306</b> in Hungarian!\n\n<i><b>Warning</b></i><i>: Be sure to write the answer with unique symbols of Hungarian letters. Copy if they are not in your keyboard.</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nЗапиши по-венгерски число <b>306</b>!\n\n<i><b>Важно</b></i><i>: Обязательно пиши ответ с уникальными символами венгерских букв. Скопируй, если их нет в твоей клавиатуре.</i>",
        answer_lv="háromszáz hat",
        answer_en="háromszáz hat",
        answer_ru="háromszáz hat",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nUzraksti skaitli <b>812</b> ungāru valodā!\n\n<i><b>Svarīgi</b></i><i>: Obligāti raksti atbildi ar unikālām ungāru burtu rakstzīmēm. Kopē, ja tie nav uz tavas tastatūras.</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWrite the number <b>812</b> in Hungarian!\n\n<i><b>Warning</b></i><i>: Be sure to write the answer with unique symbols of Hungarian letters. Copy if they are not in your keyboard.</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nЗапиши по-венгерски число <b>812</b>!\n\n<i><b>Важно</b></i><i>: Обязательно пиши ответ с уникальными символами венгерских букв. Скопируй, если их нет в твоей клавиатуре.</i>",
        answer_lv="nyolcszáz kéthét",
        answer_en="nyolcszáz kéthét",
        answer_ru="nyolcszáz kéthét",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Frekena Boka izcepa 30 maizītes. Bērns apēda dažus gabaliņus, Karlsons par 17 gabaliņiem vairāk. Sievietei atlika tikai trīs maizītes. Cik bulciņu apēda BĒRNS?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Freken Bock baked 30 buns. Junior ate a few, Karlson ate 17 more. The woman got only three buns. How many buns did JUNIOR eat?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Фрекен Бок испекла 30 плюшек. Малыш съел несколько штук, Карлсон на 17 штук больше. Женщине досталось всего три плюшки. Сколько плюшек съел МАЛЫШ?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="5",
        answer_en="5",
        answer_ru="5",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Frekena Boka izcepa 30 maizītes. Bērns apēda dažus gabaliņus, Karlsons par 17 gabaliņiem vairāk. Sievietei atlika tikai trīs maizītes. Cik bulciņu apēda KARLSONS?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Freken Bock baked 30 buns. Junior ate a few, Karlson ate 17 more. The woman got only three buns. How many buns did KARLSON eat?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Фрекен Бок испекла 30 плюшек. Малыш съел несколько штук, Карлсон на 17 штук больше. Женщине досталось всего три плюшки. Сколько плюшек съел КАРЛСОН?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="22",
        answer_en="22",
        answer_ru="22",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Tēvocis Fjodors, Šariks, kaķis Matroskins un Pečkins nolēma ziemā doties medībās. Tur viņi iztraucēja lāci un aizbēga no meža, apdzenot viens otru.\n\nŠariks skrēja ātrāk par Matroskinu, bet lēnāk par Pečkinu, Matroskins aizskrēja mājās vēlāk nekā Tēvocis Fjodors, kurš skrēja lēnāk par Šariku.\n\nKam ir lielākā iespēja tikt lāča rokās?",
        text_en="Uncle Fyodor, Sharik, the cat Matroskin and Pechkin decided to go hunting in winter. There they disturbed a bear and ran out of the forest, overtaking each other.\n\nSharik ran faster than Matroskin, but slower than Pechkin, Matroskin ran home later than Uncle Fyodor, who ran slower than Sharik.\n\nWho has the best chance of falling into the clutches of a bear?",
        text_ru="Дядя Федор, Шарик, кот Матроскин и Печкин решили пойти зимой на охоту. Там они потревожили медведя и убегали из леса, обгоняя друг друга.\n\nШарик бежал быстрее Матроскина, но медленнее Печкина, Матроскин прибежал домой позже, чем Дядя Федор, который бежал медленнее Шарика.\n\nУ кого больше всех шансов попасть в лапы к медведю?",
        answer_lv="Matroskinam",
        answer_en="Matroskin",
        answer_ru="У Матроскина",
        choices_lv=["Matroskinam", "Tēvocim Fjodoram", "Pečkinam", "Šarikam"],
        choices_en=["Matroskin", "Uncle Fyodor", "Pechkin", "Sharik"],
        choices_ru=["У Матроскина", "У Дяди Фёдора", "У Печкина", "У Шарика"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv='Sēžot klasē, Dima sapņoja: "Ja es savai naudai pievienotu uz pusi vairāk un vēl 20 rubļus, man pietiktu naudas komiksiem". Cik naudas ir Dimam, ja komiksi maksā 110 rubļus?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>',
        text_en='Sitting in class, Dima dreamed: "If I could add half my money, and another 20 rubles, I would have enough money for comics". How much money does Dima have if comics cost 110 rubles?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>',
        text_ru='Сидя на уроке Дима мечтал: "Если бы к моим деньгам добавить ещё половину, да ещё 20 рублей, мне бы хватило денег на комиксы". Сколько денег у Димы, если комиксы стоят 110 рублей?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>',
        answer_lv="60",
        answer_en="60",
        answer_ru="60",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )
    
    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Ieskaitē Vitja, Dima un Koļa pareizi atrisināja <b>dažādu uzdevumu skaitu</b>.\n\nVitja un Dima kopā atrisināja 6 uzdevumus. Koļa un Vitja - 4 uzdevumus.\n\nKurš iegūs <b>labāko</b> atzīmi?",
        text_en="During the test, Vitya, Dima, and Kolya correctly solved <b>a different number of problems</b>.\n\nVitya and Dima solved 6 problems together. Kolya and Vitya solved 4 problems.\n\nWho will get the <b>best</b> grade?",
        text_ru="На зачёте Витя, Дима и Коля верно решили <b>разное количество задач</b>.\n\nВитя и Дима вместе решили 6 задач. Коля и Витя – 4 задачи.\n\nКто из них получит <b>лучшую</b> оценку?",
        answer_lv="Dima",
        answer_en="Dima",
        answer_ru="Дима",
        choices_lv=["Vitja", "Dima", "Koļa"],
        choices_en=["Vitya", "Dima", "Kolya"],
        choices_ru=["Витя", "Дима", "Коля"],
        points=4
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv="Ieskaitē Vitja, Dima un Koļa pareizi atrisināja <b>dažādu uzdevumu skaitu</b>.\n\nVitja un Dima kopā atrisināja 6 uzdevumus. Koļa un Vitja - 4 uzdevumus.\n\nKurš iegūs <b>sliktāko</b> atzīmi?",
        text_en="During the test, Vitya, Dima, and Kolya correctly solved <b>a different number of problems</b>.\n\nVitya and Dima solved 6 problems together. Kolya and Vitya solved 4 problems.\n\nWho will get the <b>worst</b> grade?",
        text_ru="На зачёте Витя, Дима и Коля верно решили <b>разное количество задач</b>.\n\nВитя и Дима вместе решили 6 задач. Коля и Витя – 4 задачи.\n\nКто из них получит <b>худшую</b> оценку?",
        answer_lv="Vitja",
        answer_en="Vitya",
        answer_ru="Витя",
        choices_lv=["Vitja", "Dima", "Koļa"],
        choices_en=["Vitya", "Dima", "Kolya"],
        choices_ru=["Витя", "Дима", "Коля"],
        points=4
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Par 7 uzlīmēm un 2 burtnīcām Ļena samaksāja 120 rubļus. 5 uzlīmes maksā tikpat, cik puse no visa pirkuma.\n\nCik maksā <b>viena uzlīme</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="Lena paid 120 rubles for 7 stickers and 2 notebooks. 5 stickers cost the same as half of the entire purchase.\n\nHow much does <b>one sticker</b> cost?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="За 7 наклеек и две тетради Лена заплатила 120 рублей. 5 наклеек стоят столько же, сколько половина всей покупки.\n\nСколько стоит <b>одна наклейка</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="12",
        answer_en="12",
        answer_ru="12",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Par 7 uzlīmēm un 2 burtnīcām Ļena samaksāja 120 rubļus. 5 uzlīmes maksā tikpat, cik puse no visa pirkuma.\n\nCik maksā <b>viena burtnīca</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="Lena paid 120 rubles for 7 stickers and 2 notebooks. 5 stickers cost the same as half of the entire purchase.\n\nHow much does <b>one notebook</b> cost?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="За 7 наклеек и две тетради Лена заплатила 120 рублей. 5 наклеек стоят столько же, сколько половина всей покупки.\n\nСколько стоит <b>одна тетрадь</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="18",
        answer_en="18",
        answer_ru="18",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Ja Vitja nopirks 3 iepakojumus čipsu, tad viņam paliks 4 rubļi. Bet, ja viņš gribētu nopirkt 5 iepakojumus, viņam nepietiktu ar 20 rubļiem. Cik daudz naudas ir Vitjai?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="If Vitya buys 3 packs of chips, he will have 4 rubles left. But if he wanted to buy 5 packs, he would be 20 rubles short. How much money does Vitya have?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="Если Витя купит 3 пачки чипсов, то у него останется 4 рубля. А если бы он захотел купить 5 пачек, ему бы не хватило 20 рублей. Сколько денег у Вити?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="40",
        answer_en="40",
        answer_ru="40",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Vaļai patīk piena īriss, bet nepatīk šokolādes īriss.\n\nVāzē ir 7 piena un 4 šokolādes īrisi.\n\nCik konfektes ir jāpaņem uz labu laimi, lai <b>vismaz viens piena īriss</b> noteikti būtu starp tiem?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Valya likes milk toffees and doesn't like chocolate ones.\n\nThere are 7 milk toffees and 4 chocolate toffees in a vase.\n\nHow many candies do you need to take out without looking to be sure to get <b>at least one milk toffee</b> among them?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Валя любит молочные ириски и не любит шоколадные.\n\nВ вазе 7 молочных и 4 шоколадных ириски.\n\nСколько нужно достать конфет, не глядя, чтобы среди них точно попала <b>хоть одна молочная</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="5",
        answer_en="5",
        answer_ru="5",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )
    
    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Saša, Stjopa un Koļa spēlēja bumbu. Viens no zēniem izsita logu.\n\nSaša teica: "Ne es izsitu logu."\nKoļa teica: "Stjopa izsita logu."\n\nPēc kāda laika izrādījās, ka viens no zēniem runāja patiesību, bet otrs melo.\n\nKas izsita logu?',
        text_en='Sasha, Styopa and Kolya were playing ball. One of the boys hit the window and broke the glass.\n\nSasha said: "I did not break the window."\nKolya said: "Styopa broke the window."\n\nAfter some time it turned out that one of the boys was telling the truth and the other was lying.\n\nWho broke the window?',
        text_ru="Саша, Стёпа и Коля играли в мяч. Один из мальчиков попал в окно и разбил стекло.\n\nСаша сказал: «Окно разбил не я».\nКоля сказал: «Окно разбил Стёпа.\n\nСпустя некоторое время выяснилось, что один из мальчиков говорит правду, а другой врёт.\n\nКто разбил окно?",
        answer_lv="Koļa",
        answer_en="Kolya",
        answer_ru="Коля",
        choices_lv=["Saša", "Stjopa", "Koļa"],
        choices_en=["Sasha", "Styopa", "Kolya"],
        choices_ru=["Саша", "Стёпа", "Коля"],
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="multiple_choice",
        text_lv='Dievietes Hēra, Atēna un Afrodīte ieradās pie jauna Parisa, lai viņš varētu izlemt, kura no viņām ir skaistāka.\nParādījušās Parisa priekšā, dievietes izteica šādus apgalvojumus:\n\n<b>Afrodīte</b>: "Es esmu visskaistākā."\n<b>Atēna</b>: "Afrodīte nav visskaistākā."\n<b>Hēra</b>: "Es esmu visskaistākā."\n<b>Afrodīte</b>: "Hēra nav pati skaistākā."\n<b>Atēna</b>: "Es esmu visskaistākā."\n\nPariss pieņēma, ka visi skaistākās dievietes apgalvojumi ir patiesi, un visi pārējo divu dieviešu apgalvojumi bija nepatiesi. Kuru Pariss uzskatīja par skaistāko?',
        text_en='The goddesses Hera, Athena, and Aphrodite came to the young Paris to decide which of them was the most beautiful.\nAppearing before Paris, the goddesses made the following statements:\n\n<b>Aphrodite</b>: "I am the most beautiful."\n<b>Athena</b>: "Aphrodite is not the most beautiful."\n<b>Hera</b>: "I am the most beautiful."\n<b>Aphrodite</b>: "Hera is not the most beautiful."\n<b>Athena</b>: "I am the most beautiful."\n\nParis assumed that all the statements of the most beautiful of the goddesses were true, and all the statements of the other two goddesses were false. Whom did Paris consider the most beautiful?',
        text_ru='Богини Гера, Афина и Афродита пришли к юному Парису, чтобы тот решил, кто из них прекраснее.\nПредстав перед Парисом, богини высказали следующие утверждения:\n\n<b>Афродита</b>: "Я самая прекрасная".\n<b>Афина</b>: "Афродита не самая прекрасная".\n<b>Гера</b>: "Я самая прекрасная".\n<b>Афродита</b>: "Гера не самая прекрасная".\n<b>Афина</b>: "Я самая прекрасная".\n\nПарис предположил, что все утверждения прекраснейшей из богинь истинны, а все утверждения двух других богинь ложны. Кого Парис посчитал прекраснейшей?',
        answer_lv="Afrodīti",
        answer_en="Aphrodite",
        answer_ru="Афродиту",
        choices_lv=["Hēru", "Atēnu", "Afrodīti"],
        choices_en=["Hera", "Athena", "Aphrodite"],
        choices_ru=["Геру", "Афину", "Афродиту"],
        points=10
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Vienā ģimenē ir daudz bērnu. Septiņiem no tiem garšo kāposti, sešiem - burkāni, trijiem - kāposti un gurķi, diviem - burkāni un gurķi. Cik bērnu ir ģimenē?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="There are many children in one family. Seven of them like cabbage, six like carrots, three like cabbage and cucumbers, two like carrots and cucumbers. How many children are in the family?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="В одной семье много детей. Семеро из них любят капусту, шестеро - морковь, трое - капусту и огурцы, двое - морковь и огурцы. Сколько детей в семье?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="10",
        answer_en="10",
        answer_ru="10",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv="Tēvoča Fjodora dzimšanas dienā pastnieks Pečkins vēlas noskaidrot, cik viņam gadu.\n\nŠariks stāsta, ka Tēvocim Fjodoram ir vairāk nekā 11 gadi, bet kaķis Matroskins apgalvo, ka viņam ir vairāk nekā 10 gadi.\n\nCik gadi ir Tēvocim Fjodoram, ja ir zināms, ka tieši viens no viņiem kļūdījās?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="On Uncle Fyodor's birthday, postman Pechkin wants to find out how old he is.\n\nSharik says that Uncle Fyodor is over 11 years old, but the cat Matroskin claims that he is over 10 years old.\n\nHow old is Uncle Fyodor if it is known that exactly one of them was wrong?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="В день рождения дяди Федора почтальон Печкин хочет выяснить, сколько тому лет.\n\nШарик говорит, что дяде Федору больше 11 лет, а кот Матроскин утверждает, что больше 10 лет.\n\nСколько лет дяде Федору, если известно, что ровно один из них ошибся?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="11",
        answer_en="11",
        answer_ru="11",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )

    await rq.add_task(
        grade=7,
        input_type="text",
        text_lv='Kādu dienu tika atrasta burtnīca. Tajā tika ierakstīti simts apgalvojumi:\n\n"Šajā burtnīcā ir tieši 1 nepatiess apgalvojums";\n"Šajā burtnīcā ir tieši 2 nepatiesi apgalvojumi";\n"Šajā burtnīcā ir tieši 3 nepatiesi apgalvojumi";\n... \n"Šajā burtnīcā ir tieši 100 nepatiesi apgalvojumi"\n\nCik <b>PATIESU</b> apgalvojumu ir burtnīcā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='One day a notebook was found. It contained one hundred statements:\n\n"There is exactly 1 false statement in this notebook";\n"There are exactly 2 false statements in this notebook";\n"There are exactly 3 false statements in this notebook";\n...\n"There are exactly 100 false statements in this notebook"\n\nHow many <b>TRUE</b> statements are there in the notebook?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='Однажды была найдена тетрадь. В ней было записано сто утверждений:\n\n"В этой тетради ровно 1 неверное утверждение";\n"В этой тетради ровно 2 неверных утверждения";\n"В этой тетради ровно 3 неверных утверждения";\n...\n"В этой тетради ровно 100 неверных утверждений"\n\nСколько в тетраде <b>ВЕРНЫХ</b> утверждений?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="1",
        answer_en="1",
        answer_ru="1",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=6
    )



    # для 8 класса
    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Pēc kaujas ar Zmeju Goriniču trīs spēkavīri teica:\n\n<b>Iļja Muromietis</b>: "Zmeju nogalināja Dobriņa Ņikitičs."\n<b>Dobriņa Ņikitičs</b>: "Zmeju nogalināja Aļoša Popovičs."\n<b>Aļoša Popovičs</b>: "Es nogalināju Zmeju."\n\nKas nogalināja Zmeju, ja tikai viens no viņiem pateica patiesību?',
        text_en='After the battle with the Serpent, the three heroes declared:\n\n<b>Ilya Muromets</b>: "The Serpent was killed by Dobrynya Nikitich."\n<b>Dobrynya Nikitich</b>: "The Serpent was killed by Alyosha Popovich."\n<b>Alyosha Popovich</b>: "I killed the Serpent."\n\nWho killed the Serpent, if only one of them told the truth?',
        text_ru="После битвы со Змеем Горынычем три богатыря заявили:\n\n<b>Илья Муромец</b>: «Змея убил Добрыня Никитич».\n<b>Добрыня Никитич</b>: «Змея убил Алеша Попович».\n<b>Алеша Попович</b>: «Змея убил я».\n\nКто убил Змея, если только один из них сказал правду?",
        answer_lv="Dobriņa Ņikitičs",
        answer_en="Dobrynya Nikitich",
        answer_ru="Добрыня Никитич",
        choices_lv=["Iļja Muromietis", "Dobriņa Ņikitičs", "Aļoša Popovičs"],
        choices_en=["Ilya Muromets", "Dobrynya Nikitich", "Alyosha Popovich"],
        choices_ru=["Илья Муромец", "Добрыня Никитич", "Алёша Попович"],
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Imperatora pipari tika nozagti. Kā zināms, tie, kas zog piparus, vienmēr melo. Sargs sacīja, ka zina, kas nozadzis piparus. Vai viņš ir vainīgs?",
        text_en="The Emperor's pepper was stolen. As is well known, those who steal pepper always lie. The press secretary said he knew who stole the pepper. Is he guilty?",
        text_ru="У императора украли перец. Как известно, те, кто крадут перец, всегда лгут. Пресс-секретарь заявил, что знает, кто украл перец. Виновен ли он?",
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Starp trim cilvēkiem A, B un C viens ir melis (vienmēr melo), viens ir bruņinieks (vienmēr teic patiesību), bet trešais ir normāls cilvēks, kurš var teikt gan patiesību, gan melus.\n\nA saka: "Es esmu normāls cilvēks."\nB saka: "A un C dažreiz saka patiesību."\nC saka: "B ir normāls cilvēks."\n\nKas ir cilvēks A?',
        text_en='Among three people A, B and C, one is a liar (always lies), one is a knight (always tells the truth), and the third is a normal person who can tell both the truth and a lie.\n\nA says: "I am a normal person."\nB says: "A and C sometimes tell the truth."\nC: "B is a normal person."\n\nWho is person A?',
        text_ru="Среди трех человек А, В и С один лжец (всегда врёт), один рыцарь (всегда говорит правду), а третий – нормальный человек, который может говорить и правду, и ложь.\n\nА говорит: «Я нормальный человек».\nВ говорит: «А и С иногда говорят правду».\nС: «В – нормальный человек».\n\nКем является человек А?",
        answer_lv="Melis",
        answer_en="Liar",
        answer_ru="Лжец",
        choices_lv=["Melis", "Bruņinieks", "Normāls"],
        choices_en=["Liar", "Knight", "Normal"],
        choices_ru=["Лжец", "Рыцарь", "Нормальный"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Starp trim cilvēkiem A, B un C viens ir melis (vienmēr melo), viens ir bruņinieks (vienmēr teic patiesību), bet trešais ir normāls cilvēks, kurš var teikt gan patiesību, gan melus.\n\nA saka: "Es esmu normāls cilvēks."\nB saka: "A un C dažreiz saka patiesību."\nC saka: "B ir normāls cilvēks."\n\nKas ir cilvēks B?',
        text_en='Among three people A, B and C, one is a liar (always lies), one is a knight (always tells the truth), and the third is a normal person who can tell both the truth and a lie.\n\nA says: "I am a normal person."\nB says: "A and C sometimes tell the truth."\nC: "B is a normal person."\n\nWho is person B?',
        text_ru="Среди трех человек А, В и С один лжец (всегда врёт), один рыцарь (всегда говорит правду), а третий – нормальный человек, который может говорить и правду, и ложь.\n\nА говорит: «Я нормальный человек».\nВ говорит: «А и С иногда говорят правду».\nС: «В – нормальный человек».\n\nКем является человек B?",
        answer_lv="Normāls",
        answer_en="Normal",
        answer_ru="Нормальный",
        choices_lv=["Melis", "Bruņinieks", "Normāls"],
        choices_en=["Liar", "Knight", "Normal"],
        choices_ru=["Лжец", "Рыцарь", "Нормальный"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Starp trim cilvēkiem A, B un C viens ir melis (vienmēr melo), viens ir bruņinieks (vienmēr teic patiesību), bet trešais ir normāls cilvēks, kurš var teikt gan patiesību, gan melus.\n\nA saka: "Es esmu normāls cilvēks."\nB saka: "A un C dažreiz saka patiesību."\nC saka: "B ir normāls cilvēks."\n\nKas ir cilvēks C?',
        text_en='Among three people A, B and C, one is a liar (always lies), one is a knight (always tells the truth), and the third is a normal person who can tell both the truth and a lie.\n\nA says: "I am a normal person."\nB says: "A and C sometimes tell the truth."\nC: "B is a normal person."\n\nWho is person C?',
        text_ru="Среди трех человек А, В и С один лжец (всегда врёт), один рыцарь (всегда говорит правду), а третий – нормальный человек, который может говорить и правду, и ложь.\n\nА говорит: «Я нормальный человек».\nВ говорит: «А и С иногда говорят правду».\nС: «В – нормальный человек».\n\nКем является человек C?",
        answer_lv="Bruņinieks",
        answer_en="Knight",
        answer_ru="Рыцарь",
        choices_lv=["Melis", "Bruņinieks", "Normāls"],
        choices_en=["Liar", "Knight", "Normal"],
        choices_ru=["Лжец", "Рыцарь", "Нормальный"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Konferencē piedalījās 100 cilvēki – ķīmiķi un alķīmiķi.\n\nKatram tika uzdots jautājums: “<b>Neskaitot jūs</b>, kuru vairāk starp pārējiem dalībniekiem – ķīmiķu vai alķīmiķu?” .\n\nKad tika aptaujāts 51 dalībnieks un <b>visi</b> atbildēja, ka alķīmiķu ir vairāk, aptauja tika pārtraukta.\n\nAlķīmiķi vienmēr melo, bet ķīmiķi runā patiesību.\n\nCik ķīmiķu ir konferences dalībnieku vidū?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en='There were 100 participants in the conference – chemists and alchemists.\n\nEach was asked the question: "<b>If we do not count you</b>, who are there more of among the other participants – chemists or alchemists?"\n\nWhen 51 participants were surveyed, and <b>all</b> answered that there were more alchemists, the survey was interrupted.\n\nAlchemists always lie, and chemists tell the truth.\n\nHow many chemists are there among the participants?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru="В конференции участвовало 100 человек – химиков и алхимиков.\n\nКаждому был задан вопрос: «<b>Если не считать Вас</b>, то кого больше среди остальных участников – химиков или алхимиков?».\n\nКогда опросили 51 участника, и <b>все</b> ответили, что алхимиков больше, опрос прервался.\n\nАлхимики всегда лгут, а химики говорят правду.\n\nСколько химиков среди участников?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="50",
        answer_en="50",
        answer_ru="50",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )
    
    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Katra kuba skaldne pieder vai nu bruņiniekam (kurš vienmēr saka patiesību), vai melim (kurš vienmēr melo).\n\n<b>Katrs no viņiem</b> apgalvo, ka <b>uz blakus pie viņiem esošajām skaldnēm</b> meļu ir vairāk nekā bruņinieku.\n\nCik kuba skaldnes pieder bruņiniekiem un cik meļiem?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti tādā formā: "<b>1 un 5</b>", ja atbilde ir 1 skaldne bruņiniekiem un 5 skaldnes meļiem.</i>',
        text_en='Each face of the cube is owned by either a knight (who always tells the truth) or a liar (who always lies).\n\n<b>Each of them</b> claims that <b>on the faces adjacent to him</b> there are more liars than knights.\n\nHow many knights and how many liars own the faces of the cube?\n\n<i><b>Warning</b></i><i>: Write your answer in the form: "<b>1 and 5</b>", if the answer is 1 knight and 5 liars.</i>',
        text_ru='Каждой гранью куба владеет или рыцарь (который всегда говорит правду), или лжец (который всегда врёт).\n\n<b>Каждый из них</b> утверждает, что <b>на соседних к нему гранях</b> лжецов больше, чем рыцарей.\n\nСколько рыцарей и сколько лжецов владеют гранями куба?\n\n<i><b>Важно</b></i><i>: Ответ пиши в такой форме: "<b>1 и 5</b>", если ответ - 1 рыцарь и 5 лжецов.</i>',
        answer_lv="2 un 4",
        answer_en="2 and 4",
        answer_ru="2 и 4",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=12
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Sauksim testu par <b>vieglu</b>, ja pie katra galda ir skolēns, kurš ir atrisinājis visus uzdevumus. Pie kāda nosacījuma tests ir <b>grūts</b>?\n\nA - "Ja pie katra galda ir skolēns, kurš nav atrisinājis visus uzdevumus"\nB - "Ja pie katra galda nav skolēna, kurš būtu atrisinājis visus uzdevumus"\nC - "Ja vismaz pie viena galda nav skolēna, kurš būtu atrisinājis visus uzdevumus"',
        text_en="Let's call a test <b>easy</b> if there is a student at each desk who has solved all the problems. Under what condition is the test <b>difficult</b>?\n\nA - If at every desk there is a student who has not solved all the problems\nB - If there is not a student at every desk who has solved all the problems\nC - If there is not a student at at least one desk who has solved all the problems",
        text_ru='Назовём контрольную <b>лёгкой</b>, если за каждой партой найдётся ученик, решивший все задачи. При каком условии контрольная <b>трудная</b>?\n\nA - "Если за каждой партой найдётся ученик, не решивший все задачи"\nB - "Если за каждой партой не найдётся ученика, решившего все задачи"\nC - "Если хотя бы за одной партой не найдётся ученика, решившего все задачи"',
        answer_lv="C",
        answer_en="C",
        answer_ru="C",
        choices_lv=["A", "B", "C"],
        choices_en=["A", "B", "C"],
        choices_ru=["A", "B", "C"],
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Melnbaltajā fotogrāfijā melnā krāsa veido <b>80% no laukuma</b>. Šī fotogrāfija ir palielināta 3 reizes.\n\nCik procenti ir <b>baltā</b> krāsa palielinātajā fotogrāfijā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti skaitli ar procenta zīmi bez atstarpēm!</i>',
        text_en='In a black and white photograph, black is <b>80% of the area</b>. This photograph has been enlarged 3 times.\n\nWhat percentage is <b>white</b> in the enlarged photograph?\n\n<i><b>Warning</b></i><i>: In your answer, write the number with a percentage sign without spaces!</i>',
        text_ru='На черно-белой фотографии черный цвет составляет <b>80% площади</b>. Эту фотографию увеличили в 3 раза.\n\nКакой процент составляет <b>белый цвет</b> на увеличенной фотографии?\n\n<i><b>Важно</b></i><i>: В ответе пиши число со знаком процента без пробелов!</i>',
        answer_lv="20%",
        answer_en="20%",
        answer_ru="20%",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5,
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Pēteris 1/3 sava laika pavada spēlējot futbolu, 1/5 daļu mācās skolā, 1/6 daļu skatās filmas, 1/7 risina olimpiādes uzdevumus un 1/3 daļu guļ. Vai ir iespējams šādi dzīvot?",
        text_en="Peter spends 1/3 of his time playing football, 1/5 studying at school, 1/6 watching movies, 1/7 solving Olympiad problems, and 1/3 sleeping. Is it possible to live like this?",
        text_ru="Петя тратит 1/3 своего времени на игру в футбол, 1/5 — на учебу в школе, 1/6 — на просмотр кинофильмов, 1/7 — на решение олимпиадных задач, и 1/3 — на сон. Можно ли так жить?",
        answer_lv="Nē",
        answer_en="No",
        answer_ru="Нет",
        choices_lv=["Jā", "Nē"],
        choices_en=["Yes", "No"],
        choices_ru=["Да", "Нет"],
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Kādam zemniekam bija vairāki vienāda svara sivēni un vairāki vienāda svara jēri.\n\nZēns saimniekam jautāja, cik sver viens sivēns un viens jērs.\n\nZemnieks atbildēja, ka 3 sivēni un 2 jēri sver 22 kg, un 2 sivēni un 3 jēri sver 23 kg.\n\nCik sver viens <b>sivēns</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="A farmer had several piglets of the same weight and several lambs of the same weight.\n\nThe boy asked the farmer how much one piglet and one lamb weighed.\n\nThe farmer replied that 3 piglets and 2 lambs weigh 22 kg, and 2 piglets and 3 lambs weigh 23 kg.\n\nHow much does one <b>piglet</b> weigh?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="У фермера было несколько одинакового веса поросят и несколько ягнят также одинакового веса.\n\nМальчик спросил фермера, сколько весит один поросенок и один ягненок.\n\nФермер ответил, что 3 поросенка и 2 ягненка весят 22 кг, а 2 поросенка и 3 ягненка весят 23 кг.\n\nСколько весит один <b>поросенок</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="4",
        answer_en="4",
        answer_ru="4",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Kādam zemniekam bija vairāki vienāda svara sivēni un vairāki vienāda svara jēri.\n\nZēns saimniekam jautāja, cik sver viens sivēns un viens jērs.\n\nZemnieks atbildēja, ka 3 sivēni un 2 jēri sver 22 kg, un 2 sivēni un 3 jēri sver 23 kg.\n\nCik sver viens <b>jērs</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli, bez mērvienībām!</i>",
        text_en="A farmer had several piglets of the same weight and several lambs of the same weight.\n\nThe boy asked the farmer how much one piglet and one lamb weighed.\n\nThe farmer replied that 3 piglets and 2 lambs weigh 22 kg, and 2 piglets and 3 lambs weigh 23 kg.\n\nHow much does one <b>lamb</b> weigh?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number, without units!</i>",
        text_ru="У фермера было несколько одинакового веса поросят и несколько ягнят также одинакового веса.\n\nМальчик спросил фермера, сколько весит один поросенок и один ягненок.\n\nФермер ответил, что 3 поросенка и 2 ягненка весят 22 кг, а 2 поросенка и 3 ягненка весят 23 кг.\n\nСколько весит один <b>ягнёнок</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число, без единиц измерения!</i>",
        answer_lv="5",
        answer_en="5",
        answer_ru="5",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Trīs draugi katrs izteica vienu apgalvojumu par veselu skaitli x.\n\n<b>Ivans</b>: "Skaitlis x ir lielāks par 4, bet mazāks par 8."\n<b>Andrejs</b>: "Skaitlis x ir lielāks par 6, bet mazāks par 9."\n<b>Viktors</b>: "Skaitlis x ir lielāks par 5, bet mazāks par 8."\n\nAtrodi skaitli x, ja ir zināms, ka <b>divi draugi teica patiesību</b>, bet trešais meloja.\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='Three friends made one statement each about an integer x.\n\n<b>Ivan</b>: "The number x is greater than 4, but less than 8."\n<b>Andrey</b>: "The number x is greater than 6, but less than 9."\n<b>Victor</b>: "The number x is greater than 5, but less than 8."\n\nFind the number x if it is known that <b>two of the friends told the truth</b> and the third lied.\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru="Три друга сделали по одному заявлению про целое число х.\n\n<b>Иван</b>: «Число х больше 4, но меньше 8».\n<b>Андрей</b>: «Число х больше 6, но меньше 9».\n<b>Виктор</b>: «Число х больше 5, но меньше 8».\n\nНайди число х, если известно, что <b>двое из друзей сказали правду</b>, а третий солгал.\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="6",
        answer_en="6",
        answer_ru="6",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Kurai ģeometriskajai figūrai būs tāds pats attēls, ja to zīmēs no jebkura skatu punkta?",
        text_en="Which geometric figure will have the same image when drawn from any point of view?",
        text_ru="Какая геометрическая фигура будет иметь одинаковое изображение при рисовании её с любой точки зрения?",
        answer_lv="Lode",
        answer_en="Ball",
        answer_ru="Шар",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=8
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Ja reizināt trīs pilnus desmitus ar četriem pilniem desmitiem, cik <b>pilnu desmitu</b> sanāks?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="If you multiply three tens by four tens, how many <b>tens</b> do you get?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Если три десятка умножить на четыре десятка, то сколько <b>десятков</b> получится?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="120",
        answer_en="120",
        answer_ru="120",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Cik tagad ir pulkstenis, ja atlikušā dienas daļa ir divas reizes garāka par dienas iepriekšējo daļu?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="What time is it now if the remaining part of the day is twice as long as the past one?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Сколько сейчас времени, если оставшаяся часть суток в два раза превышает прошедшую?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="8",
        answer_en="8",
        answer_ru="8",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Divi zemnieki nolēma noskaidrot, kuram ir vairāk aitu.\n\n<b>Pirmais</b> no viņiem teica: "Ja tu man iedosi savu aitu, tad man to būs divreiz vairāk nekā tev."\n\n<b>Otrs</b> viņam saka: "Bet ja tu man iedosi savu aitu, tad man būs tikpat aitu kā tev.”\n\nCik aitu ir katram zemniekam?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti tādā formā: "<b>2 un 5</b>", ja atbilde ir 2 aitas pirmajam un 5 aitas otrajam.</i>',
        text_en='Two farmers decided to find out who had more sheep.\n\n<b>The first</b> of them said: "If you give me your sheep, then I will have twice as many as you."\n\n<b>The second one</b> said: "But if you give me one of your sheep, then I will have as many sheep as you."\n\nHow many sheep does each farmer have?\n\n<i><b>Warning</b></i><i>: Write your answer in the form: "<b>2 and 5</b>", if the answer is 2 sheeps the first one and 5 sheeps the second one.</i>',
        text_ru='Два фермера решили узнать, у кого больше овец.\n\n<b>Первый</b> из них сказал: «Если ты дашь мне свою овцу, то у меня будет их в два раза больше, чем у тебя».\n\n<b>Второй</b> ему говорит: «А если ты мне дашь свою одну овцу, тогда у меня овец будет столько же, сколько и у тебя».\n\nСколько овец у каждого из фермеров?\n\n<i><b>Важно</b></i><i>: Ответ пиши в такой форме: "<b>2 и 5</b>", если ответ - 2 овцы у первого и 5 овец у второго.</i>',
        answer_lv="7 un 5",
        answer_en="7 and 5",
        answer_ru="7 и 5",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Cik skaldņu ir sešstūra zīmulim, kas nekad nav bijis uzasināts?",
        text_en="How many edges a hexagonal pencil has that has never been sharpened?",
        text_ru="Сколько граней имеет шестигранный карандаш, который ни разу не затачивали?",
        answer_lv="8",
        answer_en="8",
        answer_ru="8",
        choices_lv=["6", "7", "8"],
        choices_en=["6", "7", "8"],
        choices_ru=["6", "7", "8"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Kurš no šiem secinājumiem ir patiess?\n\nA) Šeit ir trīs nepatiesi secinājumi.\nB) Šeit ir viens nepatiess secinājums.\nC) Šeit ir divi nepatiesi secinājumi.\nD) Šeit ir pieci nepatiesi secinājumi.\nE) Šeit ir četri nepatiesi secinājumi.",
        text_en="Which of the following conclusions is correct?\n\nA) There are three false conclusions.\nB) There is one false conclusion.\nC) There are two false conclusions.\nD) There are five false conclusions.\nE) There are four false conclusions.",
        text_ru="Какой из выводов, указанных ниже, верный?\n\nA) Здесь три ложных вывода.\nB) Здесь один ложный вывод.\nC) Здесь два ложных вывода.\nD) Здесь пять ложных выводов.\nE) Здесь четыре ложных вывода.",
        answer_lv="E",
        answer_en="E",
        answer_ru="E",
        choices_lv=["A", "B", "C", "D", "E"],
        choices_en=["A", "B", "C", "D", "E"],
        choices_ru=["A", "B", "C", "D", "E"],
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Uzraksti skaitli 1000, izmantojot astoņus astoņniekus un plusa zīmes.\n\n<i><b>Svarīgi</b></i><i>: Sāc no mazākajiem skaitļiem, raksti bez atstarpēm! Piemēram: 8+88+888+888+8888</i>",
        text_en="Write the number 1000 using eight eights and plus signs.\n\n<i><b>Warning</b></i><i>: Start with the smallest numbers, write without spaces! For example: 8+88+888+888+8888</i>",
        text_ru="Запиши число 1000 при помощи восьми восьмерок и знаков плюса.\n\n<i><b>Важно</b></i><i>: Начинай с наименьших чисел, пиши без пробелов! Например: 8+88+888+888+8888</i>",
        answer_lv="8+8+8+88+888",
        answer_en="8+8+8+88+888",
        answer_ru="8+8+8+88+888",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Kādu dienu tika atrasta burtnīca. Tajā tika ierakstīti simts apgalvojumi:\n\n"Šajā burtnīcā ir tieši 1 nepatiess apgalvojums";\n"Šajā burtnīcā ir tieši 2 nepatiesi apgalvojumi";\n"Šajā burtnīcā ir tieši 3 nepatiesi apgalvojumi";\n... \n"Šajā burtnīcā ir tieši 100 nepatiesi apgalvojumi"\n\nCik <b>PATIESU</b> apgalvojumu ir burtnīcā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='One day a notebook was found. It contained one hundred statements:\n\n"There is exactly 1 false statement in this notebook";\n"There are exactly 2 false statements in this notebook";\n"There are exactly 3 false statements in this notebook";\n...\n"There are exactly 100 false statements in this notebook"\n\nHow many <b>TRUE</b> statements are there in the notebook?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='Однажды была найдена тетрадь. В ней было записано сто утверждений:\n\n"В этой тетради ровно 1 неверное утверждение";\n"В этой тетради ровно 2 неверных утверждения";\n"В этой тетради ровно 3 неверных утверждения";\n...\n"В этой тетради ровно 100 неверных утверждений"\n\nСколько в тетраде <b>ВЕРНЫХ</b> утверждений?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="1",
        answer_en="1",
        answer_ru="1",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=8
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Uz galda rindā ir četras figūras: trijstūris, riņķis, taisnstūris un rombs. Tie ir krāsoti dažādās krāsās: sarkanā, zilā, dzeltenā, zaļā.\n\nIr zināms, ka sarkanā figūra atrodas starp zilo un zaļo; pa labi no dzeltenās figūras ir rombs; riņķis atrodas pa labi gan no trijstūra, gan no romba; trijstūris neatrodas malā; zilās un dzeltenās figūras neatrodas blakus.\n\nNosaki, kura figūra ir <b>PIRMĀ</b> pēc secības un kāda tai krāsa.\n\n<i><b>Svarīgi</b></i><i>: Vispirms raksti krāsu, pēc tam figūru. Neliek punktu. Izmanto noteikto galotni.</i>\n<i><b>Atbildes piemērs</b></i><i>: Sarkanais trijstūris</i>",
        text_en="There are four figures lying in a row on the table: a triangle, a circle, a rectangle and a rhombus. They are painted in different colors: red, blue, yellow and green.\n\nIt is known that the red figure lies between the blue and green; to the right of the yellow figure lies a rhombus; the circle lies to the right of both the triangle and the rhombus; the triangle does not lie on the edge; the blue and yellow figures do not lie next to each other.\n\nDetermine which figure and what color is <b>FIRST</b> in order.\n\n<i><b>Warning</b></i><i>: In your answer, write the color first, then the shape. Don't put a full stop. Don't use articles.</i>\n<i><b>Answer example</b></i><i>: Red triangle</i>",
        text_ru="На столе лежат в ряд четыре фигуры: треугольник, круг, прямоугольник и ромб. Они окрашены в разные цвета: красный, синий, жёлтый, зелёный.\n\nИзвестно, что красная фигура лежит между синей и зелёной; справа от жёлтой фигуры лежит ромб; круг лежит правее и треугольника и ромба; треугольник лежит не с краю; синяя и жёлтая фигуры лежат не рядом.\n\nОпредели, какая фигура и какого цвета <b>ПЕРВАЯ</b> по порядку.\n\n<i><b>Важно</b></i><i>: Сначала пиши цвет, потом фигуру. Не ставь точку. Используй букву Ё, если требуется.</i>\n<i><b>Пример ответа</b></i><i>: Жёлтый треугольник</i>",
        answer_lv="Dzeltenais taisnstūris",
        answer_en="Yellow rectangle",
        answer_ru="Жёлтый прямоугольник",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Uz galda rindā ir četras figūras: trijstūris, riņķis, taisnstūris un rombs. Tie ir krāsoti dažādās krāsās: sarkanā, zilā, dzeltenā, zaļā.\n\nIr zināms, ka sarkanā figūra atrodas starp zilo un zaļo; pa labi no dzeltenās figūras ir rombs; riņķis atrodas pa labi gan no trijstūra, gan no romba; trijstūris neatrodas malā; zilās un dzeltenās figūras neatrodas blakus.\n\nNosaki, kura figūra ir <b>OTRĀ</b> pēc secības un kāda tai krāsa.\n\n<i><b>Svarīgi</b></i><i>: Vispirms raksti krāsu, pēc tam figūru. Neliek punktu. Izmanto noteikto galotni.</i>\n<i><b>Atbildes piemērs</b></i><i>: Sarkanais trijstūris</i>",
        text_en="There are four figures lying in a row on the table: a triangle, a circle, a rectangle and a rhombus. They are painted in different colors: red, blue, yellow and green.\n\nIt is known that the red figure lies between the blue and green; to the right of the yellow figure lies a rhombus; the circle lies to the right of both the triangle and the rhombus; the triangle does not lie on the edge; the blue and yellow figures do not lie next to each other.\n\nDetermine which figure and what color is <b>SECOND</b> in order.\n\n<i><b>Warning</b></i><i>: In your answer, write the color first, then the shape. Don't put a full stop. Don't use articles.</i>\n<i><b>Answer example</b></i><i>: Red triangle</i>",
        text_ru="На столе лежат в ряд четыре фигуры: треугольник, круг, прямоугольник и ромб. Они окрашены в разные цвета: красный, синий, жёлтый, зелёный.\n\nИзвестно, что красная фигура лежит между синей и зелёной; справа от жёлтой фигуры лежит ромб; круг лежит правее и треугольника и ромба; треугольник лежит не с краю; синяя и жёлтая фигуры лежат не рядом.\n\nОпредели, какая фигура и какого цвета <b>ВТОРАЯ</b> по порядку.\n\n<i><b>Важно</b></i><i>: Сначала пиши цвет, потом фигуру. Не ставь точку. Используй букву Ё, если требуется.</i>\n<i><b>Пример ответа</b></i><i>: Жёлтый треугольник</i>",
        answer_lv="Zaļais rombs",
        answer_en="Green rhombus",
        answer_ru="Зелёный ромб",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Uz galda rindā ir četras figūras: trijstūris, riņķis, taisnstūris un rombs. Tie ir krāsoti dažādās krāsās: sarkanā, zilā, dzeltenā, zaļā.\n\nIr zināms, ka sarkanā figūra atrodas starp zilo un zaļo; pa labi no dzeltenās figūras ir rombs; riņķis atrodas pa labi gan no trijstūra, gan no romba; trijstūris neatrodas malā; zilās un dzeltenās figūras neatrodas blakus.\n\nNosaki, kura figūra ir <b>TREŠĀ</b> pēc secības un kāda tai krāsa.\n\n<i><b>Svarīgi</b></i><i>: Vispirms raksti krāsu, pēc tam figūru. Neliek punktu. Izmanto noteikto galotni.</i>\n<i><b>Atbildes piemērs</b></i><i>: Sarkanais trijstūris</i>",
        text_en="There are four figures lying in a row on the table: a triangle, a circle, a rectangle and a rhombus. They are painted in different colors: red, blue, yellow and green.\n\nIt is known that the red figure lies between the blue and green; to the right of the yellow figure lies a rhombus; the circle lies to the right of both the triangle and the rhombus; the triangle does not lie on the edge; the blue and yellow figures do not lie next to each other.\n\nDetermine which figure and what color is <b>THIRD</b> in order.\n\n<i><b>Warning</b></i><i>: In your answer, write the color first, then the shape. Don't put a full stop. Don't use articles.</i>\n<i><b>Answer example</b></i><i>: Red triangle</i>",
        text_ru="На столе лежат в ряд четыре фигуры: треугольник, круг, прямоугольник и ромб. Они окрашены в разные цвета: красный, синий, жёлтый, зелёный.\n\nИзвестно, что красная фигура лежит между синей и зелёной; справа от жёлтой фигуры лежит ромб; круг лежит правее и треугольника и ромба; треугольник лежит не с краю; синяя и жёлтая фигуры лежат не рядом.\n\nОпредели, какая фигура и какого цвета <b>ТРЕТЬЯ</b> по порядку.\n\n<i><b>Важно</b></i><i>: Сначала пиши цвет, потом фигуру. Не ставь точку. Используй букву Ё, если требуется.</i>\n<i><b>Пример ответа</b></i><i>: Жёлтый треугольник</i>",
        answer_lv="Sarkanais trijstūris",
        answer_en="Red triangle",
        answer_ru="Красный треугольник",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Uz galda rindā ir četras figūras: trijstūris, riņķis, taisnstūris un rombs. Tie ir krāsoti dažādās krāsās: sarkanā, zilā, dzeltenā, zaļā.\n\nIr zināms, ka sarkanā figūra atrodas starp zilo un zaļo; pa labi no dzeltenās figūras ir rombs; riņķis atrodas pa labi gan no trijstūra, gan no romba; trijstūris neatrodas malā; zilās un dzeltenās figūras neatrodas blakus.\n\nNosaki, kura figūra ir <b>CETURTĀ</b> pēc secības un kāda tai krāsa.\n\n<i><b>Svarīgi</b></i><i>: Vispirms raksti krāsu, pēc tam figūru. Neliek punktu. Izmanto noteikto galotni.</i>\n<i><b>Atbildes piemērs</b></i><i>: Sarkanais trijstūris</i>",
        text_en="There are four figures lying in a row on the table: a triangle, a circle, a rectangle and a rhombus. They are painted in different colors: red, blue, yellow and green.\n\nIt is known that the red figure lies between the blue and green; to the right of the yellow figure lies a rhombus; the circle lies to the right of both the triangle and the rhombus; the triangle does not lie on the edge; the blue and yellow figures do not lie next to each other.\n\nDetermine which figure and what color is <b>FOURTH</b> in order.\n\n<i><b>Warning</b></i><i>: In your answer, write the color first, then the shape. Don't put a full stop. Don't use articles.</i>\n<i><b>Answer example</b></i><i>: Red triangle</i>",
        text_ru="На столе лежат в ряд четыре фигуры: треугольник, круг, прямоугольник и ромб. Они окрашены в разные цвета: красный, синий, жёлтый, зелёный.\n\nИзвестно, что красная фигура лежит между синей и зелёной; справа от жёлтой фигуры лежит ромб; круг лежит правее и треугольника и ромба; треугольник лежит не с краю; синяя и жёлтая фигуры лежат не рядом.\n\nОпредели, какая фигура и какого цвета <b>ЧЕТВЁРТАЯ</b> по порядку.\n\n<i><b>Важно</b></i><i>: Сначала пиши цвет, потом фигуру. Не ставь точку. Используй букву Ё, если требуется.</i>\n<i><b>Пример ответа</b></i><i>: Жёлтый треугольник</i>",
        answer_lv="Zilais riņķis",
        answer_en="Blue circle",
        answer_ru="Синий круг",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )
    
    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Zālē pirms treniņa tikās sporta meistars Sirmais, sporta meistara kandidāts Melnais un audzēknis Rudains.\n\n— Paskatieties, — sacīja  melnmatainais, — viens no mums ir sirms, otrs ir rudmatains, trešais ir melnmatains. Taču nevienam no mums matu krāsa nesakrīt ar uzvārdu. Jocīgi, vai ne?\n— Tev taisnība, — apstiprināja sporta meistars.\n\nKādā matu krāsā ir <b>sporta meistara kandidātam</b>?',
        text_en='Master of Sports Mr.Gray, candidate for master Mr.Black and student Mr.Red met at the gym before training.\n\n"Pay attention," the black-haired man noted, "one of us is gray, the other is red-haired, and the third is black-haired. But none of us have the same hair color as our last name. It is funny, is not it?"\n"You are right," the master of sports confirmed.\n\nWhat hair color has <b>the candidate for master</b>?',
        text_ru="Мастер спорта Седов, кандидат в мастера Чернов и перворазрядник Рыжов встретились в зале перед тренировкой.\n\n— Обратите внимание, — заметил черноволосый, — один из нас седой, другой — рыжий, третий — черноволосый. Но ни у одного из нас цвет волос не совпадает с фамилией. Забавно, не правда ли?\n— Ты прав, — подтвердил мастер спорта.\n\nКакого цвета волосы у <b>кандидата в мастера</b>?",
        answer_lv="Pelēkā",
        answer_en="Gray",
        answer_ru="Седые",
        choices_lv=["Pelēkā", "Melnā", "Sarkanā"],
        choices_en=["Gray", "Black", "Red"],
        choices_ru=["Седые", "Чёрные", "Рыжие"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Zināms, ka starp Limonijas valdības locekļiem (kopā ir 20 locekļi) ir vismaz viens godīgs, kā arī zināms tas, ka no jebkuriem diviem vismaz viens ir kukuļņēmējs.\n\nCik daudz kukuļņēmēju ir valdībā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="It is known that among the members of the Limonian government (and there are 20 members in total) there is certainly at least one honest person, and also that out of any two at least one is a bribe-taker.\n\nHow many bribe-takers are there in the government?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Известно, что среди членов правительства Лимонии (а всего в нем 20 членов) заведомо имеется хотя бы один честный, а также что из любых двух хотя бы один – взяточник.\n\nСколько в правительстве взяточников?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="19",
        answer_en="19",
        answer_ru="19",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Vienīgie cilvēki, kas dzīvo uz salas, ir bruņinieki, kuri vienmēr saka patiesību, un meļi, kas vienmēr melo. Salas Domē ir 101 deputāts.\n\nLai ietaupītu budžetu, tika nolemts Domi samazināt par vienu deputātu. Bet katrs no deputātiem paziņoja, ka, ja viņu izņemtu no Domes, tad starp atlikušajiem deputātiem vairākums būtu meļi.\n\nCik bruņinieku un cik meļu ir domē?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti tādā formā: "<b>2 un 5</b>", ja atbilde ir 2 bruņinieki un 5 meļi.</i>',
        text_en="The island is inhabited only by knights, who always tell the truth, and liars, who always lie. The island's government has 101 deputies.\n\nIn order to reduce the budget, it was decided to reduce the government by one deputy. But each of the deputies declared that if he were removed from the government, then most of the remaining deputies would be liars.\n\nHow many knights and how many liars are there in the government?\n\n<i><b>Warning</b></i><i>: Write your answer in the form: '<b>2 and 5</b>', if the answer is 2 knights and 5 liars.</i>",
        text_ru='На острове живут только рыцари, которые всегда говорят правду, и лжецы, которые всегда лгут. В Думе острова – 101 депутат.\n\nВ целях сокращения бюджета было решено сократить Думу на одного депутата. Но каждый из депутатов заявил, что, если его выведут из состава Думы, то среди оставшихся депутатов большинство будут лжецами.\n\nСколько рыцарей и сколько лжецов в Думе?\n\n<i><b>Важно</b></i><i>: Ответ пиши в такой форме: "<b>2 и 5</b>", если ответ - 2 рыцаря и 5 лжецов.</i>',
        answer_lv="50 un 51",
        answer_en="50 and 51",
        answer_ru="50 и 51",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=8
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Rindā pie skolas kafejnīcas ir Vika, Sofija, Boriss, Deniss un Alla.\n\nVika ir priekšā Sofijai, bet aiz Allas; Boriss un Alla nestāv viens otram blakus; Deniss nav blakus Allai, Vikai vai Borisam.\n\nKādā secībā skolēni stāv?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti ar komatiem, ar atstarpēm, bez punkta beigās!</i>\n<i><b>Atbildes piemērs</b></i><i>: Deniss, Vika, Alla, Sofija, Boriss</i>",
        text_en="Vika, Sonya, Borya, Denis and Alla are standing in line at the school cafeteria.\n\nVika is in front of Sonya, but after Alla; Borya and Alla are not standing next to each other; Denis is not next to Alla, Vika or Borya.\n\nIn what order are the children standing?\n\n<i><b>Warning</b></i><i>: Write your answer separated by commas, with spaces, without a full stop at the end!</i>\n<i><b>Answer example</b></i><i>: Denis, Vika, Alla, Sonya, Borya</i>",
        text_ru="В очереди в школьный буфет стоят Вика, Соня, Боря, Денис и Алла.\n\nВика стоит впереди Сони, но после Аллы; Боря и Алла не стоят рядом; Денис не находится рядом ни с Аллой, ни с Викой, ни с Борей.\n\nВ каком порядке стоят ребята?\n\n<i><b>Важно</b></i><i>: Ответ пиши через запятую, с пробелами, без точки в конце!</i>\n<i><b>Пример ответа</b></i><i>: Денис, Вика, Алла, Соня, Боря</i>",
        answer_lv="Alla, Vika, Boriss, Sofija, Deniss",
        answer_en="Alla, Vika, Borya, Sonya, Denis",
        answer_ru="Алла, Вика, Боря, Соня, Денис",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Par sevi runāja 12 mēra kandidāti.\n\nPēc kāda laika viens teica: "Pirms manis meloja vienu reizi."\nCits teica: "Un tagad - divas reizes."\n"Un tagad - trīs reizes," sacīja trešais.\n Un tā tālāk līdz 12. datumam, kurš teica: "Un tagad viņi meloja 12 reizes."\n\nŠeit vadītājs pārtrauca diskusiju. Izrādījās, ka vismaz viens kandidāts pareizi saskaitīja, cik reizes pirms viņa ir melojuši. Tātad, cik reizes kandidāti ir melojuši?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='Twelve mayoral candidates were talking about themselves.\n\nAfter a while, one said, "They lied once before me."\nAnother said, "And now - twice."\n"And now - three times," said a third.\nAnd so on until the 12th, who said, "And now they have lied 12 times."\n\nAt this point, the moderator interrupted the discussion. It turned out that at least one candidate had correctly counted how many times they had lied before him. So how many times did the candidates lie in all?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='12 кандидатов в мэры рассказывали о себе.\n\nЧерез некоторое время один сказал: "До меня соврали один раз".\nДругой сказал: "А теперь – дважды".\n– "А теперь – трижды", – сказал третий.\nИ так далее до 12-го, который сказал: "А теперь соврали 12 раз".\n\nТут ведущий прервал дискуссию. Оказалось, что по крайней мере один кандидат правильно подсчитал, сколько раз соврали до него. Так сколько же раз всего соврали кандидаты?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="12",
        answer_en="12",
        answer_ru="12",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Uz salas dzīvo divas ciltis: aborigēni un citplanētieši. Aborigēni vienmēr saka patiesību, bet citplanētieši vienmēr melo.\n\nCeļotājs, kurš ieradās salā, nolīga salas iedzīvotāju par gidu. Viņi gāja un ieraudzīja citu salas iedzīvotāju. Ceļotājs nosūtīja savu gidu noskaidrot, kurai ciltij pieder šis salas iedzīvotājs.\n\nGids atgriezās un teica: "Salas iedzīvotājs saka, ka viņš ir aborigēns."\n\nKas bija <b>gids</b>: citplanētietis vai aborigēns?',
        text_en='There are two tribes living on the island: the natives and the aliens. The natives always tell the truth, and the aliens always lie.\n\nA traveler who came to the island hired an islander as a guide. They went and saw another islander. The traveler sent the guide to find out which tribe the islander belonged to.\n\nThe guide returned and said: "The islander says he is a native."\n\nWho was the <b>guide</b>: an alien or a native?',
        text_ru='На острове живут два племени: аборигены и пришельцы. Аборигены всегда говорят правду, а пришельцы всегда лгут.\n\nПутешественник, приехавший на остров, нанял островитянина в проводники. Они пошли и увидели другого островитянина. Путешественник послал проводника узнать, к какому племени принадлежит этот туземец.\n\nПроводник вернулся и сказал: "Туземец говорит, что он абориген".\n\nКем был <b>проводник</b>: пришельцем или аборигеном?',
        answer_lv="Aborigēns",
        answer_en="A native",
        answer_ru="Аборигеном",
        choices_lv=["Citplanētietis", "Aborigēns"],
        choices_en=["An alien", "A native"],
        choices_ru=["Пришельцем", "Аборигеном"],
        points=5
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Viens no pieciem brāļiem mammai izcepa pīrāgu.\n\n<b>Andrejs</b>teica: "Pīrāgu izcepa Viktors vai Anatolijs."\n<b>Viktors</b> teica: "Tas nebiju es vai Jura."\n<b>Anatolijs</b> teica: "Jūs abi jokojat."\n<b>Dima</b> teica: "Nē, viens no viņiem teica patiesību, bet otrs nē.”\n<b >Jura</b>teica: "Nē, Dima, tu kļūdies."\n\nMamma zina, ka trīs viņas dēli vienmēr teic patiesību.\nKas izcepa pīrāgu?',
        text_en='One of the five brothers baked a pie for Mom.\n\n<b>Andrey</b> said: "It was Vitya or Tolya."\n<b>Vitya</b> said: "It was not me or Yura who did it."\n<b>Tolya</b> said: "You are both joking."\n<b>Dima</b> said: "No, one of them told the truth and the other did not."\n<b>Yura</b> said: "No, Dima, you are wrong."\n\nMom knows that three of her sons always tell the truth.\nWho baked the pie?',
        text_ru='Один из пяти братьев испек маме пирог.\n\n<b>Андрей</b> сказал: "Это Витя или Толя".\n<b>Витя</b> сказал: "Это сделал не я и не Юра".\n<b>Толя</b> сказал: "Вы оба шутите".\n<b>Дима</b> сказал: "Нет, один из них сказал правду, а другой — нет".\n<b>Юра</b> сказал: "Нет, Дима, ты не прав".\n\nМама знает, что трое из ее сыновей всегда говорят правду.\nКто испек пирог?',
        answer_lv="Anatolijs",
        answer_en="Tolya",
        answer_ru="Толя",
        choices_lv=["Andrejs", "Viktors", "Anatolijs", "Dima", "Jura"],
        choices_en=["Andrey", "Vitya", "Tolya", "Dima", "Yura"],
        choices_ru=["Андрей", "Витя", "Толя", "Дима", "Юра"],
        points=8
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir ALEKSANDRS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is ALEXANDER and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является АЛЕКСАНДР и где он живёт?",
        answer_lv="Arheologs no Austrijas",
        answer_en="Archaeologist from Austria",
        answer_ru="Археолог из Австрии",
        choices_lv=["Būvnieks no Bulgārijas", "Arhitekts no Brazīlijas", "Arheologs no Austrijas", "Arheologs no Bulgārijas"],
        choices_en=["Builder from Bulgaria", "Architect from Brazil", "Archaeologist from Austria", "Archaeologist from Bulgaria"],
        choices_ru=["Бухгалтер из Болгарии", "Архитектор из Бразилии", "Археолог из Австрии", "Археолог из Болгарии"],
        points=3
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir BENDŽAMINS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is BENJAMIN and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является БЕНДЖАМИН и где он живёт?",
        answer_lv="Arhitekts no Brazīlijas",
        answer_en="Architect from Brazil",
        answer_ru="Архитектор из Бразилии",
        choices_lv=["Būvnieks no Austrijas", "Arheologs no Brazīlijas", "Arhitekts no Bulgārijas", "Arhitekts no Brazīlijas"],
        choices_en=["Builder from Austria", "Archaeologist from Brazil", "Architect from Bulgaria", "Architect from Brazil"],
        choices_ru=["Бухгалтер из Австрии", "Археолог из Брализии", "Архитектор из Болгарии", "Архитектор из Бразилии"],
        points=3
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir BORISS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is BORIS and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является БОРИС и где он живёт?",
        answer_lv="Būvnieks no Bulgārijas",
        answer_en="Builder from Bulgaria",
        answer_ru="Бухгалтер из Болгарии",
        choices_lv=["Būvnieks no Bulgārijas", "Būvnieks no Austrijas", "Arhitekts no Bulgārijas", "Arheologs no Austrijas"],
        choices_en=["Builder from Bulgaria", "Builder from Austria", "Architect from Bulgaria", "Archaeologist from Austria"],
        choices_ru=["Бухгалтер из Болгарии", "Бухгалтер из Австрии", "Архитектор из Болгарии", "Археолог из Австрии"],
        points=3
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Trīs draugi – Pēteris, Romāns un Sergejs – mācās matemātikas, fizikas un ķīmijas fakultātēs.\n\nJa Pēteris ir matemātiķis, tad Sergejs nav fiziķis. Ja Romāns nav fiziķis, tad Pēteris ir matemātiķis. Ja Sergejs nav matemātiķis, tad Romāns ir ķīmiķis.\n\nKas ir PĒTERIS?",
        text_en="Three friends - Peter, Roman and Sergey - study at the faculties of mathematics, physics and chemistry.\n\nIf Peter is a mathematician, then Sergey is not a physicist. If Roman is not a physicist, then Peter is a mathematician. If Sergey is not a mathematician, then Roman is a chemist.\n\nWho is PETER?",
        text_ru="Три друга — Пётр, Роман и Сергей — учатся на математическом, физическом и химическом факультетах.\n\nЕсли Пётр математик, то Сергей не физик. Если Роман не физик, то Пётр математик. Если Сергей не математик, то Роман — химик.\n\nКем является ПЁТР?",
        answer_lv="Ķīmiķis",
        answer_en="Chemist",
        answer_ru="Химик",
        choices_lv=["Matemātiķis", "Fiziķis", "Ķīmiķis"],
        choices_en=["Mathematician", "Physicist", "Chemist"],
        choices_ru=["Математик", "Физик", "Химик"],
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Trīs draugi – Pēteris, Romāns un Sergejs – mācās matemātikas, fizikas un ķīmijas fakultātēs.\n\nJa Pēteris ir matemātiķis, tad Sergejs nav fiziķis. Ja Romāns nav fiziķis, tad Pēteris ir matemātiķis. Ja Sergejs nav matemātiķis, tad Romāns ir ķīmiķis.\n\nKas ir ROMĀNS?",
        text_en="Three friends - Peter, Roman and Sergey - study at the faculties of mathematics, physics and chemistry.\n\nIf Peter is a mathematician, then Sergey is not a physicist. If Roman is not a physicist, then Peter is a mathematician. If Sergey is not a mathematician, then Roman is a chemist.\n\nWho is ROMAN?",
        text_ru="Три друга — Пётр, Роман и Сергей — учатся на математическом, физическом и химическом факультетах.\n\nЕсли Пётр математик, то Сергей не физик. Если Роман не физик, то Пётр математик. Если Сергей не математик, то Роман — химик.\n\nКем является РОМАН?",
        answer_lv="Fiziķis",
        answer_en="Physicist",
        answer_ru="Физик",
        choices_lv=["Matemātiķis", "Fiziķis", "Ķīmiķis"],
        choices_en=["Mathematician", "Physicist", "Chemist"],
        choices_ru=["Математик", "Физик", "Химик"],
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv="Trīs draugi – Pēteris, Romāns un Sergejs – mācās matemātikas, fizikas un ķīmijas fakultātēs.\n\nJa Pēteris ir matemātiķis, tad Sergejs nav fiziķis. Ja Romāns nav fiziķis, tad Pēteris ir matemātiķis. Ja Sergejs nav matemātiķis, tad Romāns ir ķīmiķis.\n\nKas ir SERGEJS?",
        text_en="Three friends - Peter, Roman and Sergey - study at the faculties of mathematics, physics and chemistry.\n\nIf Peter is a mathematician, then Sergey is not a physicist. If Roman is not a physicist, then Peter is a mathematician. If Sergey is not a mathematician, then Roman is a chemist.\n\nWho is SERGEY?",
        text_ru="Три друга — Пётр, Роман и Сергей — учатся на математическом, физическом и химическом факультетах.\n\nЕсли Пётр математик, то Сергей не физик. Если Роман не физик, то Пётр математик. Если Сергей не математик, то Роман — химик.\n\nКем является СЕРГЕЙ?",
        answer_lv="Matemātiķis",
        answer_en="Mathematician",
        answer_ru="Математик",
        choices_lv=["Matemātiķis", "Fiziķis", "Ķīmiķis"],
        choices_en=["Mathematician", "Physicist", "Chemist"],
        choices_ru=["Математик", "Физик", "Химик"],
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv='Telpā ir 12 cilvēki; daži no viņiem ir godīgi, tas ir, viņi vienmēr saka patiesību, pārējie vienmēr melo.\n\n"Šeit nav neviena godīga cilvēka," sacīja pirmais.\n"Šeit nav vairāk par vienu godīgu cilvēku," teica otrs.\nTrešais teica, ka nav vairāk par diviem godīgiem cilvēkiem, ceturtais - ka nav vairāk par trim, un tā līdz divpadsmitajam, kurš teica, ka godīgu cilvēku nav vairāk par vienpadsmit.\n\nCik godīgu cilvēku patiesībā ir telpā?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='There are 12 people in a room; some of them are honest, that is, they always tell the truth, the rest always lie.\n\n"There is not a single honest person here," said the first.\n"There is no more than one honest person here," said the second.\nThe third said that there are no more than two honest people, the fourth - no more than three, and so on until the twelfth, who said that there are no more than eleven honest people.\n\nHow many honest people are there in the room, really?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='В комнате 12 человек; некоторые из них честные, то есть всегда говорят правду, остальные всегда лгут.\n\n"Здесь нет ни одного честного человека", - сказал первый.\n"Здесь не более одного честного человека", - сказал второй.\nТретий сказал, что честных не более двух, четвёртый - что не более трёх, и так далее до двенадцатого, который сказал, что честных людей не более одиннадцати.\n\nСколько честных людей в комнате на самом деле?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="6",
        answer_en="6",
        answer_ru="6",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=10
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Pilsētā dzīvo bruņinieki un meļi. Bruņinieki vienmēr saka patiesību, un meļi vienmēr melo.\n\nDivi bruņinieki un divi meļi sapulcējās kopā un paskatījās viens uz otru.\n\nKurš no viņiem varētu pateikt frāzi: “Mēs VISI esam bruņinieki”?',
        text_en='Knights and liars live in the city. Knights always tell the truth, and liars always lie.\n\nTwo knights and two liars got together and looked at each other.\n\nWhich of them could say the phrase: "Among us ALL are knights"?',
        text_ru='В городе живут рыцари и лжецы. Рыцари всегда говорят правду, а лжецы всегда лгут.\n\nСобрались вместе два рыцаря и два лжеца и посмотрели друг на друга.\n\nКто из них мог сказать фразу: "Cреди нас ВСЕ рыцари"?',
        answer_lv="Tikai melis",
        answer_en="Only a liar",
        answer_ru="Только лжец",
        choices_lv=["Tikai bruņinieks", "Tikai melis", "Gan bruņinieks, gan melis", "Neviens"],
        choices_en=["Only a knight", "Only a liar", "Both a knight and a liar", "Nobody"],
        choices_ru=["Только рыцарь", "Только лжец", "И рыцарь, и лжец", "Никто"],
        points=2
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Pilsētā dzīvo bruņinieki un meļi. Bruņinieki vienmēr saka patiesību, un meļi vienmēr melo.\n\nDivi bruņinieki un divi meļi sapulcējās kopā un paskatījās viens uz otru.\n\nKurš no viņiem varētu pateikt frāzi: “Ir tieši VIENS bruņinieks starp jums”?',
        text_en='Knights and liars live in the city. Knights always tell the truth, and liars always lie.\n\nTwo knights and two liars got together and looked at each other.\n\nWhich of them could say the phrase: "There is exactly ONE knight among you"?',
        text_ru='В городе живут рыцари и лжецы. Рыцари всегда говорят правду, а лжецы всегда лгут.\n\nСобрались вместе два рыцаря и два лжеца и посмотрели друг на друга.\n\nКто из них мог сказать фразу: "Среди вас есть ровно ОДИН рыцарь"?',
        answer_lv="Gan bruņinieks, gan melis",
        answer_en="Both a knight and a liar",
        answer_ru="И рыцарь, и лжец",
        choices_lv=["Tikai bruņinieks", "Tikai melis", "Gan bruņinieks, gan melis", "Neviens"],
        choices_en=["Only a knight", "Only a liar", "Both a knight and a liar", "Nobody"],
        choices_ru=["Только рыцарь", "Только лжец", "И рыцарь, и лжец", "Никто"],
        points=3
    )

    await rq.add_task(
        grade=8,
        input_type="multiple_choice",
        text_lv='Pilsētā dzīvo bruņinieki un meļi. Bruņinieki vienmēr saka patiesību, un meļi vienmēr melo.\n\nDivi bruņinieki un divi meļi sapulcējās kopā un paskatījās viens uz otru.\n\nKurš no viņiem varētu pateikt frāzi: “Starp jums ir tieši DIVI bruņinieki”?',
        text_en='Knights and liars live in the city. Knights always tell the truth, and liars always lie.\n\nTwo knights and two liars got together and looked at each other.\n\nWhich of them could say the phrase: "There are exactly TWO knights among you"?',
        text_ru='В городе живут рыцари и лжецы. Рыцари всегда говорят правду, а лжецы всегда лгут.\n\nСобрались вместе два рыцаря и два лжеца и посмотрели друг на друга.\n\nКто из них мог сказать фразу: "Среди вас есть ровно ДВА рыцаря"?',
        answer_lv="Neviens",
        answer_en="Nobody",
        answer_ru="Никто",
        choices_lv=["Tikai bruņinieks", "Tikai melis", "Gan bruņinieks, gan melis", "Neviens"],
        choices_en=["Only a knight", "Only a liar", "Both a knight and a liar", "Nobody"],
        choices_ru=["Только рыцарь", "Только лжец", "И рыцарь, и лжец", "Никто"],
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="378",
        answer_en="378",
        answer_ru="378",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>ötszáz tizenhét</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>ötszáz tizenhét</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>ötszáz tizenhét</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="517",
        answer_en="517",
        answer_ru="517",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=8,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nUzraksti skaitli <b>306</b> ungāru valodā!\n\n<i><b>Svarīgi</b></i><i>: Obligāti raksti atbildi ar unikālām ungāru burtu rakstzīmēm. Kopē, ja tie nav uz tavas tastatūras.</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWrite the number <b>306</b> in Hungarian!\n\n<i><b>Warning</b></i><i>: Be sure to write the answer with unique symbols of Hungarian letters. Copy if they are not in your keyboard.</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nЗапиши по-венгерски число <b>306</b>!\n\n<i><b>Важно</b></i><i>: Обязательно пиши ответ с уникальными символами венгерских букв. Скопируй, если их нет в твоей клавиатуре.</i>",
        answer_lv="háromszáz hat",
        answer_en="háromszáz hat",
        answer_ru="háromszáz hat",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    # для 9 класса
    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>háromszáz hetven nyolc</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="378",
        answer_en="378",
        answer_ru="378",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>ötszáz tizenhét</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>ötszáz tizenhét</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>ötszáz tizenhét</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="517",
        answer_en="517",
        answer_ru="517",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nKāds ir šis skaitlis — <b>ezer hatszáz tíz</b>?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWhat is this number — <b>ezer hatszáz tíz</b>?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nКакое это число — <b>ezer hatszáz tíz</b>?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="1610",
        answer_en="1610",
        answer_ru="1610",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nUzraksti skaitli <b>306</b> ungāru valodā!\n\n<i><b>Svarīgi</b></i><i>: Obligāti raksti atbildi ar unikālām ungāru burtu rakstzīmēm. Kopē, ja tie nav uz tavas tastatūras.</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWrite the number <b>306</b> in Hungarian!\n\n<i><b>Warning</b></i><i>: Be sure to write the answer with unique symbols of Hungarian letters. Copy if they are not in your keyboard.</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nЗапиши по-венгерски число <b>306</b>!\n\n<i><b>Важно</b></i><i>: Обязательно пиши ответ с уникальными символами венгерских букв. Скопируй, если их нет в твоей клавиатуре.</i>",
        answer_lv="háromszáz hat",
        answer_en="háromszáz hat",
        answer_ru="háromszáz hat",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Šeit ir daži ungāru valodā rakstīti cipari:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nUzraksti skaitli <b>812</b> ungāru valodā!\n\n<i><b>Svarīgi</b></i><i>: Obligāti raksti atbildi ar unikālām ungāru burtu rakstzīmēm. Kopē, ja tie nav uz tavas tastatūras.</i>",
        text_en="Here are some numerals written in Hungarian:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nWrite the number <b>812</b> in Hungarian!\n\n<i><b>Warning</b></i><i>: Be sure to write the answer with unique symbols of Hungarian letters. Copy if they are not in your keyboard.</i>",
        text_ru="Вот несколько числительных, записанных по-венгерски:\n\n43 | negyven három\n197 | száz kilencven hét\n284 | kétszáz nyolcven négy\n772 | hétszáz hetven két\n58 | ötven nyolc\n246 | kétszáz negyven hat\n375 | háromszáz hetven öt\n910 | kilencszáz tíz\n\nЗапиши по-венгерски число <b>812</b>!\n\n<i><b>Важно</b></i><i>: Обязательно пиши ответ с уникальными символами венгерских букв. Скопируй, если их нет в твоей клавиатуре.</i>",
        answer_lv="nyolcszáz kéthét",
        answer_en="nyolcszáz kéthét",
        answer_ru="nyolcszáz kéthét",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv='Vienīgie cilvēki, kas dzīvo uz salas, ir bruņinieki, kuri vienmēr saka patiesību, un meļi, kas vienmēr melo. Salas Domē ir 101 deputāts.\n\nLai ietaupītu budžetu, tika nolemts Domi samazināt par vienu deputātu. Bet katrs no deputātiem paziņoja, ka, ja viņu izņemtu no Domes, tad starp atlikušajiem deputātiem vairākums būtu meļi.\n\nCik bruņinieku un cik meļu ir domē?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti tādā formā: "<b>2 un 5</b>", ja atbilde ir 2 bruņinieki un 5 meļi.</i>',
        text_en="The island is inhabited only by knights, who always tell the truth, and liars, who always lie. The island's government has 101 deputies.\n\nIn order to reduce the budget, it was decided to reduce the government by one deputy. But each of the deputies declared that if he were removed from the government, then most of the remaining deputies would be liars.\n\nHow many knights and how many liars are there in the government?\n\n<i><b>Warning</b></i><i>: Write your answer in the form: '<b>2 and 5</b>', if the answer is 2 knights and 5 liars.</i>",
        text_ru='На острове живут только рыцари, которые всегда говорят правду, и лжецы, которые всегда лгут. В Думе острова – 101 депутат.\n\nВ целях сокращения бюджета было решено сократить Думу на одного депутата. Но каждый из депутатов заявил, что, если его выведут из состава Думы, то среди оставшихся депутатов большинство будут лжецами.\n\nСколько рыцарей и сколько лжецов в Думе?\n\n<i><b>Важно</b></i><i>: Ответ пиши в такой форме: "<b>2 и 5</b>", если ответ - 2 рыцаря и 5 лжецов.</i>',
        answer_lv="50 un 51",
        answer_en="50 and 51",
        answer_ru="50 и 51",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv='Par sevi runāja 12 mēra kandidāti.\n\nPēc kāda laika viens teica: "Pirms manis meloja vienu reizi."\nCits teica: "Un tagad - divas reizes."\n"Un tagad - trīs reizes," sacīja trešais.\n Un tā tālāk līdz 12. datumam, kurš teica: "Un tagad viņi meloja 12 reizes."\n\nŠeit vadītājs pārtrauca diskusiju. Izrādījās, ka vismaz viens kandidāts pareizi saskaitīja, cik reizes pirms viņa ir melojuši. Tātad, cik reizes kandidāti ir melojuši?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='Twelve mayoral candidates were talking about themselves.\n\nAfter a while, one said, "They lied once before me."\nAnother said, "And now - twice."\n"And now - three times," said a third.\nAnd so on until the 12th, who said, "And now they have lied 12 times."\n\nAt this point, the moderator interrupted the discussion. It turned out that at least one candidate had correctly counted how many times they had lied before him. So how many times did the candidates lie in all?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='12 кандидатов в мэры рассказывали о себе.\n\nЧерез некоторое время один сказал: "До меня соврали один раз".\nДругой сказал: "А теперь – дважды".\n– "А теперь – трижды", – сказал третий.\nИ так далее до 12-го, который сказал: "А теперь соврали 12 раз".\n\nТут ведущий прервал дискуссию. Оказалось, что по крайней мере один кандидат правильно подсчитал, сколько раз соврали до него. Так сколько же раз всего соврали кандидаты?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="12",
        answer_en="12",
        answer_ru="12",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv='Uz salas dzīvo meļi un bruņinieki, kopā 2001 cilvēks. Bruņinieki vienmēr saka patiesību, un meļi melo.\n\nKatrs salas iedzīvotājs teica: "No atlikušajiem salas iedzīvotājiem vairāk nekā puse ir meļi."\n\nCik daudz meļu ir salā?',
        text_en='There are liars and knights on the island, 2001 people in total. Knights always tell the truth, and liars always lie.\n\nEach islander said: "Of the remaining islanders, more than half are liars."\n\nHow many liars are on the island?',
        text_ru='На острове живут лжецы и рыцари, всего 2001 человек. Рыцари всегда говорят правду, а лжецы лгут.\n\nКаждый житель острова заявил: "Среди оставшихся жителей острова более половины - лжецы".\n\nСколько лжецов на острове?',
        answer_lv='1001',
        answer_en='1001',
        answer_ru='1001',
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=3
    )
    
    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir ALEKSANDRS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is ALEXANDER and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является АЛЕКСАНДР и где он живёт?",
        answer_lv="Arheologs no Austrijas",
        answer_en="Archaeologist from Austria",
        answer_ru="Археолог из Австрии",
        choices_lv=["Būvnieks no Bulgārijas", "Arhitekts no Brazīlijas", "Arheologs no Austrijas", "Arheologs no Bulgārijas"],
        choices_en=["Builder from Bulgaria", "Architect from Brazil", "Archaeologist from Austria", "Archaeologist from Bulgaria"],
        choices_ru=["Бухгалтер из Болгарии", "Архитектор из Бразилии", "Археолог из Австрии", "Археолог из Болгарии"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir BENDŽAMINS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is BENJAMIN and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является БЕНДЖАМИН и где он живёт?",
        answer_lv="Arhitekts no Brazīlijas",
        answer_en="Architect from Brazil",
        answer_ru="Архитектор из Бразилии",
        choices_lv=["Būvnieks no Austrijas", "Arheologs no Brazīlijas", "Arhitekts no Bulgārijas", "Arhitekts no Brazīlijas"],
        choices_en=["Builder from Austria", "Archaeologist from Brazil", "Architect from Bulgaria", "Architect from Brazil"],
        choices_ru=["Бухгалтер из Австрии", "Археолог из Брализии", "Архитектор из Болгарии", "Архитектор из Бразилии"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Iepazīsimies ar trim cilvēkiem: Aleksandru, Bendžaminu un Borisu. Viens no viņiem ir arhitekts, otrs – būvnieks, bet trešais – arheologs. Viens dzīvo Brazīlijā, otrs Bulgārijā, trešais Austrijā.\n\n1) Boriss Brazīliju apmeklē tikai īslaicīgi un ļoti reti, lai gan visi viņa radinieki pastāvīgi dzīvo šajā valstī.\n2) Diviem no šiem cilvēkiem profesijas un valstis, kurās viņi dzīvo, sākas ar to pašu burtu kā viņu vārdi.\n3) Arhitekta sieva ir Borisa jaunākā māsa.\n\nKas ir BORISS un kur viņš dzīvo?",
        text_en="Let's meet three people: Alexander, Benjamin and Boris. One of them is an architect, another is a builder, the third is an archaeologist. One lives in Brazil, another in Bulgaria, the third in Austria.\n\n1) Boris only visits Brazil occasionally and very rarely, although all his relatives live permanently in this country.\n2) The names of the professions and countries in which two of these people live begin with the same letter as their names.\n3) The architect's wife is Boris's younger sister.\n\nWho is BORIS and where does he live?",
        text_ru="Познакомимся с тремя людьми: Александром, Бенджамином и Борисом. Один из них – архитектор, другой – бухгалтер, третий – археолог. Один живет в Бразилии, другой – в Болгарии, третий в Австрии.\n\n1) Борис бывает в Бразилии лишь наездами и то весьма редко, хотя все его родственники постоянно живут в этой стране.\n2) У двух из этих людей названия профессий и стран, в которых они живут, начинаются с той же буквы, что и их имена.\n3) Жена архитектора доводится Борису младшей сестрой.\n\nКем является БОРИС и где он живёт?",
        answer_lv="Būvnieks no Bulgārijas",
        answer_en="Builder from Bulgaria",
        answer_ru="Бухгалтер из Болгарии",
        choices_lv=["Būvnieks no Bulgārijas", "Būvnieks no Austrijas", "Arhitekts no Bulgārijas", "Arheologs no Austrijas"],
        choices_en=["Builder from Bulgaria", "Builder from Austria", "Architect from Bulgaria", "Archaeologist from Austria"],
        choices_ru=["Бухгалтер из Болгарии", "Бухгалтер из Австрии", "Архитектор из Болгарии", "Археолог из Австрии"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Rakstnieces Dorisas Kejas trīs meitas Džūdija, Īrisa un Linda ir ļoti talantīgas. Viņi ieguva slavu dažādos mākslas veidos – dziedāšanā, baletā un kino. Viņi visi dzīvo dažādās pilsētās, tāpēc Dorisa viņiem bieži zvana uz Parīzi, Romu un Čikāgu.\n\nIr zināms, ka:\n- Džūdija nedzīvo Parīzē, un Linda nedzīvo Romā;\n- parīziete nefilmējas kino;\n- sieviete, kas dzīvo Romā, ir dziedātāja;\n- Linda ir vienaldzīga pret baletu.\n\nKur dzīvo ĪRISA un kāda ir viņas profesija?",
        text_en="The three daughters of the writer Doris Kay - Judy, Iris and Linda - are very talented. They have gained fame in different arts - singing, ballet and cinema. They all live in different cities, so Doris often calls them in Paris, Rome and Chicago.\n\nIt is known that:\n- Judy does not live in Paris, and Linda does not live in Rome;\n- the Parisian does not act in films;\n- the one who lives in Rome is a singer;\n- Linda is indifferent to ballet.\n\nWhere does IRIS live and what is her profession?",
        text_ru="Три дочери писательницы Дорис Кей — Джуди, Айрис и Линда, очень талантливы. Они приобрели известность в разных видах искусств — пении, балете и кино. Все они живут в разных городах, поэтому Дорис часто звонит им в Париж, Рим и Чикаго.\n\nИзвестно, что:\n- Джуди живет не в Париже, а Линда — не в Риме;\n- парижанка не снимается в кино;\n- та, кто живет в Риме, певица;\n- Линда равнодушна к балету.\n\nГде живет АЙРИС, и какова ее профессия?",
        answer_lv="Balerīna no Parīzes",
        answer_en="Ballerina from Paris",
        answer_ru="Балерина из Парижа",
        choices_lv=["Dziedātāja no Romas", "Balerīna no Parīzes", "Aktrise no Čikāgas", "Balerīna no Čikāgas"],
        choices_en=["Singer from Rome", "Ballerina from Paris", "Actress from Chicago", "Ballerina from Chicago"],
        choices_ru=["Певица из Рима", "Балерина из Парижа", "Актриса из Чикаго", "Балерина из Чикаго"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Rakstnieces Dorisas Kejas trīs meitas Džūdija, Īrisa un Linda ir ļoti talantīgas. Viņi ieguva slavu dažādos mākslas veidos – dziedāšanā, baletā un kino. Viņi visi dzīvo dažādās pilsētās, tāpēc Dorisa viņiem bieži zvana uz Parīzi, Romu un Čikāgu.\n\nIr zināms, ka:\n- Džūdija nedzīvo Parīzē, un Linda nedzīvo Romā;\n- parīziete nefilmējas kino;\n- sieviete, kas dzīvo Romā, ir dziedātāja;\n- Linda ir vienaldzīga pret baletu.\n\nKur dzīvo LINDA un kāda ir viņas profesija?",
        text_en="The three daughters of the writer Doris Kay - Judy, Iris and Linda - are very talented. They have gained fame in different arts - singing, ballet and cinema. They all live in different cities, so Doris often calls them in Paris, Rome and Chicago.\n\nIt is known that:\n- Judy does not live in Paris, and Linda does not live in Rome;\n- the Parisian does not act in films;\n- the one who lives in Rome is a singer;\n- Linda is indifferent to ballet.\n\nWhere does LINDA live and what is her profession?",
        text_ru="Три дочери писательницы Дорис Кей — Джуди, Айрис и Линда, очень талантливы. Они приобрели известность в разных видах искусств — пении, балете и кино. Все они живут в разных городах, поэтому Дорис часто звонит им в Париж, Рим и Чикаго.\n\nИзвестно, что:\n- Джуди живет не в Париже, а Линда — не в Риме;\n- парижанка не снимается в кино;\n- та, кто живет в Риме, певица;\n- Линда равнодушна к балету.\n\nГде живет ЛИНДА, и какова ее профессия?",
        answer_lv="Aktrise no Čikāgas",
        answer_en="Actress from Chicago",
        answer_ru="Актриса из Чикаго",
        choices_lv=["Aktrise no Parīzes", "Aktrise no Čikāgas"],
        choices_en=["Actress from Paris", "Actress from Chicago"],
        choices_ru=["Актриса из Парижа", "Актриса из Чикаго"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Rakstnieces Dorisas Kejas trīs meitas Džūdija, Īrisa un Linda ir ļoti talantīgas. Viņi ieguva slavu dažādos mākslas veidos – dziedāšanā, baletā un kino. Viņi visi dzīvo dažādās pilsētās, tāpēc Dorisa viņiem bieži zvana uz Parīzi, Romu un Čikāgu.\n\nIr zināms, ka:\n- Džūdija nedzīvo Parīzē, un Linda nedzīvo Romā;\n- parīziete nefilmējas kino;\n- sieviete, kas dzīvo Romā, ir dziedātāja;\n- Linda ir vienaldzīga pret baletu.\n\nKur dzīvo DŽŪDIJA un kāda ir viņas profesija?",
        text_en="The three daughters of the writer Doris Kay - Judy, Iris and Linda - are very talented. They have gained fame in different arts - singing, ballet and cinema. They all live in different cities, so Doris often calls them in Paris, Rome and Chicago.\n\nIt is known that:\n- Judy does not live in Paris, and Linda does not live in Rome;\n- the Parisian does not act in films;\n- the one who lives in Rome is a singer;\n- Linda is indifferent to ballet.\n\nWhere does JUDY live and what is her profession?",
        text_ru="Три дочери писательницы Дорис Кей — Джуди, Айрис и Линда, очень талантливы. Они приобрели известность в разных видах искусств — пении, балете и кино. Все они живут в разных городах, поэтому Дорис часто звонит им в Париж, Рим и Чикаго.\n\nИзвестно, что:\n- Джуди живет не в Париже, а Линда — не в Риме;\n- парижанка не снимается в кино;\n- та, кто живет в Риме, певица;\n- Линда равнодушна к балету.\n\nГде живет ДЖУДИ, и какова ее профессия?",
        answer_lv="Dziedātāja no Romas",
        answer_en="Singer from Rome",
        answer_ru="Певица из Рима",
        choices_lv=["Dziedātāja no Romas", "Aktrise no Čikāgas", "Balerīna no Čikāgas"],
        choices_en=["Singer from Rome", "Actress from Chicago", "Ballerina from Chicago"],
        choices_ru=["Певица из Рима", "Актриса из Чикаго", "Балерина из Чикаго"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Mēģinot atcerēties pagājušā gada turnīra uzvarētājus, pieci bijušie turnīra skatītāji teica:\n\n- Antons bija otrais, un Boriss bija piektais.\n- Viktors bija otrais, un Deniss bija trešais.\n- Grigorijs bija pirmais, un Boriss bija trešais.\n- Antons bija trešais, un Jevgeņijs bija sestais.\n- Viktors bija trešais, un Jevgeņijs bija ceturtais.\n\nVēlāk izrādījās, ka katrs skatītājs kļūdījās vienā no saviem diviem paziņojumiem.\nKāds bija patiesais vietu sadalījums turnīrā?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti vietu dilstošā secībā (no pirmās līdz sestajai), bez cipariem, atdalot ar komatiem, ar atstarpēm, bez punkta beigās!</i>\n<i><b>Atbildes piemērs</b></i><i>: Deniss, Antons, Jevgeņijs, Viktors, Boriss, Grigorijs</i>!",
        text_en="Trying to remember the winners of last year's tournament, five former spectators of the tournament stated:\n\n- Anton was second, and Boris was fifth.\n- Victor was second, and Denis was third.\n- Grigory was first, and Boris was third.\n- Anton was third, and Evgeniy was sixth.\n- Victor was third, and Evgeniy was fourth.\n\nLater, it turned out that each spectator was wrong in one of their two statements.\nWhat was the true distribution of places in the tournament?\n\n<i><b>Warning</b></i><i>: Write your answer in descending order of places (from first to sixth), without numbers, separated by commas, with spaces, without a full stop at the end!</i>\n<i><b>Answer example</b></i><i>: Denis, Anton, Evgeny, Victor, Boris, Grigory</i>",
        text_ru="Пытаясь вспомнить победителей прошлогоднего турнира, пять бывших зрителей турнира заявили:\n\n- Антон был вторым, а Борис - пятым.\n- Виктор был вторым, а Денис - третьим.\n- Григорий был первый, а Борис - третьим.\n- Антон был третьим, а Евгений - шестым.\n- Виктор был третьим, а Евгений - четвертым.\n\nВпоследствии выяснилось, что каждый зритель ошибся в одном из двух своих высказываний.\nКаково было истинное распределение мест в турнире?\n\n<i><b>Важно</b></i><i>: Ответ пиши в порядке убывания мест (с первого по шестое), без цифр, через запятую, с пробелами, без точки в конце!</i>\n<i><b>Пример ответа</b></i><i>: Денис, Антон, Евгений, Виктор, Борис, Григорий</i>",
        answer_lv="Grigorijs, Viktors, Antons, Jevgeņijs, Boriss, Deniss",
        answer_en="Grigory, Victor, Anton, Evgeniy, Boris, Denis",
        answer_ru="Григорий, Виктор, Антон, Евгений, Борис, Денис",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=12
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Skolā četriem skolēniem - Andrejevam, Kostinam, Saveļjevam un Davidovam - tika uzdots tīrīt kabinetus №7, №8, №9 un №10. Skolēni ziņoja par sekojošo:\n\n- Andrejevs: "Es tīrīju kabinetu №9, un Saveļjevs - №7."\n- Kostins: "Es tīrīju kabinetu №9, un Andrejevs - №8."\n- Saveļjevs: "Es tīrīju kabinetu №8, un Kostins №10."\n\nDavidovs neko neteica. Vēlāk izrādījās, ka katrs skolēns teica patiesību vienā no saviem diviem apgalvojumiem, bet otrais ir aplams. Kuru kabinetu katrs skolēns tīrīja?\n\nA) Saveļjevs 7, Andrejevs 9, Kostins 10, Davidovs 8.\nB) Saveļjevs 8, Andrejevs 7, Kostins 10, Davidovs 9.\nC) Saveļjevs 10, Andrejevs 8, Kostins 9, Davidovs 7.\nD) Saveļjevs 7, Andrejevs 9, Kostins 10, Davidovs 8.\nE) Saveļjevs 7, Andrejevs 8, Kostins 10, Davidovs 9.',
        text_en='At school, four students - Andreev, Kostin, Savelyev and Davydov - were assigned to clean classrooms №7, №8, №9 and №10. The students reported the following:\n\n- Andreev: "I cleaned classroom №9, and Savelyev - №7."\n- Kostin: "I cleaned classroom №9, and Andreev - №8."\n- Savelyev: "I cleaned classroom №8, and Kostin - №10."\n\nDavydov said nothing. Later it turned out that each student was telling the truth in one of his two statements, but the second was false. Which classroom did each student clean?\n\nA) Savelyev 7 , Andreev 9 , Kostin 10 , Davydov 8.\nB) Savelyev 8 , Andreev 7 , Kostin 10 , Davydov 9.\nC) Savelyev 10 , Andreev 8 , Kostin 9 , Davydov 7.\nD) Savelyev 7, Andreev 9, Kostin 10, Davydov 8.\nE) Savelyev 7, Andreev 8, Kostin 10, Davydov 9.',
        text_ru="В школе четырем старшеклассникам: Андрееву, Костину, Савельеву и Давыдову поручили убрать 7-ой, 8-ой, 9-ый и 10-ый классы. Неушедшие домой ученики сообщили о следующем:\n\n- Андреев: «Я убирал 9-ый класс, а Савельев — 7-ой».\n- Костин: «Я убирал 9-ый класс, а Андреев — 8-ой».\n- Савельев: «Я убирал 8-ой класс, а Костин - 10-ый».\n\nДавыдов уже ушел домой. В дальнейшем выяснилось, что каждый ученик в одном из двух высказываний говорил правду, а во втором ложь. Какой класс убирал каждый ученик?\n\nA) Савельев 7 , Андреев 9 , Костин 10 , Давыдов 8.\nB) Савельев 8 , Андреев 7 , Костин 10 , Давыдов 9.\nC) Савельев 10 , Андреев 8 , Костин 9 , Давыдов 7.\nD) Савельев 7 , Андреев 9 , Костин 10 , Давыдов 8.\nE) Савельев 7 , Андреев 8 , Костин 10 , Давыдов 9.",
        answer_lv="E",
        answer_en="E",
        answer_ru="E",
        choices_lv=["A", "B", "C", "D", "E"],
        choices_en=["A", "B", "C", "D", "E"],
        choices_ru=["A", "B", "C", "D", "E"],
        points=9
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Ir zināms, ka:\n\n- ja Boriss kolekcionē pastmarkas, tad Ivans un Nikolajs arī;\n- ja Ivans kolekcionē, ​​tad arī Pēteris kolekcionē pastmarkas;\n- no diviem draugiem (Pēteris un Aleksejs) tikai viens kolekcionē pastmarkas;\n- Aleksejs kolekcionē pastmarkas tikai tad, ja Nikolajs tās kolekcionē;\n- vismaz Nikolajs vai Boriss kolekcionē pastmarkas.\n\nKurš no draugiem kolekcionē pastmarkas?",
        text_en="It is known that:\n\n- if Boris collects stamps, then Ivan and Nikolai also collect them;\n- if Ivan collects them, then Peter also collects stamps;\n- of two friends (Peter and Alexey), only one collects stamps;\n- Alexey collects stamps only if Nikolai collects them;\n- at least Nikolai or Boris collects stamps.\n\nWhich of the friends collects stamps?",
        text_ru="Известно, что:\n\n- если Борис коллекционирует марки, то их коллекционируют Иван и Николай;\n- если их коллекционирует Иван, то Пётр тоже коллекционирует марки;\n- из двух друзей (Петра и Алексея) коллекционирует марки только один;\n- Алексей лишь в том случае коллекционирует марки, если их коллекционирует Николай;\n- по крайней мере, Николай или Борис коллекционирует марки.\n\nКто из друзей коллекционирует марки?",
        answer_lv="Aleksejs un Nikolajs",
        answer_en="Alexey and Nikolai",
        answer_ru="Алексей и Николай",
        choices_lv=["Boriss, Ivans un Nikolajs", "Pēteris un Ivans", "Aleksejs un Nikolajs"],
        choices_en=["Boris, Ivan and Nikolai", "Peter and Ivan", "Alexey and Nikolai"],
        choices_ru=["Борис, Иван и Николай", "Пётр и Иван", "Алексей и Николай"],
        points=7
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Slepkavības lietā ir divi aizdomās turamie: A un B. Tika nopratināti četri liecinieki.\n\nPirmais liecinieks teica: "A nav vainīgs."\nOtrs liecinieks teica: "B nav vainīgs. ”\nTrešais liecinieks: "No abām liecībām vismaz viena ir patiesa."\nCeturtais: "Trešā liecinieka liecība ir nepatiesa."\n\nCeturtajam lieciniekam bija taisnība. Kurš izdarījis noziegumu?',
        text_en='There are two suspects in a murder case: A and B. Four witnesses have been questioned.\n\nThe first witness testified: "A is not guilty."\nThe second witness said: "B is not guilty."\nThe third witness: "Of the two testimonies, at least one is true."\nThe fourth: "The testimony of the third witness is false."\n\nThe fourth witness was right. Who committed the crime?',
        text_ru="В деле об убийстве имеются двое подозреваемых: A и B. Допросили четверых свидетелей.\n\nПоказания первого таковы: «A не виноват».\nВторой свидетель сказал: «B не виноват».\nТретий свидетель: «Из двух показаний по крайней мере одно истинно».\nЧетвертый: «Показания третьего свидетеля ложны».\n\nЧетвертый свидетель оказался прав. Кто же совершил преступление?",
        answer_lv="Abi",
        answer_en="Both",
        answer_ru="Оба",
        choices_lv=["A", "B", "Neviens", "Abi"],
        choices_en=["A", "B", "Nobody", "Both"],
        choices_ru=["A", "B", "Никто", "Оба"],
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Ir piecas kastītes: balta, melna, sarkana, zila un zaļa. Un desmit bumbiņas tādās pašās krāsās kā kastītes, pa divām katrā krāsā. Katrā kastē ir divas bumbiņas. Tomēr:\n\n1) neviena bumbiņa neatrodas tādas pašas krāsas kastītē kā pati bumbiņa;\n2) sarkanajā kastītē nav zilu bumbiņu;\n3) neitrālas krāsas kastītē (baltā vai melnā) atrodas viena sarkana un viena zaļa bumbiņa;\n4) melnajā kastītē atrodas aukstu toņu bumbiņas (zaļi un zili toņi);\n5) vienā no kastītēm ir viena balta un viena zila bumbiņa;\n6) zilā kastītē atrodas viena melna bumbiņa.\n\nKādas krāsas bumbiņas ir BALTAJĀ kastītē?",
        text_en="There are five boxes: white, black, red, blue and green. And ten balls of the same colors as the boxes, two of each color. Each box contains two balls. Moreover:\n\n1) no ball is in a box of the same color as itself;\n2) there are no blue balls in the red box;\n3) in a box of a neutral color (white or black) there are one red and one green ball;\n4) in a black box there are balls of cold tones (green and blue tones);\n5) in one of the boxes there are one white and one blue ball;\n6) in a blue box there is one black ball.\n\nWhat colors are the balls in the WHITE box?",
        text_ru="Есть пять коробочек: белая, черная, красная, синяя и зелёная. И десять шариков тех же цветов, что и коробочки, по два каждого цвета. В каждой коробочке лежат по два шарика. При этом:\n\n1) ни один шарик не лежит в коробочке того же цвета, что и он сам;\n2) в красной коробочке нет синих шариков;\n3) в коробочке нейтрального цвета (белый или черный) лежат один красный и один зеленый шарик;\n4) в черной коробочке лежат шарики холодных тонов (зеленые и синие тона);\n5) в одной из коробочек лежат один белый и один синий шарик;\n6) в синей коробочке находится один черный шарик.\n\nКаких цветов шарики лежат в БЕЛОЙ коробочке?",
        answer_lv="Sarkana un zaļa",
        answer_en="Red and Green",
        answer_ru="Красный и зелёный",
        choices_lv=["Melna un sarkana", "Sarkana un zaļa", "Zaļa un zila", "Melna un balta", "Balta un zila"],
        choices_en=["Black and Red", "Red and Green", "Green and Blue", "Black and White", "White and Blue"],
        choices_ru=["Чёрный и красный", "Красный и зелёный", "Зелёный и синий", "Чёрный и белый", "Белый и синий"],
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Ir piecas kastītes: balta, melna, sarkana, zila un zaļa. Un desmit bumbiņas tādās pašās krāsās kā kastītes, pa divām katrā krāsā. Katrā kastē ir divas bumbiņas. Tomēr:\n\n1) neviena bumbiņa neatrodas tādas pašas krāsas kastītē kā pati bumbiņa;\n2) sarkanajā kastītē nav zilu bumbiņu;\n3) neitrālas krāsas kastītē (baltā vai melnā) atrodas viena sarkana un viena zaļa bumbiņa;\n4) melnajā kastītē atrodas aukstu toņu bumbiņas (zaļi un zili toņi);\n5) vienā no kastītēm ir viena balta un viena zila bumbiņa;\n6) zilā kastītē atrodas viena melna bumbiņa.\n\nKādas krāsas bumbiņas ir ZAĻAJĀ kastītē?",
        text_en="There are five boxes: white, black, red, blue and green. And ten balls of the same colors as the boxes, two of each color. Each box contains two balls. Moreover:\n\n1) no ball is in a box of the same color as itself;\n2) there are no blue balls in the red box;\n3) in a box of a neutral color (white or black) there are one red and one green ball;\n4) in a black box there are balls of cold tones (green and blue tones);\n5) in one of the boxes there are one white and one blue ball;\n6) in a blue box there is one black ball.\n\nWhat colors are the balls in the GREEN box?",
        text_ru="Есть пять коробочек: белая, черная, красная, синяя и зелёная. И десять шариков тех же цветов, что и коробочки, по два каждого цвета. В каждой коробочке лежат по два шарика. При этом:\n\n1) ни один шарик не лежит в коробочке того же цвета, что и он сам;\n2) в красной коробочке нет синих шариков;\n3) в коробочке нейтрального цвета (белый или черный) лежат один красный и один зеленый шарик;\n4) в черной коробочке лежат шарики холодных тонов (зеленые и синие тона);\n5) в одной из коробочек лежат один белый и один синий шарик;\n6) в синей коробочке находится один черный шарик.\n\nКаких цветов шарики лежат в ЗЕЛЁНОЙ коробочке?",
        answer_lv="Balta un zila",
        answer_en="White and Blue",
        answer_ru="Белый и синий",
        choices_lv=["Melna un sarkana", "Sarkana un zaļa", "Zaļa un zila", "Melna un balta", "Balta un zila"],
        choices_en=["Black and Red", "Red and Green", "Green and Blue", "Black and White", "White and Blue"],
        choices_ru=["Чёрный и красный", "Красный и зелёный", "Зелёный и синий", "Чёрный и белый", "Белый и синий"],
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Ir piecas kastītes: balta, melna, sarkana, zila un zaļa. Un desmit bumbiņas tādās pašās krāsās kā kastītes, pa divām katrā krāsā. Katrā kastē ir divas bumbiņas. Tomēr:\n\n1) neviena bumbiņa neatrodas tādas pašas krāsas kastītē kā pati bumbiņa;\n2) sarkanajā kastītē nav zilu bumbiņu;\n3) neitrālas krāsas kastītē (baltā vai melnā) atrodas viena sarkana un viena zaļa bumbiņa;\n4) melnajā kastītē atrodas aukstu toņu bumbiņas (zaļi un zili toņi);\n5) vienā no kastītēm ir viena balta un viena zila bumbiņa;\n6) zilā kastītē atrodas viena melna bumbiņa.\n\nKādas krāsas bumbiņas ir SARKANAJĀ kastītē?",
        text_en="There are five boxes: white, black, red, blue and green. And ten balls of the same colors as the boxes, two of each color. Each box contains two balls. Moreover:\n\n1) no ball is in a box of the same color as itself;\n2) there are no blue balls in the red box;\n3) in a box of a neutral color (white or black) there are one red and one green ball;\n4) in a black box there are balls of cold tones (green and blue tones);\n5) in one of the boxes there are one white and one blue ball;\n6) in a blue box there is one black ball.\n\nWhat colors are the balls in the RED box?",
        text_ru="Есть пять коробочек: белая, черная, красная, синяя и зелёная. И десять шариков тех же цветов, что и коробочки, по два каждого цвета. В каждой коробочке лежат по два шарика. При этом:\n\n1) ни один шарик не лежит в коробочке того же цвета, что и он сам;\n2) в красной коробочке нет синих шариков;\n3) в коробочке нейтрального цвета (белый или черный) лежат один красный и один зеленый шарик;\n4) в черной коробочке лежат шарики холодных тонов (зеленые и синие тона);\n5) в одной из коробочек лежат один белый и один синий шарик;\n6) в синей коробочке находится один черный шарик.\n\nКаких цветов шарики лежат в КРАСНОЙ коробочке?",
        answer_lv="Melna un balta",
        answer_en="Black and White",
        answer_ru="Чёрный и белый",
        choices_lv=["Melna un sarkana", "Sarkana un zaļa", "Zaļa un zila", "Melna un balta", "Balta un zila"],
        choices_en=["Black and Red", "Red and Green", "Green and Blue", "Black and White", "White and Blue"],
        choices_ru=["Чёрный и красный", "Красный и зелёный", "Зелёный и синий", "Чёрный и белый", "Белый и синий"],
        points=2
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Bibliotēkā trūkst piecu grāmatu:\n- Žila Verna romāna (1872);\n- Čārlza Dikensa romāna (1838);\n- Žigmunda Morica stāstu (1920);\n- Janoša Araņas dzejoļu "Toldi" (1847);\n- Attilas Jožefa dzejoļu (1929).\n\nBibliotekārs atcerējās sekojošo:\n1) bibliotēku apmēklēja draugi - Andrejs, Filips, Ilona, ​​Jekaterina un Viktors;\n2) bibliotēka izsniedz tikai vienu grāmatu, un jauna grāmata tiek izsniegta tikai pēc iepriekšējas atgriešanas;\n3) Filips nevarēja paņemt Dikensu;\n4) Andrejs varēja paņemt tikai Attilas Jožefa dzejoļus un Žila Verna romānus;\n5) Jekaterina dod priekšroku XX gadsimta literatūrai;\n6) Ilona lasa tikai ungāru autoru (Morica, Araņas un Jožefa) darbus;\n7) Viktors lasa tikai dzeju.\n\nKuru grāmatu draugi <b>NEVARĒJA</b> paņemt?',
        text_en='The library is missing five books:\n- a novel by Jules Verne (1872);\n- a novel by Charles Dickens (1838);\n- a short story by Zsigmond Móricz (1920);\n- the poem "Toldi" by János Arany (1847);\n- poems by Attila József (1929).\n\nThe librarian remembered the following:\n1) Friends - Andrey, Philip, Ilona, ​​Ekaterina and Victor - visited the library;\n2) the library only issues one book at a time, and a new book is issued only after the previous one is returned;\n3) Philip could not take Dickens;\n4) Andrey could only take poems by Attila József and the novel by Jules Verne;\n5) Ekaterina prefers 20th century literature;\n6) Ilona reads works only by Hungarian authors (Móricz, Arany and József);\n7) Victor only reads poetry.\n\nWhat book <b>COULD NOT</b> the friends take?',
        text_ru="В библиотеке не хватает пяти книг:\n- романа Жюля Верна (1872 г.);\n- романа Чарлза Диккенса (1838 г.);\n- рассказов Жигмунда Морица (1920 г.);\n- поэмы Яноша Араня «Тольди» (1847 г.);\n- стихов Аттилы Йожефа (1929 г.).\n\nБиблиотекарь вспомнил следующее:\n1) в библиотеку заходили Андрей, Филипп, Илона, Екатерина и Виктор;\n2) выдают только по одной книге, причём новую книгу выдают лишь после того, как возвращена предыдущая;\n3) Филипп не мог взять Диккенса;\n4) Андрей мог взять только стихи Аттилы Йожефа и романы Жюля Верна;\n5) Екатерина отдает предпочтение литературе ХХ века;\n6) Илона читает произведения только венгерских авторов (Морица, Араня и Йожефа);\n7) Виктор читает только поэзию.\n\nКакую книгу <b>НЕ МОГЛИ</b> взять ребята?",
        answer_lv="Č.Dikensa grāmatu",
        answer_en="The Book by Dickens",
        answer_ru="Книгу Ч.Диккенса",
        choices_lv=["Ž.Verna grāmatu", "Č.Dikensa grāmatu", "Ž.Morica grāmatu", "J.Araņas grāmatu", "A.Jožefa grāmatu"],
        choices_en=["The Book by Verne", "The Book by Dickens", "The Book by Móritz", "The Book by Arany", "The Book by József"],
        choices_ru=["Книгу Ж.Верна", "Книгу Ч.Диккенса", "Книгу Ж.Морица", "Книгу Я.Араня", "Книгу А.Йожефа"],
        points=8
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Vakar vakarā:\n\n1) Andrejs devās uz koncertu;\n2) Boriss visu laiku pavadīja kopā ar Olgu;\n3) Sergejs Ritu nekad nav redzējis;\n4) Poļina devās uz kino;\n\5) Rita skatījās izrādi teātrī;\n6) Arī kompānijā bija Dima, kā arī Sveta;\n7) Kopā ar katru puisi bija meitene;\n8) Kāds pāris apmēklēja mākslas izstādi.\n\nKurš pāris bija <b>mākslas izstādē</b>?",
        text_en="Yesterday evening:\n\n1) Andrey went to the concert;\n2) Boris spent the whole time with Olga;\n3) Sergey never saw Rita;\n4) Polina went to the cinema;\n\5) Rita saw a play at the theatre;\n6) Dima and Sveta were also in the company;\n7) Each guy had a girl with him;\n8) Some couple visited an art exhibition.\n\nWhich couple was at the <b>art exhibition</b>?",
        text_ru="Вчера вечером:\n\n1) Андрей отправился на концерт;\n2) Борис провёл всё время с Ольгой;\n3) Сергей так и не увиделся с Ритой;\n4) Полина побывала в кино;\n5) Рита посмотрела спектакль в театре;\n6) В компании ещё были Дима, а также Света;\n7) Вместе с каждым парнем была девушка;\n8) Какая-то пара посетила художественную выставку.\n\nКакая пара была на <b>художественной выставке</b>?",
        answer_lv="Boriss + Olga",
        answer_en="Boris + Olga",
        answer_ru="Борис + Ольга",
        choices_lv=["Boriss + Olga", "Rita + Dima", "Andrejs + Sveta", "Poļina + Sergejs"],
        choices_en=["Boris + Olga", "Rita + Dima", "Andrey + Sveta", "Polina + Sergey"],
        choices_ru=["Борис + Ольга", "Рита + Дима", "Андрей + Света", "Полина + Сергей"],
        points=5
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Reiz pie apaļā galda bija pieci cilvēki no Maskavas, Rīgas, Viļņas, Berlīnes un Jūrmalas: Jurijs, Anatolijs, Aleksejs, Nikolajs un Viktors.\n\nMaskavietis sēdēja starp jūrmalnieku un Viktoru, rīdzinieks starp Juriju un Anatoliju, un pretī rīdziniekam sēdēja Berlīnes iedzīvotājs un Aleksejs.\n\nNikolajs nekad nav bijis Rīgā, Jurijs nebija Maskavā vai Jūrmalā, bet jūrmalnieks un Anatolijs regulāri sarakstās.\n\nKur Anatolijs dzīvo?",
        text_en="One day, there were five people from Moscow, Riga, Vilnius, Berlin and Jurmala at a round table: Yury, Anatoly, Alexey, Nikolay and Viktor.\n\nThe Moscovian sat between the Jurmala resident and Viktor, the Riga resident between Yury and Anatoly, and opposite the Riga resident sat the Berliner and Alexey.\n\nNikolay had never been to Riga, and Yury had never been to Moscow or Jurmala, but the Jurmala resident and Anatoly correspond regularly.\n\nWhere does Anatoly live?",
        text_ru="Однажды за круглым столом оказалось пятеро человек родом из Москвы, Риги, Вильнюса, Берлин и Юрмалы: Юрий, Анатолий, Алексей, Николай и Виктор.\n\nМосквич сидел между юрмальчанином и Виктором, рижанин — между Юрием и Анатолием, а напротив рижанина сидели берлинец и Алексей.\n\nНиколай никогда не был в Риге, а Юрий не бывал в Москве и Юрмале, но юрмальчанин с Анатолием регулярно переписываются.\n\nГде живёт Анатолий?",
        answer_lv="Maskavā",
        answer_en="In Moscow",
        answer_ru="В Москве",
        choices_lv=["Maskavā", "Rīgā", "Viļņā", "Berlīnē", "Jūrmalā"],
        choices_en=["In Moscow", "In Riga", "In Vilnius", "In Berlin", "In Jurmala"],
        choices_ru=["В Москве", "В Риге", "В Вильнюсе", "В Берлине", "В Юрмале"],
        points=10
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Zālē pirms treniņa tikās sporta meistars Sirmais, sporta meistara kandidāts Melnais un audzēknis Rudains.\n\n— Paskatieties, — sacīja  melnmatainais, — viens no mums ir sirms, otrs ir rudmatains, trešais ir melnmatains. Taču nevienam no mums matu krāsa nesakrīt ar uzvārdu. Jocīgi, vai ne?\n— Tev taisnība, — apstiprināja sporta meistars.\n\nKādā matu krāsā ir <b>sporta meistara kandidātam</b>?',
        text_en='Master of Sports Mr.Gray, candidate for master Mr.Black and student Mr.Red met at the gym before training.\n\n"Pay attention," the black-haired man noted, "one of us is gray, the other is red-haired, and the third is black-haired. But none of us have the same hair color as our last name. It is funny, is not it?"\n"You are right," the master of sports confirmed.\n\nWhat hair color has <b>the candidate for master</b>?',
        text_ru="Мастер спорта Седов, кандидат в мастера Чернов и перворазрядник Рыжов встретились в зале перед тренировкой.\n\n— Обратите внимание, — заметил черноволосый, — один из нас седой, другой — рыжий, третий — черноволосый. Но ни у одного из нас цвет волос не совпадает с фамилией. Забавно, не правда ли?\n— Ты прав, — подтвердил мастер спорта.\n\nКакого цвета волосы у <b>кандидата в мастера</b>?",
        answer_lv="Pelēkā",
        answer_en="Gray",
        answer_ru="Седые",
        choices_lv=["Pelēkā", "Melnā", "Sarkanā"],
        choices_en=["Gray", "Black", "Red"],
        choices_ru=["Седые", "Чёрные", "Рыжие"],
        points=5
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Pudelē, glāzē, krūzē un burkā ir piens, limonāde, kvass un ūdens.\n\nZināms, ka ūdens un piena pudelē nav, starp krūzi un trauku ar kvasu stāv trauks ar limonādi, burkā nav ne limonādes, ne ūdens, starp burku un trauku ar pienu stāv glāze.\n\nKādā traukā ir kvass?",
        text_en="The bottle, glass, jug and jar contain milk, lemonade, kvass and water.\n\nIt is known that the water and milk are not in the bottle, the vessel with lemonade is between the jug and the vessel with kvass, the jar contains neither lemonade nor water, the glass is between the jar and the vessel with milk.\n\nWhich vessel contains the kvass?",
        text_ru="В бутылке, стакане, кувшине и банке находятся молоко, лимонад, квас и вода.\n\nИзвестно, что вода и молоко не в бутылке, сосуд с лимонадом стоит между кувшином и сосудом с квасом, в банке не лимонад и не вода, стакан стоит между банкой и сосудом с молоком.\n\nВ каком сосуде находится квас?",
        answer_lv="Burkā",
        answer_en="In a jar",
        answer_ru="В банке",
        choices_lv=["Pudelē", "Glāzē", "Krūzē", "Burkā"],
        choices_en=["In a bottle", "In a glass", "In a jug", "In a jar"],
        choices_ru=["В бутылке", "В стакане", "В кувшине", "В банке"],
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Trīs meitenes - Roze, Māra un Lilija - izaudzēja konkursam rozes, mārgrietiņas un lilijas. Meitene, kura audzēja mārgrietiņas, pievērsa Rozes uzmanību tam, ka nevienas meitenes vārds nesakrita ar viņu iecienītāko ziedu nosaukumiem. Kādus ziedus izauga <b>Lilija</b>?",
        text_en="Three girls - Rose, Daisy and Lily grew roses, daisies and lilies for the competition. The girl who grew the daisies drew Rose's attention to the fact that none of the girls had the same name as their favourite flowers. What flowers did <b>Lily</b> grow?",
        text_ru="Три девочки — Роза, Маргарита и Анюта представили на конкурс цветоводов корзины выращенных ими роз, маргариток и анютиных глазок. Девочка, вырастившая маргаритки, обратила внимание Розы на то, что ни у одной из девочек имя не совпадает с названием любимых цветов. Какие цветы вырастила <b>Анюта</b>?",
        answer_lv="Mārgrietiņas",
        answer_en="Daisies",
        answer_ru="Маргаритки",
        choices_lv=["Rozes", "Mārgrietiņas", "Lilijas"],
        choices_en=["Roses", "Daisies", "Lilies"],
        choices_ru=["Розы", "Маргаритки", "Анютины глазки"],
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Nikolajs, Boriss, Vladimirs un Jurijs peldēšanas sacensībās ieņēma pirmās četras vietas. Uz jautājumu, kādas vietas viņi ieņēma, puiši atbildēja:\n\n1) Nikolajs neieņēma pirmo vai ceturto vietu.\n2) Boriss bija otrais.\n3) Vladimirs nebija pēdējais.\n\nKādu vietu ieņēma Vladimirs?",
        text_en="Nikolai, Boris, Vladimir and Yuri took the first four places in the swimming competition. When asked what places they took, the boys answered:\n\n1) Nikolai took neither first nor fourth place.\n2) Boris was second.\n3) Vladimir was not last.\n\nWhat place did Vladimir take?",
        text_ru="Николай, Борис, Владимир и Юрий заняли первые четыре места в спортивном соревновании по плаванью. На вопрос, какие места они заняли, мальчики ответили:\n\n1) Николай не занял ни первое, ни четвёртое место.\n2) Борис был вторым.\n3) Владимир не был последним.\n\nКакое место занял Владимир?",
        answer_lv="1",
        answer_en="1",
        answer_ru="1",
        choices_lv=["1", "2", "3", "4"],
        choices_en=["1", "2", "3", "4"],
        choices_ru=["1", "2", "3", "4"],
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Sestdienas vakarā Semjons, Koļa un Vitja nolēma izklaidēties. Viņiem bija izvēle: kino, rokkoncerts vai dejas.\n\n• Semjonam patīk kino, taču viņš ir mazāk neiecietīgs pret dejām, nevis rokmūziku.\n• Koļai patīk dejas, taču viņš drīzāk ir gatavs doties uz kino nekā uz rokkoncertu.\n• Vitja rokmūziku mīl mazāk nekā dejas, taču kino viņam nav tik nepatīkams kā dejas vai koncerts.\n\nTā kā jautājums tiks izlemts ar balsu vairākumu, kur dosies puiši?",
        text_en="On Saturday evening, Semyon, Kolya and Vitya decided to have some fun. They had a choice: cinema, rock concert or dancing.\n\n• Semyon likes cinema, but he is less intolerant of dancing than of rock music.\n• Kolya likes dancing, but he would rather go to the cinema than a rock concert.\n• Vitya likes rock music less than dancing, but he doesn't find cinema as unpleasant as dancing or a concert.\n\nSince the question will be decided by a majority vote, where did these guys go?",
        text_ru="В субботний вечер Семён, Коля и Витя решили развлечься. У них был выбор: кино, рок-концерт или танцы.\n\n• Семён любит кино, но к танцам менее нетерпим, чем к рок-музыке.\n• Коля любит танцевать, но готов пойти в кино скорее, чем на рок концерт.\n• Витя любит рок-музыку меньше чем танцы, но кино ему всё-таки не так неприятно, как танцы или концерт.\n\nПоскольку вопрос решатся большинством голосов, то куда отправились эти ребята?",
        answer_lv="Uz kino",
        answer_en="To the cinema",
        answer_ru="В кино",
        choices_lv=["Uz kino", "Uz koncertu", "Uz dejām"],
        choices_en=["To the cinema", "To the concert", "To the dance"],
        choices_ru=["В кино", "На концерт", "На танцы"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Trīs zēni – Kostja, Foma un Marats – draudzējās ar trim meitenēm – Žeņu, Svetu un Marinu. Taču drīz vien kompānija sadalījās pāros, jo izrādījās, ka:\n\n• Sveta ienīst slēpošanu.\n• Kostja (Žeņas brālis) bieži dodas slēpot kopā ar savu draudzeni.\n• Foma tagad skrien uz randiņu ar Kostjas māsu.\n\nAr ko Marats pavada laiku?",
        text_en="Three boys – Kostya, Foma and Marat – were friends with three girls - Zhenya, Sveta and Marina. But soon the company split into pairs, because it turned out that:\n\n• Sveta hates skiing.\n• Kostya, Zhenya's brother, often goes skiing with his girlfriend.\n• Foma now runs to Kostya's sister's on a date.\n\nWho does Marat spend his time with?",
        text_ru="Трое мальчиков – Костя, Фома и Марат – дружили с тремя девочками – Женей, Светой и Мариной. Но вскоре компания разделилась на пары, потому что оказалось, что:\n\n• Света ненавидит ходить на лыжах.\n• Костя (Женин брат) часто катается со своей подружкой на лыжах.\n• Фома теперь бежит на свидание к Костиной сестре.\n\nС кем же проводит время Марат?",
        answer_lv="Ar Svetu",
        answer_en="With Sveta",
        answer_ru="Со Светой",
        choices_lv=["Ar Žeņu", "Ar Svetu", "Ar Marinu"],
        choices_en=["With Zhenya", "With Sveta", "With Marina"],
        choices_ru=["С Женей", "Со Светой", "С Мариной"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Vienā nelielā kafejnīcā maiņā vienlaikus strādāja 5 cilvēki: administrators(-e), pavārs(-e), konditors(-e), kasieris(-e), sētnieks(-ce). Galbraites kundze, Šermenes kundze, Viljamsa kungs, Vortmena kungs un Bleika kungs visi devās strādāt vienlaikus. Ir zināms, ka:\n\n1. Pavāram nav sievas.\n2. Kasieris(-e) un administrators(-e) dzīvoja vienā istabā, kad viņi mācījās koledžā.\n3. Bleika kungs un Šermenes kundze tiekas tikai darbā.\n4. Viljamsas kundze bija sarūgtināta, kad viņas vīrs viņai pateica, ka administrators(-e) viņam nedeva atvaļinājumu.\n5. Vortmena kungs būs šoferis kasiera(-es) un konditora(-es) kāzās.\n\nKāds ir Šermenes kundzes amats?",
        text_en="In one small cafe, 5 people worked on the same shift: the administrator, the cook, the pastry chef, the cashier, and the janitor. Miss Galbraith, Miss Sherman, Mr. Williams, Mr. Wortman, and Mr. Blake all went to work at the same time. It is known that:\n\n1. The cook doesn't have a wife.\n2. The cashier and the administrator shared a room when they were in college.\n3. Mr. Blake and Miss Sherman only meet at work.\n4. Mrs. Williams was upset when her husband told her that the administrator didn't give him a vacation.\n5. Wortman is going to be a chauffeur at the cashier and the pastry chef's wedding.\n\nWhat job does Miss Sherman hold?",
        text_ru="В одном небольшом кафе в смене одновременно работали 5 человек: администратор, повар, кондитер, кассир, дворник. Одновременно на работу выходили мисс Галбрейт, мисс Шерман, мистер Вильямс, мистер Вортман и мистер Блейк. При этом известно, что:\n\n1. Повар – холостяк.\n2. Кассир и администратор жили в одной комнате, когда учились в колледже.\n3. Мистер Блейк и мисс Шерман встречаются только на работе.\n4. Миссис Вильямс расстроилась, когда муж сказал ей, что администратор отказал ему в отгуле.\n5. Вортман собирается быть шофёром на свадьбе у кассира и кондитера.\n\nНа какой должности работает <b>мисс Шерман</b>?",
        answer_lv="Administratore",
        answer_en="Administrator",
        answer_ru="Администратор",
        choices_lv=["Administratore", "Pavāre", "Konditore", "Kasiere", "Sētnieke"],
        choices_en=["Administrator", "Cook", "Pastry Chef", "Cashier", "Janitor"],
        choices_ru=["Администратор", "Повар", "Кондитер", "Кассир", "Дворник"],
        points=12
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Četras meitenes - Maša, Tanja, Sofija un Poļina - nopirka sulu kafejnīcā. Katra no viņiem nopirka tikai vienu sulu. Divi no viņiem iegādājās ābolu sulu, viena - vīnogu sulu un viena meitene bumbieru sulu.\n\nIr zināms, ka Mašai un Tanjai ir dažādas gaumes.\nDažādas sulas nopirka Maša un Sofija, Polina un Sofija, Polina un Maša, Tanja un Sofija.\nTurklāt ir zināms, ka Maša nepirka bumbieru sulu.\n\nNosaki, kādu sulu dzēra <b>Sofija</b>.",
        text_en="Four girls - Masha, Tanya, Sofia and Polina - bought juice in a cafe. Each of them bought only one juice. Two of them bought apple juice, one bought grape juice, and one bought pear juice.\n\nIt is known that Masha and Tanya have different tastes.\nMasha and Sofia, Polina and Sofia, Polina and Masha, and Tanya and Sofia bought different juices.\nIn addition, it is known that Masha did not buy pear juice.\n\nDetermine what juice <b>Sofia</b> drank.",
        text_ru="Четыре девочки - Маша, Таня, София и Полина - купили в кафе сок. Каждая из них покупала только один сок, причём две из них купили сок яблочный, одна виноградный, и одна – грушевый.\n\nИзвестно, что у Маши и Тани разные вкусы.\nРазные соки взяли Маша с Софией, Полина с Софией, Полина с Машей и Таня с Софией.\nКроме того известно, что Маша купила не грушевый сок.\n\nОпределить, какой сок пила <b>София</b>.",
        answer_lv="Bumbieru",
        answer_en="Pear",
        answer_ru="Грушевый",
        choices_lv=["Ābolu", "Vīnogu", "Bumbieru"],
        choices_en=["Apple", "Grape", "Pear"],
        choices_ru=["Яблочный", "Виноградный", "Грушевый"],
        points=9
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Ģimenē aug četri bērni. Viņiem ir 5, 8, 13 un 15 gadi. Viņus sauc Anna, Boriss, Vera un Grigorijs. Cik gadu ir <b>Grigorijam</b>, ja viena meitene ej uz bērnudārzu, Anna ir vecāka par Borisu, un Annas un Veras gadu summa tiek dalīta ar trīs?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>",
        text_en="There are four children in a family. They are 5, 8, 13 and 15 years old. Their names are Anna, Boris, Vera and Grigoriy. How old is <b>Grigoriy</b> if one girl goes to kindergarten, Anna is older than Boris and the sum of Anna's and Vera's ages is divisible by three?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>",
        text_ru="В семье четверо детей. Им 5, 8, 13 и 15 лет. Их зовут Анна, Борис, Вера и Григорий. Сколько лет <b>Григорию</b>, если одна девочка ходит в детский сад, Анна старше Бориса и сумма лет Анны и Веры делится на три?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>",
        answer_lv="15",
        answer_en="15",
        answer_ru="15",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Klauni Bims, Bams un Boms ienāca arēnā sarkanos, zilos un zaļos kreklos (visi dažādos). Viņu kurpes bija tajās pašās krāsās (katram klaunam savs). Bima kurpes un krekls bija vienā krāsā. Boms nebija valkājis neko sarkanu. Bama kurpes bija zaļas, bet krekls ne. Kādās krāsās bija Boma kurpes un krekls?",
        text_en="Clowns Bim, Bam and Bom came out into the arena wearing red, blue and green shirts (all different). Their shoes were the same colors (each clown had his own). Bim's shoes and shirt were the same color. Bom wasn't wearing anything red. Bam's shoes were green, but his shirt wasn't. What colors were Bom's shoes and shirt?",
        text_ru="Клоуны Бим, Бам и Бом вышли на арену в красной, синей и зелёной рубашках (все в разных). Их туфли были тех же цветов (у каждого клоуна свой). Туфли и рубашка Бима были одного цвета. На Боме не было ничего красного. Туфли Бама были зелёные, а рубашка нет. Каких цветов были туфли и рубашка у Бима?",
        answer_lv="Sarkanās",
        answer_en="Red",
        answer_ru="Красные",
        choices_lv=["Zilās", "Zaļās", "Sarkanās"],
        choices_en=["Blue", "Green", "Red"],
        choices_ru=["Синие", "Зелёные", "Красные"],
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Skolas skolēni nolēma izveidot instrumentālo ansambli.\n\nMihails spēlē saksofonu. Pianists mācās 9. klasē. Bundzinieka vārds nav Valērijs, un 10. klases skolnieku nesauc Leonīds. Mihails nemācās 11. klasē. Andrejs nav pianists vai 8. klases skolnieks. Valērijs nemācās 9.klasē, bundzinieks nemācās 11.klasē Leonīds nespēlē kontrabasu.\n\nKādu instrumentu spēlē Valērijs un kurā klasē viņš mācās?",
        text_en="The school students decided to organize an instrumental ensemble.\n\nMikhail plays the saxophone. The pianist is in the 9th grade. The drummer's name is not Valery, and the 10th grade student's name is not Leonid. Mikhail is not in the 11th grade. Andrey is not a pianist and not an 8th grade student. Valery is not in the 9th grade, the drummer is not in the 11th. Leonid does not play the double bass.\n\nWhat instrument does Valery play and what grade is he in?",
        text_ru="Учащиеся школы решили организовать инструментальный ансамбль.\n\nМихаил играет на саксофоне. Пианист учится в 9 классе. Ударника зовут не Валерием, а ученика 10 класса зовут не Леонидом. Михаил учится не в 11 классе. Андрей – не пианист и не ученик 8 класса. Валерий учится не в 9 классе, ударник - не в 11. Леонид играет не на контрабасе.\n\nНа каком инструменте играет Валерий и в каком классе он учится?",
        answer_lv="Kontrabass, 11.klase",
        answer_en="Double bass, grade 11",
        answer_ru="Контрабас, 11 класс",
        choices_lv=["Klavieres, 10.klase", "Klavieres, 11.klase", "Kontrabass, 11.klase", "Kontrabass, 10.klase"],
        choices_en=["Piano, grade 10", "Piano, grade 11", "Double bass, grade 11", "Double bass, grade 10"],
        choices_ru=["Пианино, 10 класс", "Пианино, 11 класс", "Контрабас, 11 класс", "Контрабас, 10 класс"],
        points=8
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Anna gaida autobusu. Kuram notikumam ir vislielākā varbūtība?\n\nA = {Anna autobusu gaida vismaz minūti},\nB = {Anna autobusu gaida vismaz divas minūtes},\nC = {Anna autobusu gaida vismaz piecas minūtes}.",
        text_en="Anna is waiting for the bus. Which event has the highest probability?\n\nA = {Anna waits for the bus for at least a minute},\nB = {Anna waits for the bus for at least two minutes},\nC = {Anna waits for the bus for at least five minutes}.",
        text_ru="Аня ждёт автобус. Какое событие имеет наибольшую вероятность?\n\nА = {Аня ждёт автобус не меньше минуты},\nВ = {Аня ждёт автобус не меньше двух минут},\nС = {Аня ждёт автобус не меньше пяти минут}.",
        answer_lv="A",
        answer_en="A",
        answer_ru="A",
        choices_lv=["A", "B", "C"],
        choices_en=["A", "B", "C"],
        choices_ru=["A", "B", "C"],
        points=3
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Pilsētu apdzīvo meļi un bruņinieki. Meļi vienmēr melo, bet bruņinieki vienmēr saka patiesību. Kāds ceļotājs, kurš ieradās pilsētā, satika četrus cilvēkus un uzdeva viņiem jautājumu: "Kas jūs esat?" Viņš saņēma šādas atbildes:\n\n1.cilvēks: "Mēs visi esam meļi."\n2.cilvēks: "Mūsu vidū ir 1 melis."\n3.cilvēks: "Mūsu vidū ir 2 meli."\n4.cilvēks: "Es ne reizi neesmu melojis un nemeloju arī tagad."\n\nKas ir ceturtais cilvēks?',
        text_en='The state is inhabited by liars and knights. Liars always lie, and knights always tell the truth. A traveler who came to the state met four people and asked them: "Who are you?" He received the following answers:\n\n1st: "We are all liars."\n2nd: "There is 1 liar among us."\n3rd: "There are 2 liars among us."\n4th: "I have never lied and I am not lying now."\n\nWho is the fourth inhabitant?',
        text_ru='Государство населено лжецами и рыцарями. Лжецы всегда лгут, а рыцари всегда говорят правду. Путешественник, попавший в государство, встретил четырёх людей и задал им вопрос: "Кто вы?". Он получил такие ответы:\n\n1-ый: "Все мы лжецы".\n2-ой: "Среди нас 1 лжец".\n3-ий: "Среди нас 2 лжеца".\n4-ый: "Я ни разу не соврал и сейчас не вру".\n\nКем является четвёртый житель?',
        answer_lv="Bruņinieks",
        answer_en="Knight",
        answer_ru="Рыцарь",
        choices_lv=["Bruņinieks", "Melis"],
        choices_en=["Knight", "Liar"],
        choices_ru=["Рыцарь", "Лжец"],
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv='Uz salas ir 100 bruņinieku un 100 meļu. Katram no viņiem ir vismaz viens draugs.\n\nReiz tieši 100 cilvēki teica: "Visi mani draugi ir bruņinieki," un tieši 100 cilvēki teica: "Visi mani draugi ir meļi."\n\nKas ir mazākais iespējamais draugu pāru skaits, no kuriem viens ir bruņinieks un otrs melis?\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti tikai skaitli!</i>',
        text_en='There are 100 knights and 100 liars on an island. Each of them has at least one friend.\n\nOne day, exactly 100 people said, "All my friends are knights," and exactly 100 people said, "All my friends are liars."\n\nWhat is the smallest possible number of pairs of friends, one of whom is a knight and the other is a liar?\n\n<i><b>Warning</b></i><i>: In your answer, write only the number!</i>',
        text_ru='На острове 100 рыцарей и 100 лжецов. У каждого из них есть хотя бы один друг.\n\nОднажды ровно 100 человек сказали: "Все мои друзья – рыцари", и ровно 100 человек сказали: "Все мои друзья – лжецы".\n\nКаково наименьшее возможное количество пар друзей, один из которых рыцарь, а другой лжец?\n\n<i><b>Важно</b></i><i>: В ответе пиши только число!</i>',
        answer_lv="50",
        answer_en="50",
        answer_ru="50",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Ceļotājs apmeklēja ciematu, kurā katrs cilvēks vai nu vienmēr teic patiesību, vai vienmēr melo. Ciemata iedzīvotāji nostājās aplī, un katrs ceļotājam pateica par savu kaimiņu labajā pusē - vai viņš ir patiess. Balstoties uz šiem ziņojumiem, ceļotājs spēja viennozīmīgi noteikt, cik lielu daļu no visiem ciema iedzīvotājiem veido meļi. Nosaki, ar ko tā ir vienāda.\n\n<i><b>Svarīgi</b></i><i>: Atbildē raksti skaitli ar procenta zīmi bez atstarpēm!</i>",
        text_en="A traveler visited a village where every person either always tells the truth or always lies. The villagers stood in a circle, and each told the traveler about the neighbor on the right, whether he was telling the truth. Based on these reports, the traveler was able to clearly determine what proportion of all the villagers were liars. Determine what it is.\n\n<i><b>Warning</b></i><i>: In your answer, write the number with a percentage sign without spaces!</i>",
        text_ru="Путешественник посетил деревню, в котором каждый человек либо всегда говорит правду, либо всегда лжёт. Жители деревни стали в круг, и каждый сказал путешественнику про соседа справа, правдив ли он. На основании этих сообщений путешественник смог однозначно определить, какую долю от всех жителей деревни составляют лжецы. Определи, чему она равна.\n\n<i><b>Важно</b></i><i>: В ответе пиши число со знаком процента без пробелов!</i>",
        answer_lv="50%",
        answer_en="50%",
        answer_ru="50%",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Zemūdens karalim kalpo astoņkāji ar sešām, septiņām vai astoņām kājām. Tie, kuriem ir 7 kājas, vienmēr melo, un tie, kuriem ir 6 vai 8 kājas, vienmēr saka patiesību. Satikās četri astoņkāji.\n\nZils teica: "Kopā mums ir 28 kājas."\nZaļš: "Kopā mums ir 27 kājas."\nDzeltens: "Kopā mums ir 26 kājas."\nSarkans: "Kopā mums ir 25 kājas. "\n\nCik kājas viņiem patiesībā ir kopā?',
        text_en='The underwater king has octopuses with six, seven or eight legs. Those with seven legs always lie, and those with six or eight legs always tell the truth. Four octopuses met.\n\nThe blue one said, "We have 28 legs together."\nGreen: "We have 27 legs together."\nYellow: "We have 26 legs together."\nRed: "We have 25 legs together."\n\nHow many legs do they really have together?',
        text_ru='У подводного царя служат осьминоги с шестью, семью или восемью ногами. Те, у кого 7 ног, всегда лгут, а у кого 6 или 8 ног, всегда говорят правду. Встретились четыре осьминога.\n\nСиний сказал: "Вместе у нас 28 ног."\nЗёленый: "Вместе у нас 27 ног."\nЖёлтый: "Вместе у нас 26 ног."\nКрасный: "Вместе у нас 25 ног."\n\nСколько у них вместе ног на самом деле?',
        answer_lv="27",
        answer_en="27",
        answer_ru="27",
        choices_lv=["25", "26", "27", "28"],
        choices_en=["25", "26", "27", "28"],
        choices_ru=["25", "26", "27", "28"],
        points=4
    )

    await rq.add_task(
        grade=9,
        input_type="text",
        text_lv="Astoņi cilvēki ierindojās tā, ka:\n\n1) Aleksejs bija priekšā Borisam un Viktoram;\n2) Boriss - priekšā Konstantīnam caur vienu;\n3) Leonīds priekšā Aleksejam, bet aiz Dmitrija;\n4) Viktors - pēc Erlenda caur vienu;\n5) Dmitrijs - starp Borisu un Gļebu;\n6) Erlends - blakus Konstantīnam, bet priekšā Viktoram.\n\nKādā secībā sastājušies cilvēki?\n\n<i><b>Svarīgi</b></i><i>: Atbildi raksti ar komatiem, ar atstarpēm, bez punkta beigās!</i>\n<i><b>Atbildes piemērs</b></i><i>: Erlends, Viktors, Aleksejs, Gļebs, Leonīds, Dmitrijs, Konstantīns, Boriss</i>",
        text_en="Eight people lined up in a row so that:\n\n1) Alexey was ahead of Boris and Victor;\n2) Boris was ahead of Konstantin, one behind;\n3) Leonid was ahead of Alexey, but after Dmitry;\n4) Victor was behind Yegor, one behind;\n5) Dmitry was between Boris and Gleb;\n6) Yegor was next to Konstantin, but ahead of Victor.\n\nIn what order did the people line up?\n\n<i><b>Warning</b></i><i>: Write your answer separated by commas, with spaces, without a full stop at the end!</i>\n<i><b>Answer example</b></i><i>: Yegor, Victor, Alexey, Gleb, Leonid, Dmitry, Konstantin, Boris</i>",
        text_ru="При построении восемь человек разместились так, что:\n\n1) А был впереди Б и В;\n2) Б - впереди К через одного;\n3) Л впереди А, но после Д;\n4)В - после Е через одного;\n5) Д - между Б и Г;\n6) Е - рядом с К, но впереди В.\n\nВ каком порядке выстроились люди?n\n<i><b>Важно</b></i><i>: Ответ пиши через запятую, с пробелами, без точки в конце!</i>\n<i><b>Пример ответа</b></i><i>: К, А, Л, В, Б, Г, Е, Д</i>",
        answer_lv="Gļebs, Dmitrijs, Leonīds, Aleksejs, Boriss, Erlends, Konstantīns, Viktors",
        answer_en="Gleb, Dmitry, Leonid, Alexey, Boris, Yegor, Konstantin, Victor",
        answer_ru="Г, Д, Л, А, Б, Е, К, В",
        choices_lv=None,
        choices_en=None,
        choices_ru=None,
        points=7
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv='Ja astoņkājam ir pāra skaits kāju, tas vienmēr teic patiesību. Ja nepāra, tad viņš vienmēr melo.\n\nKādu dienu zaļais astoņkājis teica tumši zilajam: "Man ir 8 kājas. Un tev ir tikai 6."\n"Man ir 8 kājas," tumši zilais apvainojās. "Bet tev ir tikai 7."\n"Tumši zilajam patiešām ir 8 kājas," violetais sacīja: "Bet man ir 9!"\n"Nevienam no jums nav 8 kājas," sarunā iesaistījās svītrains astoņkājis: "Tikai man ir 8 kājas!"\n\nKuram astoņkājam bija tieši 8 kājas?',
        text_en="If an octopus has an even number of legs, it always tells the truth. If it has an odd number of legs, it always lies.\n\nOne day, the green octopus said to the dark blue one: - I have 8 legs. And you only have 6.\n- I have 8 legs, - the dark blue one was offended. - And you only have 7.\n- The dark blue one really does have 8 legs, - the purple one supported him and bragged: - But I have 9!\n- None of you have 8 legs, - the striped octopus joined the conversation. - Only I have 8 legs!\n\nWhich octopus had exactly 8 legs?",
        text_ru="Если у осьминога чётное число ног, он всегда говорит правду. Если нечётное, то он всегда лжет.\n\nОднажды зелёный осьминог сказал тёмно-синему: - У меня 8 ног. А у тебя только 6.\n- Это у меня 8 ног, - обиделся тёмно-синий. - А у тебя всего 7.\n- У тёмно-синего действительно 8 ног, - поддержал фиолетовый и похвастался: - А вот у меня целых 9!\n- Ни у кого из вас не 8 ног, - вступил в разговор полосатый осьминог. - Только у меня 8 ног!\n\nУ кого из осьминогов было ровно 8 ног?",
        answer_lv="Svītrainajam",
        answer_en="The striped one",
        answer_ru="У полосатого",
        choices_lv=["Zaļajam", "Tumši zilajam", "Violetajam", "Svītrainajam"],
        choices_en=["The green one", "The dark blue one", "The purple one", "The striped one"],
        choices_ru=["У зелёного", "У тёмно-синего", "У фиолетового", "У полосатого"],
        points=6
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Lādē bija divas baltas cepures un trīs melnas.\n\nTumšā istabā ieveda trīs gudriniekus un uzvilka tiem kaut kādas cepures no lādes. Pēc tam ieveda uz citu istabu. Viņi neredz, kādas krāsas cepure ir viņiem pašiem, bet redz, kādas cepures ir citiem.\n\nPēc kāda laika viens no gudriniekiem uzminēja, kādas krāsas viņam ir cepure. Kādas krāsas bija cepure?",
        text_en="There were two white caps and three black ones in the chest.\n\nThe three wise men were brought into a dark room and some caps from the chest were put on them. Then they were taken into another room. They could not see what color the cap was on them, but they could see the caps of others.\n\nAfter a while, one of them guessed what color the cap was on him. What color was the cap?",
        text_ru="В сундуке лежали два колпака белого цвета и три черного.\n\nВ темную комнату завели трех мудрецов и надели на них какие-то колпаки из сундука. Потом вывели в другую комнату. Они не видят, какого цвета колпак на них, но видят колпаки других.\n\nЧерез некоторое время один из них догадался, какого цвета на нем колпак. Какого цвета был колпак?",
        answer_lv="Melna",
        answer_en="Black",
        answer_ru="Чёрный",
        choices_lv=["Melna", "Balta"],
        choices_en=["Black", "White"],
        choices_ru=["Чёрный", "Белый"],
        points=5
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Tiesas priekšā stāv trīs cilvēki, no kuriem katrs var būt aborigēns vai citplanētietis.\nTiesnesis zina, ka aborigēni vienmēr atbild uz jautājumiem patiesi, bet citplanētieši vienmēr melo. Taču tiesnesis nezina, kurš no viņiem ir aborigēns un kurš citplanētietis.\nViņš jautāja pirmajam, bet viņa atbildi nedzirdēja. Tāpēc viņš vispirms jautā otrajam, bet pēc tam trešajam par to, ko atbildēja pirmais.\n\nOtrais saka, ka pirmais sevi sauca par aborigēnu, trešais - ka pirmais sevi sauca par citplanētieti.\n\nKas bija otrais un trešais apsūdzētie?",
        text_en="Three men stand before a judge, each of whom could be either an aborigine or an alien.\nThe judge knows that aborigines always answer questions truthfully, and aliens always lie. However, the judge does not know which of them is an aborigine and which is an alien.\nHe asked the first one, but did not hear his answer. So he asks first the second, and then the third, what the first one answered.\n\nThe second one says that the first one said he was an aborigine, and the third one says that the first one said he was an alien.\n\nWho were the second and third defendants?",
        text_ru="Перед судом стоят три человека, из которых каждый может быть либо аборигеном, либо пришельцем.\nСудья знает, что аборигены всегда отвечают на вопросы правдиво, а пришельцы всегда лгут. Однако судья не знает, кто из них абориген, а кто — пришелец.\nОн сначала спросил первого, но не расслышал его ответа. Поэтому он спрашивает сначала второго, а потом третьего о том, что ответил первый.\n\nВторой говорит, что первый назвался аборигеном, третий — что первый назвался пришельцем.\n\nКем были второй и третий подсудимые?",
        answer_lv="Otrais ir aborigēns, trešais ir citplanētietis",
        answer_en="The second is an aborigine, the third is an alien",
        answer_ru="Второй - абориген, третий - пришелец",
        choices_lv=["Otrais ir aborigēns, trešais ir citplanētietis", "Otrais ir citplanētietis, trešais ir aborigēns", "Otrais un trešais ir aborigēni", "Otrais un trešais ir citplanētieši"],
        choices_en=["The second is an aborigine, the third is an alien", "The second is an alien, the third is an aborigine", "The second and third are natives", "The second and third are aborigines"],
        choices_ru=["Второй - абориген, третий - пришелец", "Второй - пришелец, третий - абориген", "Второй и третий - аборигены", "Второй и третий - пришельцы"],
        points=12
    )

    await rq.add_task(
        grade=9,
        input_type="multiple_choice",
        text_lv="Kad trīs draudzenes - Jana, Nastja un Maša - izgāja ārā pastaigāties, viņas bija ģērbušās baltā, sarkanā un zilā kleitās.\n\nViņu kurpes bija tās pašas trīs krāsas, bet tikai Janas <b>kurpju un kleitas krāsas ir vienādas</b>. Tajā pašā laikā Nastjas kleita un kurpes <b>nebija zilas</b>, bet Mašai bija <b>sarkanas kurpes</b>.\n\nNosaki <b>JANAS</b> kurpju un kleitas krāsas.",
        text_en="When three friends - Yana, Nastya and Masha - went out for a walk, they were wearing white, red and blue dresses.\n\nTheir shoes were the same three colors, but only Yana's shoes and dress <b>matched</b>. At the same time, neither Nastya's dress nor shoes <b>were blue</b>, and Masha was <b>wearing red shoes</b>.\n\nDetermine the colors of <b>YANA's</b> shoes and dress.",
        text_ru="Когда три подруги — Яна, Настя и Маша — вышли гулять, на них были белое, красное и синее платья.\n\nТуфли их были тех же трёх цветов, но только у Яны цвета туфель и платья <b>совпадали</b>. При этом у Насти ни платье, ни туфли <b>не были синими</b>, а Маша была <b>в красных туфлях</b>.\n\nОпредели цвета туфель и платья <b>ЯНЫ</b>.",
        answer_lv="Zilas kurpes un zila kleita",
        answer_en="Blue shoes and a blue dress",
        answer_ru="Синие туфли и синее платье",
        choices_lv=["Sarkanas kurpes un sarkana kleita", "Zilas kurpes un zila kleita", "Baltas kurpes un balta kleita"],
        choices_en=["Red shoes and a red dress", "Blue shoes and a blue dress", "White shoes and a white dress"],
        choices_ru=["Красные туфли и красное платье", "Синие туфли и синее платье", "Белые туфли и белое платье"],
        points=9
    )

if __name__ == "__main__":
    asyncio.run(main()) 