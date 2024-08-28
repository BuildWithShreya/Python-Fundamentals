# Creating a dictionary for student information
student_dict = {
    "name": "JethaLal Gada",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "English", "History"],
    "address": {
        "street": "123 Main St",
        "city": "Unknown",
        "state": "ABC",
        "zip": "12345"
    }
}

# Accessing values in the student dictionary
print("Student Information:")
print("Name:", student_dict["name"])
print("Age:", student_dict["age"])
print("Grade:", student_dict["grade"])
print("Courses:", student_dict["courses"])
print("Address:")
print("  Street:", student_dict["address"]["street"])
print("  City:", student_dict["address"]["city"])
print("  State:", student_dict["address"]["state"])
print("  Zip:", student_dict["address"]["zip"])

student_dict["age"] = 21
student_dict["courses"].append("Science")
print("\nModified Student Information:")
print("Name:", student_dict["name"])
print("Age:", student_dict["age"])
print("Courses:", student_dict["courses"])

student_dict["phone"] = "555-1234"
print("\nStudent Information with Phone Number:")
print("Name:", student_dict["name"])
print("Phone:", student_dict["phone"])

del student_dict["address"]
print("\nStudent Information after removing address:")
print("Name:", student_dict["name"])
print("Address:", student_dict.get("address", "Address not available"))

is_present = "grade" in student_dict
print("\nIs 'grade' present in the dictionary?", is_present)
