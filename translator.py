from google_trans_new import google_translator
sentence=str(input ("Sentence to translate: "))
# you can change the code below to change the language the input is translated to
# to check the code go to https://www.labnol.org/code/19899-google-translate-languages
trans_lang="hi"
translator=google_translator()
translated_sentence=translator.translate(sentence,lang_tgt=trans_lang)
print(translated_sentence)