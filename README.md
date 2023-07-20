# Image Processing Script

This Python code contains functions to create a custom birthday image using a template model and a profile picture. The final image is generated with the contributor's name and birth date inserted into the template.

1.  Packages used:
    
    -   `PIL`: The Python Imaging Library package is used for image manipulation.
    -   `logging`: The logging package is used to log information and errors to a log file.
2.  Functions: a) `calc_new_height(new_width, profile_picture)`: Calculates the new height of the profile picture by providing a specific width, maintaining the original aspect ratio. b) `resize_image(new_width, profile_picture)`: Resizes the profile picture to a specific width and saves the resized image. c) `paste_picture(template, profile_picture, box_coords)`: Inserts the resized profile picture into the provided template model and saves the resulting image. d) `create_birthday_image(name, birth_date, template_path, profile_picture_path, font_name_path, font_date_path, font_size_name=45, font_size_date=33)`: The main function that creates the final birthday image by adding the contributor's name and birth date to the template image.
    
3.  Program flow:
    
    -   In the `main()` function, paths to fonts, the template model, and the profile picture are defined.
    -   The `create_birthday_image()` function is called with the required parameters to create the custom image.
    -   The image is created by inserting the contributor's name and birth date into the template model.
4.  File structure:
    
    -   The resized image is saved in the "./imagesResized/" folder with the name "Nome_do_contribuinte_Picture.png".
    -   The final image is saved in the "./imagesCreated/" folder with the name "Nome_do_contribuinte_Template.jpg".
    -   The font files are stored in the "./fonts/" folder.
5.  Logging records:
    
    -   The code uses the `logging` package to log information about the image creation process and possible errors.
    -   The log information is recorded in a file named "log_automated_action.log".

Note: To ensure the code runs correctly, the PIL (Pillow) package and the font file 'BaksoSapi.otf' must be installed in the "./fonts/" folder.