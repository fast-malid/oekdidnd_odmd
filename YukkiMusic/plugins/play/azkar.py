import asyncio

import os
import time
import datetime
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint


@app.on_message(
    command(["اذكار","الازكار"])
    & ~filters.edited)
async def azkar(c: Client, m: Message):
    if datetime.datetime.now().hour == 1 or datetime.datetime.now().hour == 4 or datetime.datetime.now().hour == 7 \
            or datetime.datetime.now().hour == 10 or datetime.datetime.now().hour == 13 \
            or datetime.datetime.now().hour == 16 or datetime.datetime.now().hour == 19 \
            or datetime.datetime.now().hour == 22:
        listAzkar = ["لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
                     "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
                     "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
                     "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "سبحان الله وبحمده سبحان الله العظيم🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
                     "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
                     "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
                     "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
                     "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
                     "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
                     "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
                     "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
                     "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
                     "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
                     "استغفر الله العظيم وأتوبُ إليه.",
                     "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
                     " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
                     "ماتستغفر ربنا كده🥺❤️",
                     "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
                     "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
                     "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
                     "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
                     "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
                     "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
                     "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
                     "أصبحنا وأصبح الملك لله ولا اله الا الله.",
                     "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
                     "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
                     "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
                     "- اللهم القبول الذي لا يزول ❤️🍀.",
                     "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
                     "سبحان الله وبحمده ،سبحان الله العظيم.",
                     "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
                     " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
                     "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
                     "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
                     "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
                     "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
                     "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
                     "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
                     "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
                     "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
                     "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
                     "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
                     "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
                     "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
                     "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
                     "صلي على النبي بنيه الفرج❤️",
                     "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
                     "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
                     "لا اله الا الله سيدنا محمد رسول الله🌿💜",
                     "قول معايا - استغفر الله استفر الله استغفر الله -",
                     "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
                     "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
                     "صلي على محمد❤️",
                     "ماتيجو نقرء الفاتحه سوا🥺"]
        await c.send_message(m.chat.id, random.choice(listAzkar))
        
