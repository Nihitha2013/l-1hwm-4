import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Full JSON response: {fact_data}")
        return fact_data['fact']
    else:
        return "Failed to fetch cat fact."

def main():
    print("Welcome to the cat fact generator!")
    while True:
        user_input = input("Press Enter to get a cat fact or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        fact = get_cat_fact()
        print(f"🐱 Cat Fact: {fact}\n")

if __name__ == "__main__":
    main()