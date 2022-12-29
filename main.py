from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

nome = 'Nome do contribuinte'
cargo = 'Cargo'
data_aniversario = '00/00/0000'

template = Image.open('./template/template.jpg')
fotoPerfil = Image.open('./pictures/fotoPerfil.jpeg')
png = Image.open('./imagesCreated/ImagemPNG.png')
imagemRotacionada = Image.open('./imagesCreated/imagemRotacionada.png')

Drawtemplate = ImageDraw.Draw(template)
drawPng = ImageDraw.Draw(png)

fontName = ImageFont.truetype('./fonts/BaksoSapi.otf',50)
fontCargo = ImageFont.truetype('./fonts/BaksoSapi.otf',37)

def createPNG():
    newTemplate = Image.new("RGBA", (1080, 1920), (0,0,0,0) )
    return newTemplate.save('./imagesCreated/ImagemPNG.png')

def imageRotated(fotoPerfil, png):
    png.paste(fotoPerfil, box=(250,600))
    im_rotated = png.rotate(3)
    return im_rotated.save('./imagesCreated/imagemRotacionada.png')
    
def pastPicture(template, fotoPerfil):
    template.paste(fotoPerfil, box=(250,600))
    return template.save('./imagesCreated/fotoColada.jpg')

def createPicture(nome, cargo, data_aniversario, Drawtemplate, fontName, fontCargo):
    Drawtemplate.text((260,1270), nome, fill='Black', font=fontName)
    Drawtemplate.text((260,1310), cargo, fill='Black', font=fontCargo)
    Drawtemplate.text((700,1150), data_aniversario, fill='Black', font=fontCargo)
    return template.save('./imagesCreated/TextoColado.jpg')

createPNG()
imageRotated(fotoPerfil, png)
pastPicture(template, fotoPerfil)
createPicture(nome, cargo, data_aniversario, Drawtemplate, fontName, fontCargo)