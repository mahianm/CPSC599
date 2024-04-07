import requests
from bs4 import BeautifulSoup
import serial
import time

arduino_port = 'COM4'
ser = serial.Serial(arduino_port, 9600)

def get_subscriber_count(url):
    headers = {'Cache-Control': 'no-cache'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    subscriber_count_element = soup.find(class_='id_odometer__dDC1d mainOdometer')
    if subscriber_count_element:
        subscriber_count = subscriber_count_element.get_text().strip()
        return int(subscriber_count.replace(',', ''))
    else:
        print("Subscriber count element not found.")
        return None

def main():
    url = input("Enter the URL of the YouTube channel: ")
    daily_goal = int(input("Enter the total subscribers you want to get for your daily goal: "))
    subscriber_threshold = daily_goal // 10
    print("Token Weight:", subscriber_threshold)
    prev_subscriber_count = get_subscriber_count(url)
    servo_moves = 0

    while True:
        subscriber_count = get_subscriber_count(url)
        if subscriber_count is not None:
            print("Subscriber Count:", subscriber_count)
            new_subscribers = subscriber_count - prev_subscriber_count
            if new_subscribers >= subscriber_threshold:
                moves = new_subscribers // subscriber_threshold
                servo_moves += moves
                print("Servo moves:", servo_moves)
                ser.write(str(servo_moves).encode())
                prev_subscriber_count += moves * subscriber_threshold
                servo_moves = 0
        time.sleep(5)

if __name__ == "__main__":
    main()
