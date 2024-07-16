# CODSOFT-3
A simple and intuitive contact management application built using Python and PySimpleGUI. This application allows users to efficiently manage their personal and professional contacts by providing features to add, update, delete, and search for contacts. All contact information is stored in a CSV file, ensuring easy data persistence and portability.

Sure! Here's a more detailed README file with an extended description for your Contact Book project:

---
## Project Title

**Contact Book**

A comprehensive and user-friendly contact management application designed to store and manage personal and professional contacts efficiently.

## Description

The Contact Book application is designed to streamline the process of managing contacts. Whether you need to store personal contact details or maintain a professional contact list, this application provides an easy-to-use interface and essential features to handle your needs. 

### Key Functionalities

1. **Add Contacts**: Users can add new contacts by entering the first name, last name, phone number, email, and address. The application validates the inputs and saves the contact information to a CSV file.
2. **Update Contacts**: Users can update existing contacts by searching for them using the last name or phone number. Once found, the details can be edited and saved back to the CSV file.
3. **Delete Contacts**: Users can delete contacts by searching for them and confirming the deletion. This ensures that unwanted contacts are removed from the CSV file.
4. **Search Contacts**: A search functionality allows users to quickly find contacts by last name or phone number. The results are displayed in a table format for easy viewing.
5. **Display Contacts**: All contacts are displayed in a table with columns for first name, last name, phone number, email, and address. This provides a clear and organized view of all stored contacts.
6. **Clear Inputs**: The application includes a feature to clear all input fields, making it easy to reset the form and enter new data.

## API Reference

This project does not use an external API. It uses the `csv` and `os` modules from Python's standard library for data storage and manipulation.

## Color Reference

This project uses the default color scheme provided by PySimpleGUI, which is designed to be simple and visually appealing across different operating systems.

## Features

- **Add Contacts**: Enter first name, last name, phone number, email, and address to add a new contact.
- **Update Contacts**: Search for a contact by last name or phone number and update their details.
- **Delete Contacts**: Remove contacts from the list by searching and deleting them.
- **Search Contacts**: Find contacts quickly by last name or phone number.
- **Display Contacts**: View a list of all saved contacts in a table format with columns for first name, last name, phone number, email, and address.
- **Clear Inputs**: Easily clear all input fields to enter new data or reset the form.
- **Data Persistence**: Contacts are stored in a CSV file, ensuring data is saved between sessions.

## Environment Variables

No environment variables are required for this project.

## Demo

A demo of the Contact Book application can be seen in the screenshots below:
![Screenshot (105)](https://github.com/user-attachments/assets/60ce60d7-cc07-4fb1-853b-4a1dd23e3a59)

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/KartikyeThakur/CODSOFT-3.git
   ```
2. Navigate to the project directory:
   ```sh
   cd contact-book
   ```
3. Install the required dependencies:
   ```sh
   pip install PySimpleGUI
   ```
4. Run the application:
   ```sh
   python contact_book.py
   ```

## Lessons Learned

- **GUI Development**: Learned how to create a graphical user interface using PySimpleGUI, including layout design and event handling.
- **Data Management**: Gained experience in reading from and writing to CSV files for data storage and persistence.
- **User Interaction**: Improved understanding of designing user-friendly forms and handling user inputs and actions.

## Optimizations

Future improvements for the project could include:
- **Input Validation**: Adding validation for input fields to ensure correct data entry (e.g., email format, phone number format).
- **Enhanced Search**: Making the search functionality case-insensitive and supporting partial matches to improve usability.
- **Data Storage**: Implementing a more robust data storage solution, such as a database (e.g., SQLite, PostgreSQL).
- **User Experience**: Enhancing the user interface with additional features like sorting and filtering contacts.

## Run Locally

To run this project locally, follow the steps in the [Installation](#installation) section.

## Running Tests

This project does not currently include automated tests. Testing can be done manually by running the application and verifying the functionality of each feature.

## Usage/Examples

To use the Contact Book application:

1. **Add a Contact**:
   - Enter the contact information (first name, last name, phone number, email, address) in the provided fields.
   - Click the "Save" button to add the contact to the CSV file.
   - A confirmation popup will appear indicating the contact was saved successfully.

2. **Search for a Contact**:
   - Enter the last name or phone number of the contact you want to search for in the search field.
   - Click the "Search" button to find and display the matching contacts in the table.
   - If no matching contacts are found, a popup will inform you.

3. **Update a Contact**:
   - Search for the contact you want to update.
   - Modify the contact details in the input fields.
   - Click the "Update" button to save the changes.
   - A confirmation popup will appear indicating the contact was updated successfully.

4. **Delete a Contact**:
   - Search for the contact you want to delete.
   - Click the "Delete" button to remove the contact from the CSV file.
   - A confirmation popup will appear indicating the contact was deleted successfully.

5. **Clear Inputs**:
   - Click the "Cancel" button to clear all input fields and reset the form.

## Example Code

Below is a snippet of how the main functions are implemented in the Contact Book application:

```python
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
```

## Conclusion

The Contact Book project provides a practical example of using PySimpleGUI for building simple yet functional desktop applications in Python. It demonstrates how to handle user inputs, manage data storage with CSV files, and create an interactive GUI for managing contacts. This project serves as a great foundation for further enhancements and learning in the realm of Python-based GUI development and data management.

## Sample output
![Screenshot (111)](https://github.com/user-attachments/assets/9c19a94f-d398-431f-95da-85b5305b6f2d)
![Screenshot (110)](https://github.com/user-attachments/assets/31a4f966-e4fd-47a8-a560-e6c70ad99168)
![Screenshot (109)](https://github.com/user-attachments/assets/5349f954-a40f-43cd-b1b2-99f7c9f5a0a8)
![Screenshot (108)](https://github.com/user-attachments/assets/961b241c-7427-471a-8d14-9cf4bb6e33f9)
![Screenshot (107)](https://github.com/user-attachments/assets/27bf4e7f-0d76-4321-8370-3cca88d718dc)
![Screenshot (106)](https://github.com/user-attachments/assets/d77550e9-b50a-4508-a01f-1f2c24c98da6)
![Screenshot (105)](https://github.com/user-attachments/assets/c4050659-519e-4bb4-9847-8b37d08fdfc6)

