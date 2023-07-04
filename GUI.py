import tkinter
from lexico import lexer as lx
from sintactico import sintactico as sx


def analisis_lexico():
    lexreturn = ''
    cadena = text_input.get("1.0", tkinter.END)
    s = cadena
    if s:
        lx.input(s)
        for tok in lx:
            lexreturn = lexreturn + str(tok) + '\n'
    return lexreturn

def analisis_sintactico():
    result = ''
    cadena = text_input.get("1.0", tkinter.END)
    s = cadena
    if s:
        sx.output = ''
        result = sx.parse(s)
    if sx.output:
        return str(sx.output)+str(result)
    else:
        return str(result)


def clear_input():
    text_input.delete("1.0", tkinter.END)
    text_output_lexico.delete("1.0", tkinter.END)
    text_output_semantico.delete("1.0", tkinter.END)
    text_output_sintactico.delete("1.0", tkinter.END)


def analisis():
    text_output_lexico.delete("1.0", "end")
    text_output_lexico.insert(tkinter.INSERT, analisis_lexico())
    text_output_sintactico.delete("1.0", "end")
    text_output_sintactico.insert(tkinter.INSERT, analisis_sintactico())


Window = tkinter.Tk()
Window.title("Analizador Rust")
Window.geometry("800x600")
Window.resizable(False, False)

mainLabel = tkinter.Label(Window, text="Analizador Rust", font=("Arial Bold", 20))
mainLabel.pack()

text_input = tkinter.Text(Window, height=20, width=100)
text_input.pack()

button = tkinter.Button(Window, text="Analizar", command=analisis)
button.pack()

button = tkinter.Button(Window, text="Limpiar", command=clear_input)
button.pack()

text_output_lexico = tkinter.Text(Window, height=10, width=100)
text_output_lexico.pack()

text_output_sintactico = tkinter.Text(Window, height=10, width=100)
text_output_sintactico.pack()

text_output_semantico = tkinter.Text(Window, height=10, width=100)
text_output_semantico.pack()

Window.mainloop()
