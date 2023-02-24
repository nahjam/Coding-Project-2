from hdnhd_utils import *
from PIL import  ImageFont

def label_image(img):
    """
    Creates and returns a copy of the image, labeled as either Hot Dog or Not Hot Dog
    based off of the results from GCP Vision API.
    :param img: a string that is either the URL or filename for the image
    :return: a copy of the image labeled as either Hot Dog or Not Hot Dog
    """
    filename=img
    results = detect_image_labels(filename)
    labels = [label['description'].lower() for label in results]
    img_bytes = load_image_bytes(filename)
    pillow_img = create_pillow_img(img_bytes)
    green = (0,255,0,200)
    red = (255,0,0)
    white=(255,255,255)
    img_font=ImageFont.truetype('ariblk.ttf', 40)
    img_w,img_h=pillow_img.width,pillow_img.height
    is_hotdog='hot dog' in labels
    if is_hotdog:
        img_text = "Hot Dog"
        img_color=green
    else:
        img_text = "Not Hot Dog"
        img_color=red

    text_w,text_h=text_rect_size(img_text,img_font)
    padding=10
    if is_hotdog:
        y_pos=padding
    else:
        y_pos=img_h-text_h - padding

    labeled_img = add_text_to_img(pillow_img,img_text,(img_w//2 - (text_w//2),y_pos),white,img_color,font=img_font)
    return labeled_img


def main():
    """
    Main function that runs the program.
    """
    # URLs for some sample images to try
    # NOTE: the TAs may use other images for testing your program
    # Hot Dog
    # img = 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Hot_dog_with_mustard.png'
    # Not Hot Dog (Pizza)
    # img = 'https://render.fineartamerica.com/images/rendered/default/poster/8/10/break/images/artworkimages/medium/1/pizza-slice-diane-diederich.jpg'
    # The image below is an example of a hot dog that is not labeled as a hot dog
    # since your program relies on GCP Vision API, which is not perfect,
    # such an image will be (mis-)labeled as Not Hot Dog by your program
    # that is the expected behavior, you don't need to build your own better hot dog detector ;)
    # img = 'https://i.kinja-img.com/gawker-media/image/upload/s--6RyJpgBM--/c_scale,f_auto,fl_progressive,q_80,w_800/tmlwln8revg44xz4f0tj.jpg'

    # DONE: your code to read the URL/filename from the user
    # DONE: and then call label_image
    # DONE: and then finally show the image returned by the call to label_image
    
    img=input("Enter either a URL or filename for an image: ")
    if img.strip() == "":
        print("No image URL/filename provided")
        exit(1)

    labeled_img = label_image(img)
    labeled_img.show()
    
    
if __name__ == "__main__":
    main()
