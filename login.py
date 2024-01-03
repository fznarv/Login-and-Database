class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_key(self):
        with open('Login.txt', 'r') as file:
            file.seek(0)
            content = file.readlines()
            counter = 0
            number_of_tries = 3
            try:
                if not content:
                    number_of_tries -= 1

                    while counter < 3:
                        print(f'Login Failed! You have {number_of_tries} tries left.')
                        counter += 1
                        
                        if number_of_tries == 0:
                            print(f'You have {number_of_tries} tries left. Program exit.')
                            break
                        else:
                            Lwelcome = Login()

                            print(f'Welcome {Lwelcome.username}!')
                else:
            except FileNotFoundError:
                print('Wrong!')
               
            

