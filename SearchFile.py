
# ===================IMPORTS======================
import json
import pyquran as q
import io
import string
import pyarabic.araby as araby


#===============================================


# #==================Loading Surhas json file==========================#
# with io.open('files/surahNames.json' ,'r' ,encoding='utf8') as file:
#   SurhaNames = json.load(file)
# SurhaNames =   SurhaNames[0]
# SurhaNames_arabic = SurhaNames['arabic']
# SurhaNames_english = SurhaNames['english']
# print(SurhaNames_arabic)

#==================Loading Surhas json file==========================#
with io.open('files/surahNames.json' ,'r' ,encoding='utf8') as file:
  SurhaNames = json.load(file)
SurhaNames =   SurhaNames[0]
SurhaNames_arabic = SurhaNames['arabic']
SurhaNames_english = SurhaNames['english']
#print(type(SurhaNames_arabic))
#==================================================================#

#==================Loading Ayahs json file==========================#
with io.open('files/surahAyahs.json' ,'r' ,encoding='utf8') as file:
  SurhasAyahs = json.load(file)
SurhasAyahs = SurhasAyahs
# print(SurhasAyahs[0]['verse'])
# print(f"Length : ",len(SurhasAyahs))
#==================================================================#

# ================Method For Matching Surha Names====================#
def match_index_surha(surha_name):
  # index_surah = q.quran.get_sura_number(surha_name)
  # print(index_surah)
  if surha_name in SurhaNames_arabic:
    print("FOUND")
    indexSurha =  SurhaNames_arabic.index(surha_name)
    print(indexSurha)
    print(surha_name)
    if indexSurha == 0:
       indexSurha=1
    print(f"Surha Number : {indexSurha+1}")
    indexSurha = indexSurha+1
    #print(q.quran.get_sura(indexSurha, with_tashkeel=True))
    data = q.quran.get_sura(indexSurha, with_tashkeel=True)
    data.insert(0,""+q.quran.get_sura_name(indexSurha))
   # print(data)
    #print(q.quran.get_sura_name(indexSurha))
    return data
  else:
    return "Not Found"


def match_surha_ayaha(ayaha_name):
  found = False
  dict_index =   0
  surha_length = len(SurhasAyahs)
  for i in range(surha_length):
    if ayaha_name in SurhasAyahs[i]['verse']:
      dict_index = i
      found = True
      break
    else:
      found = False
  if found == True:
   # print(f"Surah Number : ",SurhasAyahs[dict_index]['index'])
    index_id = SurhasAyahs[dict_index]['index']
      # q.quran.get_sura_name(int(SurhasAyahs[dict_index]['index']))
    # print(f"Surah Name : ",q.quran.get_sura_name(int(SurhasAyahs[dict_index]['index'])))
    # print(f"Total Ayats : ",SurhasAyahs[dict_index]['count'])
    # print(f"Ayats :",SurhasAyahs[dict_index]['verse'])
    print(type(index_id))
    return index_id
  else:
    print("No Match Found")

  
  
#match_surha_ayaha('لَتَرَوُنَّ ٱلْجَحِيمَ')


#match_index_surha('فاطر')


