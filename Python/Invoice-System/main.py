# <editor-fold desc="Imports">
import os
import platform
import subprocess
from datetime import date, timedelta
from os import getcwd
from sqlite3 import *
from tkinter import *

from fpdf import FPDF

# <editor-fold desc="Model section">
# Program name
program_name = 'Invoice System'
credit_text = "developed by Kielland Consulting"

# informatonal strings (TODO: should be in .txt files and be read in from file)
about_message = '''
Created by Kaspar Kielland for Kielland Consulting
'''
instruction_message = ''' 
 Here comes some good instructions
 '''

# Full file path to data base file
db_file = getcwd() + '/invoice-system.db'

# List to hold language variables
language_eng = ['File', 'Open', 'Save', 'Save as PDF', 'Exit Application'
                                                       'Edit', 'Appearance', 'Light Theme', 'Dark Theme',
                'Customers', 'Products', 'Add...', 'Remove...', 'Edit...',
                'Clear all fields',
                'Help', 'About', 'Instructions',
                'Invoice', 'Invoice No.', 'Invoice date', 'Due date', 'Delivery date',
                'Default interests', 'Upon payment by the due date, interest will accrue after the law',
                'Product', 'Product Id', 'Product name', 'Unit price', 'Unit', '# of units']

ACCOUNT_NUMBER = '1234.00.98765'
OUR_REF = 'KK'


# </editor-fold>

# <editor-fold desc="Controller section">

def on_add_product_btn_clicked():
    for product_widget in product_widget_preferences:
        product_widget[1] = product_widget[1] + 1
    # widgets.append(make_label(product_widget_preferences, product_labels, product_frame))
    widgets.append(make_product_io_field(product_widget_preferences, product_io_fields, product_frame))
    if product_widget_preferences[0][1] >= 9:
        add_product_btn.configure(state=DISABLED)
    if product_widget_preferences[0][1] >= 2:
        remove_product_btn.configure(state=NORMAL)


def on_remove_product_btn_clicked():
    if product_widget_preferences[0][1] >= 2:
        for product_io_field in product_io_fields[-6:]:
            product_io_field.grid_remove()
        del product_io_fields[-6:]
        del widgets[-14:]
        del option_menu_val_var[-2:]
        for product_widget in product_widget_preferences:
            product_widget[1] = product_widget[1] - 1
    if product_widget_preferences[0][1] < 2:
        remove_product_btn.configure(state=DISABLED)
    if product_widget_preferences[0][1] < 9:
        add_product_btn.configure(state=NORMAL)
    update_total_fields()


def retrieve_from_database(file, table, column='*', as_list=False):
    connection = create_connection(file)
    if as_list:
        connection.row_factory = lambda cursor, row: row[0]
        cur = connection.cursor()
        query = 'SELECT {} FROM {}'.format(column, table)
        retrieved_from_database = cur.execute(query).fetchall()
    else:
        cur = connection.cursor()
        query = 'SELECT {} FROM {}'.format(column, table)
        retrieved_from_database = cur.execute(query).fetchall()
    if connection:
        connection.close()
    return retrieved_from_database


def display_message(title, message):
    win = Toplevel(app)
    win.wm_title(title)
    win_width = (win.winfo_screenwidth()) * (50 / 100)
    win_height = (win.winfo_screenheight()) * (50 / 100)
    win_pos_x = (win.winfo_screenwidth()) / 2 - win_width / 2
    win_pos_y = (win.winfo_screenwidth()) / 2 - win_height

    win.wm_geometry("%dx%d+%d+%d" % (win_width, win_height, win_pos_x, win_pos_y))

    l = Text(win, font=body, fg=text_color, bg=background, wrap=WORD)
    l.grid(row=0, column=0, sticky=W + E + N + S)
    l.delete(1.0, END)
    l.insert(1.0, message)
    l.configure(state=DISABLED)

    b = Button(win, text="Close", command=win.destroy)
    b.grid(row=1, column=0, sticky=N + S)
    # widgets[8][0].configure(text=title)
    # widgets[10][0].configure(state=NORMAL)
    # widgets[10][0].delete(1.0, END)
    # widgets[10][0].insert(END, message)
    # widgets[10][0].configure(state=DISABLED)
    # Shows the user that the above code has been executed


def make_label(widget_list, label_list, frame):
    for label in widget_list:
        label_text = label[0]
        color = text_color
        # Build label
        new_label = Label(frame,
                          text=label_text, font=body, fg=color, justify=RIGHT,
                          anchor=E, bg=background)
        # Make row and column inside LabelFrame resizable as well
        Grid.rowconfigure(frame, label[1], weight=1)
        Grid.columnconfigure(frame, label[2], weight=1)
        # Position label
        new_label.grid(row=label[1], column=label[2], columnspan=1, pady=0, sticky=E)
        if label[6][0]:
            new_label.grid(row=label[1], column=label[2], columnspan=1, rowspan=2, pady=0, sticky=E)
        # Add to list
        label_list.append(new_label)
    return label_list


