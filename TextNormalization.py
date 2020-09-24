import re
# def translitArabic(text):
#   buckwalterMod = {
#     'ء': 'c', 'ا': 'A', 'إ': 'A',
#     'أ': 'A', 'آ': 'A', 'ب': 'b',
#     'ة': 'o', 'ت': 't', 'ث': 'v',
#     'ج': 'j', 'ح': 'H', 'خ': 'x',
#     'د': 'd', 'ذ': 'V', 'ر': 'r',
#     'ز': 'z', 'س': 's', 'ش': 'E',
#     'ص': 'S', 'ض': 'D', 'ط': 'T',
#     'ظ': 'Z', 'ع': 'C', 'غ': 'g',
#     'ف': 'f', 'ق': 'q', 'ك': 'k',
#     'ل': 'l', 'م': 'm', 'ن': 'n',
#     'ه': 'h', 'ؤ': 'c', 'و': 'w',
#     'ى': 'y', 'ئ': 'c', 'ي': 'y',
#   }
#   for k, v in buckwalterMod.items():
#     text = re.sub(k, v, text)
#   return (text)
#
#   def normalizeArabic(text):
#     text = re.sub("[إأٱآا]", "ا", text)
#     text = re.sub("ى", "ي", text)
#     text = re.sub("ؤ", "ء", text)
#     text = re.sub("ئ", "ء", text)
#     return (text)
#
#   def deNormalize(text):
#     alifs = '[إأٱآا]'
#     alifReg = '[إأٱآا]'
#     # -------------------------------------
#     alifMaqsura = '[يى]'
#     alifMaqsuraReg = '[يى]'
#     # -------------------------------------
#     taMarbutas = 'ة'
#     taMarbutasReg = '[هة]'
#     # -------------------------------------
#     hamzas = '[ؤئء]'
#     hamzasReg = '[ؤئءوي]'
#     # Applying deNormalization
#     text = re.sub(alifs, alifReg, text)
#     text = re.sub(alifMaqsura, alifMaqsuraReg, text)
#     text = re.sub(taMarbutas, taMarbutasReg, text)
#     text = re.sub(hamzas, hamzasReg, text)
#     return text
#
#   def deNoiseText(text):
#     noise = re.compile(""" ّ    | # Tashdid
#                              َ    | # Fatha
#                              ً    | # Tanwin Fath
#                              ُ    | # Damma
#                              ٌ    | # Tanwin Damm
#                              ِ    | # Kasra
#                              ٍ    | # Tanwin Kasr
#                              ْ    | # Sukun
#                              ـ     # Tatwil/Kashida
#                          """, re.VERBOSE)
#     text = re.sub(noise, '', text)
#     return text
#
#
# #print(translitArabic('سوره المؤمنون'))
#
# #print(deNoiseText("سوره المؤمنون"))

noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
text = re.sub(noise, '', "ۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ")
print(text)


text =  "ۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ"
text = re.sub("[إأٱآا]", "ا", text)
text = re.sub("ى", "ي", text)
text = re.sub("ؤ", "ء", text)
text = re.sub("ئ", "ء", text)
print(text)
