#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, font, messagebox, simpledialog
from tkinter.colorchooser import askcolor
from tkinter.scrolledtext import ScrolledText
import datetime
import notepadcodes

notepad_name = "Notepad Doradas"


class NotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.counter_colour_text = 0
        self.counter_font_text = 0
        self.counter_font_box = -1
        self.counter_font = 0
        self.counter_word_warp = 0

        self.title(notepad_name)
        self.geometry("800x600")
        self.textfont = font.Font(family='Arial', size='12')

        self.create_widgets()
        self.create_menus()
        self.bind_hotkeys()

        self.font_chooser_visible = False
        self.create_font_chooser()

    def create_widgets(self):
        self.notepad = ScrolledText(self, exportselection=False, bg="#ffffff", font=self.textfont,
                                    foreground="#000000", insertbackground='black', undo=True, height=40, width=60)
        self.notepad.config(wrap=tk.WORD)
        self.notepad.grid(row=0, column=0, sticky='nswe', columnspan=3)

    def create_menus(self):
        menu_general = tk.Menu(self)
        self.config(menu=menu_general)

        menu_items = {
            'File': {
                'New': {'accelerator': 'Ctrl+N', 'command': self.cmd_new_file},
                'New Window': {'accelerator': 'Ctrl+Shift+N', 'command': cmd_new_window},
                'Open...': {'accelerator': 'Ctrl+O', 'command': self.cmd_open},
                'Save as...': {'accelerator': 'Ctrl+Shift+S', 'command': self.cmd_save_as},
                'Print': {'accelerator': 'Ctrl+P', 'command': self.cmd_print},
                'Exit': {'accelerator': 'Ctrl+W', 'command': self.cmd_exit}
            },
            'Edit': {
                'Redo': {'accelerator': 'Ctrl+Y', 'command': self.cmd_redo},
                'Undo': {'accelerator': 'Ctrl+Z', 'command': self.cmd_undo},
                'Clear': {'accelerator': 'Ctrl+Shift+C', 'command': self.cmd_clear},
                'Copy': {'accelerator': 'Ctrl+C', 'command': self.cmd_copy},
                'Cut': {'accelerator': 'Ctrl+X', 'command': self.cmd_cut},
                'Paste': {'accelerator': 'Ctrl+V', 'command': self.cmd_paste},
                'Select All': {'accelerator': 'Ctrl+A', 'command': self.cmd_select_all},
                'Sort Alphabetically by row': {'accelerator': 'Ctrl+B', 'command': self.cmd_sort_alphabetically_by_row},
                'Sort Alphabetically by Word': {'accelerator': 'Ctrl+S', 'command': self.cmd_sort_alphabetically_by_word},
                'Time/Date': {'accelerator': 'F5', 'command': self.cmd_time_date},
                'Find': {'accelerator': 'Ctrl+F', 'command': self.cmd_find}
            },
            'Format': {
                'Change Background Colour': {'accelerator': 'F2', 'command': self.cmd_change_colour_background},
                'Change Text Colour': {'accelerator': 'Ctrl+Q', 'command': self.cmd_change_colour_text},
                'Change Text Font': {'accelerator': 'Ctrl+E', 'command': self.toggle_font_chooser},
                'Word Wrap': {'accelerator': '', 'command': self.cmd_word_wrap},
                'Align Left': {'accelerator': 'Ctrl+L', 'command': lambda: self.cmd_text_alignment('left')},
                'Align Center': {'accelerator': 'Ctrl+R', 'command': lambda: self.cmd_text_alignment('center')},
                'Align Right': {'accelerator': 'Ctrl+T', 'command': lambda: self.cmd_text_alignment('right')}
            },
            'Help': {
                'Show Alt Codes': {'accelerator': 'F11', 'command': self.cmd_alt_codes},
                'About Notepad Doradas': {'accelerator': 'F12', 'command': self.cmd_about}
            }
        }

        for menu_name, menu_items in menu_items.items():
            menu = tk.Menu(menu_general, tearoff=False)
            menu_general.add_cascade(label=menu_name, menu=menu)
            for label, options in menu_items.items():
                menu.add_command(label=label, accelerator=options['accelerator'], command=options['command'])

    def bind_hotkeys(self):
        hotkeys = {
            '<F12>': self.cmd_about,
            '<F11>': self.cmd_alt_codes,
            '<F2>': self.cmd_change_colour_background,
            '<Control-q>': self.cmd_change_colour_text,
            '<Control-e>': self.toggle_font_chooser,
            '<Control-KeyRelease-C>': self.cmd_clear,
            '<Control-w>': self.cmd_exit,
            '<Control-n>': self.cmd_new_file,
            '<Control-KeyRelease-N>': cmd_new_window,
            '<Control-o>': self.cmd_open,
            '<Control-y>': self.cmd_redo,
            '<Control-KeyRelease-S>': self.cmd_save_as,
            '<Control-a>': self.cmd_select_all,
            '<Control-s>': self.cmd_sort_alphabetically_by_row,
            '<Control-b>': self.cmd_sort_alphabetically_by_word,
            '<F5>': self.cmd_time_date,
            '<Control-z>': self.cmd_undo,
            '<Control-p>': self.cmd_print,
            '<Control-f>': self.cmd_find,
            '<Control-l>': lambda event: self.cmd_text_alignment('left'),
            '<Control-r>': lambda event: self.cmd_text_alignment('center'),
            '<Control-t>': lambda event: self.cmd_text_alignment('right')
        }

        for hotkey, command in hotkeys.items():
            self.bind(hotkey, command)

    def create_font_chooser(self):
        self.font_label = tk.Label(self, text="Choose Font", font=("Arial", 14))
        self.font_label.grid(row=1, column=0, padx=1, sticky='nswe')

        self.font_listbox = tk.Listbox(self, exportselection=False, selectmode=tk.SINGLE, width=20)
        self.font_listbox.grid(row=2, column=0, padx=1)
        for f in font.families():
            self.font_listbox.insert('end', f)

        self.size_label = tk.Label(self, text="Size", font=("Arial", 14))
        self.size_label.grid(row=1, column=1, padx=1, sticky='nswe')

        self.font_size_listbox = tk.Listbox(self, exportselection=False, selectmode=tk.SINGLE, width=15)
        self.font_size_listbox.grid(row=2, padx=100, column=1)
        font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
        for size in font_sizes:
            self.font_size_listbox.insert('end', size)

        self.style_label = tk.Label(self, text="Style", font=("Arial", 14))
        self.style_label.grid(row=1, column=2, padx=1, sticky='nswe')

        self.font_style_listbox = tk.Listbox(self, exportselection=False, selectmode=tk.SINGLE, width=15)
        self.font_style_listbox.grid(row=2, column=2, padx=50)
        font_styles = ["Regular", "Bold", "Italic", "Bold/Italic", "Underline", "Strike"]
        for style in font_styles:
            self.font_style_listbox.insert('end', style)

        self.font_size_listbox.bind('<ButtonRelease-1>', self.cmd_font_size)
        self.font_style_listbox.bind('<ButtonRelease-1>', self.cmd_font_style)
        self.font_listbox.bind('<ButtonRelease-1>', self.cmd_font_chooser)
        self.hide_font_chooser()

    def toggle_font_chooser(self):
        self.font_chooser_visible = not self.font_chooser_visible
        if self.font_chooser_visible:
            self.show_font_chooser()
        else:
            self.hide_font_chooser()

    def show_font_chooser(self):
        self.font_label.grid()
        self.font_listbox.grid()
        self.size_label.grid()
        self.font_size_listbox.grid()
        self.style_label.grid()
        self.font_style_listbox.grid()

    def hide_font_chooser(self):
        self.font_label.grid_remove()
        self.font_listbox.grid_remove()
        self.size_label.grid_remove()
        self.font_size_listbox.grid_remove()
        self.style_label.grid_remove()
        self.font_style_listbox.grid_remove()

    def cmd_font_size(self, event):
        self.textfont.config(size=self.font_size_listbox.get(self.font_size_listbox.curselection()))
        self.toggle_font_chooser()

    def cmd_font_style(self, event):
        style = self.font_style_listbox.get(self.font_style_listbox.curselection())

        if style == "Bold":
            self.textfont.config(weight="bold")
        elif style == "Regular":
            self.textfont.config(weight="normal", slant="roman", underline=0, overstrike=0)
        elif style == "Bold/Italic":
            self.textfont.config(weight="bold", slant="italic")
        elif style == "Italic":
            self.textfont.config(slant="italic")
        elif style == "Underline":
            self.textfont.config(underline=1)
        elif style == "Strike":
            self.textfont.config(overstrike=1)

        self.toggle_font_chooser()

    def cmd_font_chooser(self, event):
        self.textfont.config(family=self.font_listbox.get(self.font_listbox.curselection()))
        self.toggle_font_chooser()

    def cmd_new_file(self):
        """Menu, Sub-Menu: File, Function: New File"""
        if len(self.notepad.get('1.0', tk.END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.cmd_save_as()
            else:
                self.notepad.delete(0.0, tk.END)
        self.title("Untitled File")

        def cmd_about(self):
        """Menu, Sub-Menu: Help, Function: About"""
        name = "Bekruiper"
        name = name.center(20)
        messagebox.showinfo(f"About {notepad_name}", f"Notepad by\n{name}")

    def cmd_alt_codes(self):
        """Menu, Sub-Menu: Help, Function: Show Alt-Codes"""
        if len(self.notepad.get('1.0', tk.END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "This action will clear the notepad \n Do you want to continue?"):
                self.notepad.delete(0.0, tk.END)
                self.notepad.insert(0.0, notepadcodes.alt_codes)
            else:
                pass
        else:
            self.notepad.insert(0.0, notepadcodes.alt_codes)

    def cmd_change_colour_background(self):
        """Menu, Sub-Menu: Format, Function: Change Background Colour """
        colours = askcolor(title="Choose Colour")
        self.notepad.configure(bg=colours[1])

    def cmd_change_colour_text(self):
        """Menu, Sub-Menu: Format, Function: Change Text Colour """
        color = askcolor(title="Choose Colour")
        if self.notepad.tag_ranges('sel'):
            self.notepad.tag_add(
                'textcolor_' + str(self.counter_colour_text), tk.SEL_FIRST, tk.SEL_LAST)
            self.notepad.tag_configure(
                'textcolor_' + str(self.counter_colour_text), foreground=color[1])
            self.counter_colour_text += 1
        else:
            self.notepad.config(foreground=color[1])

    def cmd_clear(self):
        """Menu, Sub-Menu: Edit, Function: Clear"""
        self.notepad.delete(0.0, tk.END)

    def cmd_copy(self):
        """Menu, Sub-Menu: Edit, Function: Copy"""
        self.notepad.event_generate("<<Copy>>")

    def cmd_cut(self):
        """Menu, Sub-Menu: Edit, Function: Cut"""
        self.notepad.event_generate("<<Cut>>")

    def cmd_exit(self):
        """Menu, Sub-Menu: File, Function: Exit"""
        if messagebox.askyesno(notepad_name, f"Are you sure you want to exit {notepad_name}?"):
            self.destroy()

    def cmd_redo(self):
        """Menu, Sub-Menu: Edit, Function: Redo"""
        self.notepad.event_generate("<<Redo>>")

    def cmd_select_all(self):
        """Menu, Sub-Menu: Edit, Function: Select All"""
        self.notepad.tag_add(tk.SEL, "1.0", tk.END)
        self.notepad.mark_set(tk.INSERT, "1.0")
        self.notepad.see(tk.INSERT)
        return 'break'

    def cmd_sort_alphabetically_by_row(self):
        text = list((self.notepad.get('1.0', tk.END)).splitlines())
        text.sort()
        self.notepad.delete(0.0, tk.END)
        for line in text:
            self.notepad.insert(tk.INSERT, f"{line}\n")
            self.notepad.pack(expand=1, fill=tk.BOTH)

    def cmd_sort_alphabetically_by_word(self):
        text = list((self.notepad.get('1.0', tk.END)).split())
        text.sort()
        self.notepad.delete(0.0, tk.END)
        for line in text:
            self.notepad.insert(tk.INSERT, f"{line}\n")
            self.notepad.pack(expand=1, fill=tk.BOTH)

    def cmd_time_date(self):
        """Menu, Sub-Menu: Edit, Function: Time/Date"""
        now = datetime.datetime.now()  # dd/mm/YY H:M:S AM/PM
        date_time_Str = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if len(self.notepad.get('1.0', tk.END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "This action will clear the notepad \n Do you want to continue?"):
                self.notepad.delete(0.0, tk.END)
                self.notepad.insert(tk.INSERT, date_time_Str)
                self.notepad.pack(expand=1, fill=tk.BOTH)
            else:
                pass
        else:
            self.notepad.insert(tk.INSERT, date_time_Str)
            self.notepad.pack(expand=1, fill=tk.BOTH)

    def cmd_undo(self):
        """Menu, Sub-Menu: Edit, Function: Undo"""
        self.notepad.event_generate("<<Undo>>")

    def cmd_save_as(self):
        """Menu, Sub-Menu: File, Function: Save As..."""
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.notepad.get('1.0', tk.END))

    def cmd_open(self):
        """Menu, Sub-Menu: File, Function: Open"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.notepad.delete('1.0', tk.END)
                self.notepad.insert(tk.INSERT, file.read())
                self.title(file_path)

        def cmd_new_file(self):
        """Menu, Sub-Menu: File, Function: New File"""
        if len(self.notepad.get('1.0', tk.END+'-1c')) > 0:
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.cmd_save_as()
            else:
                self.notepad.delete(0.0, tk.END)
        self.title("Untitled File")

    def cmd_open(self):
        """Menu, Sub-Menu: File, Function: Open"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.notepad.delete('1.0', tk.END)
                self.notepad.insert(tk.INSERT, file.read())
                self.title(file_path)

    def cmd_paste(self):
        """Menu, Sub-Menu: Edit, Function: Paste"""
        self.notepad.event_generate("<<Paste>>")

    def cmd_save_as(self):
        """Menu, Sub-Menu: File, Function: Save As..."""
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.notepad.get('1.0', tk.END))

    def cmd_find(self):
    """Menu, Sub-Menu: Edit, Function: Find"""
    self.find_window = tk.Toplevel(self)
    self.find_window.title("Find")
    self.find_window.transient(self)
    
    find_label = tk.Label(self.find_window, text="Find:")
    find_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    
    self.find_entry = tk.Entry(self.find_window, width=30)
    self.find_entry.grid(row=0, column=1, padx=5, pady=5)
    
    find_button = tk.Button(self.find_window, text="Find Next", command=self.find_next)
    find_button.grid(row=0, column=2, padx=5, pady=5)
    
    self.find_entry.focus_set()

    def find_next(self):
    """Find the next occurrence of the search text"""
    search_text = self.find_entry.get()
    if search_text:
        start_pos = self.notepad.search(search_text, tk.INSERT, stopindex=tk.END)
        if start_pos:
            end_pos = f"{start_pos}+{len(search_text)}c"
            self.notepad.tag_remove(tk.SEL, "1.0", tk.END)
            self.notepad.tag_add(tk.SEL, start_pos, end_pos)
            self.notepad.mark_set(tk.INSERT, end_pos)
            self.notepad.see(tk.INSERT)
            return 'break'
        return None

    def cmd_print(self):
    """Menu, Sub-Menu: File, Function: Print"""
    print_text = self.notepad.get("1.0", tk.END)
    
    # Perform printing operation here using the print_text
    
    # Dummy print statement for demonstration
    print("Printing the text:\n", print_text)

    def cmd_text_alignment(self, alignment):
    """Menu, Sub-Menu: Format, Function: Text Alignment"""
    if alignment == "left":
        self.notepad.tag_configure("align_left", justify=tk.LEFT)
        self.notepad.tag_remove("align_center", "1.0", tk.END)
        self.notepad.tag_remove("align_right", "1.0", tk.END)
        self.notepad.tag_add("align_left", "1.0", tk.END)
    elif alignment == "center":
        self.notepad.tag_configure("align_center", justify=tk.CENTER)
        self.notepad.tag_remove("align_left", "1.0", tk.END)
        self.notepad.tag_remove("align_right", "1.0", tk.END)
        self.notepad.tag_add("align_center", "1.0", tk.END)
    elif alignment == "right":
        self.notepad.tag_configure("align_right", justify=tk.RIGHT)
        self.notepad.tag_remove("align_left", "1.0", tk.END)
        self.notepad.tag_remove("align_center", "1.0", tk.END)
        self.notepad.tag_add("align_right", "1.0", tk.END)



def cmd_new_window(event=' '):
    """Menu, Sub-Menu: File, Function: New Window"""
    window_2 = NotepadApp()
    window_2.mainloop()


if __name__ == '__main__':
    window = NotepadApp()
    window.mainloop()
