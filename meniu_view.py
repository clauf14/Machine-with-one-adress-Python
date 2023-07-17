import tkinter as tk

import tkinter.messagebox as messagebox

from functie_grad_2 import get_coefficients
from masina_cu_o_adresa import MasinaCuAdresa

masina = MasinaCuAdresa(90, 90)


def perform_operation(user_choice):
    # Implement the calculation logic for each option here
    if user_choice == 'Adunare':
        print("Operatia de adunare a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        programAdunare = [
            ('CIT', 0),  # Read input and store at memory location 0
            ('LOAD', 0),  # Load the first input into the accumulator
        ]
        for i in range(1, n):
            programAdunare.append(('CIT', i))  # Read input and store at memory location i
            programAdunare.append(('ADD', i))  # Add the value at memory location i to the accumulator

        programAdunare.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('TIP', n),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])
        masina.load_program(programAdunare)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'Scadere':
        print("Operatia de scadere a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        programScadere = [
            ('CIT', 0),  # Read input and store at memory location 0
            ('LOAD', 0),  # Load the first input into the accumulator
        ]

        for i in range(1, n):
            programScadere.append(('CIT', i))  # Read input and store at memory location i
            programScadere.append(('SUBTRACTION', i))  # Add the value at memory location i to the accumulator

        programScadere.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('TIP', n),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])

        masina.load_program(programScadere)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'Inmultire':
        print("Operatia de inmultire a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        programInmultire = [
            ('CIT', 0),  # Read input and store at memory location 0
            ('LOAD', 0),  # Load the first input into the accumulator
        ]
        for i in range(1, n):
            programInmultire.append(('CIT', i))  # Read input and store at memory location i
            programInmultire.append(('MUL', i))  # Add the value at memory location i to the accumulator

        programInmultire.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('TIP', n),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])
        masina.load_program(programInmultire)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'Impartire':
        print("Operatia de impartire a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        programImpartire = [
            ('CIT', 0),  # Read input and store at memory location 0
            ('LOAD', 0),  # Load the first input into the accumulator
        ]
        for i in range(1, n):
            programImpartire.append(('CIT', i))  # Read input and store at memory location i
            programImpartire.append(('DIVISION', i))  # Add the value at memory location i to the accumulator

        programImpartire.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('TIP', n),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])
        masina.load_program(programImpartire)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'Radical':
        print("Operatia de radical a fost selectata!")
        programRadical = [
            ('CIT', 0),  # Read input and store at memory location 0
            ('LOAD', 0),  # Load the first input into the accumulator
            ('SQRT', 0),
            ('STORE', 1),  # Store the accumulator value at memory location n
            ('TIP', 1),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ]
        masina.load_program(programRadical)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'MediaAritmetica':
        print("Operatia pentru media aritmetica a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        masina.set_data_memory(0, n)
        programMA = [
            ('CIT', 1),  # Read input and store at memory location 0
            ('LOAD', 1),  # Load the first input into the accumulator
        ]
        for i in range(2, n + 1):
            programMA.append(('CIT', i))  # Read input and store at memory location i
            programMA.append(('ADD', i))  # Add the value at memory location i to the accumulator

        programMA.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('LOAD', n),
            ('STORE', n + 1),
            ('DIVISION', 0),
            ('STORE', n + 1),
            ('TIP', n + 1),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])
        masina.load_program(programMA)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'MediaGeometrica':

        print("Operatia pentru media geometrica a fost selectata!")
        n = 2
        masina.set_data_memory(0, n)

        programMG = [
            ('CIT', 1),  # Read input and store at memory location 0
            ('LOAD', 1),  # Load the first input into the accumulator
        ]

        for i in range(2, n + 1):
            programMG.append(('CIT', i))  # Read input and store at memory location i
            programMG.append(('MUL', i))  # Add the value at memory location i to the accumulator

        programMG.extend([
            ('STORE', n),  # Store the accumulator value at memory location n
            ('LOAD', n),
            ('STORE', n + 1),
            ('SQRT', n),
            ('STORE', n + 1),
            ('TIP', n + 1),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])

        masina.load_program(programMG)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'Factorial':

        print("Operatia pentru factorialul unui numar a fost selectata!")
        n = int(input("Enter the value of 'n': "))
        masina.set_data_memory(0, n)
        programFactorial = [
            ('LOAD', 0),  # Load the first input into the accumulator
        ]
        for i in range(2, masina.get_data_memory(0) + 1):
            masina.set_data_memory(i, i - 1)
            programFactorial.append(('MUL', i))

        programFactorial.extend([
            ('STORE', masina.get_data_memory(0)),  # Store the accumulator value at memory location n
            ('TIP', masina.get_data_memory(0)),  # Print the value at memory location n
            ('STOP', 0),  # Stop execution
        ])
        masina.load_program(programFactorial)
        masina.execute_program()
        masina.print_memory()
        input()

    elif user_choice == 'Modulo':
        print("Operatia pentru modulo a fost selectata!")
        programModulo = [
            ('CIT', 1),
            ('CIT', 2),
            ('LOAD', 1),  # Load the first input into the accumulator
            ('DIVISION', 2),
            ('STORE', 4),
            ('PARTINT', 4),
            ('STORE', 5),  # Store the accumulator value at memory location n  AICI AM [n/m]
            ('LOAD', 5),
            ('MUL', 2),
            ('STORE', 6),  # aici e m * [n/m]
            ('LOAD', 1),
            ('SUBTRACTION', 6),
            ('STORE', 7),
            ('TIP', 7),
            ('STOP', 0),  # Stop execution
        ]
        masina.load_program(programModulo)
        masina.execute_program()
        masina.print_memory()
        input()

    elif user_choice == 'EcuatieGrad1':
        print("Operatia pentru ecuatia de gradul 1 a fost selectata!")
        programEcuatieGrad1 = [
            ('CIT', 1),  # Read input value 1 and store it
            ('CIT', 2),  # Read input value 2 and store it
            ('CIT', 3),  # Read input value 3 and store it
            ('LOAD', 3),
            ('SUBTRACTION', 2),
            ('STORE', 4),
            ('DIVISION', 1),
            ('STORE', 5),
            ('TIP', 5),
            ('STOP', 0)
        ]
        masina.load_program(programEcuatieGrad1)
        masina.execute_program()
        masina.print_memory()

    elif user_choice == 'EcuatieGrad2':
        print("Operatia pentru ecuatia de gradul 1 a fost selectata!")
        programFunctieDeGrad2 = [
            ('CIT', 84),
            ('CIT', 85),
            ('CIT', 86),
            ('LOAD', 84),
            ('MUL', 2),
            ('STORE', 87),
            ('LOAD', 0),
            ('SUBTRACTION', 85),
            ('DIVISION', 89),
            ('STORE', 87),
            ('LOAD', 89),
            ('MUL', 2),
            ('MUL', 86),
            ('STORE', 88),
            ('LOAD', 84),
            ('MUL', 85),
            ('SUBTRACTION', 88),
            ('DIVISION', 89),
            ('DIVISION', 89),
            ('GREATER', 62),
            ('EQUAL', 56),
            # ('TIP', 87),
            ('LOAD', 0),
            ('SUBTRACTION', 88),
            ('STORE', 88),
            ('SQRT', 88),
            ('STORE', 88),
            # ('TIP', 88),
            ('STOP', 0),
            # ('TIP', 87),
            ('STOP', 0),
            ('SQRT', 88),
            ('STORE', 88),
            ('LOAD', 87),
            ('SUBTRACTION', 88),
            ('STORE', 89),
            # ('TIP', 89),
            ('LOAD', 87),
            ('ADD', 88),
            ('STORE', 89),
            ('TIP', 89),
            ('STOP', 0)
        ]
        masina.load_program(programFunctieDeGrad2)
        masina.execute_program()
        masina.print_memory()
        print(get_coefficients(masina.get_data_memory(84), masina.get_data_memory(85), masina.get_data_memory(86)))

    elif user_choice == 'SumaCif':
        print("Operatia pentru suma cifrelor unui numar a fost selectata!")
        programSumaCif = [
            ('CIT', 0),
            ('LOAD', 0),  # A <- data_memory[0]
            ('SUMCIF', 0),  # Calculează suma cifrelor numărului
            ('STORE', 1),  # data_memory[1] <- A
            ('TIP', 1),  # Afișează suma cifrelor
            ('STOP', 0)  # Oprește execuția programului
        ]
        masina.load_program(programSumaCif)
        masina.execute_program()
        masina.print_memory()


