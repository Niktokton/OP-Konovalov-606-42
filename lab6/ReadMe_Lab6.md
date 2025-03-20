# Задача
Написать программу с графическим интерфейсом, расчитывающую удельный заряд и комптоновскую длину волны Электрона, Нейтрона и Протона. Добавить возможность сохранения в формате .doc или .xls. Сохранять результаты расчётов программы в БД. Использовать БД
## Решение: 
``` python
import tkinter as tk
from pack.particles import Electron, Proton, Neutron
import sqlite3
from openpyxl import Workbook


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
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            particle_type TEXT NOT NULL,
            specific_charge REAL,
            compton_wavelength REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def save_to_db(particle_name, specific_charge, compton_wavelength):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (particle_type, specific_charge, compton_wavelength)
        VALUES (?, ?, ?)
    ''', (particle_name, specific_charge, compton_wavelength))
    conn.commit()
    conn.close()


def get_last_record():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY id DESC LIMIT 1')
    last_record = cursor.fetchone()
    conn.close()
    return last_record


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
        self.geometry("400x250")

        self.particle_var = tk.StringVar()
        self.particle_var.set("Выберите частицу")
        particle_menu = tk.OptionMenu(self, self.particle_var, "Электрон", "Протон", "Нейтрон")
        particle_menu.pack(pady=20)

        calculate_button = tk.Button(self, text="Рассчитать", command=self.calculate_properties)
        calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", justify=tk.LEFT)
        self.result_label.pack(padx=20, pady=(10, 0))

        save_xls_button = tk.Button(self, text="Сохранить в XLS",
                                    command=lambda: create_report(self.result_label['text'], '.xls'))
        save_xls_button.pack(pady=10)

        display_last_record(self)

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
```
## Объяснение: 
Внутри constants.py находятся константы. В calculations.py расчёты заряда и длины волны. В particles.py общий класс Particle для частиц, а также дочерние класса дял Электрона, Протона и Нейтрона. Класс возвращает название, массу и заряд частицы. 
В main основной код программы. create_report сохраняет результат в .xls. create_database создаёт БД, используется единожды. save_to_db сохраняет в БД. get_last_record получает последнее значение из БД. display_last_record отображает последнее значение БД при запуске программы. 
class MainWindow - основной графический интерфейс. __init__ - база интерфейса. calculate_properties - вычисление.
## Скриншот:
![image](https://github.com/user-attachments/assets/83ab39cf-be7a-4341-99e3-dfe4f82b4845)
# Источники:
[Нейросеть ГигаЧат](https://giga.chat/gigachat/)
