import sys
import requests
from datetime import datetime
from colorama import init, Fore
import time
import argparse

# Colorama'nın Windows'ta da düzgün çalışabilmesi için gerekli
init()

def get_current_time():
    current_time = datetime.now()
    hour = int(current_time.strftime("%H"))
    minutes = int(current_time.strftime("%M"))
    return hour, minutes

def get_prayer_times(city):
    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=Turkey&method=2'
    response = requests.get(url)
    data = response.json()
    timings = data['data']['timings']
    return timings

def get_time_difference(current_value, target_value):
    if current_value > target_value:
        target_value += 24 * 60  # Gece yarısını geçmişse, hedef değeri bir gün arttır
    time_difference = target_value - current_value
    hours = time_difference // 60
    minutes = time_difference % 60
    return hours, minutes

def print_time_remaining(hours, minutes):
    if hours < 0 or minutes < 0:
        print(Fore.RED + "Hedef saat geçmiş.")
    else:
        print(Fore.GREEN + f"İftar saatine toplamda {hours} saat {minutes} dakika kaldı.")

def main():
    parser = argparse.ArgumentParser(description='Get remaining time until Maghrib prayer.')
    parser.add_argument('--city', type=str, help='City name to get prayer times', required=True)
    parser.add_argument('--end-hour', type=str, help='End hour of work', required=True)
    parser.add_argument('-j', action='store_true', help='Show remaining time until job end')
    parser.add_argument('-i', action='store_true', help='Show remaining time until iftar')
    args, unknown = parser.parse_known_args()

    while True:
        current_hour, current_minutes = get_current_time()
        print("Sistem saati:", current_hour, current_minutes)

        city = args.city
        prayer_times = get_prayer_times(city)
        maghrib_hour, maghrib_minute = map(int, prayer_times['Maghrib'].split(':'))
        maghrib_value = maghrib_hour * 60 + maghrib_minute + 5

        # İş bitiş saati
        end_hour, end_minutes = map(int, args.end_hour.split(':'))
        end_value = end_hour * 60 + end_minutes

        current_value = current_hour * 60 + current_minutes
        hours, minutes = get_time_difference(current_value, maghrib_value)

        # -j parametresi kontrolü
        if args.j:
            job_hours, job_minutes = get_time_difference(current_value, end_value)
            print(Fore.YELLOW + f"İş bitimine {job_hours} saat {job_minutes} dakika kaldı.")

        # -i parametresi kontrolü
        if args.i:
            print_time_remaining(hours, minutes)

        # Bir dakika bekle
        time.sleep(60)

if __name__ == "__main__":
    main()
