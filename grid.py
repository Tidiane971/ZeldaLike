from PIL import Image

path = input("Entrer le chemin du fichier : ")

im = Image.open(path)
pix = im.load()


T = []

x,y = im.size
for k in range(y//64):
    T.append([])
j=0
for k in range(0,y,64):
    for i in range(0,x,64):
        if pix[i+32,k+32] == (255,0,0):
            T[k//64].append(1)
        else:
            T[k//64].append(0)
print(T)
