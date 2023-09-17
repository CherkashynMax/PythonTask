from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        return Translator().translate(text, src=src, dest=dest).text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
        translator = Translator()
        try:
            lang = translator.detect(text)
            if set == "lang":
                return lang.lang
            elif set == "confidence":
                return str(lang.confidence)
            else:
                return f"Мова: {lang.lang}, Коефіцієнт довіри: {lang.confidence}"
        except Exception as e:
            return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
        lang = lang.lower()
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():
            return [k for k, v in LANGUAGES.items() if v == lang][0]
        else:
             return f"Мову або код мови '{lang}' не знайдено"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        if out == "screen":
            if text:
                table = "N\tLanguage\tISO-639 code\tText\n"
                table += "-" * 50 + "\n"
                for i, (code, lang) in enumerate(LANGUAGES.items()):
                    translation = translator.translate(text, src="auto", dest=code)
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\t\t\t\t{translation.text}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\t\t\t\t{translation.text}\n"
            else:
                table = "N\tLanguage\tISO-639 code\n"
                table += "-" * 35 + "\n"
                for i, (code, lang) in enumerate(LANGUAGES.items()):
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\n"
            print(table)
            return "Ok"
        elif out == "file":
            if text:
                with open("list_lang_transl_ex1.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\tText\n")
                    file.write("-" * 50 + "\n")
                    for i, (code, lang) in enumerate(LANGUAGES.items()):
                        translation = translator.translate(text, src="auto", dest=code)
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\t\t{translation.text}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\t\t{translation.text}\n")
                    return "Ok"
            else:
                with open("list_lang_transl_ex1.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\n")
                    file.write("-" * 35 + "\n")
                    for i, (code, lang) in enumerate(LANGUAGES.items()):
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\n")
                    return "Ok"
        else:
            return "Неправильний параметр 'out'"
    except Exception as e:
        return str(e)