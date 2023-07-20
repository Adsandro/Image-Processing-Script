from PIL import Image, ImageDraw, ImageFont
import logging

logging.basicConfig(level=logging.INFO, filename='log_automated_action.log', format='%(asctime)s - %(levelname)s - %(message)s')

def calc_new_height(new_width, profile_picture):
    try:
        width, height = profile_picture.size
        new_height = round((new_width * height) / width)
        logging.info('Calculation of width and height successful!')
        return new_height
    except Exception as e:
        logging.error('Failed to calculate the new profile picture height: %s', str(e))
        return None

def resize_image(new_width, profile_picture):
    try:
        new_height = calc_new_height(new_width, profile_picture)
        if new_height:
            new_picture = profile_picture.resize((new_width, new_height), Image.LANCZOS)
            new_picture.save(f'./imagesResized/Nome_do_contribuinte_Picture.png')
            logging.info('Image resized successfully!')
    except Exception as e:
        logging.error('Failed to resize the profile picture: %s', str(e))

def paste_picture(template, profile_picture, box_coords):
    try:
        template.paste(profile_picture, box=box_coords)
        template.save(f'./imagesCreated/Nome_do_contribuinte_Template.jpg')
        logging.info('Profile picture pasted on template successfully!')
    except Exception as e:
        logging.error('Failed to paste the profile picture on the template: %s', str(e))

def create_birthday_image(name, birth_date, template_path, profile_picture_path, font_name_path, font_date_path, font_size_name=45, font_size_date=33):
    try:
        template = Image.open(template_path)
        profile_picture = Image.open(profile_picture_path)

        new_width = 600
        resize_image(new_width, profile_picture)

        picture_resized = Image.open(f'./imagesResized/Nome_do_contribuinte_Picture.png')
        draw_template = ImageDraw.Draw(template)

        font_name = ImageFont.truetype(font_name_path, font_size_name)
        font_date = ImageFont.truetype(font_date_path, font_size_date)

        draw_template.text((260, 1400), name, fill='Black', font=font_name)
        draw_template.text((630, 1470), birth_date, fill='Black', font=font_date)
        template.save(f'./imagesCreated/Nome_do_contribuinte_Template.jpg')

        logging.info('Template for Nome_do_contribuinte created successfully!')
    except Exception as e:
        logging.error('Failed to create the birthday image: %s', str(e))
    finally:
        print('Finally!')

def main():
    name = 'Nome_do_contribuinte'
    cargo = 'Cargo'
    data_aniversario = '00/00/0000'

    font_name_path = './fonts/BaksoSapi.otf'
    font_date_path = './fonts/BaksoSapi.otf'
    template_path = './template/template.png'
    profile_picture_path = './pictures/profilePicture.jpeg'

    create_birthday_image(name, data_aniversario, template_path, profile_picture_path, font_name_path, font_date_path)

if __name__ == "__main__":
    main()
