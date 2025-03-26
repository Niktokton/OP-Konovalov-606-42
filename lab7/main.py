import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder

from pack.particles import Electron, Proton, Neutron
import psycopg2
from openpyxl import Workbook

DB_CONFIG = {
    'host': 'localhost',
    'database': 'my_database',
    'user': 'postgres',
    'password': '1234'
}

Builder.load_string("""
<MyWidget>:
    orientation: 'vertical'
    padding: 50
    spacing: 20

    Label:
        text: 'Выберите частицу:'
        size_hint_y: None
        height: dp(30)

    Spinner:
        id: spinner
        values: ['Электрон', 'Протон', 'Нейтрон']
        on_text: root.update_result()

    Button:
        text: 'Рассчитать'
        size_hint_y: None
        height: dp(60)
        on_release: root.calculate_properties()

    Label:
        id: result_label
        text: ''
        halign: 'left'
        valign: 'top'
        text_size: self.width, None
        size_hint_y: None
        height: dp(100)

    Button:
        text: 'Сохранить в XLS'
        size_hint_y: None
        height: dp(60)
        on_release: root.save_results('.xls')
""")


class MyWidget(BoxLayout):
    result_text = StringProperty('')
    spinner_value = ObjectProperty(None)

    def update_result(self):
        """Обновляем результат после выбора частицы"""
        if self.ids.spinner.text != 'Выберите частицу':
            self.result_text = f'{self.ids.spinner.text}'

    def calculate_properties(self):
        """Метод расчета свойств частиц"""
        create_database()
        selected_particle = self.ids.spinner.text  # Исправлено на self.ids.spinner.text

        if selected_particle == "Электрон":
            particle = Electron()
        elif selected_particle == "Протон":
            particle = Proton()
        elif selected_particle == "Нейтрон":
            particle = Neutron()
        else:
            self.ids.result_label.text = "Не выбрана частица!"
            return

        result_text = f"{particle.name}\n" \
                      f"Удельный заряд: {particle.specific_charge:.2e} Кл/кг\n" \
                      f"Комптоновская длина волны: {particle.compton_wavelength:.2e} м"

        self.ids.result_label.text = result_text
        save_to_db(selected_particle, particle.specific_charge, particle.compton_wavelength)

        result_text = f"{particle.name}\n" \
                      f"Удельный заряд: {particle.specific_charge:.2e} Кл/кг\n" \
                      f"Комптоновская длина волны: {particle.compton_wavelength:.2e} м"

        self.ids.result_label.text = result_text
        save_to_db(selected_particle, particle.specific_charge, particle.compton_wavelength)

    def save_results(self, file_format):
        """Метод сохранения результатов в формате .xls"""
        create_report(self.ids.result_label.text, file_format)

    def __repr__(self):
        return f"MyWidget(result_text={self.result_text}, spinner_value={self.spinner_value})"

    def __str__(self):
        return f"Result Text: {self.result_text}"


class MyApp(App):
    def build(self):
        return MyWidget()


def create_report(results, file_format):
    if file_format == ".doc":
        pass
    elif file_format == ".xls":
        workbook = Workbook()
        worksheet = workbook.active
        row = 1
        for line in results.split("\n"):
            column = 1
            worksheet[f"A{row}"].value = line
            row += 1
        workbook.save(f"results_{file_format}")


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
    MyApp().run()