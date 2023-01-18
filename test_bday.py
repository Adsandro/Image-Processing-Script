from faker import Faker
import unittest
import requests
from manipulation import calc_new_height, create_birthday_image, resize_image, paste_picture, create_birthday_image

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class TestBday(unittest.TestCase):
    # def test_bday_text_sucess(self):
    #     webhook = ('b6ba8d5c-19a1-4c38-8f5b-3966f11f2bbe')
    #     api_key = ('663efa01-a3c5-4464-b501-b8e4bc71f4fa')
    #     baseurl = ('https://backend.botconversa.com.br/api/v1/webhook')
    #     bot = Botconversa(webhook, api_key, baseurl)

    #     fake = Faker()
    #     text = fake.text()

    #     response, type, content, recipient = bot.send_message('text',text, '102126396')

    #     self.assertEqual(response.status_code, 200)

    #     self.assertEqual(type, 'text')
    #     self.assertEqual(content, text)
    #     self.assertEqual(recipient, '102126396')
    
    # def test_bday_text_error(self):
    #     webhook = ('b6ba8d5c-19a1-4c38-8f5b-3966f11f2bbe')
    #     api_key = ('663efa01-a3c5-4464-b501-b8e4bc71f4fa')
    #     baseurl = ('https://backend.botconversa.com.br/api/v1/webhook')
    #     bot = Botconversa(webhook, api_key, baseurl)

    #     fake = Faker()
    #     text = fake.text()

    #     #o atrr type deve ser quando o content for algum arquivo como png ou jpg
    #     response, type, content, recipient = bot.send_message('file',text, '102126396')

    #     self.assertEqual(response.status_code, 200)

    #     self.assertEqual(type, 'text')
    #     self.assertEqual(content, text)
    #     self.assertEqual(recipient, '102126396')


    # def test_calc_new_height_sucess(self):
    #     newWidth = 600
    #     profilePicture = Image.open('./pictures/profile.png')
    #     self.assertEqual(calc_new_height(newWidth, profilePicture), 632)

    # def test_calc_new_height_error(self):
    #     newWidth = 600
    #     profilePicture = Image.open('./pictures/profile.png')
    #     self.assertEqual(calc_new_height(newWidth, profilePicture), 600)

    def test_create_birthday_image_sucess(self):
        name = 'Nome_do_contribuinte'
        cargo = 'Cargo'
        data_aniversario = '00/00/0000'
        template = Image.open('./template/template.png')
        Drawtemplate = ImageDraw.Draw(template)
        fontName = ImageFont.truetype('./fonts/BaksoSapi.otf',45)
        fontCargo = ImageFont.truetype('./fonts/BaksoSapi.otf',27)

        name, data_aniversario  = create_birthday_image('Nome_do_contribuinte', '00/00/0000')

        self.assertEqual(name, 'Nome_do_contribuinte')
        self.assertEqual(cargo, 'Cargo')
        self.assertEqual(data_aniversario, '00/00/0000')

    
if __name__ == "__main__":
    unittest.main()
