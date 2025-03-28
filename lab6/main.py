import tkinter as tk
from pack.particles import Electron, Proton, Neutron
import psycopg2
from openpyxl import Workbook

DB_CONFIG = {
    'host': 'localhost',
    'database': 'my_database',
    'user': 'postgres',
    'password': '1234'
}


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


def display_last_record(self):
    last_record = get_last_record()
    if last_record is not None:
        self.result_label.config(text=f"{last_record[1]}\n"
                                      f"Удельный заряд: {last_record[2]:.2e} Кл/кг\n"
                                      f"Комптоновская длина волны: {last_record[3]:.2e} м")


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Физические расчеты")
        self.geometry("1200x750")

        self.particle_var = tk.StringVar()
        self.particle_var.set("Выберите частицу")
        particle_menu = tk.OptionMenu(self, self.particle_var, "Электрон", "Протон", "Нейтрон")
        particle_menu.pack(pady=20)
        particle_menu.config(font='Times 20')

        calculate_button = tk.Button(self, text="Рассчитать", font='Times 20', command=self.calculate_properties)
        calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font='Times 20', justify=tk.LEFT)
        self.result_label.pack(padx=20, pady=(10, 0))

        save_xls_button = tk.Button(self, text="Сохранить в XLS", font='Times 20',
                                    command=lambda: create_report(self.result_label['text'], '.xls'))
        save_xls_button.pack(pady=10)

        display_last_record(self)

    def __repr__(self):
        return f"<MainWindow title='{self.title()}'>"

    def calculate_properties(self):
        create_database()
        selected_particle = self.particle_var.get()

        if selected_particle == "Электрон":
            particle = Electron()
        elif selected_particle == "Протон":
            particle = Proton()
        elif selected_particle == "Нейтрон":
            particle = Neutron()
        else:
            self.result_label.config(text="Не выбрана частица!")
            return

        result_text = f"{particle.name}\n" \
                      f"Удельный заряд: {particle.specific_charge:.2e} Кл/кг\n" \
                      f"Комптоновская длина волны: {particle.compton_wavelength:.2e} м"

        self.result_label.config(text=result_text)

        save_to_db(selected_particle, particle.specific_charge, particle.compton_wavelength)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()