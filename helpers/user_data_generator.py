import random
import string

class RandomRegistrationGenerator:
    @staticmethod
    def generate_random_name():
        names = ["Alex", 'Dana', 'Andrey']
        return random.choice(names)

    @staticmethod
    def generate_random_email():
        login_length = random.randint(5, 10)
        login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=login_length))

        domains = ['ya.ru', 'gmail.com', 'mail.ru']
        domain = random.choice(domains)

        return f"{login}@{domain}"

    @staticmethod
    def generate_password_random():
        length = random.randint(6, 12)
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

    @staticmethod
    def generate_incorrect_password(length=None):
        if length is None:
            length = random.randint(1, 5)  # Генерируем длину от 1 до 5

        characters = string.ascii_letters + string.digits + string.punctuation

        incorrect_password = ''.join(random.choice(characters) for _ in range(length))
        return incorrect_password