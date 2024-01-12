import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ReqDb import ReqDb

class ReqGuiCtk(customtkinter.CTk):

    def __init__(self, dataBase=ReqDb()):
        super().__init__()
        self.db = dataBase

        self.title('School Requirements Manager')
        self.geometry('1500x800')
        self.config(bg='#1D3557')
        self.resizable(False, False)

        self.font1 = ('Arial', 20, 'bold')
        self.font2 = ('Times', 12)

        # Data Entry Form
        # 'ID' Label and Entry Widgets
        self.id_label = self.newCtkLabel('ID')
        self.id_label.place(x=420, y=60)
        self.id_entry = self.newCtkEntry()
        self.id_entry.place(x=580, y=60)

        # 'Name' Label and Entry Widgets
        self.description_label = self.newCtkLabel('Description')
        self.description_label.place(x=420, y=110)
        self.description_entry = self.newCtkEntry()
        self.description_entry.place(x=580, y=110)

        # 'Role' Label and Combo Box Widgets
        self.subject_label = self.newCtkLabel('Subject')
        self.subject_label.place(x=420, y=160)
        self.subject_cboxVar = StringVar()
        self.subject_cboxOptions = ['Math 21', 'Physics 71', 'EEE 111', 'EEE 113', 'EEE 118']
        self.subject_cbox = self.newCtkComboBox(options=self.subject_cboxOptions, 
                                    entryVariable=self.subject_cboxVar)
        self.subject_cbox.place(x=580, y=160)

        # 'Gender' Label and Combo Box Widgets
        self.priority_label = self.newCtkLabel('Priority')
        self.priority_label.place(x=420, y=210)
        self.priority_cboxVar = StringVar()
        self.priority_cboxOptions = ['High', 'Moderate', 'Low']
        self.priority_cbox = self.newCtkComboBox(options=self.priority_cboxOptions, 
                                    entryVariable=self.priority_cboxVar)
        self.priority_cbox.place(x=580, y=210)

        # 'Status' Label and Combo Box Widgets
        self.status_label = self.newCtkLabel('Status')
        self.status_label.place(x=420, y=260)
        self.status_cboxVar = StringVar()
        self.status_cboxOptions = ['Pending', 'Done']
        self.status_cbox = self.newCtkComboBox(options=self.status_cboxOptions, 
                                    entryVariable=self.status_cboxVar)
        self.status_cbox.place(x=580, y=260)


        self.clear_button = self.newCtkButton(text='Clear',
                                onClickHandler=lambda:self.clear_form(True))
        self.clear_button.place(x=520,y=310)

        self.add_button = self.newCtkButton(text='Add',
                                onClickHandler=self.add_entry,
                                fgColor='#05A312',
                                hoverColor='#00850B',
                                borderColor='#05A312')
        self.add_button.place(x=880,y=60)

        self.delete_button = self.newCtkButton(text='Delete',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#E40404',
                                    hoverColor='#AE0000',
                                    borderColor='#E40404')
        self.delete_button.place(x=880,y=110)

        self.update_button = self.newCtkButton(text='Update',
                                    onClickHandler=self.update_entry)
        self.update_button.place(x=880,y=160)

        self.export_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv)
        self.export_button.place(x=880,y=210)

        self.import_button = self.newCtkButton(text='Import from CSV',
                                    onClickHandler=self.import_from_csv)
        self.import_button.place(x=880,y=260)

        self.json_button = self.newCtkButton(text='Export to JSON',
                                    onClickHandler=self.export_to_json)
        self.json_button.place(x=880,y=310)

        # Tree View for Database Entries
        self.style = ttk.Style(self)
        self.style.theme_use('default')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#FAF3EE',
                        background='#457B9D',
                        fieldlbackground='#FAF3EE',
                        )

        self.style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('ID', 'Description', 'Subject', 'Priority', 'Status')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=10)
        self.tree.column('Description', anchor=tk.CENTER, width=150)
        self.tree.column('Subject', anchor=tk.CENTER, width=150)
        self.tree.column('Priority', anchor=tk.CENTER, width=10)
        self.tree.column('Status', anchor=tk.CENTER, width=150)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Subject', text='Subject')
        self.tree.heading('Priority', text='Priority')
        self.tree.heading('Status', text='Status')

        self.tree.place(x=250, y=400, width=1000, height=350)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()

    # new Label Widget
    def newCtkLabel(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#FAF3EE'
        widget_BgColor='#1D3557'

        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget

    # new Entry Widget
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#1D3557'
        widget_FgColor='#FAF3EE'
        widget_BgColor='#1D3557'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=250

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    bg_color=widget_BgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget

    # new Combo Box Widget
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#1D3557'
        widget_FgColor='#FAF3EE'
        widget_BgColor='#1D3557'
        widget_DropdownHoverColor='#0C9295'
        widget_ButtonColor='#0C9295'
        widget_ButtonHoverColor='#0C9295'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=250
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        bg_color=widget_BgColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        
        # set default value to 1st option
        widget.set(options[0])

        return widget

    # new Button Widget
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#457B9D', hoverColor='#023E8A', bgColor='#1D3557', borderColor='#457B9D'):
        widget_Font=self.font1
        widget_TextColor='#FAF3EE'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=3
        widget_Cursor='hand2'
        widget_CornerRadius=5
        widget_Width=200
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width)
       
        return widget

    # Handles
    def add_to_treeview(self):
        requirements = self.db.fetch_requirements()
        self.tree.delete(*self.tree.get_children())
        for requirement in requirements:
            print(requirement)
            self.tree.insert('', END, values=requirement)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.id_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.subject_cboxVar.set('Math 21')
        self.priority_cboxVar.set('High')
        self.status_cboxVar.set('Pending')

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.id_entry.insert(0, row[0])
            self.description_entry.insert(0, row[1])
            self.subject_cboxVar.set(row[2])
            self.priority_cboxVar.set(row[3])
            self.status_cboxVar.set(row[4])
        else:
            pass

    def add_entry(self):
        id=self.id_entry.get()
        description=self.description_entry.get()
        subject=self.subject_cboxVar.get()
        priority=self.priority_cboxVar.get()
        status=self.status_cboxVar.get()

        if not (id and description and subject and priority and status):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.id_exists(id):
            messagebox.showerror('Error', 'ID already exists')
        else:
            self.db.insert_requirement(id, description, subject, priority, status)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a requirement to delete')
        else:
            id = self.id_entry.get()
            self.db.delete_requirement(id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a requirement to update')
        else:
            id=self.id_entry.get()
            description=self.description_entry.get()
            subject=self.subject_cboxVar.get()
            priority=self.priority_cboxVar.get()
            status=self.status_cboxVar.get()
            self.db.update_requirement(description, subject, priority, status, id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been updated')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}')
    
    def import_from_csv(self):
        self.db.import_csv()
        self.add_to_treeview()
        messagebox.showinfo('Success', f'Data imported from {self.db.dbName}')
    
    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', f'Data exported to ReqDB.json')