def make_io_field(widget_list, io_field_list, frame):
    for io_field in widget_list:
        new_io_field = None
        color = text_color
        # Build io-field
        if io_field[3][0]:
            new_io_field = Entry(frame,
                                 font=body, fg=color, justify=LEFT, state=io_field[3][1],
                                 width=15)
            if io_field[3][2] is not None:
                set_entry_field_text(new_io_field, io_field[3][2])

        elif io_field[4][0]:
            new_io_field = Spinbox(frame,
                                   font=body,
                                   width=15, justify=LEFT,
                                   from_=0, to=1000, increment=0.5, readonlybackground=background,
                                   state=NORMAL, fg=text_color)
            new_io_field.configure(command=lambda obj=new_io_field: spn_box_clicked(obj))
            new_io_field.bind('<Return>', (lambda obj=new_io_field: spn_box_clicked(obj)))
        elif io_field[5][0]:
            # Create a Tkinter variable
            val_var = StringVar(app)
            # Dictionary with options
            choices = io_field[5][1]
            val_var.set(choices[0])
            option_menu_val_var.append(val_var)
            new_io_field = OptionMenu(frame,
                                      val_var, *choices,
                                      command=lambda e, i=option_menu_val_var[-1]: io_field_callback(e, i))
            new_io_field.config(width=15, font=body, fg=text_color)
        # elif io_field[6][0]:
        #     new_io_field = Checkbutton(frame,
        #                                font=body, text=io_field[6][1], justify=LEFT,
        #                                fg=text_color, selectcolor=background, state=NORMAL, variable=chk_var)
        elif io_field[7][0]:
            new_io_field = Text(frame, font=body, fg=text_color, state=NORMAL, width=10, height=2)

        if new_io_field is not None:
            # Make row and column inside LabelFrame resizable as well
            Grid.rowconfigure(frame, io_field[1], weight=1)
            Grid.columnconfigure(frame, io_field[2], weight=1)
            # Position label
            new_io_field.grid(row=io_field[1], column=io_field[2] + 1, columnspan=1, pady=0, sticky=W + E)

        if io_field[6][0]:
            new_io_field = Checkbutton(frame,
                                       font=body, text=io_field[6][1], justify=LEFT,
                                       fg=text_color, selectcolor=background, state=NORMAL, variable=chk_var)
            # Make row and column inside LabelFrame resizable as well
            Grid.rowconfigure(frame, io_field[1], weight=1)
            Grid.columnconfigure(frame, io_field[2], weight=1)
            # Position label
            new_io_field.grid(row=io_field[1], column=io_field[2] + 1, columnspan=1, rowspan=2, pady=0, sticky=W + E)

        # Add to list
        io_field_list.append(new_io_field)
    return io_field_list


def make_product_label(widget_list, label_list, frame):
    for label in widget_list:
        label_text = label[0]
        color = text_color
        # Build label
        new_label = Label(frame,
                          text=label_text, font=body, fg=color, justify=RIGHT,
                          anchor='sw', bg=background)
        # Make row and column inside LabelFrame resizable as well
        Grid.rowconfigure(frame, label[1], weight=1)
        Grid.columnconfigure(frame, label[2], weight=1)
        # Position label
        new_label.grid(row=label[1], column=label[2], columnspan=1, pady=0, sticky=E + W + S)
        if label[6][0]:
            new_label.grid(row=label[1], column=label[2], columnspan=1, rowspan=1, pady=0, sticky=E + W + S)
        # Add to list
        label_list.append(new_label)
    return label_list


def make_product_io_field(widget_list, io_field_list, frame):
    for io_field in widget_list:
        new_io_field = None
        color = text_color
        # Build io-field
        if io_field[3][0]:
            new_io_field = Entry(frame,
                                 font=body, fg=color, justify=LEFT, state=io_field[3][1],
                                 width=15)
            if io_field[3][2] is not None:
                set_entry_field_text(new_io_field, io_field[3][2])

        elif io_field[4][0]:
            new_io_field = Spinbox(frame,
                                   font=body,
                                   width=15, justify=LEFT,
                                   from_=0, to=1000, increment=0.5, readonlybackground=background,
                                   state=NORMAL, fg=text_color)
            new_io_field.configure(command=lambda obj=new_io_field: spn_box_clicked(obj))
            new_io_field.bind('<Return>', (lambda obj=new_io_field: spn_box_clicked(obj)))
        elif io_field[5][0]:
            # Create a Tkinter variable
            val_var = StringVar(app)
            # Dictionary with options
            choices = io_field[5][1]
            val_var.set(choices[0])
            option_menu_val_var.append(val_var)
            new_io_field = OptionMenu(frame,
                                      val_var, *choices,
                                      command=lambda e, i=option_menu_val_var[-1]: io_field_callback(e, i))
            new_io_field.config(width=15, font=body, fg=text_color)
        # elif io_field[6][0]:
        #     new_io_field = Checkbutton(frame,
        #                                font=body, text=io_field[6][1], justify=LEFT,
        #                                fg=text_color, selectcolor=background, state=NORMAL, variable=chk_var)
        elif io_field[7][0]:
            new_io_field = Text(frame, font=body, fg=text_color, state=NORMAL, width=20, height=2, highlightbackground='black', highlightthickness=0.5)

        if new_io_field is not None:
            # Make row and column inside LabelFrame resizable as well
            Grid.rowconfigure(frame, io_field[1], weight=0)
            Grid.columnconfigure(frame, io_field[2], weight=1)
            # Position label
            new_io_field.grid(row=io_field[1] + 1, column=io_field[2], columnspan=1, pady=0, sticky=W + E)

        if io_field[6][0]:
            new_io_field = Checkbutton(frame,
                                       font=body, text=io_field[6][1], justify=LEFT,
                                       fg=text_color, selectcolor=background, state=NORMAL, variable=chk_var)
            # Make row and column inside LabelFrame resizable as well
            Grid.rowconfigure(frame, io_field[1], weight=1)
            Grid.columnconfigure(frame, io_field[2], weight=1)
            # Position label
            new_io_field.grid(row=io_field[1] + 1, column=io_field[2], columnspan=1, rowspan=2, pady=0, sticky=W + E)

        # Add to list
        io_field_list.append(new_io_field)
    return io_field_list


