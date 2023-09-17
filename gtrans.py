
import google_trans.Ex1

transtext = input("Введіть текст для перекладу: ")
print("https://cloud.google.com/translate/docs/languages -- сайт з кодами мов для перекладу")
target_language = input("Введіть код мови, на яку потрібно перекласти (можна підглянути в посиланні вище): ")

print(google_trans.Ex1.TransLate(transtext, "auto", target_language))

print("\nВизначення мови та коеф. довіри  для введенного тексту:")
print(google_trans.Ex1.LangDetect(transtext, "all"))

print(f"\nНазва мови на яку переклали {target_language}:")
print(google_trans.Ex1.CodeLang(target_language))

print("\nСписок мов у консолі:")
print(google_trans.Ex1.LanguageList("screen"))

print("\nСписок мов з перекладом введеного тексту занесені у файл. \nВи можете переконатися це в файлі list_lang_transl")
print(google_trans.Ex1.LanguageList("file", transtext))