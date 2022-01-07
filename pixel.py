from PIL import Image

im = Image.open('1.png')
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

#degiştirilecekPixelKodları = [(204,204,204,255),
 #                             (205,205,205,255),]

resimÜzerindeDeğiştirilecekPixelKodları = [(i,i,i,255) for i in range(204,249)]
#print (resimÜzerindeDeğiştirilecekPixelKodları)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if  pixelMap[i,j] in resimÜzerindeDeğiştirilecekPixelKodları:
           #print(pixelMap[i,j]) 
           pixelMap[i,j] = (255,255,255,255)
        pixelsNew[i,j] = pixelMap[i,j]
im.close()
img.show()       
img.save("out.png") 
img.close()