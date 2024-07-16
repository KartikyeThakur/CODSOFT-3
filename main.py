import PySimpleGUI as sg
import csv
import os

# Function to clear input fields
def clear_inputs():
    window['-fname-'].update('')
    window['-lname-'].update('')
    window['-phone-'].update('')
    window['-email-'].update('')
    window['-address-'].update('')

# Function to read all contacts
def read_contacts():
    contacts = []
    if os.path.exists('contacts.csv'):
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    return contacts

# Function to write all contacts
def write_contacts(contacts):
    with open('contacts.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Layout for the main window
layout = [
    [sg.Text('Enter First Name'), sg.InputText(key='-fname-')],
    [sg.Text('Enter Last Name'), sg.InputText(key='-lname-')],
    [sg.Text('Enter Phone Number'), sg.InputText(key='-phone-')],
    [sg.Text('Enter Email'), sg.InputText(key='-email-')],
    [sg.Text('Enter Address'), sg.InputText(key='-address-')],
    [sg.Button('Save'), sg.Button('Update'), sg.Button('Delete'), sg.Button('Cancel')],
    [sg.Text("Search by Last Name or Phone Number"), sg.InputText(key='-searchText-')],
    [sg.Button('Search')],
    [sg.Text("Contacts List")],
    [sg.Table(values=[], headings=['First Name', 'Last Name', 'Phone', 'Email', 'Address'],
              key='-contactList-', enable_events=True, auto_size_columns=False, col_widths=[15, 15, 15, 25, 30], num_rows=10)],
    [sg.Text(key='-searchOutput-', size=(50, 2))]
]

# Create the window
window = sg.Window('Contact Book', layout)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    fname = values['-fname-']
    lname = values['-lname-']
    phone = values['-phone-']
    email = values['-email-']
    address = values['-address-']
    contact_info = [fname, lname, phone, email, address]

    if event == 'Save':
        if fname and lname and phone:
            with open('contacts.csv', 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(contact_info)
            clear_inputs()
            sg.popup('Contact saved successfully!')
        else:
            sg.popup('First name, last name, and phone number are required!')

    elif event == 'Search':
        searchText = values['-searchText-']
        contacts = read_contacts()
        results = [contact for contact in contacts if searchText.lower() in contact[1].lower() or searchText in contact[2]]
        if results:
            window['-contactList-'].update(results)
        else:
            window['-contactList-'].update([])
            sg.popup('No contact found!')

    elif event == 'Update':
        searchText = values['-searchText-']
        contacts = read_contacts()
        updated = False
        for i, contact in enumerate(contacts):
            if searchText.lower() in contact[1].lower() or searchText in contact[2]:
                contacts[i] = contact_info
                updated = True
                break
        if updated:
            write_contacts(contacts)
            clear_inputs()
            sg.popup('Contact updated successfully!')
        else:
            sg.popup('Contact not found!')

    elif event == 'Delete':
        searchText = values['-searchText-']
        contacts = read_contacts()
        contacts = [contact for contact in contacts if searchText.lower() not in contact[1].lower() and searchText not in contact[2]]
        write_contacts(contacts)
        clear_inputs()
        sg.popup('Contact deleted successfully!')

window.close()
