def calculate_bmi(weight, height):
    try:
        # Convert height from centimeters to meters
        height_in_meters = height / 100

        # Calculate BMI
        bmi = weight / (height_in_meters ** 2)

        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    if bmi < 18.5:
        category = "Underweight"
        feedback = "Eat more and healthy!"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        feedback = "Awesome! Keep maintaining the same level of fitness."
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        feedback = "Exercise a little bit more and eat healthy."
    else:
        category = "Obesity"
        feedback = "You need to take care of your health seriously."

    return category, feedback

if __name__ == "__main__":
    
    print("""
    
_________  ________                             
| ___ \  \/  |_   _|                            
| |_/ / .  . | | |                              
| ___ \ |\/| | | |                              
| |_/ / |  | |_| |_                             
\____/\_|  |_/\___/                             
                                                
                                                
 _____       _            _       _             
/  __ \     | |          | |     | |            
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
                                                

    """)
    
    
    # Input from user
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    if isinstance(bmi, str):  # Check for error message
        print(bmi)
    else:
        # Determine BMI category and feedback
        category, feedback = bmi_category(bmi)

        # Display results
        print(f"Dear {name.upper()}, Your BMI is {bmi}. You are categorized as: {category}.")
        print(f"Feedback: {feedback}")
