import customtkinter as ctk
import os

os.system('cls')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title("Calculadora de IMC")

titulo = ctk.CTkLabel(janela, text="Calculadora de IMC", font=("Arial", 20))
peso_label = ctk.CTkLabel(janela, text="Peso (kg):")
altura_label = ctk.CTkLabel(janela, text="Altura (m):")
IMC_result = ctk.CTkLabel(janela, text="Resultado IMC:")
text_result = ctk.CTkLabel(janela, text="")

campo_pes = ctk.CTkEntry(janela, width=100, placeholder_text="Kilogramas")
campo_alt = ctk.CTkEntry(janela, width=100, placeholder_text="Metros")

def calcular_IMC():
    try:
        peso = float(campo_pes.get())
        altura = float(campo_alt.get())
        if altura > 0  and peso > 0:
            result = peso / (altura * altura)
            if result < 17:
                text_result.configure(text=f"{result:.2f} - Muito abaixo do peso", text_color='white')
            elif 17 <= result < 18.5:
                text_result.configure(text=f"{result:.2f} - Abaixo do peso", text_color='yellow')
            elif 18.5 <= result < 24.9:
                text_result.configure(text=f"{result:.2f} - Peso normal", text_color='green')
            elif 25 <= result < 29.9:
                text_result.configure(text=f"{result:.2f} - Acima do peso", text_color='yellow')
            elif 30 <= result < 34.9:
                text_result.configure(text=f"{result:.2f} - Obesidade I", text_color='orange')
            elif 35 <= result < 39.9:
                text_result.configure(text=f"{result:.2f} - Obesidade II (severa)", text_color='red')
            else:
                text_result.configure(text=f"{result:.2f} - Obesidade III (mórbida)", text_color='red')
        else:
            text_result.configure(text="Altura deve ser maior que zero.", text_color='red')
    except ValueError:
        text_result.configure(text="Entrada inválida.", text_color='red')

btc_calc = ctk.CTkButton(janela, text="Calcular", command=calcular_IMC)

titulo.grid(row=0, column=0, columnspan=2, pady=20)
peso_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
campo_pes.grid(row=1, column=1, padx=10, pady=10)
altura_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
campo_alt.grid(row=2, column=1, padx=10, pady=10)
btc_calc.grid(row=3, column=0, columnspan=2, pady=20)
IMC_result.grid(row=4, column=0, padx=10, pady=10, sticky='e')
text_result.grid(row=4, column=1, padx=10, pady=10, sticky='w')

janela.mainloop()
