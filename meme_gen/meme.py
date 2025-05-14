import os
import random
import shutil
import datetime
import pygame
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import tkinter as tk
from tkinter import filedialog

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000
FPS = 60


class NoMoodSelectedError(Exception):
    pass


class EmptyTextFileError(Exception):
    pass


class MissingImagesFolderError(Exception):
    pass


class DatabaseConnectionError(Exception):
    pass


class MemeNotGeneratedError(Exception):
    pass


class MemGen:
    def __init__(self, texts_folder, image_folder, db_path, save_folder):
        self.theme = None
        self.texts_folder = texts_folder
        self.image_folder = image_folder
        self.db_path = db_path
        self.save_folder = save_folder

    def select_random_text(self, mood):
        self.theme = mood
        text_file = os.path.join(self.texts_folder, f"{mood.lower()}.txt")
        with open(text_file, encoding="utf-8") as file:
            lines = file.readlines()
            return random.choice(lines).strip()

    def select_random_image(self):
        images = os.listdir(self.image_folder)
        return os.path.join(self.image_folder, random.choice(images))


def wrap_text(draw, text, font, max_width):
    words = text.split()
    current_line = ''
    wrapped_lines = []
    for word in words:
        test_line = current_line + word + ' '
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]
        if line_width > max_width:
            wrapped_lines.append(current_line.strip())
            current_line = word + ' '
        else:
            current_line += word + ' '
    if current_line.strip():
        wrapped_lines.append(current_line.strip())
    return wrapped_lines


class MemUp(MemGen):
    def add_text_to_image(self, image_path, text):
        original_image = Image.open(image_path).convert('RGBA')
        width, height = original_image.size

        text_area_height = 128
        new_height = height + text_area_height
        new_image = Image.new('RGBA', (width, new_height), (0, 0, 0))
        new_image.paste(original_image, (0, text_area_height))

        draw = ImageDraw.Draw(new_image)
        font = ImageFont.truetype("arial.ttf", size=26)

        wrapped_lines = wrap_text(draw, text, font, width)

        line_spacing = font.getbbox("A")[3]
        total_height = len(wrapped_lines) * line_spacing
        first_line_top = (text_area_height - total_height) / 2

        for idx, line in enumerate(wrapped_lines):
            _, _, line_right, line_bottom = draw.textbbox((0, 0), line, font=font)
            line_width = line_right - _
            x = (width - line_width) / 2
            y = first_line_top + idx * line_spacing
            draw.text((x, y), line, fill=(255, 255, 255), font=font)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM memes")
        count = cursor.fetchone()[0]
        next_number = count + 1

        filename = f'mem_{next_number:04d}.png'
        full_save_path = os.path.join(self.save_folder, filename)

        new_image.save(full_save_path)
        print(f"Сохранено: {full_save_path}")

        direction = "Up"
        cursor.execute("""
                    INSERT INTO memes (id, theme, direction, creation_date, filename, path)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (next_number, self.theme, direction, now, filename, full_save_path))
        conn.commit()
        conn.close()

        return new_image


class MemDown(MemGen):
    def add_text_to_image(self, image_path, text):
        original_image = Image.open(image_path).convert('RGBA')
        width, height = original_image.size

        text_area_height = 128
        new_height = height + text_area_height
        new_image = Image.new('RGBA', (width, new_height), (0, 0, 0))
        new_image.paste(original_image, (0, 0))

        draw = ImageDraw.Draw(new_image)
        font = ImageFont.truetype("arial.ttf", size=26)

        wrapped_lines = wrap_text(draw, text, font, width)

        line_spacing = font.getbbox("A")[3]
        total_height = len(wrapped_lines) * line_spacing
        last_line_bottom = height + (
                text_area_height - total_height) / 2

        for idx, line in enumerate(reversed(wrapped_lines)):
            _, _, line_right, line_bottom = draw.textbbox((0, 0), line, font=font)
            line_width = line_right - _
            x = (width - line_width) / 2
            y = last_line_bottom - idx * line_spacing
            draw.text((x, y), line, fill=(255, 255, 255), font=font)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM memes")
        count = cursor.fetchone()[0]
        next_number = count + 1

        filename = f'mem_{next_number:04d}.png'
        full_save_path = os.path.join(self.save_folder, filename)

        new_image.save(full_save_path)
        print(f"Сохранено: {full_save_path}")

        direction = "Down"
        cursor.execute("""
                    INSERT INTO memes (id, theme, direction, creation_date, filename, path)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (next_number, self.theme, direction, now, filename, full_save_path))
        conn.commit()
        conn.close()

        return new_image


