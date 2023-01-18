from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import logging

logging.basicConfig(level=logging.INFO, 
                    filename='log_automated_action.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# A função calc_new_height realiza um calculo para definir o melhor tamanho
# da imagem conforme a largura selecionada, como padrão foi utilizado
# largura de 600px para encaixar no template selecionado.
def calc_new_height(newWidth, profilePicture):
    try:
        width, height = profilePicture.size
        newHeight = round((newWidth * height) / width)
    except:
        logging.info('Não foi possivel calcular o novo tamanho da foto de perfil')
    else:
        logging.info('Calculo de largura e altura realizado com sucesso!')
        return newHeight

# Em conjunto com a calc_new_height, a resize_image utiliza o calculo realizado
# e a largura ja definida para redimencionar as imagens selecionadas.
def resize_image(newWidth, profilePicture):
    try:
        newHeight = calc_new_height(newWidth, profilePicture)
        newPicture = profilePicture.resize((newWidth, newHeight), Image.LANCZOS)
    except:
        logging.info('Não foi possivel colar a imagem no template')
    else:
        logging.info('Imagem redimencionada com sucesso!')
        return newPicture.save(f'./imagesResized/Nome_do_contribuinte_Picture.png')

# A função paste_picture possui como objetivo colar uma imagem em cima da
# outra, o parametro box trata-se das coordenadas no template.
def paste_picture(template, profilePicture):
    try:
        paste_picture = template.paste(profilePicture, box=(245,890))
    except:
        logging.info('Nãofoi possivel colar a imagem no template')
    else:
        logging.info('Imagem colada no template com sucesso!')
        return paste_picture

# No create_birthday_image o pillow estara escrevendo os textos que deseja,
# as alterações relacionadas a fonte deve ser realizadas nas variaveis
# que foram declaras como fontName, fontCargo e fontDate, o parametro
# fill é responsavel pela cor do texto e o parametro restante esta relacionado
# as coordenadas que serão escritas cada texto.
def create_birthday_image(name, cargo, data_aniversario, Drawtemplate, fontName, fontCargo):
    try:
        Drawtemplate.text((260,1400), name, fill='Black', font=fontName)
        Drawtemplate.text((630,1470), data_aniversario, fill='Black', font=fontDate)
    except:
        logging.info('A operação de criação de imagem falhou')
    else:
        logging.info(f'Template de Nome_do_contribuinte criado com sucesso!')
        return template.save(f'./imagesCreated/Nome_do_contribuinte_Template.jpg')
    finally:
        print('Programa finalizado!')

if __name__ == "__main__":

    newWidth = 600

    name = 'Nome_do_contribuinte'
    cargo = 'Cargo'
    data_aniversario = '00/00/0000'

    template = Image.open('./template/template.png')
    profilePicture = Image.open('./pictures/profilePicture.jpeg')

    resize_image(newWidth, profilePicture)
    pictureResized = Image.open(f'./imagesResized/Nome_do_contribuinte_Picture.png')
    Drawtemplate = ImageDraw.Draw(template)

    fontName = ImageFont.truetype('./fonts/BaksoSapi.otf',45)
    fontOffice = ImageFont.truetype('./fonts/BaksoSapi.otf',27)
    fontDate = ImageFont.truetype('./fonts/BaksoSapi.otf',33)
    
    paste_picture(template, pictureResized)
    create_birthday_image(name, cargo, data_aniversario, Drawtemplate, fontName, fontOffice)