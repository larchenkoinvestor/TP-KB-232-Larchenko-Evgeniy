import requests

def get_exch_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['rate']
    else:
        raise Exception("Не вдалося отримати дані про курс валюти.")

def convert_cur(amount, currency_code):
    
    rate = get_exch_rate(currency_code)
    return amount * rate

def main_converter():
    print("Конвертація валют: EUR, USD, PLN у гривню.")
    supported_currencies = ["EUR", "USD", "PLN"]
    
    while True:
        currency = input("Введіть валюту (EUR, USD, PLN) або 'exit' для виходу: ").strip().upper()
        if currency == "EXIT":
            print("Програму завершено.")
            break
        if currency not in supported_currencies:
            print("Некоректна валюта. Спробуйте ще раз.")
            continue
        
        try:
            amount = float(input(f"Введіть кількість {currency}: "))
            result = convert_cur(amount, currency)
            print(f"{amount} {currency} = {result:.2f} UAH")
        except ValueError:
            print("Будь ласка, введіть коректне числове значення.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main_converter()
