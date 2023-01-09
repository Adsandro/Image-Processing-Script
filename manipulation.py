from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# A função calcNewHeight realiza um calculo para definir o melhor tamanho
# da imagem conforme a largura selecionada, como padrão foi utilizado
# largura de 600px para encaixar no template selecionado.
def calcNewHeight(newWidth, profilePicture):
    width, height = profilePicture.size
    newHeight = round((newWidth * height) / width)
    return newHeight

# Em conjunto com a calcNewHeight, a resizeImage utiliza o calculo realizado
# e a largura ja definida para redimencionar as imagens selecionadas.
def resizeImage(newWidth, profilePicture):
    newHeight = calcNewHeight(newWidth, profilePicture)
    newPicture = profilePicture.resize((newWidth, newHeight), Image.LANCZOS)
    return newPicture.save(f'./imagesResized/{name}Picture.png')

# A função pastePicture possui como objetivo colar uma imagem em cima da
# outra, o parametro box trata-se das coordenadas no template.
def pastePicture(template, profilePicture):
    pastePicture = template.paste(profilePicture, box=(245,890))
    return pastePicture

# No createDraw o pillow estara escrevendo os textos que deseja,
# as alterações relacionadas a fonte deve ser realizadas nas variaveis
# que foram declaras como fontName, fontCargo e fontDate, o parametro
# fill é responsavel pela cor do texto e o parametro restante esta relacionado
# as coordenadas que serão escritas cada texto.
def createDraw(name, cargo, data_aniversario, Drawtemplate, fontName, fontCargo):
    Drawtemplate.text((260,1400), name, fill='Black', font=fontName)
    Drawtemplate.text((260,1470), cargo, fill='Black', font=fontCargo)
    Drawtemplate.text((630,1470), data_aniversario, fill='Black', font=fontDate)
    return template.save(f'./imagesCreated/{name}_Template.jpg')

if __name__ == "__main__":

    newWidth = 600

    name = 'Nome_do_contribuinte'
    cargo = 'Cargo'
    data_aniversario = '00/00/0000'

    template = Image.open('./template/template.jpg')
    profilePicture = Image.open('./pictures/profilePicture.jpeg')

    resizeImage(newWidth, profilePicture)
    pictureResized = Image.open(f'./imagesResized/{name}Picture.png')
    Drawtemplate = ImageDraw.Draw(template)

    fontName = ImageFont.truetype('./fonts/BaksoSapi.otf',45)
    fontOffice = ImageFont.truetype('./fonts/BaksoSapi.otf',27)
    fontDate = ImageFont.truetype('./fonts/BaksoSapi.otf',33)
    
    pastePicture(template, pictureResized)
    createDraw(name, cargo, data_aniversario, Drawtemplate, fontName, fontOffice)