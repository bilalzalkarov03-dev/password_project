import hashlib
import logging
import os

# Пункт 4: Все действия записать в логах
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_password(password):
    # Пункт 3: Учитывать как буквенные, так и числовые символы
    has_letters = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    return has_letters and has_digits

def main():
    # Пункт 1: Программа запрашивает файл
    filename = input("Введите имя файла с паролями (например, users_passwords.txt): ").strip()
    
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден!")
        logging.error(f"Файл {filename} не найден.")
        return

    # Чтение паролей из файла
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            valid_passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        logging.error(f"Ошибка чтения файла {filename}: {e}")
        return

    # Пункт 2: Программа запрашивает ваш пароль
    user_password = input("Введите ваш пароль: ").strip()
    logging.info("Пользователь ввел пароль для проверки.")

    # Проверка на совпадение
    if user_password in valid_passwords:
        if validate_password(user_password):
            # Шифрование пароля
            encrypted_password = hashlib.sha256(user_password.encode()).hexdigest()
            
            # Пункт 4: Программа говорит требуемую фразу
            print(f"«Проходите» Ваш пароль успешно зашифрован: {encrypted_password}")
            logging.info(f"Успешный вход. Пароль зашифрован: {encrypted_password}")
        else:
            print("Ошибка валидации: пароль должен содержать как буквы, так и цифры.")
            logging.warning("Пароль найден, но нет букв или цифр.")
    else:
        print("Доступ запрещен: неверный пароль.")
        logging.warning("Попытка входа с неверным паролем.")

if __name__ == '__main__':
    main()