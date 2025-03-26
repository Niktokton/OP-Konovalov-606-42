from flask import Flask, request
from pack.particles import Electron, Proton, Neutron
import psycopg2

app = Flask(__name__)

# Настройки подключения к PostgreSQL
DB_CONFIG = {
    'host': 'localhost',  # замените на ваш хост
    'database': 'my_database',  # замените на имя вашей базы данных
    'user': 'postgres',  # замените на ваше имя пользователя
    'password': '1234'  # замените на ваш пароль
}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_particle = request.form.get('particle')

        if selected_particle == "Electron":
            particle = Electron()
        elif selected_particle == "Proton":
            particle = Proton()
        elif selected_particle == "Neutron":
            particle = Neutron()
        else:
            return "Не выбрана частица!"

        result_text = f"{particle.name}<br>" \
                      f"Удельный заряд: {particle.specific_charge:.2e} Кл/кг<br>" \
                      f"Комптоновская длина волны: {particle.compton_wavelength:.2e} м"

        save_to_db(selected_particle, particle.specific_charge, particle.compton_wavelength)

        return f'''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Физические расчеты</title>
        </head>
        <body>
            <h1>Результат расчета</h1>
            {result_text}
        </body>
        </html>
        '''
    else:
        return '''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Физические расчеты</title>
        </head>
        <body>
            <h1>Выбор частицы</h1>
            <form method="post" action="/">
                <select name="particle">
                    <option value="">Выберите частицу</option>
                    <option value="Electron">Электрон</option>
                    <option value="Proton">Протон</option>
                    <option value="Neutron">Нейтрон</option>
                </select>
                <button type="submit">Рассчитать</button>
            </form>
        </body>
        </html>
        '''


def create_database():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id SERIAL PRIMARY KEY,
                particle_type TEXT NOT NULL,
                specific_charge DOUBLE PRECISION,
                compton_wavelength DOUBLE PRECISION,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")


def save_to_db(particle_name, specific_charge, compton_wavelength):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO history (particle_type, specific_charge, compton_wavelength)
            VALUES (%s, %s, %s);
        ''', (particle_name, specific_charge, compton_wavelength))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Ошибка при вставке записи: {e}")


def get_last_record():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM history ORDER BY id DESC LIMIT 1')
        last_record = cursor.fetchone()
        conn.close()
        return last_record
    except Exception as e:
        print(f"Ошибка при получении последней записи: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True)
