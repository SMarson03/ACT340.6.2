# Problem 1

# Add the following key/value pair to the dictionary below. "oceans": ["Pacific", "Atlantic", "Indian", "Arctic"]
# geography= {"continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"]}

geography= {"continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"],
"oceans": ["Pacific", "Atlantic", "Indian", "Arctic"]
}

print(geography)

# Problem 2

# Use the Dictionary below
# Change the value for the height key to 72 inches
# patient= {"name": "John Doe", "age": 25, "height": 64, "symptoms": "cough" }

patient= {"name": "John Doe", "age": 25, "height": 72, "symptoms": "cough" }

print(patient)

# Problem 3

# Use the same dictionary as above
# Use a Class method to generate a list of tuples that consists of each key:value pair

class Patient:
    def __init__(self, name, age, height, symptoms):
        self.data = {
            "name": name,
            "age": age,
            "height": height,
            "symptoms": symptoms
        }
    
    def to_tuples(self):
        return list(self.data.items())

# Example usage
patient = Patient("John Doe", 25, 72, "cough")
print(patient.to_tuples())

# Problem 4: Print the value of "name"
# You can create a method to print the value of the "name" key:
class Patient:
    def __init__(self, name, age, height, symptoms):
        self.data = {
            "name": name,
            "age": age,
            "height": height,
            "symptoms": symptoms
        }
    
    def print_name(self):
        print(self.data["name"])

# Example usage
patient = Patient("John Doe", 25, 72, "cough")
patient.print_name()

# Problem 5: Look for the key "weight" with a default argument
# You can implement a method to look for the "weight" key and return a default value if not found:

class Patient:
    def __init__(self, name, age, height, symptoms):
        self.data = {
            "name": name,
            "age": age,
            "height": height,
            "symptoms": symptoms
        }
    
    def get_weight(self, default=150):
        return self.data.get("weight", default)

# Example usage
patient = Patient("John Doe", 25, 72, "cough")
print(patient.get_weight())

# Problem 6: Remove everything from the dictionary
# You can create a method to clear the dictionary:

class Patient:
    def __init__(self, name, age, height, symptoms):
        self.data = {
            "name": name,
            "age": age,
            "height": height,
            "symptoms": symptoms
        }
    
    def clear_data(self):
        self.data.clear()

# Example usage
patient = Patient("John Doe", 25, 72, "cough")
patient.clear_data()
print(patient.data)  # Should print an empty dictionary

# Problem 7: Loop through a dictionary and modify values
# Assuming you have a dictionary with numeric values, you can use a loop to process it:

values_dict = {
    "a": 1500,
    "b": 2500,
    "c": 3000,
    "d": 1800
}

new_list = []
for key, value in values_dict.items():
    if value > 2000:
        new_list.append(value - 500)

print(new_list)  # Output will be [2000, 2500]