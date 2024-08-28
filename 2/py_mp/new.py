import random
import string

DATA_FILE = "hospital_data.txt"

def load_data():
    patients = {}
    appointments = {}
    prescriptions = {}
    bills = {}
    medical_records = {}
    
    try:
        with open(DATA_FILE, 'r') as file:
            for line in file:
                category, data = line.strip().split(':')
                if category == 'patients':
                    patients = eval(data)
                elif category == 'appointments':
                    appointments = eval(data)
                elif category == 'prescriptions':
                    prescriptions = eval(data)
                elif category == 'bills':
                    bills = eval(data)
                elif category == 'medical_records':
                    medical_records = eval(data)
    except FileNotFoundError:
        pass
    
    return patients, appointments, prescriptions, bills, medical_records

def save_data(patients, appointments, prescriptions, bills, medical_records):
    with open(DATA_FILE, 'w') as file:
        file.write(f"patients:{patients}\n")
        file.write(f"appointments:{appointments}\n")
        file.write(f"prescriptions:{prescriptions}\n")
        file.write(f"bills:{bills}\n")
        file.write(f"medical_records:{medical_records}\n")

def generate_patient_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def register_patient(name, age, gender, phone, patients):
    patient_id = generate_patient_id()
    patients[patient_id] = {'Name': name, 'Age': age, 'Gender': gender, 'Phone': phone}
    save_data(patients, {}, {}, {}, {})
    print('Patient registered successfully.')
    print(f'Patient ID: {patient_id}')

def update_patient_info(patient_id, key, value, patients):
    if patient_id in patients:
        patients[patient_id][key] = value
        save_data(patients, {}, {}, {}, {})
        print('Patient information updated successfully.')
    else:
        print('Patient ID not found.')

def add_prescription(patient_id, prescription, prescriptions):
    if patient_id in prescriptions:
        prescriptions[patient_id].append(prescription)
    else:
        prescriptions[patient_id] = [prescription]
    save_data({}, {}, prescriptions, {}, {})
    print('Prescription added successfully.')

def generate_bill(patient_id, amount, bills):
    bill_id = len(bills) + 1
    bills[bill_id] = {'PatientID': patient_id, 'Amount': amount}
    save_data({}, {}, {}, bills, {})
    print('Bill generated successfully.')

def schedule_appointment(patient_id, date, time, doctor, appointments):
    appointment_id = len(appointments) + 1
    appointments[appointment_id] = {'PatientID': patient_id, 'Date': date, 'Time': time, 'Doctor': doctor}
    save_data({}, appointments, {}, {}, {})
    print('Appointment scheduled successfully.')

def search_patient(query, patients):
    result = []
    for patient_id, patient_info in patients.items():
        if query.lower() in patient_info['Name'].lower() or query == str(patient_id):
            result.append((patient_id, patient_info))
    return result

def manage_medical_records(patient_id, option, record, medical_records):
    if option == '1':  # Add new record
        if patient_id in medical_records:
            medical_records[patient_id].append(record)
        else:
            medical_records[patient_id] = [record]
        save_data({}, {}, {}, {}, medical_records)
        print('Medical record added successfully.')
    elif option == '2':  # View records
        if patient_id in medical_records:
            print('Medical Records:')
            for idx, rec in enumerate(medical_records[patient_id], start=1):
                print(f'{idx}. {rec}')
        else:
            print('No medical records found for this patient.')
    elif option == '3':  # Update record
        if patient_id in medical_records:
            record_index = int(input('Enter the index of the record to update: '))
            if 1 <= record_index <= len(medical_records[patient_id]):
                medical_records[patient_id][record_index - 1] = record
                save_data({}, {}, {}, {}, medical_records)
                print('Medical record updated successfully.')
            else:
                print('Invalid record index.')
        else:
            print('No medical records found for this patient.')
    elif option == '4':  # Delete record
        if patient_id in medical_records:
            record_index = int(input('Enter the index of the record to delete: '))
            if 1 <= record_index <= len(medical_records[patient_id]):
                del medical_records[patient_id][record_index - 1]
                save_data({}, {}, {}, {}, medical_records)
                print('Medical record deleted successfully.')
            else:
                print('Invalid record index.')
        else:
            print('No medical records found for this patient.')
    else:
        print('Invalid option.')

def main():
    patients, appointments, prescriptions, bills, medical_records = load_data()

    while True:
        print('\nHospital Management System')
        print('1. Register New Patient')
        print('2. Update Patient Information')
        print('3. Add Prescription')
        print('4. Generate Bill')
        print('5. Schedule Appointment')
        print('6. Search Patient')
        print('7. Manage Medical Records')
        print('8. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter patient name: ')
            age = input('Enter patient age: ')
            gender = input('Enter patient gender: ')
            phone = input('Enter patient phone number: ')
            register_patient(name, age, gender, phone, patients)
        elif choice == '2':
            patient_id = input('Enter patient ID: ')
            key = input('Enter information to update (Name/Age/Gender/Phone): ')
            value = input(f'Enter new {key}: ')
            update_patient_info(patient_id, key, value, patients)
        elif choice == '3':
            patient_id = input('Enter patient ID: ')
            prescription = input('Enter prescription details: ')
            add_prescription(patient_id, prescription, prescriptions)
        elif choice == '4':
            patient_id = input('Enter patient ID: ')
            amount = input('Enter bill amount: ')
            generate_bill(patient_id, amount, bills)
        elif choice == '5':
            patient_id = input('Enter patient ID: ')
            date = input('Enter appointment date (YYYY-MM-DD): ')
            time = input('Enter appointment time (HH:MM): ')
            doctor = input('Enter doctor name: ')
            schedule_appointment(patient_id, date, time, doctor, appointments)
        elif choice == '6':
            query = input('Enter patient name or ID: ')
            results = search_patient(query, patients)
            if results:
                print('Search Results:')
                for patient_id, patient_info in results:
                    print(f'Patient ID: {patient_id}')
                    for key, value in patient_info.items():
                        print(f'{key}: {value}')
            else:
                print('No matching patients found.')
        elif choice == '7':
            patient_id = input('Enter patient ID: ')
            print('1. Add New Record')
            print('2. View Records')
            print('3. Update Record')
            print('4. Delete Record')
            option = input('Enter your option: ')
            manage_medical_records(patient_id, option, "", medical_records)
        elif choice == '8':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
