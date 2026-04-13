def calculate_life_path_number(birthdate):
    day, month, year = map(int, birthdate.split('/'))
    total = sum(int(digit) for digit in str(day + month + year))
    
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    
    return total


def numerology_analysis():
    birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
    
    try:
        number = calculate_life_path_number(birthdate)
        print(f"\n🔢 Life Path Number: {number}")
        
        if number <= 2:
            return "You may feel emotionally sensitive and introspective."
        elif number <= 4:
            return "You are practical but sometimes overwhelmed."
        elif number <= 6:
            return "You are caring but can feel emotionally heavy."
        else:
            return "You are generally positive and energetic."
            
    except:
        return "Invalid date format!"


def personality_quiz():
    print("\n🧠 Personality Quiz (Answer honestly)\n")
    
    score = 0
    
    q1 = input("Do you enjoy social gatherings? (yes/no): ").lower()
    if q1 == "yes":
        score += 2
        
    q2 = input("Do you often overthink? (yes/no): ").lower()
    if q2 == "yes":
        score += 1
        
    q3 = input("Do you handle stress well? (yes/no): ").lower()
    if q3 == "yes":
        score += 2
        
    q4 = input("Do you prefer staying alone? (yes/no): ").lower()
    if q4 == "yes":
        score -= 1
        
    # Result
    if score >= 4:
        return "You are extroverted, confident, and emotionally stable."
    elif score >= 2:
        return "You are balanced with both introvert and extrovert traits."
    else:
        return "You are more introverted and emotionally aware."


def generate_report(num_result, quiz_result):
    print("\n📊 ===== PERSONALITY REPORT =====")
    print("\n🔮 Numerology Insight:")
    print(num_result)
    
    print("\n🧠 Personality Insight:")
    print(quiz_result)
    
    print("\n💡 Overall Suggestion:")
    print("Focus on self-awareness, manage stress, and maintain healthy relationships.")
    print("=================================\n")


def main():
    print("✨ Welcome to Persona Scanner ✨")
    
    while True:
        print("\n1. Take Full Personality Test")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num_result = numerology_analysis()
            quiz_result = personality_quiz()
            generate_report(num_result, quiz_result)
            
        elif choice == "2":
            print("Thank you for using Persona Scanner!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()