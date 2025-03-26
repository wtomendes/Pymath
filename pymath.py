import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import pygame
import os
import time
import threading
import webbrowser

_icons = []
should_play_background = True
should_flash = True

# Usando caminhos relativos
current_dir = os.path.dirname(os.path.abspath(__file__))
sounds_dir = os.path.join(current_dir, "sounds")

MUSIC_PATH = os.path.join(sounds_dir, "background_music..wav")
CLICK_SOUND_PATH = os.path.join(sounds_dir, "click.wav")
DEVIL_SOUND_PATH = os.path.join(sounds_dir, "devil.wav")
SOUNDTRACK_PATH = os.path.join(sounds_dir, "soundtrack.mp3")

pygame.mixer.init()

try:
    click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)
    click_sound.set_volume(1.0)
    devil_sound = pygame.mixer.Sound(DEVIL_SOUND_PATH)
    devil_sound.set_volume(1.0)
    soundtrack = pygame.mixer.Sound(SOUNDTRACK_PATH)
    soundtrack.set_volume(1.0)
    devil_channel = pygame.mixer.Channel(1)
    soundtrack_channel = pygame.mixer.Channel(2)
except Exception as e:
    print(f"Erro ao carregar sons: {str(e)}")
    click_sound = None
    devil_sound = None
    soundtrack = None
    devil_channel = None
    soundtrack_channel = None

def play_click_sound():
    try:
        if click_sound:
            click_sound.play()
    except Exception as e:
        print(f"Erro ao tocar som de clique: {str(e)}")

def play_devil_sound():
    try:
        if devil_sound and devil_channel:
            devil_channel.play(devil_sound)
    except Exception as e:
        print(f"Erro ao tocar som do diabo: {str(e)}")

def play_soundtrack_loop():
    try:
        if soundtrack and soundtrack_channel:
            soundtrack_channel.play(soundtrack, loops=-1)
    except Exception as e:
        print(f"Erro ao tocar soundtrack: {str(e)}")

def flash_red():
    def toggle_red():
        if root.winfo_exists() and should_flash:
            if root.cget("bg") == "red":
                root.configure(bg="#49769e")
                for widget in root.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.configure(bg=button_color if widget.cget("text") not in ['C', '/', '*', '-', '+', '=', '0'] else symbol_color)
                    elif isinstance(widget, tk.Entry):
                        widget.configure(bg="#ffe483")
                    elif isinstance(widget, tk.Label):
                        widget.configure(bg="#306998")
            else:
                root.configure(bg="red")
                for widget in root.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.configure(bg="#ff4444")
                    elif isinstance(widget, tk.Entry):
                        widget.configure(bg="#ffcccc")
                    elif isinstance(widget, tk.Label):
                        widget.configure(bg="#cc0000")
            root.after(500, toggle_red)

    toggle_red()

def stop_flash_and_stay_red():
    global should_flash
    should_flash = False
    root.configure(bg="red")
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(bg="#ff4444")
        elif isinstance(widget, tk.Entry):
            widget.configure(bg="#ffcccc")
        elif isinstance(widget, tk.Label):
            widget.configure(bg="#cc0000")

def check_warning_closed():
    if root.winfo_exists():
        stop_flash_and_stay_red()

def play_background_music():
    try:
        print("Iniciando música...")
        print(f"Verificando arquivo: {MUSIC_PATH}")
        
        if not os.path.exists(MUSIC_PATH):
            print(f"ERRO: Arquivo não encontrado em: {MUSIC_PATH}")
            return
            
        print("Arquivo encontrado, inicializando mixer...")
        
        print("Mixer inicializado, carregando música...")
        
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        
        print("Música iniciada com sucesso!")
        
        time.sleep(10)
        
        pygame.mixer.music.stop()
        print("Música parada após 10 segundos")
        
    except Exception as e:
        print(f"ERRO ao tocar música: {str(e)}")

def play_music_loop():
    global should_play_background
    while should_play_background:
        play_background_music()
        time.sleep(1)

def calcular():
    global should_play_background
    try:
        expressao = entry.get()
        if expressao == "666+666":
            should_play_background = False
            pygame.mixer.music.stop()
            play_soundtrack_loop()
            play_devil_sound()
            flash_red()
            label_resultado.config(text="YOU ARE NOW FATED TO ETERNAL DAMNATION", fg="red", font=("Consolas", 16, "bold"))
            messagebox.showwarning("WARNING", "YOU HAVE SUMMONED THE DARK FORCES!")
            root.after(100, check_warning_closed)
        elif expressao == "1+1":
            should_play_background = False
            pygame.mixer.music.stop()
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=7SmsRcslz8fYpWkZ")
            label_resultado.config(text="Never gonna give you up!", fg="#ff69b4", font=("Consolas", 16, "bold"))
        else:
            resultado = eval(expressao)
            label_resultado.config(text="Resultado: " + str(resultado), fg="white", font=("Consolas", 16))
    except:
        messagebox.showerror("Erro", "Expressão inválida!")

root = tk.Tk()
root.title("Pymath")
root.configure(bg="#49769e")

root.resizable(False, False)

try:
    img = Image.open(os.path.join(current_dir, "pyculator.png"))
    sizes = [(32,32), (48,48), (64,64), (128,128), (256,256), (512,512)]
    for size in sizes:
        resized = img.resize(size, Image.Resampling.LANCZOS)
        icon = ImageTk.PhotoImage(resized)
        _icons.append(icon)
    root.iconphoto(True, *_icons)
except:
    print("Não foi possível carregar o ícone")

entry = tk.Entry(root, width=20, font=("Consolas", 22), justify="right", bg="#ffe483", fg="#306998", relief="flat")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

label_resultado = tk.Label(root, text="Resultado: ", font=("Consolas", 16), bg="#306998", fg="white")
label_resultado.grid(row=1, column=0, columnspan=4, pady=5)

buttons = [
    ('C', 2, 0), ('/', 2, 1), ('*', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('=', 4, 3),
    ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('0', 5, 3)
]

def adicionar_botao(valor):
    play_click_sound()
    if valor == 'C':
        entry.delete(0, tk.END)
    elif valor == '=':
        calcular()
    else:
        entry.insert(tk.END, valor)

button_color = "#4B8BBE"
symbol_color = "#ffe483"

button_style = {
    'font': ('Consolas', 14, 'bold'),
    'width': 10,
    'height': 3,
    'relief': 'flat',
    'bd': 0,
    'padx': 10,
    'pady': 5,
    'cursor': 'hand2'
}

for (texto, linha, coluna) in buttons:
    if texto in ['C', '/', '*', '-', '+', '=', '0']:
        button = tk.Button(root, text=texto, bg=symbol_color, fg="black",
                          command=lambda valor=texto: adicionar_botao(valor),
                          **button_style)
    else:
        button = tk.Button(root, text=texto, bg=button_color, fg="white",
                          command=lambda valor=texto: adicionar_botao(valor),
                          **button_style)
    
    button.grid(row=linha, column=coluna, padx=5, pady=5)

music_thread = threading.Thread(target=play_music_loop, daemon=True)
music_thread.start()

root.mainloop() 