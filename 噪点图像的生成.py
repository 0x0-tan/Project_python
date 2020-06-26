import random
import tkinter
from PIL import Image, ImageTk,ImageDraw,ImageFont
import time
class App(object):
    def __init__(self, size, root):
        self.root = root
        self.root.title("time error")
        self.img = Image.new("RGB", size)
        self.label = tkinter.Label(root)
        self.label.pack()
        self.time = 0.0
        self.frames = 0
        self.size = size
        self.loop()


    def loop(self):
        self.ta = time.time()
        # 13 FPS boost. half integer idea from C#.
        rnd = random.random
        draw = ImageDraw.Draw(self.img)
        font = ImageFont.truetype("HelveticaObl-Heavy.ttf",66)
        white = (255, 255, 255)
        black = (0, 0, 0)
        npixels = self.size[0] * self.size[1]
        data = [white if rnd() > 0.5 else black for i in range(npixels)]
        self.img.putdata(data)
        st = '123456789qwertyuiopasdfghjkzxcvbnm'
        rand_str = ''
        for x in range(0, 4):
            rand_str += str((random.randint(0, len(st))))
        # 设置字体颜色
        font_color = (random.randrange(100, 255), random.randrange(0, 100), random.randrange(0, 255))
        # 文字写入图片，参数，第一个是文字写入的位置(宽高），第二个参数字体样式，字体颜色
        draw.text((10, 80), rand_str[0], font=font, fill=font_color)
        draw.text((88, 80), rand_str[1], font=font, fill=font_color)
        draw.text((176, 80), rand_str[2], font=font, fill=font_color)
        draw.text((242, 80), rand_str[3], font=font, fill=font_color)


        self.pimg = ImageTk.PhotoImage(self.img)

        self.label["image"] = self.pimg
        self.tb = time.time()
        self.time += (self.tb - self.ta)
        self.frames += 1
        if self.frames == 30:
            try:
                self.fps = self.frames / self.time
            except:
                self.fps = "INSTANT"
            print ("%d frames in %3.2f seconds (%s FPS)" %(self.frames, self.time, self.fps))
            self.root.title("www.nowcoder.com (%3.2f FPS)" % (self.fps))
            self.time = 0
            self.frames = 0
            self.root.after(1, self.loop)


def main():
    root = tkinter.Tk()
    app = App((320, 240), root)
    root.mainloop()

main()