# function to establish a database connection to an SQLite database specified by the database file.
def create_connection(file):
    """
    create a database connection to the SQLite database specified by file
    :param  file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = connect(file)
    except Error as e:
        print("Connection error: %s" % e)
    except Exception as e:
        print("Could not establish connection to file '%s''\nError message: %s" % file % e)
    finally:
        return connection


def retrieve_from_list(table_list, index):
    temp = []
    for item in table_list:
        temp.append(item[index])
    return temp


def set_entry_field_text(field, text):
    if text is None:
        text = ''
    state = str(field['state'])
    if state == 'readonly':
        field.configure(state=NORMAL)
        field.delete(0, END)
        field.insert(0, text)
        field.configure(state='readonly')
    else:
        field.delete(0, END)
        field.insert(0, text)


def io_field_callback(choice, val_var_object):
    if val_var_object == option_menu_val_var[0]:
        for customer in all_customers_info:
            if customer[0] == choice:
                option_menu_val_var[1].set(customer_full_name[choice - 1])
                set_entry_field_text(customer_io_fields[2], customer[3])
                set_entry_field_text(customer_io_fields[4], customer[4])
                set_entry_field_text(customer_io_fields[5], customer[5] + ' ' + customer[6])
                set_entry_field_text(customer_io_fields[3], customer[1][0] + customer[2])
                set_entry_field_text(customer_io_fields[6], customer[7])
                set_entry_field_text(customer_io_fields[7], customer[8])
                set_entry_field_text(customer_io_fields[8], customer[9])
                return
    elif val_var_object == option_menu_val_var[1]:
        for customer in all_customers_info:
            if (customer[1] + ' ' + customer[2]) == choice:
                option_menu_val_var[0].set(customer[0])
                set_entry_field_text(customer_io_fields[2], customer[3])
                set_entry_field_text(customer_io_fields[4], customer[4])
                set_entry_field_text(customer_io_fields[5], customer[5] + ' ' + customer[6])
                set_entry_field_text(customer_io_fields[3], customer[1][0] + customer[2])
                set_entry_field_text(customer_io_fields[6], customer[7])
                set_entry_field_text(customer_io_fields[7], customer[8])
                set_entry_field_text(customer_io_fields[8], customer[9])
                return
    else:
        val_var_choice_index = option_menu_val_var.index(val_var_object)
        for product in all_products_info:
            if product[0] == choice:
                entry_field_index = ((val_var_choice_index - 2) * 3) + 3
                option_menu_val_var[val_var_choice_index + 1].set(product[1])
                set_entry_field_text(product_io_fields[entry_field_index], product[3])
                calculate_totals(entry_field_index)
            elif product[1] == choice:
                entry_field_index = ((val_var_choice_index - 2) * 3)
                option_menu_val_var[val_var_choice_index - 1].set(product[0])
                set_entry_field_text(product_io_fields[entry_field_index], product[3])
                calculate_totals(entry_field_index)


def calculate_totals(start_index):
    unit_price_field_index = start_index
    unit_price_value = product_io_fields[unit_price_field_index].get()
    num_of_units_field_index = start_index + 1
    num_of_units_value = product_io_fields[num_of_units_field_index].get()
    total = float(unit_price_value) * float(num_of_units_value)
    # total = round(total)
    total_field_index = start_index + 2
    set_entry_field_text(product_io_fields[total_field_index], f"{total:_.2f}".replace("_", "\'"))
    update_total_fields()
    # mva_field_index = start_index + 3
    # mva = product_io_fields[mva_field_index].get()
    # total_mva = int(total) * (float(mva) / 100) + int(total)
    # total_mva = round(total_mva)
    # total_mva_field_index = start_index + 4
    # set_entry_field_text(product_io_fields[total_mva_field_index], total_mva)


def spn_box_clicked(spn_box_object):
    number_of_products = len(product_io_fields) // 6
    for product_no in range(number_of_products):
        calculate_totals(3 + (6 * product_no))


def update_total_fields():
    total_sum = 0
    total_incl_mva = 0
    number_of_products = len(product_io_fields) // 6
    for product_no in range(number_of_products):
        total_sum = total_sum + float(product_io_fields[(5 + (6 * product_no))].get().replace("\'", ""))
    set_entry_field_text(total_entry, f"{total_sum:_.2f}".replace("_", "\'"))
    total_incl_mva = total_sum + (float(mva_sb.get()) / 100) * total_sum
    set_entry_field_text(total_incl_mva_entry, f"{total_incl_mva:_.2f}".replace("_", "\'"))


def make_invoice_pdf():
    invoice_number = invoice_io_fields[0].get()
    invoice_date = invoice_io_fields[1].get()
    invoice_due_date = invoice_io_fields[2].get()
    invoice_delivery_date = invoice_io_fields[3].get()
    invoice_ref = invoice_io_fields[4].get()
    if chk_var.get():
        invoice_interest_msg = 'Ved betaling etter forfall beregnes rente etter forsinkelsesrenteloven.'
        invoice_interest_description = 'Forsinkelsesrente'
    else:
        invoice_interest_msg = ''
        invoice_interest_description = ''
    customer_id = int(option_menu_val_var[0].get())
    customer_name = option_menu_val_var[1].get()
    customer_organization = customer_io_fields[2].get()
    customer_ref = customer_io_fields[3].get()
    customer_street_address = customer_io_fields[4].get()
    customer_postal_code = customer_io_fields[5].get()
    customer_mail = customer_io_fields[7].get()
    customer_KID = customer_io_fields[8].get()
    if customer_KID == "":
        customer_KID = "-"
        payment_msg = 'Vennligst angi fakturanummer ved betaling'
    else:
        payment_msg = 'Vennligst angi KID ved betaling'

    # A4 dimensions: h=297mm w=210mm
    invoice_pdf = FPDF()
    invoice_pdf.add_page()
    invoice_pdf.set_xy(0, 0)
    invoice_pdf.set_font('Arial', 'B', 16)
    invoice_pdf.set_auto_page_break(True, margin=10)
    invoice_pdf.set_margins(1, 1, 1)

    invoice_pdf.set_xy(10, 10)
    invoice_pdf.set_font('Arial', 'B', 16)
    invoice_pdf.cell(60, 10, 'Faktura', align='L', ln=2)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(40, 5, 'Fakturanummer', align='L')
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(20, 5, invoice_number, align='L')

    invoice_pdf.image('KiellandConsulting-Logo.png', x=150, y=10, w=50)

    if customer_organization != "":
        customer_label = customer_organization + '\n'
    else:
        customer_label = customer_name + '\n'
    customer_label = customer_label + customer_street_address + '\n'
    customer_label = customer_label + customer_postal_code

    invoice_pdf.set_xy(10, 30)
    invoice_pdf.multi_cell(w=70, h=5, txt=customer_label, border=1, align='L')

    invoice_pdf.set_xy(120, 50)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.multi_cell(w=35, h=5, txt='Kundenr.\n'
                                          'Fakturadato\n'
                                          'Leveringsdato\n'
                                          'Deres referanse\n'
                                          'Vår referanse\n' +
                                          invoice_interest_description, border=0, align='L')
    invoice_pdf.set_xy(155, 50)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_label = str(f"{customer_id:02n}") + '\n'
    invoice_label = invoice_label + invoice_date + '\n'
    invoice_label = invoice_label + invoice_delivery_date + '\n'
    invoice_label = invoice_label + customer_ref + '\n'
    invoice_label = invoice_label + invoice_ref + '\n'
    invoice_label = invoice_label + invoice_interest_msg
    invoice_pdf.multi_cell(w=45, h=5, txt=invoice_label, border=0, align='L')

    invoice_pdf.set_xy(10, 100)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(w=20, h=7, txt='Produktnr.', align='L', border='LTB', ln=0)
    invoice_pdf.cell(w=90, h=7, txt='Beskrivelse', align='L', border='TB', ln=0)
    invoice_pdf.cell(w=15, h=7, txt='Antall', align='L', border='TB', ln=0)
    invoice_pdf.cell(w=15, h=7, txt='Enhet', align='L', border='TB', ln=0)
    invoice_pdf.cell(w=25, h=7, txt='Enhetspris', align='R', border='TB', ln=0)
    invoice_pdf.cell(w=25, h=7, txt='Sum', align='R', border='TRB', ln=1)
    invoice_pdf.set_xy(10, invoice_pdf.get_y())
    invoice_pdf.cell(w=190, h=2, txt='', align='L', border='LR', ln=1)
    invoice_pdf.set_xy(10, invoice_pdf.get_y())
    invoice_pdf.set_font('Arial', '', 10)
    number_of_products = len(product_io_fields) // 6
    for product_no in range(number_of_products):
        product_id = int(option_menu_val_var[2 + (2 * product_no)].get())
        product_name = option_menu_val_var[3 + (2 * product_no)].get()
        product_unit_no = product_io_fields[(4 + (6 * product_no))].get()
        product_unit = 'NA'
        product_unit_price = float(product_io_fields[(3 + (6 * product_no))].get().replace("\'", ""))
        product_sum = float(product_io_fields[(5 + (6 * product_no))].get().replace("\'", ""))
        product_description = product_io_fields[(2 + (6 * product_no))].get("1.0", 'end-1c')

        invoice_pdf.cell(w=20, h=5, txt=f"{product_id:02n}", align='C', border='L',
                         ln=0)
        invoice_pdf.cell(w=90, h=5, txt=product_name, align='L', border='', ln=0)
        invoice_pdf.cell(w=15, h=5, txt=product_unit_no, align='C', border='', ln=0)

        for product in all_products_info:
            if product[0] == product_id:
                product_unit = product[2]

        invoice_pdf.cell(w=15, h=5, txt=product_unit, align='L', border='', ln=0)
        invoice_pdf.cell(w=25, h=5, txt=f"{product_unit_price:_.2f}".replace("_", "\'"),
                         align='R', border='', ln=0)
        invoice_pdf.cell(w=25, h=5, txt=f"{product_sum:_.2f}".replace("_", "\'"),
                         align='R', border='R', ln=1)

        if len(product_description) != 0:
            y_position = invoice_pdf.get_y()
            invoice_pdf.set_font('Arial', 'I', 9)
            invoice_pdf.set_xy(30, y_position)
            invoice_pdf.multi_cell(w=90, h=3, txt=product_description, align='L',
                                   border='')

            height_to_fill = invoice_pdf.get_y() - y_position
            invoice_pdf.set_xy(10, y_position)
            invoice_pdf.cell(w=20, h=height_to_fill, txt='', align='L', border='L', ln=0)
            invoice_pdf.set_xy(120, y_position)
            invoice_pdf.cell(w=80, h=height_to_fill, txt='', align='L', border='R', ln=1)

        invoice_pdf.set_xy(10, invoice_pdf.get_y())
        invoice_pdf.cell(w=190, h=1, txt='', align='L', border='LR', ln=1)
        invoice_pdf.set_xy(10, invoice_pdf.get_y())
        invoice_pdf.set_font('Arial', '', 10)

    height_to_fill = 297 - invoice_pdf.get_y() - (297 - 260) - 10
    invoice_pdf.set_xy(10, invoice_pdf.get_y())
    invoice_pdf.cell(w=190, h=height_to_fill, txt='', align='L', border='LR', ln=2)
    invoice_pdf.cell(w=190, h=1, txt='', align='L', border='LBR', ln=0)

    total_excl_mva = float(total_entry.get().replace("\'", ""))
    mva = float(mva_sb.get())
    total_incl_mva = float(total_incl_mva_entry.get().replace("\'", ""))

    invoice_pdf.set_xy(10, invoice_pdf.get_y() - 15)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(w=35, h=5, txt='Ekskl. MVA', align='L', border='T', ln=0)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(w=35, h=5, txt=f"{total_excl_mva:_.2f}".replace("_", "\'"), align='R', border='TR', ln=1)
    invoice_pdf.set_x(10)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(w=35, h=5, txt=f"MVA utgjør ({mva:.2f}%)", align='L', border='', ln=0)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(w=35, h=5, txt=f"{(total_incl_mva - total_excl_mva):_.2f}".replace("_", "\'"), align='R',
                     border='R', ln=1)
    invoice_pdf.set_x(10)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(w=35, h=5, txt='Inkl. MVA', align='L', border='', ln=0)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(w=35, h=5, txt=f"{total_incl_mva:_.2f}".replace("_", "\'"), align='R', border='R', ln=2)
    invoice_pdf.cell(w=35, h=1, txt='', align='R', border='R', ln=1)

    invoice_pdf.set_xy(80, 205)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(w=60, h=7, txt='Forfallsdato', align='L', border='LT', ln=2)
    invoice_pdf.cell(w=60, h=7, txt='KID', align='L', border='L', ln=2)
    invoice_pdf.cell(w=60, h=7, txt='Fakturanummer', align='L', border='L', ln=2)
    invoice_pdf.set_font('Arial', 'I', 9)
    invoice_pdf.cell(w=120, h=7, txt=payment_msg, align='L', border='L', ln=2)
    invoice_pdf.set_font('Arial', 'B', 10)
    # invoice_pdf.cell(w=60, h=7, txt='', align='L', border='L', ln=2)
    invoice_pdf.cell(w=60, h=7, txt='Bankkonto', align='L', border='L', ln=2)
    invoice_pdf.set_font('Arial', 'B', 14)
    invoice_pdf.cell(w=60, h=10, txt='Å betale', align='L', border='L', ln=2)

    invoice_pdf.set_xy(140, 205)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(w=60, h=7, txt=invoice_due_date, align='R', border='TR', ln=2)
    invoice_pdf.cell(w=60, h=7, txt=customer_KID, align='R', border='R', ln=2)
    invoice_pdf.cell(w=60, h=7, txt=invoice_number, align='R', border='R', ln=2)
    invoice_pdf.cell(w=60, h=7, txt='', align='R', border='R', ln=2)
    # invoice_pdf.cell(w=60, h=7, txt='', align='R', border='R', ln=2)
    invoice_pdf.cell(w=60, h=7, txt=ACCOUNT_NUMBER, align='R', border='R', ln=2)
    invoice_pdf.set_font('Arial', 'B', 14)
    invoice_pdf.cell(w=60, h=10, txt=f"{total_incl_mva:_.2f}".replace("_", "\'"), align='R', border='R', ln=2)

    # Footer
    invoice_pdf.set_xy(10, 260)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(63, 7, 'Adresse', align='L', ln=2)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.multi_cell(63, 5, 'Kielland Consulting\n'
                                  'c/o Kaspar Kielland\n'
                                  'Vardegaten 10\n'
                                  '4876 Grimstad', align='L')

    invoice_pdf.set_xy(73, 260)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(63, 7, 'Telefon', align='C', ln=2)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(63, 5, '00 99 00 99', align='C')

    invoice_pdf.set_xy(73, 275)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(63, 7, 'Mail', align='C', ln=2)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(63, 5, 'mail@address.com', align='C')

    invoice_pdf.set_xy(136, 260)
    invoice_pdf.set_font('Arial', 'B', 10)
    invoice_pdf.cell(63, 7, 'Organisasjonsnr.', align='R', ln=2)
    invoice_pdf.set_font('Arial', '', 10)
    invoice_pdf.cell(63, 5, '123 456 789', align='R')

    # Set path-/filename
    invoice_pdf_file_name = invoice_number
    if customer_io_fields[2].get() != "":
        invoice_pdf_file_name = invoice_pdf_file_name + '-' + customer_io_fields[2].get().replace('/', '_')
    else:
        invoice_pdf_file_name = invoice_pdf_file_name + '-' + option_menu_val_var[1].get().replace('/', '_')
    invoice_pdf_file_name = invoice_pdf_file_name.replace(" ", "_")
    invoice_pdf_filepath = getcwd() + '/' + 'Generated invoices/' + invoice_pdf_file_name + '.pdf'
    invoice_pdf.output(name=invoice_pdf_filepath, dest='F')

    # Open pdf depending on system
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', invoice_pdf_filepath))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(invoice_pdf_filepath)
    else:  # linux variants
        subprocess.call(('xdg-open', invoice_pdf_filepath))

    columns = "InvoiceNumber,CustomerID,Amount,AmountInclMVA,InvoiceDate,DueDate,FilePath"
    to_commit = int(invoice_number[3:]), customer_id, f"{total_excl_mva:.2f}", f"{total_incl_mva:.2f}", invoice_date, \
                invoice_due_date, invoice_pdf_filepath
    to_commit_var_string = "?," * len(to_commit)
    to_commit_var_string = to_commit_var_string[:-1:]

    save_to_db(db_file, 'invoiceLog', columns, to_commit, to_commit_var_string)


def save_to_db(file, table, columns, to_commit, to_commit_var_string):
    """
    Calls data base related functions to commit
    """
    connection = create_connection(file)
    sql = f''' INSERT INTO {table}({columns})
              VALUES({to_commit_var_string}) '''
    try:
        cur = connection.cursor()
        # for story in stories:
        #     for requested_stories in range(story[0]):
        #         story_information = story[3][requested_stories], story[1], story[7][
        #             requested_stories]
        #         cur.execute(sql, story_information)
        cur.execute(sql, to_commit)
        connection.commit()
    except Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in commit: %s" % e)
    if connection:
        connection.close()


# </editor-fold

# <editor-fold desc="View section">
# Define color and text constants
background = 'WHITE'
widget_background = 'GHOSTWHITE'
text_color = 'DARKSLATEGRAY'
contrast_color = 'TOMATO'
header_1 = 'Helvetica, 28'
header_2 = 'Helvetica, 22'
header_3 = 'Helvetica, 18'
body = 'Helvetica, 14'
footer = 'Helvetica, 12'

# List to hold all widgets
widgets = []

# Creating window
app = Tk()
# Sets window background color
app['bg'] = background

# Define window size and position
width = (app.winfo_screenwidth()) * (80 / 100)
height = (app.winfo_screenheight()) * (95 / 100)
pos_x = (app.winfo_screenwidth()) / 2 - width / 2
pos_y = 0

# Sets window size and position
app.wm_geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))

# Set grid weight to app for column and row so window will resize more nicely
for row_no in range(6):
    Grid.rowconfigure(app, row_no, weight=1)
for col_no in range(4):
    Grid.columnconfigure(app, col_no, weight=1)

# Window title
app.title(program_name)
# Widgets will get focus whenever mouse pointer moves over it
app.tk_focusFollowsMouse()

# Add to widget list [0]
widgets.append([app])

# Create the title label
title_label = Label(app,
                    text=program_name, font=header_1,
                    fg=text_color, bg=background)
# Positions the label at top-center
title_label.grid(row=0, column=0, columnspan=4, sticky=W + E + N + S)
# Add to widget list [1]
widgets.append([title_label])
# # Create the credit label
# credits_label = Label(app,
#                     text=credits, font=body + ' italic',
#                     fg=text_color, bg=background)
# # Positions the label at top-center
# credits_label.grid(row=0, column=0, columnspan=4, sticky=W + E)
# # Add to widget list [1]
# widgets.append([credits_label])
# Create the program icon and display it through a label
feed_image = PhotoImage(file='KiellandConsulting-Logo.png')
feed_logo = Label(app, image=feed_image, bg=background)
# Positions the program icon at right upper corner
feed_logo.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=E + N, padx=5, pady=5)
# Add to widget list [2]
widgets.append([feed_logo])

# Create frame to hold invoice labels and input-fields
invoice_frame = LabelFrame(app,
                           text='Invoice information', font=header_3,
                           bg=background, bd=5, fg=text_color,
                           padx=5, pady=2, labelanchor=N + W,
                           relief=SOLID)
# Positions the frame at left upper corner
invoice_frame.grid(row=1, column=0, columnspan=2, rowspan=2, padx=10, pady=10, sticky=W + E + N + S)
# Add to widget list [3]
widgets.append([invoice_frame])

# Create frame to hold customer labels and input-fields
customer_frame = LabelFrame(app,
                            text='Customer information', font=header_3,
                            bg=background, bd=5, fg=text_color,
                            padx=5, pady=2, labelanchor=N + W,
                            relief=SOLID)
# Positions the frame at right upper corner
customer_frame.grid(row=1, column=2, columnspan=2, rowspan=2, padx=10, pady=10, sticky=W + E + N + S)
# Add to widget list [4]
widgets.append([customer_frame])

# # Create frame to hold personal information labels and input-fields
# personalInfo_frame = LabelFrame(app,
#                                 text='Our information', font=header_3,
#                                 bg=background, bd=5, fg=text_color,
#                                 padx=5, pady=2, labelanchor=N + W,
#                                 relief=SOLID)
# # Positions the frame at right upper corner
# personalInfo_frame.grid(row=2, column=2, padx=20, pady=10, sticky=W + E + N + S)
# # Add to widget list [5]
# widgets.append([personalInfo_frame])

# Create frame to hold product labels and input-fields
product_frame = LabelFrame(app,
                           text='Product information', font=header_3,
                           bg=background, bd=5, fg=text_color,
                           padx=5, pady=2, labelanchor=N + W,
                           relief=SOLID)
# Positions the frame at right upper corner
product_frame.grid(row=3, column=0, rowspan=2, columnspan=4, padx=10, pady=10, sticky=W + E + N + S)

# Add to widget list [6]
widgets.append([product_frame])
for row_no in range(9):
    Grid.rowconfigure(product_frame, row_no, weight=2)
Grid.columnconfigure(product_frame, 0, weight=0)
for col_no in range(1, 6):
    Grid.columnconfigure(product_frame, col_no, weight=2)
# Create frame to hold buttons on bottom
buttons_frame = Frame(app, bg=background)
# Positions the frame at right upper corner
buttons_frame.grid(row=5, column=0, rowspan=1, columnspan=4, padx=10, pady=10, sticky=W + E + N + S)
# Add to widget list [6]
widgets.append([buttons_frame])
# for row_no in range(2):
#     Grid.rowconfigure(buttons_frame, row_no, weight=1)
# for col_no in range(4):
#     Grid.columnconfigure(buttons_frame, col_no, weight=1)


# list to hold all labels
labels = []

# list to hold all invoice labels
invoice_labels = []
# list to hold all customer labels
customer_labels = []
# list to hold all personal labels
# personalInfo_labels = []
# list to hold all product labels
product_labels = []

# list to hold all invoice io-fields
invoice_io_fields = []
# list to hold all customer io-fields
customer_io_fields = []
# list to hold all personal io-fields
# personalInfo_io_fields = []
# list to hold all product io-fields
product_io_fields = []

# list to hold all database entries for customer
all_customers_info = retrieve_from_database(db_file, 'customers')
customer_full_name = []
for customer in all_customers_info:
    full_name = customer[1] + ' ' + customer[2]
    customer_full_name.append(full_name)
# list to hold all database entries for customer
all_products_info = retrieve_from_database(db_file, 'products')
# list to hold all database entries for customer
all_invoiceLog_info = retrieve_from_database(db_file, 'invoiceLog')
if len(all_invoiceLog_info) > 0:
    invoice_number = f"INV{(all_invoiceLog_info[-1][1] + 1):04n}"
else:
    invoice_number = f"INV{1:04n}"

option_menu_val_var = []
chk_var = IntVar()

date_today = date.today()

# [label text, row (for label/spinbox), column (for label/spinbox), isTextbox, isSpinner, isDropdown]
invoice_widget_preferences = [
    ["Invoice No.:", 0, 0, [True, NORMAL, invoice_number], [False], [False], [False],
     [False]],
    ["Invoice date:", 1, 0, [True, NORMAL, date_today.strftime('%d.%m.%Y')], [False], [False], [False], [False]],
    ["Due date:", 2, 0, [True, NORMAL, (date_today + timedelta(days=15)).strftime('%d.%m.%Y')], [False], [False],
     [False], [False]],
    ["Date of delivery:", 3, 0, [True, NORMAL, date_today.strftime('%d.%m.%Y')], [False], [False], [False],
     [False]],
    ["Our ref.:", 0, 2, [True, NORMAL, OUR_REF], [False], [False], [False], [False]],
    ["Account:", 1, 2, [True, NORMAL, ACCOUNT_NUMBER], [False], [False], [False], [False]],
    ["Interests\nmessage:", 2, 2, [False], [False], [False],
     [True, 'Upon payment by\nthe due date,\ninterest will\naccrue after the law'], [False]],

]
customer_widget_preferences = [
    ["Customer Id:", 0, 0, [False], [False],
     [True, retrieve_from_database(db_file, 'customers', 'CustomerID', True)], [False], [False]],
    ["Name:", 1, 0, [False], [False], [True, customer_full_name], [False], [False]],
    ["Organisation:", 2, 0, [True, NORMAL, all_customers_info[0][3]], [False], [False], [False], [False]],
    ["Customer ref.:", 3, 0, [True, NORMAL, all_customers_info[0][1][0] + all_customers_info[0][2]], [False], [False],
     [False], [False]],
    ["Address:", 0, 2, [True, NORMAL, all_customers_info[0][4]], [False], [False], [False], [False]],
    ["", 1, 2, [True, NORMAL, all_customers_info[0][5] + ' ' + all_customers_info[0][6]], [False], [False],
     [False], [False]],
    ["Phone:", 2, 2, [True, NORMAL, all_customers_info[0][7]], [False], [False], [False], [False]],
    ["Mail:", 3, 2, [True, NORMAL, all_customers_info[0][8]], [False], [False], [False], [False]],
    ["KID:", 4, 2, [True, NORMAL, all_customers_info[0][9]], [False], [False], [False], [False]]
]

product_widget_preferences = [
    ["Product Id:", 1, 0, [False], [False],
     [True, retrieve_from_database(db_file, 'products', 'ProductID', True)], [False], [False]],
    ["Product:", 1, 1, [False], [False], [True, retrieve_from_database(db_file, 'products', 'Name', True)], [False],
     [False]],
    ["Comment:", 1, 2, [False], [False], [False], [False], [True]],
    ["Unit price:", 1, 3, [True, NORMAL, all_products_info[0][3]], [False], [False], [False], [False]],
    ["# of units:", 1, 4, [False], [True], [False], [False], [False]],
    ["Total:", 1, 5, [True, NORMAL, '0.0'], [False], [False], [False], [False]],
    # ["MVA %:", 7, 0, [False], [True], [False], [False], [False]],
    # ["Total incl. MVA:", 8, 0, [True, 'readonly', '0'], [False], [False], [False], [False]]
]

# For every invoice field we need a label
for widget in [[invoice_widget_preferences, invoice_labels, invoice_frame],
               [customer_widget_preferences, customer_labels, customer_frame]]:
    # Add to widget list [[7], [8], [9], [10]]
    widgets.append(make_label(widget[0], widget[1], widget[2]))

for widget in [[invoice_widget_preferences, invoice_io_fields, invoice_frame],
               [customer_widget_preferences, customer_io_fields, customer_frame]]:
    # Add to widget list [[11], [12], [13], [14]]
    widgets.append(make_io_field(widget[0], widget[1], widget[2]))

widgets.append(make_product_label(product_widget_preferences, product_labels, product_frame))
widgets.append(make_product_io_field(product_widget_preferences, product_io_fields, product_frame))


add_product_btn = Button(product_frame,
                         text='Add product', font=body, fg=text_color,
                         padx=5, pady=2, command=on_add_product_btn_clicked)
add_product_btn.grid(row=0, column=0, padx=1, pady=0, sticky=W)
widgets.append([add_product_btn])
remove_product_btn = Button(product_frame,
                            text='Remove product', font=body, fg=text_color,
                            padx=5, pady=2, command=on_remove_product_btn_clicked, state=DISABLED)
remove_product_btn.grid(row=0, column=1, padx=1, pady=0, sticky=W)
widgets.append([remove_product_btn])
Grid.rowconfigure(product_frame, add_product_btn, weight=1)
Grid.columnconfigure(product_frame, remove_product_btn, weight=1)

total_label = Label(buttons_frame, text='Total:', font=body, fg=text_color, padx=5, pady=2)
total_label.grid(row=0, column=0, padx=1, pady=0, sticky=E)
mva_label = Label(buttons_frame, text='MVA (%):', font=body, fg=text_color, padx=5, pady=2)
mva_label.grid(row=1, column=0, padx=1, pady=0, sticky=E)
total_incl_mva_label = Label(buttons_frame, text='Total incl. MVA:', font=body, fg=text_color, padx=5, pady=2)
total_incl_mva_label.grid(row=2, column=0, padx=1, pady=0, sticky=E)

total_entry = Entry(buttons_frame, font=body, fg=text_color, justify=LEFT, state='readonly', width=15)
set_entry_field_text(total_entry, f"{0.00:.2f}")
total_entry.grid(row=0, column=1, padx=1, pady=0, sticky=W)
mva_sb = Spinbox(buttons_frame, font=body, width=15, justify=LEFT, from_=0, to=100, increment=0.5,
                 readonlybackground=background, state=NORMAL, fg=text_color)
mva_sb.configure(command=lambda obj=mva_sb: spn_box_clicked(obj))
mva_sb.bind('<Return>', (lambda obj=mva_sb: spn_box_clicked(obj)))

mva_sb.grid(row=1, column=1, padx=1, pady=0, sticky=W)

total_incl_mva_entry = Entry(buttons_frame, font=body, fg=text_color, justify=LEFT, state='readonly', width=15)
set_entry_field_text(total_incl_mva_entry, f"{0.00:.2f}")
total_incl_mva_entry.grid(row=2, column=1, padx=1, pady=0, sticky=W)

make_pdf_btn = Button(buttons_frame,
                      text='Create PDF', font=body, fg=text_color,
                      padx=5, pady=2, command=make_invoice_pdf, state=NORMAL)
make_pdf_btn.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky=E + N + S)
widgets.append([make_pdf_btn])
# Grid.rowconfigure(buttons_frame, add_product_btn, weight=1)
# Grid.columnconfigure(product_frame, make_pdf_btn, weight=1)


# Adds a menubar to the program
menubar = Menu(app)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open html", command=None)
filemenu.add_command(label="Save selections", command=None)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
# appearance_submenu = Menu(editmenu, tearoff=0)
# appearance_submenu.add_command(label="Dark mode", command=lambda: change_theme(True))
# appearance_submenu.add_command(label="Light mode", command=lambda: change_theme(False), state=DISABLED)
# editmenu.add_cascade(label='Appearance', menu=appearance_submenu)
editmenu.add_command(label="Edit customers...", command=None)
editmenu.add_command(label="Edit products...", command=None)
# editmenu.add_command(label="Clear all fields", command=clear_all)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: display_message('About', about_message))
helpmenu.add_command(label="Instructions", command=lambda: display_message('Instructons', instruction_message))
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
app.config(menu=menubar)

# Restricting window to change it's size
app.resizable(0, 0)
# </editor-fold>

# Start the event loop
app.mainloop()