def create_interface():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x400")

    def exit_program():
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if result == "yes":
            window.destroy()

    def handle_restart():
        # Restart the application by destroying the current window and creating a new one
        window.destroy()
        create_interface()

    menu_bar = tk.Menu(window)
    entry_frame = tk.Frame(window)
    entry_frame.pack()

    label = tk.Label(entry_frame, text="Introdu numele operatiei:")
    label.pack(side=tk.LEFT)
    label.configure(pady=20)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Restart", command=handle_restart)
    file_menu.add_command(label="Exit", command=exit_program)
    menu_bar.add_cascade(label="Options", menu=file_menu)
    window.config(menu=menu_bar)

    entry = tk.Entry(entry_frame)
    entry.pack(side=tk.LEFT)

    def handle_button_click():
        user_choice = entry.get()
        perform_operation(user_choice)

    button = tk.Button(window, text="Calculeaza", command=handle_button_click)
    button.pack()
    button.configure(padx=10, bg="red", fg="white", activebackground="green")

    result_label = tk.Label(window, text="")
    result_label.pack()

    label_text = ["1.Adunare", "2.Scadere", "3.Inmultire", "4.Impartire", "5.Radical",
                  "6.MediaAritmetica", "7.MediaGeometrica", "8.Factorial", "9.Modulo",
                  "10.EcuatieGrad1", "11.SumaCif", "12.EcuatiaDeGrad2"]

    labels = []
    for text in label_text:
        label = tk.Label(window, text=text)
        label.pack()
        labels.append(label)

    window.mainloop()


# Main program
create_interface()
