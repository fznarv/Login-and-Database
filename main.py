def data_delete(file_name, Data_number):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        if Data_number > len(lines) or Data_number == 0:
            print('Data not found')
            return
        
        with open(file_name, 'w') as file:
            for i, line in enumerate(lines, 1):
                if i != Data_number:
                    file.write(line)
        print(f'Data #{Data_number} has been deleted.')
    except FileNotFoundError:
        print('Data not found!')

        
file_name = 'info.txt'

while True:
    try:
        print('A. ENTER A DATA | B. REVIEW ALL DATA | C. DELETE A DATA | D. EXIT PROGRAM')
        input_choice = input('Input: ')
        input_choice.lower()
        if input_choice == 'a':
            Nname = input('Input name: ')
            try:
                Aage = int(input('Enter Age: '))
            except ValueError:
                print('Invalid input. please enter age.')

            Aaddress = input('Enter Address: ')
            with open('info.txt', 'a') as file:
                file.write(f'{Nname} {Aage} {Aaddress}')
                print('Data Added!')
                continue

        elif input_choice == 'b':
            with open('info.txt', 'r') as file:
                content = file.readlines()
                if not content:
                    print('No Data found.')
                else:
                    print('{:<15} {:<15} {:<15} {:<15} '.format('Data#', 'Name', 'Age', 'Address'))
                    for i, line in enumerate(content, 1):
                        columns = line.strip().split()
                        Data_number, Nname, Aage, Aaddress = str(i), columns[0], columns[1], ' '.join(columns[2:])
                        print('{:<15} {:<15} {:<15} {:<15}'.format(Data_number, Nname, Aage, Aaddress))
                    print()
                    continue

        elif input_choice == 'c':
            with open('info.txt', 'r') as file:
                content = file.readlines()
                if not content:
                    print('No data found.')
                else:
                    while True:
                        try:
                            Data_number = int(input('Enter Data#: '))
                            if Data_number == 0:
                                break
                            else:
                                data_delete(file_name, Data_number)
                                break
                        except ValueError:
                            print('Please enter Data#.')

        elif input_choice == 'd':
            print('Exit Program')
            break
        else:
            print('Invalid input! please chooise between A-D only.') 
    except:
        pass