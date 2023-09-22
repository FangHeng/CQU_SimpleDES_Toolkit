from django.shortcuts import render,HttpResponse
from SDES.SDES import SDES
from django.http import JsonResponse

def start(request):
    return render(request,"index.html")

def index(request):
    return render(request,"index.html")


def plaintext_sent(request):
    if request.method == 'POST':
        key_input = request.POST['key']
        plaintext_input = request.POST['plaintext']
        type = request.POST['type']
        if (type == "ASCII"):
            sdes = SDES(key=key_input)
            out = ""
            for i in range(len(plaintext_input)):
                temp = bin(ord(plaintext_input[i])).replace("0b","").zfill(8)
                out_bin = sdes.encrypt(temp)
                out_hex = hex(int(out_bin, 2))[2:].zfill(2)
                out += (out_hex)

            data = {
                "ciphertext" : out
            }

            return JsonResponse(data)

        elif(type == "Bit"):
            sdes = SDES(key=key_input)
            out_bin = sdes.encrypt(plaintext_input)
            data = {
                "ciphertext": out_bin
            }
            return JsonResponse(data)


def ciphertext_sent(request):
    #
    # 用户输入的文本就记作：plaintext
    if request.method == 'POST':
        key_input = request.POST['key']
        ciphertext_input = request.POST['plaintext']
        type = request.POST['type']
        if(type == "ASCII"):
            sdes = SDES(key=key_input)
            out = ""
            for i in range(len(ciphertext_input)//2):
                temp1 = bin(int(ciphertext_input[2*i], 16)).replace("0b", "").zfill(4)
                temp2 = bin(int(ciphertext_input[2*i+1], 16)).replace("0b", "").zfill(4)
                out_bin = sdes.decrypt(temp1+temp2)
                out_chr=chr(int(out_bin, 2))
                out += (out_chr)

            data = {
                "ciphertext": out
            }
            return JsonResponse(data)

        elif(type == "Bit"):
            sdes = SDES(key=key_input)
            out_bin = sdes.decrypt(ciphertext_input)
            data = {
                "ciphertext": out_bin
            }
            return JsonResponse(data)