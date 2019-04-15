from PIL import Image
from PIL import ImageFilter

class sponsoredImageInsertion:

    def insert(mg, sponsored_item):
        # retrieve the width and height of the image for the scale
        width, height = img.size

        # create a scale for insert to be resized to
        scale = round(width/5)

        # create a copy of the original image
        img_copy = img.copy()

        # retrieve the proper sponsored item insert
        insert = Image.open('sponsored_items/' + sponsored_item + '.png')

        # resize the sponsored item
        insert = insert.resize((scale,scale), Image.ANTIALIAS)

        for x in range(scale):
            for y in range(scale):
                pixel = insert.getpixel((x, y))
                img_copy.putpixel((x, y), pixel)

        # return the image with the sponsored content inserted
        return img_copy

# Main which is just here for testing
if __name__ == '__main__':
    # Open the image file and read in its data so that we can access it
    img = Image.open('../fisher.jpeg')

    new_img = sponsoredImageInsertion.insert(img, "pepsi")

    # Save the image file so that we can view it
    new_img.save('sponsored_item_pic.bmp')
