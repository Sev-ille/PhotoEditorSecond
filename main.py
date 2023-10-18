from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen


class PhotoEditorApp(App):
    pass

class Display(Screen,BoxLayout,Image):

    def loadimage(self):
        self.ids.img.source = self.ids.pic.source.text
    def blue_filter(self):
        pic = self.ids.img.source
        img = Image.open(pic)
        pixel = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixel[x, y] = (pixel[x, y][0] == 255, pixel[x, y][1], pixel[x, y][2])

        img.save("Blue.png")
    def red_filter(self,image):
        pixel = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel[x, y] = (pixel[x, y][0] + 255, pixel[x, y][1], pixel[x, y][2])

        image.save("Red.png")

    def invert(self,image):
        pixel = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel[x, y] = (255 - pixel[x, y][0], 255 - pixel[x, y][1], 255 - pixel[x, y][2])

        image.save("Inverse.png")

    def sepia(self,image):
        pixel = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = pixel[x, y][0]
                green = pixel[x, y][1]
                blue = pixel[x, y][2]
                red1 = red * .393 + green * 0.769 + blue * 0.189
                green1 = red * .349 + green * 0.686 + blue * 0.168
                blue1 = red * .272 + green * 0.534 + blue * 0.131
                pixel[x, y] = (int(red1), int(green1), int(blue1))

        image.save("Sepia.png")

    def pixelate(self,image, x, y, width, height):
        ing = image.open(image)
        pixels = ing.load()
        for _i in range(y, height + y, 20):
            for _a in range(x, width + x, 20):
                for s in range(20):
                    for d in range(20):
                        pixels[_a + d, _i + s] = pixels[_a, _i]
        ing.save("pixelate.png")

    def mirror_horizontal(self,image):
        list = []
        ing = image.open(image)
        pixels = ing.load()
        for y in range(ing.size[1]):
            list.append([])
            for x in range(ing.size[0]):
                list[y].append(pixels[x, y])
            list[y].reverse()
        for y in range(ing.size[1]):
            for x in range(ing.size[0]):
                pixels[x, y] = list[y][x]
        ing.save("mirror.png")
    pass

PhotoEditorApp().run()
