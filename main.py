from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

funcionarios = {"Nome":                 ["Adsandro Carvalho", "Adsandro Lucas Martins"],
                "Data de nascimento":   ["01/12/2002", "23/06/2003"],
                "Cargo":                ["Desenvolvedor Python", "Database analyst"]
                }


nome = (funcionarios["Nome"][1])
cargo = (funcionarios["Cargo"][1])
data_aniversario = (funcionarios["Data de nascimento"][1])

image = Image.new('RGB', (1080, 1920), color=(0,0,0,0))
image.save('./imagesCreated/transparentIMage.png')

template =          Image.open('./pictures/template.jpg')
transparentImage =  Image.open('./imagesCreated/transparentIMage.png')

Drawtemplate = ImageDraw.Draw(template)

fontName = ImageFont.truetype('./fonts/BaksoSapi.otf',50)
fontCargo = ImageFont.truetype('./fonts/BaksoSapi.otf',37)


Drawtemplate.text((260,1270), nome, font=fontName)
Drawtemplate.text((260,1310), cargo, font=fontCargo)
Drawtemplate.text((700,1150), data_aniversario, font=fontCargo)

template.save('./imagesCreated/teste3.jpg')



