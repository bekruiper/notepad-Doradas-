#!/usr/bin/env python3
from tkinter import *
from tkinter import filedialog, font, messagebox, simpledialog
from tkinter.colorchooser import *
from tkinter.scrolledtext import ScrolledText
import datetime
import notepadcodes

notepad_name = "Notepad Doradas"


class Window():
    def __init__(self):
        '''' ►►►GUI◄◄◄'''
        # Variables
        self.counter_colour_text = 0
        self.counter_font_text = 0
        self.counter_font_box = -1
        self.counter_font = 0
        self.counter_word_warp = 0

        # Root
        self.root = Tk()
        self.root.title(notepad_name)
        self.root.resizable(1, 1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Notepad
        self.textfont = font.Font(family='Arial', size='12')
        self.notepad = ScrolledText(self.root, exportselection=False, bg="#ffffff", font=self.textfont,
                                    foreground="#000000", insertbackground='black', undo=True, height=40, width=60,)
        self.notepad.config(wrap=WORD)

        # Menu: Gerneral
        menu_general = Menu(self.root)
        self.root.configure(menu=menu_general)

        # Menu: File
        menu_file = Menu(menu_general, tearoff=False)
        menu_general.add_cascade(label='File', menu=menu_file)
        menu_file.add_command(
            label='New', accelerator="Ctrl+N", command=self.cmd_new_file)
        menu_file.add_command(
            label='New Window', accelerator="Ctrl+Shift+N", command=cmd_new_window)
        menu_file.add_command(
            label='Open...', accelerator="Ctrl+O", command=self.cmd_open)
        menu_file.add_command(
            label='Save as...', accelerator="Ctrl+Shift+S", command=self.cmd_save_as)
        menu_file.add_separator()
        menu_file.add_command(
            label='Exit', accelerator="Ctrl+W", command=self.cmd_exit)

        # Menu: Edit
        menu_edit = Menu(menu_general, tearoff=False)
        menu_general.add_cascade(label='Edit', menu=menu_edit)
        menu_edit.add_command(
            label='Redo', accelerator="Ctrl+Y", command=self.cmd_redo)
        menu_edit.add_command(
            label='Undo', accelerator="Ctrl+Z", command=self.cmd_undo)
        menu_edit.add_separator()
        menu_edit.add_command(
            label='Clear', accelerator="Ctrl+Shift+C", command=self.cmd_clear)
        menu_edit.add_command(
            label='Copy', accelerator="Ctrl+C", command=self.cmd_copy)
        menu_edit.add_command(
            label='Cut', accelerator="Ctrl+X", command=self.cmd_cut)
        menu_edit.add_command(
            label='Paste', accelerator="Ctrl+V", command=self.cmd_paste)
        menu_edit.add_separator()
        menu_edit.add_command(label='Find...', accelerator="Ctrl+F", command=self.cmd_find)
        menu_edit.add_command(label='Select All',
                              accelerator="Ctrl+A", command=self.cmd_select_all)
        menu_edit.add_command(label='Sort Alphabetically',
                              accelerator="Alt+A", command=self.cmd_sort_alphabetically)
        menu_edit.add_command(
            label='Time/Date', accelerator="F5", command=self.cmd_time_date)

        #Menu: Format
        menu_format = Menu(menu_general, tearoff=False)
        menu_general.add_cascade(label='Format', menu=menu_format)
        menu_format.add_command(
            label='Change Background Colour', accelerator="F2", command=self.cmd_change_colour_background)
        menu_format.add_command(
            label='Change Text Colour', accelerator="Ctrl+Q", command=self.cmd_change_colour_text)
        menu_format.add_command(
            label='Change Text Font', accelerator="Ctrl+E", command=self.cmd_font_chooser)
        checkvar1 = IntVar(value=1)
        menu_format.add_separator()
        menu_format.add_checkbutton(
            label='Word Wrap', onvalue=1, offvalue=0, variable=checkvar1, command=self.cmd_word_wrap)

        # Menu: Help
        menu_help = Menu(menu_general, tearoff=False)
        menu_general.add_cascade(label='Help', menu=menu_help)
        menu_help.add_command(label='Show Alt Codes',
                              accelerator="F11", command=self.cmd_alt_codes)
        menu_help.add_separator()
        menu_help.add_command(label='About Notepad Doradas',
                              accelerator="F12", command=self.cmd_about)

        # Hotkeys .bind
        self.root.bind('<F12>', self.cmd_about)
        self.root.bind('<F11>', self.cmd_alt_codes)
        self.root.bind('<F2>', self.cmd_change_colour_background)
        self.root.bind('<Control-q>', self.cmd_change_colour_text)
        self.root.bind('<Control-e>', self.cmd_font_chooser)
        self.root.bind('<Control-KeyRelease-C>', self.cmd_clear)
        self.root.bind('<Control-w>', self.cmd_exit)
        self.root.bind('<Control-f>', self.cmd_find)
        self.root.bind('<Control-n>', self.cmd_new_file)
        self.root.bind("<Control-KeyRelease-N>", cmd_new_window)
        self.root.bind('<Control-o>', self.cmd_open)
        self.root.bind('<Control-y>', self.cmd_redo)
        self.root.bind('<Control-KeyRelease-S>', self.cmd_save_as)
        self.root.bind('<Control-a>', self.cmd_select_all)
        self.root.bind('<Alt-Key-A>', self.cmd_sort_alphabetically)
        self.root.bind('<F5>', self.cmd_time_date)
        self.root.bind('<Control-z>', self.cmd_undo)

        

        # Start GUI
        self.notepad.grid(row=0, column=0, sticky='nswe', columnspan=3)
        self.root.mainloop()

    def cmd_about(self, event=' '):
        """Menu, Sub-Menu: Help, Function: About"""
        name = "Bekruiper"
        name = name.center(20)
        messagebox.showinfo(f"About {notepad_name}", f"Notepad by\n{name}")

    def cmd_alt_codes(self, event=' '):
        """Menu, Sub-Menu: Help, Function: Show Alt-Codes"""
        if len(self.notepad.get('1.0', END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "This action will clear the notepad \n Do you want to continue?"):
                self.notepad.delete(0.0, END)
                self.notepad.insert(0.0, notepadcodes.alt_codes)
            else:
                pass
        else:
            self.notepad.insert(0.0, notepadcodes.alt_codes)

    def cmd_change_colour_background(self, event=' '):
        """Menu, Sub-Menu: Format, Function: Change Background Colour """
        colours = askcolor(title="Choose Colour")
        self.notepad.configure(bg=colours[1])

    def cmd_change_colour_text(self, event=' '):
        """Menu, Sub-Menu: Format, Function: Change Text Colour """
        color = askcolor(title="Choose Colour")
        if self.notepad.tag_ranges('sel'):
            self.notepad.tag_add(
                'textcolor_' + str(self.counter_colour_text), SEL_FIRST, SEL_LAST)
            self.notepad.tag_configure(
                'textcolor_' + str(self.counter_colour_text), foreground=color[1])
            self.counter_colour_text += 1
        else:
            self.notepad.config(foreground=color[1])


    def cmd_clear(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Clear"""
        self.notepad.delete(0.0, END)

    def click(self, event):
        self.notepad.tag_config(
            'Found', background='white', foreground='black')

    def cmd_copy(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Copy"""
        self.notepad.event_generate("<<Copy>>")

    def cmd_cut(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Cut"""
        self.notepad.event_generate("<<Cut>>")

    def cmd_exit(self, event=' '):
        """Menu, Sub-Menu: File, Function: Exit"""
        if messagebox.askyesno(notepad_name, f"Are you sure you want to exit {notepad_name}?"):
            self.root.destroy()

    def cmd_find(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Find..."""
        self.notepad.tag_remove("Found", '1.0', END)
        find = simpledialog.askstring("Find", "Find:")
        if find:
            id = '1.0'
        while 1:
            id = self.notepad.search(find, id, nocase=1, stopindex=END)
            if not id:
                messagebox.showinfo(title=None, message="Nothing found")
                break
            lastidx = '%s+%dc' % (id, len(find))
            self.notepad.tag_add('Found', id, lastidx)
            id = lastidx
        self.notepad.tag_config('Found', foreground='white', background='black')
        self.notepad.bind("<1>", self.click)

    def cmd_font_chooser(self, event=''):
        """Menu, Sub-Menu: Format, Function: Change Text Font """
        self.counter_font_box += 1
        if self.counter_font_box % 2 == 0:
            # Font Type Chooser
            self.font_label = Label(
                self.root, text="Choose Font", font=("Arial", 14))
            self.font_label.grid(row=1, column=0, padx=1, sticky='nswe')
            self.font_listbox = Listbox(
                self.root, exportselection=False, selectmode=SINGLE, width=20)
            self.font_listbox.grid(row=2, column=0, padx=1)
            for f in font.families():
                self.font_listbox.insert('end', f)

            # Font Size Chooser
            self.size_label = Label(self.root, text="Size", font=("Arial", 14))
            self.size_label.grid(row=1, column=1, padx=1, sticky='nswe')
            self.font_size_listbox = Listbox(
                self.root, exportselection=False, selectmode=SINGLE, width=15)
            self.font_size_listbox.grid(row=2, padx=100, column=1)
            font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
            for size in font_sizes:
                self.font_size_listbox.insert('end', size)

            # Font Style Chooser
            self.style_label = Label(
                self.root, text="Style", font=("Arial", 14))
            self.style_label.grid(row=1, column=2, padx=1, sticky='nswe')
            self.font_style_listbox = Listbox(
                self.root, exportselection=False, selectmode=SINGLE, width=15)
            self.font_style_listbox.grid(row=2, column=2, padx=50)
            font_styles = ["Regular", "Bold", "Italic",
                           "Bold/Italic", "Underline", "Strike"]
            for style in font_styles:
                self.font_style_listbox.insert('end', style)

            def cmd_font_size(event=''):
                self.cmd_word_wrap()
                self.textfont.config(size=self.font_size_listbox.get(
                    self.font_size_listbox.curselection()))
                self.cmd_word_wrap()

            def cmd_font_style(event=''):
                style = self.font_style_listbox.get(
                    self.font_style_listbox.curselection())

                if style == "Bold":
                    self.textfont.config(weight="bold")
                if style == "Regular":
                    self.textfont.config(
                        weight="normal", slant="roman", underline=0, overstrike=0)
                if style == "Bold/Italic":
                    self.textfont.config(
                        weight="bold", slant="italic")
                if style == "Italic":
                    self.textfont.config(slant="italic")
                if style == "Underline":
                    self.textfont.config(underline=1)
                if style == "Strike":
                    self.textfont.config(overstrike=1)

            def cmd_font_chooser(event=''):
                self.textfont.config(family=self.font_listbox.get(
                    self.font_listbox.curselection()))

            self.font_size_listbox.bind('<ButtonRelease-1>', cmd_font_size)
            self.font_style_listbox.bind('<ButtonRelease-1>', cmd_font_style)
            self.font_listbox.bind('<ButtonRelease-1>', cmd_font_chooser)
        else:
            self.font_label.destroy()
            self.size_label.destroy()
            self.style_label.destroy()
            self.font_size_listbox.destroy()
            self.font_listbox.destroy()
            self.font_style_listbox.destroy()

    def cmd_new_file(self, event=' '):
        """Menu, Sub-Menu: File, Function: New File"""
        if len(self.notepad.get('1.0', END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.cmd_save_as()
            else:
                self.notepad.delete(0.0, END)
            self.notepad.delete(0.0, END)
            self.root.title("Untitled File")

    def cmd_open(self, event=' '):
        """Menu, Sub-Menu: File, Function: Open"""
        try:
            self.file = filedialog.askopenfile(
                parent=self.root, filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")), mode='r', title="Please select files")
            self.text = self.file.read()
            self.notepad.delete(0.0, END)
            self.notepad.insert(0.0, self.text)
            self.filename = self.file.name
            self.root.title(self.filename)
        except:
            return None

    def cmd_paste(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Paste"""
        self.notepad.event_generate("<<Paste>>")

    def cmd_redo(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Redo"""
        self.notepad.event_generate("<<Redo>>")

    def cmd_save_as(self, event=' '):
        """Menu, Sub-Menu: File, Function: Save As..."""
        try:
            self.file = filedialog.asksaveasfile(
                mode='w', defaultextension='.txt')
            text = self.notepad.get('1.0', END)
            self.file.write(text)

        except:
            return None

    def cmd_select_all(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Clear"""
        self.notepad.tag_add(SEL, "1.0", END)
        self.notepad.mark_set(INSERT, "1.0")
        self.notepad.see(INSERT)
        return 'break'

    def cmd_sort_alphabetically(self):
        text = list((self.notepad.get('1.0', END)).split())
        text.sort()
        self.notepad.delete(0.0, END)
        for line in text:
            self.notepad.insert(INSERT, f"{line}\n")
            self.notepad.pack(expand=1, fill=BOTH)

    def cmd_time_date(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Time/Date"""
        now = datetime.now()  # dd/mm/YY H:M:S AM/PM
        date_time_Str = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if len(self.notepad.get('1.0', END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "This action will clear the notepad \n Do you want to continue?"):
                self.notepad.delete(0.0, END)
                self.notepad.insert(INSERT, date_time_Str)
                self.notepad.pack(expand=1, fill=BOTH)
            else:
                pass
        else:
            self.notepad.insert(INSERT, date_time_Str)
            self.notepad.pack(expand=1, fill=BOTH)

    def cmd_undo(self, event=' '):
        """Menu, Sub-Menu: Edit, Function: Undo"""
        self.notepad.event_generate("<<Undo>>")

    def cmd_word_wrap(self):
        """Menu, Sub-Menu: Format, Function: Word Warp"""
        self.counter_word_warp += 1
        if self.counter_word_warp % 2 == 0:
            self.notepad.config(wrap=WORD)
        else:
            self.notepad.config(wrap=NONE)


def cmd_new_window(event=' '):
    """Menu, Sub-Menu: File, Function: New Window"""
    window_2 = Window()
    window_2


if __name__ == '__main__':
    window = Window()
    window

# TODO: AddIcon
# TODO: Change font Listbox resizable
# TODO: Change alignment of text
# TODO: Fix Find
# TODO: Print