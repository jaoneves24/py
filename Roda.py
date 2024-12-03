import tkinter as tk
import random
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Imagem Aleatória")

        self.label = tk.Label(root)
        self.label.pack(pady=20)

        self.label2 = tk.Label(root, font=("Helvetica", 48))
        self.label2.pack(pady=20)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.running = False

        # Lista de imagens
        self.imagens = [
            "image/dado.gif",  # Substitua pelo caminho da sua imagem
            "image/dado(1).gif",  # Substitua pelo caminho da sua imagem
            "image/dado(2).gif",  # Substitua pelo caminho da sua imagem
            "image/dado(3).gif",  # Substitua pelo caminho da sua imagem
            "image/dado(4).gif",  # Substitua pelo caminho da sua imagem
            "image/dado(5).gif",  # Substitua pelo caminho da sua imagem
        ]

    def start(self):
        self.running = True
        self.update_image()

    def update_image(self):
        if self.running:
            # Seleciona uma imagem aleatória
            self.imagem_path = random.choice(self.imagens)
            imagem = Image.open(self.imagem_path)
            imagem = imagem.resize((200, 200))  # Redimensiona a imagem
            self.imagem_tk = ImageTk.PhotoImage(imagem)  # Converte para um formato que o Tkinter pode usar
            self.label.config(image=self.imagem_tk)  # Atualiza o label com a nova imagem
            self.root.after(100, self.update_image)  # Chama esta função novamente após 1 segundo

    def stop(self):
        self.running = False

        # Exibe uma mensagem de vitória ou derrota
        if self.imagem_path in [ "image/dado.gif",  # Substitua pelo caminho da sua imagem
                            "image/dado(1).gif",  # Substitua pelo caminho da sua imagem
                            "image/dado(2).gif",]: # Verifica a imagem atual
            self.label2.config(text="Você perdeu!")
        else:
            self.label2.config(text="Você ganhou!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()