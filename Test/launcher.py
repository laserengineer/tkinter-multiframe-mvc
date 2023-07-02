from BoN import BoN
from HA import HA

APP_MAP = {"BoN": BoN, "HA": HA}

def main(choice):
    try:
        app = APP_MAP[choice]("Launcher")
        app.launch()
    except KeyError:
        print(f"Invalid choice: {choice}")

if __name__ == "__main__":
    choice = input("What is your choice: ")
    main(choice)