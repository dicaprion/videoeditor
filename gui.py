from tkinter import colorchooser, filedialog, messagebox
from tkinter import *

import editor


class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.center_window(575, 150)
        self.parent.title("VideoEditor")
        self.parent.iconbitmap("icon.ico")
        self.filename = ""
        self.filename1 = ""
        self.filename2 = ""
        self.toolbar()

    def center_window(self, width, height):
        self.w = width
        self.h = height
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - self.w) / 2
        y = (sh - self.h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))

    def toolbar(self):
        button_choose = Button(self.parent, text="Выбрать\nвидео", width=30, height=2, cursor="hand2",
                               command=lambda: self.video_chooser())
        button_choose.grid(row=0, column=0, columnspan=2, ipadx=5)
        button_play = Button(self.parent, text="Play", width=15, height=2, cursor="hand2",
                               command=lambda: self.video_play())
        button_play.grid(row=0, column=2, columnspan=1)
        button_save = Button(self.parent, text="Сохранить", width=30, height=2, cursor="hand2",
                               command=lambda: editor.save_video)
        button_save.grid(row=0, column=3, columnspan=2, ipadx=5)
        button_speed = Button(self.parent, text="Изменить\nскорость", width=15, height=2, cursor="hand2",
                              command=lambda: self.change_speed())
        button_speed.grid(row=1, column=0)
        button_cut = Button(self.parent, text="Обрезать\nфрагмент", width=15, height=2, cursor="hand2",
                            command=lambda: self.cut())
        button_cut.grid(row=1, column=1)
        button_join = Button(self.parent, text="Склеить", width=15, height=2, cursor="hand2",
                             command=lambda: self.join())
        button_join.grid(row=1, column=2)
        button_insert = Button(self.parent, text="Вставить\nкартинку", width=15, height=2, cursor="hand2",
                               command=lambda: self.insert())
        button_insert.grid(row=1, column=3)
        button_filter= Button(self.parent, text="Фильтр", width=15, height=2, cursor="hand2",
                               command=lambda: self.insert())
        button_filter.grid(row=1, column=4)

    def video_play(self):
        self.center_window(575, 300)
        if self.filename == "":
            self.filename = filedialog.askopenfilename(
                filetypes=(("Supported Video Files", "*.mp4"), ("All files", "*.*")))
        editor.play_video(self.filename)

    def video_chooser(self):
        self.filename = filedialog.askopenfilename(filetypes=(("Supported Video Files", "*.mp4"), ("All files", "*.*")))

    def change_speed(self):
        self.center_window(575, 170)
        label_speed = Label(self.parent, text="Введите во сколько раз\nускорить/замедлить видео:")
        label_speed.grid(row=4, column=0, columnspan=2)
        entry_speed = Entry(width=7)
        entry_speed.grid(row=4, column=1, columnspan=2)
        button_speed = Button(self.parent, text="OK", width=7, height=1, cursor="hand2",
                               command=lambda: editor.change_speed(self.filename,
                                                                   "video", float(entry_speed.get())))
        button_speed.grid(row=4, column=2, columnspan=1)

    def cut(self):
        self.center_window(575, 170)
        label_cut = Label(self.parent, text="Введите количество\nсекунд для обрезки видео:")
        label_cut.grid(row=3, column=0, columnspan=2)
        entry_cut = Entry(width=7)
        entry_cut.grid(row=3, column=1, columnspan=2)
        button_cut = Button(self.parent, text="OK", width=7, height=1, cursor="hand2",
                               command=lambda: editor.cut_video(self.filename,
                                                                "cutVideo", int(entry_cut.get())))
        button_cut.grid(row=3, column=2, columnspan=1)

    def join(self):
        self.center_window(575, 200)
        button_first = Button(self.parent, width=15, height=2, text="Выбрать видео",
                              command=lambda: self.ask_file_name())
        button_OK = Button(self.parent, width=15, height=2, text="OK",
                           command=lambda: self.get_joined())
        button_first.grid(row=5, column=1, columnspan=1)
        button_OK.grid(row=5, column=2, columnspan=1)

    def ask_file_name(self):
        self.filename1 = filedialog.askopenfilename(
            filetypes=(("Supported Video Files", "*.mp4"), ("All files", "*.*")))
        self.filename2 = filedialog.askopenfilename(
            filetypes=(("Supported Video Files", "*.mp4"), ("All files", "*.*")))

    def get_joined(self):
        editor.join([self.filename1, self.filename2])

    def insert(self):
        self.center_window(575, 300)


def main():
    root = Tk()
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
