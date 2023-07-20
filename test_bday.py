import unittest
from PIL import Image
from manipulation import calc_new_height, resize_image

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        self.test_profile_picture = Image.new('RGB', (800, 600))

    def test_calc_new_height(self):
        new_width = 400
        new_height = calc_new_height(new_width, self.test_profile_picture)
        self.assertEqual(new_height, 300)

        new_width = 200
        new_height = calc_new_height(new_width, self.test_profile_picture)
        self.assertEqual(new_height, 150)

    def test_resize_image(self):
        new_width = 400
        resize_image(new_width, self.test_profile_picture)
        resized_image = Image.open('./imagesResized/Nome_do_contribuinte_Picture.png')
        self.assertEqual(resized_image.size, (400, 300))

        new_width = 200
        resize_image(new_width, self.test_profile_picture)
        resized_image = Image.open('./imagesResized/Nome_do_contribuinte_Picture.png')
        self.assertEqual(resized_image.size, (200, 150))

if __name__ == '__main__':
    unittest.main()
