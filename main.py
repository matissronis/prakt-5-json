import requests

def get_fruit_info(fruit_name):
    url = f"https://www.fruityvice.com/api/fruit/{fruit_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("\nFruit Information:")
        print(f"Name: {data['name']}")
        print(f"Family: {data['family']}")
        print(f"Order: {data['order']}")
        print(f"Genus: {data['genus']}")
        print("Nutritions:")
        for key, value in data['nutritions'].items():
            print(f"  {key.capitalize()}: {value}")
        return data
    else:
        print("Error: Could not fetch data. Please check the fruit name and try again.")
        return None

def compare_protein(fruit1, fruit2):
    data1 = get_fruit_info(fruit1)
    data2 = get_fruit_info(fruit2)
    
    if data1 and data2:
        protein1 = data1['nutritions']['protein']
        protein2 = data2['nutritions']['protein']
        
        print(f"\nProtein comparison:")
        print(f"{fruit1.capitalize()}: {protein1}g")
        print(f"{fruit2.capitalize()}: {protein2}g")
        
        if protein1 > protein2:
            print(f"{fruit1.capitalize()} has more protein than {fruit2.capitalize()}.")
        elif protein1 < protein2:
            print(f"{fruit2.capitalize()} has more protein than {fruit1.capitalize()}.")
        else:
            print(f"Both {fruit1.capitalize()} and {fruit2.capitalize()} have the same protein content.")

def calculate_nutrition_for_weight(fruit_name, weight):
    data = get_fruit_info(fruit_name)
    if data:
        print(f"\nNutrition for {weight}g of {fruit_name.capitalize()}:")
        for key, value in data['nutritions'].items():
            adjusted_value = (value / 100) * weight
            print(f"  {key.capitalize()}: {adjusted_value:.2f}")

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Display fruit nutrients")
        print("2. Compare protein content of two fruits")
        print("3. Calculate nutrients based on weight")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            fruit_name = input("Enter the name of the fruit: ").lower()
            get_fruit_info(fruit_name)
        elif choice == "2":
            fruit1 = input("Enter the first fruit: ").lower()
            fruit2 = input("Enter the second fruit: ").lower()
            compare_protein(fruit1, fruit2)
        elif choice == "3":
            fruit_name = input("Enter the name of the fruit: ").lower()
            weight = float(input("Enter the weight in grams: "))
            calculate_nutrition_for_weight(fruit_name, weight)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")