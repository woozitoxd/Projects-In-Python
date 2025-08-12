# main.py
from autenticacion import Autenticacion

def main():
    auth = Autenticacion()
    auth.login("admin", "1234")

if __name__ == "__main__":
    main()
