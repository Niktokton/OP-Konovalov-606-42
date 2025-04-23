import os
import random
import pygame
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import win32clipboard

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


class MemeGeneratorApp:
    def __init__(self):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FPS = FPS

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        self.IMAGE_FOLDER = 'img'
        self.TEXTS_FOLDER = 'texts/'
        self.SAVE_FOLDER = 'save/'
        os.makedirs(self.SAVE_FOLDER, exist_ok=True)

        self.DB_PATH = 'memes.db'
        self.setup_database()

        self.MOOD_OPTIONS = [
            'Без темы', 'IT',
            'Студенты', 'DnD',
            'Животные', 'Локальные'
        ]

        self.selected_mood = None
        self.meme_generated = False
        self.current_meme = None

        self.buttons = []
        self.create_button = None
        self.save_clipboard_button = None
        self.download_button = None

    def setup_database(self):
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mood TEXT
                )
            ''')
            conn.commit()
            conn.close()
        except Exception as e:
            raise DatabaseConnectionError(f"Ошибка подключения к базе данных: {e}")

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

        def handle_click(pos):
            for i, rect in enumerate(self.buttons):
                if rect.collidepoint(pos):
                    self.selected_mood = self.MOOD_OPTIONS[i]
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
                color = BLACK if self.selected_mood == self.MOOD_OPTIONS[i] else WHITE
                pygame.draw.rect(screen, color, rect)
                text_surface = font.render(self.MOOD_OPTIONS[i], True,
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

            if self.meme_generated:
                screen.blit(self.current_meme, (544, 320))

            pygame.display.flip()
            clock.tick(self.FPS)

    def load_random_line_from_file(self, file_path):
        try:
            with open(file_path, encoding="utf-8") as file:
                lines = file.readlines()
                if not lines:
                    raise EmptyTextFileError(f"Файл '{file_path}' пуст или не найден.")
                return random.choice(lines).strip()
        except FileNotFoundError:
            raise EmptyTextFileError(f"Файл '{file_path}' не найден.")

    def create_meme(self, image_path, text):
        original_image = Image.open(image_path).convert('RGBA')
        width, height = original_image.size

        new_height = height + 128
        new_image = Image.new('RGBA', (width, new_height), BLACK)
        new_image.paste(original_image, (0, 0))

        draw = ImageDraw.Draw(new_image)

        font_size = 48
        max_attempts = 10

        for attempt in range(max_attempts):
            font = ImageFont.truetype("arial.ttf", size=font_size)
            _, _, w, h = draw.textbbox((0, 0), text, font=font)

            if w <= width:
                break

            font_size -= 5

        x = (width - w) / 2
        y = height + (new_height - height - h) / 2

        draw.text((x, y), text, fill=WHITE, font=font)

        return new_image

    def show_meme_in_window(self, screen, img):
        self.current_meme = pygame.image.frombuffer(img.tobytes(), img.size, img.mode)
        self.meme_generated = True

    def generate_and_display_meme(self, screen):
        if self.selected_mood is None:
            raise NoMoodSelectedError("Сначала выберите настройку!")

        text_file = os.path.join(self.TEXTS_FOLDER, f"{self.selected_mood.lower()}.txt")
        random_text = self.load_random_line_from_file(text_file)

        images = [f for f in os.listdir(self.IMAGE_FOLDER)]
        if not images:
            raise MissingImagesFolderError("Нет изображений для создания мема.")

        image_path = os.path.join(self.IMAGE_FOLDER, random.choice(images))

        meme_image = self.create_meme(image_path, random_text)

        self.show_meme_in_window(screen, meme_image)

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM memes")
        count = cursor.fetchone()[0]
        next_number = count + 1

        filename = f'mem_{str(next_number).zfill(4)}.png'
        full_save_path = os.path.join(self.SAVE_FOLDER, filename)
        meme_image.save(full_save_path)
        print(f"Сохранено: {full_save_path}")

        cursor.execute("INSERT INTO memes (id, mood) VALUES (?, ?)", (next_number, self.selected_mood))
        conn.commit()
        conn.close()

    def save_to_clipboard(self):
        if not self.meme_generated:
            raise MemeNotGeneratedError("Мем ещё не создан.")

        pil_image = Image.frombytes(mode='RGBA',
                                    size=self.current_meme.get_size(),
                                    data=pygame.image.tostring(self.current_meme, 'RGBA'))

        bgrx_data = bytearray()
        pixels = pil_image.load()
        width, height = pil_image.size
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                bgrx_data.extend([b, g, r, 0])

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, bytes(bgrx_data))
        win32clipboard.CloseClipboard()

        print("Мем успешно скопирован в буфер обмена.")

    def download_meme(self):
        if not self.meme_generated:
            raise MemeNotGeneratedError("Мем ещё не создан.")

        pil_image = Image.frombytes(mode='RGBA',
                                    size=self.current_meme.get_size(),
                                    data=pygame.image.tostring(self.current_meme, 'RGBA'))

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM memes")
        last_id = cursor.fetchone()[0]
        conn.close()

        if last_id is None:
            raise RuntimeError("Ошибка: мем не найден в базе данных.")

        filename = f'mem_{str(last_id).zfill(4)}.png'
        downloads_folder = os.path.expanduser("~/Downloads")
        full_save_path = os.path.join(downloads_folder, filename)
        pil_image.save(full_save_path)
        print(f"Мем успешно скачался в {downloads_folder}.")

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
