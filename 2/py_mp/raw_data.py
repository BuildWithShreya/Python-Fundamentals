import pandas as pd
from datetime import datetime
from tkinter import *
from tkinter import messagebox

# Load patient data from CSV
def load_patient_data():
    try:
        return pd.read_csv('patients.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Patient ID', 'Name', 'Age', 'Gender', 'Phone'])

# Load appointment data from CSV
def load_appointment_data():
    try:
        return pd.read_csv('appointments.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Patient ID', 'Date', 'Time', 'Doctor'])

# Save patient data to CSV
def save_patient_data(patients_df):
    patients_df.to_csv('patients.csv', index=False)

# Save appointment data to CSV
def save_appointment_data(appointments_df):
    appointments_df.to_csv('appointments.csv', index=False)

# Register a new patient
def register_patient(name, age, gender, phone, patients_df):
    new_patient_id = patients_df['Patient ID'].max() + 1 if not patients_df.empty else 1
    new_patient = pd.DataFrame([[new_patient_id, name, age, gender, phone]],
                               columns=['Patient ID', 'Name', 'Age', 'Gender', 'Phone'])
    patients_df = patients_df.append(new_patient, ignore_index=True)
    save_patient_data(patients_df)
    messagebox.showinfo('Success', 'Patient registered successfully.')

# Schedule a new appointment
def schedule_appointment(patient_id, date, time, doctor, appointments_df):
    new_appointment = pd.DataFrame([[patient_id, date, time, doctor]],
                                   columns=['Patient ID', 'Date', 'Time', 'Doctor'])
    appointments_df = appointments_df.append(new_appointment, ignore_index=True)
    save_appointment_data(appointments_df)
    messagebox.showinfo('Success', 'Appointment scheduled successfully.')

# Search for a patient by name or ID
def search_patient(query, patients_df):
    result = patients_df[(patients_df['Name'].str.contains(query, case=False)) |
                         (patients_df['Patient ID'].astype(str).str.contains(query))]
    return result

# Main GUI window
def main_window():
    root = Tk()
    root.title('Hospital Management System')

    # Load data
    patients_df = load_patient_data()
    appointments_df = load_appointment_data()

    # Functions for button actions
    def register_patient_action():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        phone = phone_entry.get()
        if name and age and gender and phone:
            register_patient(name, int(age), gender, phone, patients_df)
        else:
            messagebox.showwarning('Warning', 'Please fill in all fields.')

    def schedule_appointment_action():
        patient_id = patient_id_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        doctor = doctor_entry.get()
        if patient_id and date and time and doctor:
            schedule_appointment(int(patient_id), date, time, doctor, appointments_df)
        else:
            messagebox.showwarning('Warning', 'Please fill in all fields.')

    def search_patient_action():
        query = search_entry.get()
        result_df = search_patient(query, patients_df)
        if not result_df.empty:
            search_results_text.config(state=NORMAL)
            search_results_text.delete('1.0', END)
            search_results_text.insert(END, result_df.to_string(index=False))
            search_results_text.config(state=DISABLED)
        else:
            messagebox.showinfo('Search Results', 'No matching patients found.')

    # GUI elements
    Label(root, text='Register New Patient').pack()
    Label(root, text='Name:').pack()
    name_entry = Entry(root)
    name_entry.pack()

    Label(root, text='Age:').pack()
    age_entry = Entry(root)
    age_entry.pack()

    Label(root, text='Gender:').pack()
    gender_entry = Entry(root)
    gender_entry.pack()

    Label(root, text='Phone:').pack()
    phone_entry = Entry(root)
    phone_entry.pack()

    Button(root, text='Register', command=register_patient_action).pack()

    Label(root, text='\nSchedule Appointment').pack()
    Label(root, text='Patient ID:').pack()
    patient_id_entry = Entry(root)
    patient_id_entry.pack()

    Label(root, text='Date (YYYY-MM-DD):').pack()
    date_entry = Entry(root)
    date_entry.pack()

    Label(root, text='Time (HH:MM):').pack()
    time_entry = Entry(root)
    time_entry.pack()

    Label(root, text='Doctor:').pack()
    doctor_entry = Entry(root)
    doctor_entry.pack()

    Button(root, text='Schedule', command=schedule_appointment_action).pack()

    Label(root, text='\nSearch Patient').pack()
    search_entry = Entry(root)
    search_entry.pack()

    search_button = Button(root, text='Search', command=search_patient_action)
    search_button.pack()

    search_results_text = Text(root, height=5, width=50, state=DISABLED)
    search_results_text.pack()

    root.mainloop()

if _name_ == '_main_':
    main_window()