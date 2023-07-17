import math


class MasinaCuAdresa:
    def __init__(self, data_memory_size, stack_size):
        self.registri = {
            'A': 0,  # registrul acumulator
            'I': 0,  # registrul index
            'B': 0  # registrul de bază
        }
        self.program_memory = [0] * 256  # zona de memorie rezervată pentru program
        self.data_memory = [0] * data_memory_size  # zona de memorie rezervată pentru date
        self.stack_memory = [0] * stack_size  # zona de memorie rezervată pentru stivă
        self.stack_pointer = -1  # pointerul stivei, inițializat la -1
        self.program_counter = 0

    def load_program(self, program):
        """

        :rtype: object
        """
        address = 0
        for instruction in program:
            opcode, operand = instruction
            self.program_memory[address] = opcode
            self.program_memory[address + 1] = operand
            address += 2

    def print_memory(self):
        for i, value in enumerate(self.program_memory):
            if value != 0:
                print(f"Memory[{i}] = {value}")
                # print(f"test[{i}]")

    def run(self):
        self.execute_program()

    def set_register(self, register, value):
        self.registri[register] = value

    def get_register(self, register):
        return self.registri[register]

    def set_program_memory(self, address, instruction):
        if address < len(self.program_memory):
            self.program_memory[address] = instruction

    def get_program_memory(self, address):
        return self.program_memory[address]

    def set_data_memory(self, address, value):
        self.data_memory[address] = value

    def get_data_memory(self, address):
        return self.data_memory[address]

    def push_stack(self, value):
        if self.stack_pointer < len(self.stack_memory) - 1:
            self.stack_pointer += 1
            self.stack_memory[self.stack_pointer] = value
        else:
            raise Exception("Stack overflow")

    def pop_stack(self):
        if self.stack_pointer >= 0:
            value = self.stack_memory[self.stack_pointer]
            self.stack_pointer -= 1
            return value
        else:
            raise Exception("Stack underflow")

    def get_program_counter(self):
        return self.program_counter

    def set_program_counter(self, address):
        self.program_counter = address

    def execute_program(self):
        program_counter = 0
        while True:
            opcode = self.program_memory[program_counter]
            operand = self.program_memory[program_counter + 1]

            if opcode == 'A':
                self.registri['A'] = self.registri['A'] + self.data_memory[operand]
            elif opcode == 'S':
                self.registri['A'] = self.registri['A'] - self.data_memory[operand]
            elif opcode == 'M':
                self.registri['A'] = self.registri['A'] * self.data_memory[operand]
            elif opcode == 'L':
                self.registri['A'] = self.data_memory[operand]
            elif opcode == 'B':
                self.registri['B'] = self.registri['A']
            elif opcode == 'I':
                self.registri['I'] = operand
            elif opcode == 'P':
                value = self.pop_stack()
                self.registri['A'] = value
            elif opcode == 'D':
                value = self.registri['A']
                self.push_stack(value)
            elif opcode == 'LOAD':
                self.registri['A'] = self.data_memory[operand]  # Valoarea indicată de X se depune în registrul
                # acumulator A
            elif opcode == 'STORE':
                self.set_data_memory(operand, self.get_register('A'))  # Valoarea din registrul acumulator A se depune
                # in locaţia din zona de date indicată de X
            elif opcode == 'LOADI' or opcode == '←I ':
                self.registri['A'] = self.registri['I']  # Conţinutul registrului index I se depune în registrul
                # acumulator A
            elif opcode == 'STOREI' or opcode == '→I':
                self.registri['I'] = self.registri['A']  # Conţinutul registrului acumulator A se depune în registrul
                # index I
            elif opcode == 'LOADB' or opcode == '←B':
                self.registri['A'] = self.registri['B']  # Conţinutul registrului de bază B se depune în registrul
                # acumulator A
            elif opcode == 'STOREB' or opcode == '→B':
                self.registri['B'] = self.registri['A']  # Conţinutul registrului acumulator A se depune în
                # registru de bază B
            elif opcode == '↓':
                self.push_stack(self.data_memory[operand])  # Valoarea indicată prin X este depusă în vârful stivei;
                # numărul elementelor din stivă creşte cu 1
            elif opcode == '↑':
                value = self.pop_stack()  # Este extras elementul din vârful stivei şi este depus înlocaţia de date
                # indicată de X; numărul elementelor din stivă scade cu 1
                self.data_memory[operand] = value
            elif opcode == '↓':
                self.push_stack(self.registri['A'])  # Valoarea din registrul acumulator A este depusă în vârful stivei;
                # numărul elementelor din stivă creşte cu 1
            elif opcode == '↑':
                value = self.pop_stack()
                self.registri['A'] = value  # Este extras elementul din vârful stivei şi este depus în registrul
                # acumulator A; numărul elementelor din stivă scade cu 1
            elif opcode == 'ADD':
                self.registri['A'] = self.registri['A'] + self.data_memory[operand]  # Adunare A:=A+X
            elif opcode == 'SUBTRACTION':
                self.registri['A'] = self.registri['A'] - self.data_memory[operand]  # Scădere A:=A–X
            elif opcode == 'MUL':
                self.registri['A'] = self.registri['A'] * self.data_memory[operand]  # Inmulţire A:=A*X
            elif opcode == 'DIVISION' or opcode == '/':
                if self.data_memory[operand] != 0:
                    if self.data_memory[operand] != 0:
                        self.registri['A'] = self.registri['A'] / self.data_memory[operand]
                    else:
                        print("Error: Division by zero")
                        # Handle the error condition (e.g., set a default value, exit the program, etc.)
            elif opcode == 'SUMCIF':
                numar = self.data_memory[operand]
                suma = 0
                while numar > 0:
                    cifra = numar % 10
                    suma += cifra
                    numar = numar // 10
                self.registri['A'] = suma
            elif opcode == 'SQRT' or opcode == '√':
                self.registri['A'] = math.sqrt(self.data_memory[operand])  # Radical de ordin 2 A:=√X
            elif opcode == 'ABS' or opcode == '| |':
                self.registri['A'] = abs(self.data_memory[operand])  # Valoare absolută A:=|X|
            elif opcode == 'PARTINT' or opcode == '[ ]':
                self.registri['A'] = math.trunc(self.data_memory[operand])  # Partea întreagă A:=[X]
            elif opcode == 'SN':
                program_counter = self.program_memory[operand]  # adresa din zona de program indicată de X
            elif opcode == '<':
                if self.registri['A'] < 0:
                    program_counter = operand - 1  # Salt la X dacă A < 0
            elif opcode == '≤':
                if self.registri['A'] <= 0:
                    program_counter = operand - 1  # Salt la X dacă A ≤ 0
            elif opcode == 'GREATER':
                if self.registri['A'] > 0:
                    program_counter = operand
                    continue  # Salt la X dacă A > 0
            elif opcode == '≥':
                if self.registri['A'] >= 0:
                    program_counter = operand - 1  # Salt la X dacă A ≥ 0
            elif opcode == 'EQUAL':
                if self.registri['A'] == 0:
                    program_counter = operand
                    continue  # Salt la X dacă A = 0
            elif opcode == '≠':
                if self.registri['A'] != 0:
                    program_counter = operand - 1  # Salt la X dacă A ≠ 0
            elif opcode == 'ADR ':
                self.registri['A'] = operand  # Determină adresa (nu valoarea) din zona de date
                # a variabilei indicate de X şi depune această
                # adresă în registrul acumulator A
            elif opcode == 'CIT':
                value = int(input("Introdu valoarea numărului: "))
                self.data_memory[operand] = value  # Citeşte de la intrare valoarea unui număr şi o
                # depune în locaţia din zona de date indicată de X
            elif opcode == 'TIP':
                value = self.data_memory[operand]
                print("Valoarea numărului: ", value)  # Afişează la ieşire valoarea numărului aflat în
                # locaţia din zona de date indicată de X
            elif opcode == 'STOP':
                break  # Incheie execuţia programului (oprire)

            program_counter += 2
