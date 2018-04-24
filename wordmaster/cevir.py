# -*- coding: utf-8 -*-
import requests, json, pickle, os.path
urlTemplate = "http://cevir.ws/v1?q={0}&m=25&p=exact&l=en"

print("bu uygulama cevir.im alt yapısını kullanmaktadır. kullanımı ve dağıtımı, cevir.ws kullanım koşullarını değiştirmediği sürece tamamen serbesttir.\r\n ")

if not os.path.isfile("vocabulary.p"):
    open("vocabulary.p", "w")


def printVocabulary():
    print("\n -- start of local vocabulary -- \n")

    filex = open("vocabulary.p", "r")

    while 1:
        try:
            entry = pickle.load(filex)
            print("{0} : {1}".format(entry["word"], entry["desc"].encode("utf-8")))
            print("\n")
        except (EOFError):
            break

    filex.close()
    print("-- end of local vocabulary -- \n")

def findInLocal(word):
        filex = open("vocabulary.p", "r")

        while 1:
            try:
                entry = pickle.load(filex)
                if entry["word"] == word:
                    filex.close()
                    return entry["desc"]
            except (EOFError):
                break
        filex.close()
        return "not found"

def addWord():
    word = raw_input("eklemek istediğiniz kelimeyi yazın: ")
    meaning = raw_input("anlamını yazın: ").decode("utf-8")
    pickle.dump({ "word":word , "desc": meaning }, open( "vocabulary.p", "a" ) )
    print("kelime sözlüğe eklendi.")

def showHelp():
    print("""türkçe anlamını öğrenmek istediğiniz ingilizce kelimeyi yazıp enter'a basın.
        aralarında birer boşluk bırakarak birden fazla kelime sorgulayabilirsiniz.
        kelime eklemek için a yazıp enter'a basın.
        kelime dağarcığınızı görmek için v'ye, çıkmak için q yazıp enter'a basın
        bu açıklamayı tekrar görüntülemek için h yazıp enter'a basın""")

showHelp()

while True:

    userInput = str(raw_input())

    if userInput == "q":
        quit()
    elif userInput == "v":
        printVocabulary()
    elif userInput == "a":
        addWord()
    elif userInput == "h":
        showHelp()
    else:

        words = userInput.split()

        for word in words:

            local = findInLocal(word)
            if  local == "not found":
                print("yerel db'de bulunamadı. cevir.ws'ye soruluyor...")
                url = urlTemplate.format(str(word))
                response = requests.get(url)
                result = json.loads(response.text)

                if result["control"]["results"] == 0:
                    print("sonuç bulunamadı")
                else:
                    print("{0} : {1}".format(word, result["word"][0]["desc"].encode("utf-8")))
                    pickle.dump({ "word":word , "desc": result["word"][0]["desc"] }, open( "vocabulary.p", "a" ) )
                    print("")

            else:
                print("yerel db'de bulundu")
                print(local)
