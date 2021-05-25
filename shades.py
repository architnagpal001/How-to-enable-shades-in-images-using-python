from PIL import Image

img = Image.open('mark.jpg')
img.show()
sh_img = img.convert('L')
sh_img.show()
#sh_img.save(sh_mark.jpg)
bw_img = img.convert('1')
bw_img.show()
