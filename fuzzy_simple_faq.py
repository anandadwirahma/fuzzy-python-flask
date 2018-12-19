from flask import Flask
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

def simple_faq():
    context = 0
    entity = []
    reff_user_says = ["jual apaan?", "jual produk apa saja?", "apa yg dijual?"]
    products       = ["rengginang keju", "rengginang coklat", "rengginang kacang ijo"]
    sizes          = ["small","medium","large"] 

    while True:
        if context == 0:
            #-- Context Global Opening  --#
            question  = input("Halo, Selamat datang di toko kami : ")
            print("================================")
            matching  = process.extractOne(question, reff_user_says)
            print('score : ' + str(matching[1]))
            if matching[1] >= 75:
                entity.append(matching[0])
                context = 1
                products_type = ','.join(products)
                answer = "kita ada berbagai macam rengginang. ada %s" % (products_type)
                
                print('entity : ' + str(entity))
                print(answer)
                print("================================")
            else:
                answer = "maaf kami belum mengerti pertanyaan kamu."
                print(answer)
                print("================================")
        elif context == 1:
            #-- Context Choose Product  --#
            question = input("masukan rengginang yang kamu inginkan : ")
            matching = process.extractOne(question, products)
            print('score : ' + str(matching[1]))
            if matching[1] >= 75:
                entity.append(matching[0])
                context = 2
                answer = "Oke baik. Kamu memilih %s ya.." % (matching[0])

                print('entity : ' + str(entity))
                print(answer)
                print("================================")
            else:
                products_type = ','.join(products)
                answer = "maaf masukan pilihan rengginangnya ya. Kita punya %s" % (products_type)
                print(answer)
                print("================================")
        elif context == 2:
            #-- Context Choose Size --#
            question = input("kamu mau rengginang dengan size apa ? ")
            matching = process.extractOne(question, sizes)
            print('score : ' + str(matching[1]))
            if matching[1] >= 75:
                entity.append(matching[0])
                context = 3
                answer = "Oke baik. Rengginang kamu mau size %s ya.." % (matching[0])

                print('entity : ' + str(entity))
                print(answer)
                print("================================")
            else:
                answer = "maaf masukan size yang kamu inginkan. (small/medium/large)"
                print(answer)
                print("================================")
        elif context == 3:
            #-- Context Detail Order --#
            answer = "Berikut detail pesanan kamu : %s (Size : %s)" % (entity[1],entity[2])
            print(answer)
            print("================================")
            context = 0
            entity = []

simple_faq()