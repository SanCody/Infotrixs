import requests
import time
import json


key = '48ddf22a0d664bf183d80201240301'

def weather(city):
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={city}'
    try:
        res = requests.get(url)
        return res.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def add_favorites(city=None):
    if city is None:
        city = input('Enter the city name or "n" to back: ').lower()
    with open('fav.json', 'r') as file:
        fav_data = json.load(file)

    existing = fav_data.get('favs', [])

    if city != "":
        if city.lower() == 'n':
            time.sleep(5)
        elif city not in existing:
            existing.append(city)

            fav_data['favs'] = existing

            with open('fav.json', 'w') as file:
                json.dump(fav_data, file, indent=4)

            print('City added to favorites')
        else:
            print("City already exists in favorites")
    else:
        print("please enter a valid name!")
    time.sleep(5)

def show_favorites():
    while True:
        with open('fav.json', 'r') as file:
            fav_data = json.load(file)
            favorite_cities = fav_data.get('favs', [])
            if favorite_cities:
                print("Your favorite cities:")
                for i, city in enumerate(favorite_cities, start=1):
                    print(f"{i}. {city}")
                time.sleep(5)
                action_choice = input('Choose an action:\n1. Update a city\n2. Delete a city\n3. Back\nEnter the number: ')

                if action_choice == '1':
                    update_city(favorite_cities, fav_data)
                elif action_choice == '2':
                    delete_city(favorite_cities)
                elif action_choice == '3':
                    break
                else:
                    print('Invalid input.')
                    time.sleep(5)
            else:
                print("You haven't added any cities to your favorites yet.")

def delete_city(favorite_cities):
    rem = input('Enter the number of city to remove: ')
    try:
        city_num = int(rem) - 1
        if 0 <= city_num < len(favorite_cities):
            rem_city = favorite_cities.pop(city_num)
            with open('fav.json', 'w') as file:
                json.dump({"favs": favorite_cities}, file, indent=2)
            print(f"'{rem_city}' removed from favorites.")
            time.sleep(5)
        else:
            print("Invalid number. No changes made to favorites.")
            time.sleep(5)
    except ValueError:
        print("Invalid input. No changes made to favorites.")
        time.sleep(5)

def update_city(favorite_cities, fav_data):
    update_choice = input('Enter the number of the city to update: ')

    try:
        city_index = int(update_choice) - 1

        if 0 <= city_index < len(favorite_cities):
            new_city_name = input("Enter the updated city name: ")
            favorite_cities[city_index] = new_city_name
            fav_data['favs'] = favorite_cities

            with open('fav.json', 'w') as file:
                json.dump(fav_data, file, indent=2)

            print(f"City updated to '{new_city_name}'.")
        else:
            print("Invalid number. No changes made to favorites.")
    except ValueError:
        print("Invalid input. No changes made to favorites.")


def menu():
    while True:
        print('-------------------')
        print('1. Check Weather')
        print('2. Add to favorites')
        print('3. Show favorites')
        print('4. Quit')
        print('-------------------')

        choice = input('Enter the number: ')

        if choice == '1':
            city = input('Enter city name: ') or 'chennai'
            data = weather(city)
            if data:
                temp = data['current']['temp_c']
                print(f'{city}: {temp} °C')
                add=input('Add to favorites y/n: ')
                if add.lower() == 'y':
                    add_favorites(city)
                elif add.lower() == 'n':
                    pass
                else:
                    print('Invalid Input')
                time.sleep(5)
        elif choice == '2':
            add_favorites()
        elif choice == '3':
            show_favorites()
        elif choice == '4':
            print('Thank you')
            time.sleep(15)
            break
        else:
            print('Invalid input')
            time.sleep(5)
            

if __name__ == "__main__":
    menu()