class MemeGeneratorApp:
    def __init__(self):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FPS = FPS
        self.GREY = (128, 128, 128)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.IMAGE_FOLDER = 'img'
        self.TEXTS_FOLDER = 'texts/'
        self.SAVE_FOLDER = 'save/'
        os.makedirs(self.SAVE_FOLDER, exist_ok=True)

        self.DB_PATH = 'memes.db'
        self.setup_database()

        self.THEME_OPTIONS = ['Без темы', 'IT', 'Студенты', 'DnD', 'Животные', 'Локальные']

        self.selected_theme = None
        self.meme_generated = False
        self.current_meme = None

        self.buttons = []
        self.create_button = None
        self.save_clipboard_button = None
        self.download_button = None
        self.clear_cache_button = None

        self.mem_gen_up = MemUp(self.TEXTS_FOLDER, self.IMAGE_FOLDER, self.DB_PATH, self.SAVE_FOLDER)
        self.mem_gen_down = MemDown(self.TEXTS_FOLDER, self.IMAGE_FOLDER, self.DB_PATH, self.SAVE_FOLDER)

        self.confirm_clear_cache = False
        self.answer_confirm = None

        self.current_direction = None

        self.meme_visible = False

    def setup_database(self):
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    theme TEXT,
                    direction TEXT,          -- Новое поле: направление (Up или Down)
                    creation_date DATETIME, -- Новое поле: дата создания
                    filename TEXT,          -- Новое поле: имя файла
                    path TEXT               -- Новое поле: полный путь
                )
            ''')
            conn.commit()
            conn.close()
        except Exception as e:
            raise Exception(f"Ошибка подключения к базе данных: {e}")

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        columns = 3
        rows_per_column = 2
        button_width = 150
        button_height = 40
        padding_x = 20
        padding_y = 20

        start_x = (self.WINDOW_WIDTH - (columns * button_width + (columns - 1) * padding_x)) // 2
        start_y = 100

        for col in range(columns):
            for row in range(rows_per_column):
                index = col * rows_per_column + row
                btn_rect = pygame.Rect(start_x + col * (button_width + padding_x),
                                       start_y + row * (button_height + padding_y),
                                       button_width, button_height)
                self.buttons.append(btn_rect)

        self.create_button = pygame.Rect(self.WINDOW_WIDTH // 2 - 100, 250, 200, 40)

        self.save_clipboard_button = pygame.Rect(50, 400, 200, 40)

        self.download_button = pygame.Rect(50, 500, 200, 40)

        self.clear_cache_button = pygame.Rect(50, 600, 200, 40)

        def handle_click(pos):
            for i, rect in enumerate(self.buttons):
                if rect.collidepoint(pos):
                    self.selected_theme = self.THEME_OPTIONS[i]
                    break
            if self.create_button.collidepoint(pos):
                try:
                    self.generate_and_display_meme(screen)
                except Exception as e:
                    self.show_error_message(screen, str(e))
            elif self.save_clipboard_button.collidepoint(pos):
                try:
                    self.save_to_clipboard()
                except Exception as e:
                    self.show_error_message(screen, str(e))
            elif self.download_button.collidepoint(pos):
                try:
                    self.download_meme()
                except Exception as e:
                    self.show_error_message(screen, str(e))
            elif self.clear_cache_button.collidepoint(pos):
                self.confirm_clear_cache = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    handle_click(pos)

            screen.fill(GREY)

            pygame.draw.rect(screen, WHITE, (544, 320, 512, 640))

            font = pygame.font.SysFont(None, 36)
            text_surface = font.render("Выберите тему мема:", True, BLACK)
            screen.blit(text_surface, (10, 10))

            for i, rect in enumerate(self.buttons):
                color = BLACK if self.selected_theme == self.THEME_OPTIONS[i] else WHITE
                pygame.draw.rect(screen, color, rect)
                text_surface = font.render(self.THEME_OPTIONS[i], True,
                                           self.BLACK if color == self.WHITE else self.WHITE)
                screen.blit(text_surface, rect.topleft)

            pygame.draw.rect(screen, WHITE, self.create_button)
            text_surface = font.render("Создать мем", True, BLACK)
            screen.blit(text_surface, self.create_button.topleft)

            pygame.draw.rect(screen, GREY, self.save_clipboard_button)
            text_surface = font.render("Сохранить в буфер обмена", True, BLACK)
            screen.blit(text_surface, self.save_clipboard_button.topleft)

            pygame.draw.rect(screen, GREY, self.download_button)
            text_surface = font.render("Скачать", True, BLACK)
            screen.blit(text_surface, self.download_button.topleft)

            pygame.draw.rect(screen, self.GREY, self.clear_cache_button)
            text_surface = font.render("Очистить кэш", True, self.BLACK)
            screen.blit(text_surface, self.clear_cache_button.topleft)

            if self.confirm_clear_cache:
                confirm_box = pygame.Rect(self.WINDOW_WIDTH // 2 - 150, self.WINDOW_HEIGHT // 2 - 50, 300, 100)
                pygame.draw.rect(screen, self.WHITE, confirm_box)
                pygame.draw.rect(screen, self.BLACK, confirm_box, 2)

                yes_btn = pygame.Rect(confirm_box.left + 50, confirm_box.top + 50, 80, 30)
                no_btn = pygame.Rect(confirm_box.right - 130, confirm_box.top + 50, 80, 30)

                pygame.draw.rect(screen, self.GREEN, yes_btn)
                pygame.draw.rect(screen, self.RED, no_btn)

                font = pygame.font.SysFont(None, 24)
                text_surface = font.render("Вы действительно хотите очистить кэш?", True, self.BLACK)
                screen.blit(text_surface,
                            (confirm_box.centerx - text_surface.get_width() // 2, confirm_box.centery - 30))

                text_surface = font.render("Да", True, self.BLACK)
                screen.blit(text_surface, yes_btn.midtop)

                text_surface = font.render("Нет", True, self.BLACK)
                screen.blit(text_surface, no_btn.midtop)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if yes_btn.collidepoint(mouse_pos):
                        self.clear_cache()
                        self.confirm_clear_cache = False
                    elif no_btn.collidepoint(mouse_pos):
                        self.confirm_clear_cache = False

            if self.meme_generated:
                screen.blit(self.current_meme, (544, 320))

            pygame.display.flip()
            clock.tick(self.FPS)

    def clear_cache(self):
        if os.path.exists(self.SAVE_FOLDER):
            shutil.rmtree(self.SAVE_FOLDER)
            os.makedirs(self.SAVE_FOLDER, exist_ok=True)

        if os.path.exists(self.DB_PATH):
            os.remove(self.DB_PATH)

        self.setup_database()

        self.meme_visible = False
        self.meme_generated = False
        self.current_meme = None

        print("Кэш успешно очищен.")

    def show_meme_in_window(self, screen, img):
        self.current_meme = pygame.image.frombuffer(img.tobytes(), img.size, img.mode)
        self.meme_generated = True

    def generate_and_display_meme(self, screen):
        if self.selected_theme is None:
            raise ValueError("Сначала выберите тему!")

        random_text = self.mem_gen_up.select_random_text(self.selected_theme)
        image_path = self.mem_gen_up.select_random_image()

        generator = random.choice([self.mem_gen_up, self.mem_gen_down])
        self.current_direction = "Up" if isinstance(generator, MemUp) else "Down"

        meme_image = generator.add_text_to_image(image_path, random_text)

        self.show_meme_in_window(screen, meme_image)

    def save_to_clipboard(self):
        pass

    def download_meme(self):
        if not self.meme_generated:
            raise MemeNotGeneratedError("Мем ещё не создан.")

        root = tk.Tk()
        root.withdraw()

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM memes")
        result = cursor.fetchone()
        conn.close()

        last_id = result[0] or 0

        default_filename = f"mem_{last_id:04d}"

        file_path = filedialog.asksaveasfilename(initialfile=f"{default_filename}.png",
                                                 defaultextension=".png",
                                                 initialdir=os.path.expanduser("~"),
                                                 title="Сохранить мем",
                                                 filetypes=(("PNG-файлы", "*.png"), ("Все файлы", "*.*")))

        if not file_path:
            return

        pil_image = Image.frombytes(mode='RGBA',
                                    size=self.current_meme.get_size(),
                                    data=pygame.image.tostring(self.current_meme, 'RGBA'))

        pil_image.save(file_path)
        print(f"Мем успешно сохранён в {file_path}.")

        direction = self.current_direction

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        filename = os.path.basename(file_path)

        full_path = file_path

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE memes SET
              theme = ?,
              direction = ?,
              creation_date = ?,
              filename = ?,
              path = ?
            WHERE id = ?
        """, (self.selected_theme, direction, now, filename, full_path, last_id))
        conn.commit()
        conn.close()

    def show_error_message(self, screen, message):
        font = pygame.font.SysFont(None, 36)
        error_surface = font.render(message, True, RED)
        screen.blit(error_surface, (10, 50))
        pygame.display.flip()
        pygame.time.wait(3000)


if __name__ == "__main__":
    app = MemeGeneratorApp()
    try:
        app.run()
    except Exception as e:
        print(e)
