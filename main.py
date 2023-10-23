from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from PIL import Image
from kivy.uix.widget import Widget


class PhotoEditorApp(App):
    pass




class Display(Screen,BoxLayout,Widget):

    def loadimage(self):
        self.ids.img.source = self.ids.pic.text
    def blue_filter(self):
        pic = self.ids.img.source
        img = Image.open(pic)
        pixel = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixel[x, y] = (pixel[x, y][0] == 255, pixel[x, y][1], pixel[x, y][2])

        img.save("Blue.png")
        self.ids.img.source = "Blue.png"
    def red_filter(self):
        pic = self.ids.img.source
        image = Image.open(pic)
        pixel = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel[x, y] = (pixel[x, y][0] + 255, pixel[x, y][1], pixel[x, y][2])

        image.save("Red.png")
        self.ids.img.source = "Red.png"

    def invert(self):
        pic = self.ids.img.source
        image = Image.open(pic)
        pixel = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel[x, y] = (255 - pixel[x, y][0], 255 - pixel[x, y][1], 255 - pixel[x, y][2])

        image.save("Inverse.png")
        self.ids.img.source = "Inverse.png"

    def sepia(self):
        pic = self.ids.img.source
        image = Image.open(pic)
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
        self.ids.img.source = "Sepia.png"

    cordinates = []

    def on_touch_up(self, touch):
        x, y = touch.x, touch.y
        self.cordinates.append(int(x))
        self.cordinates.append(int(y))
        if len(self.cordinates) > 4:
            self.cordinates = self.cordinates[2:]
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_up(touch)
        touch.pop()
        return ret

    def on_touch_down(self, touch):
        x, y = touch.x, touch.y
        self.cordinates.append(x)
        self.cordinates.append(y)
        if len(self.cordinates)>4:
            self.cordinates =self.cordinates[2:]
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_down(touch)
        touch.pop()
        return ret

    def pixelate(self):
        pic = self.ids.img.source
        image = Image.open(pic)
        ing = image.open(image)
        pixels = ing.load()
        self.on_touch_down(touch)
        self.on_touch_up(touch)
        y = self.cordinates[1]
        x = self.cordinates[0]
        height = self.cordinates[3]
        width = self.cordinates[2]
        for _i in range(y, height, 20):
            for _a in range(x, width, 20):
                for s in range(20):
                    for d in range(20):
                        pixels[_a + d, _i + s] = pixels[_a, _i]
        ing.save("pixelate.png")
        self.ids.img.source = "pixelate.png"

        pass

    def mirror_horizontal(self):
        pic = self.ids.img.source
        ing = Image.open(pic)
        list = []
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
        self.ids.img.source = "mirror.png"
    pass

PhotoEditorApp().run()
