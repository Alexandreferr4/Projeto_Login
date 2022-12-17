
# Classe de Usuário
class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    # Função responsável pela criação da instâcia
    @staticmethod
    def createUser(users: list[dict], name, email, password):
        if email not in users.keys():
            users[email] = User(name, email, password)

    # Classe responsável pelas mesnagens
    class Log:
        EXISTING_EMAIL = 'E-mail já existente!'
        INVALID_PASSWORD = 'Senha inválida!'
        EMAIL_NOT_FOUND = 'E-mail não cadastrado!'
        USER_LOGGED = 'Usuário logado! Realize o logoff e tente novamente!'
        UNMATCH_PASSWORD = 'Senhas não correspondentes!'
        USER_NOT_LOGGED = 'Nenhum usuário logado!'
        LOGOFF = 'Logoff realizado com sucesso!'

# Validações Login
def checkLogin(loginStatus, email, password):
    if loginStatus == None:
        if email in users.keys():
            if password != users[email].password:
                return User.Log.INVALID_PASSWORD

            else:
                return True

        elif email not in users.keys():
            return User.Log.EMAIL_NOT_FOUND

    else:
        return User.Log.USER_LOGGED

# Validações Cadastro
def checkSingup(email, password, password2):
    if email not in users.keys():
        if password == password2:
            return True
        
        else:
            return User.Log.UNMATCH_PASSWORD

    else:
        return User.Log.EXISTING_EMAIL

# Checa o status de login
def checkStauts(loginStatus):
    if loginStatus == None:
        print(User.Log.USER_NOT_LOGGED)
    
    else:
        print(
            f'\nUsuário logado:\n'
            f'Nome: {users[loginStatus].name}\n'
            f'E-mail: {users[loginStatus].email}'
        )

# Login
def login(loginStatus):
    if loginStatus != None:
        print(User.Log.USER_LOGGED)
        return

    email = input("Digite o email: ")
    password = input("Digite a senha: ")

    loginCheck = checkLogin(loginStatus, email, password)

    if loginCheck == True:
        print("\nLogin realizado com sucesso!")
        loginStatus = email

    else:
        print("\nNão foi possível realizar o login!")
        print(loginCheck)
    
    return loginStatus

# Logoff
def logoff(loginStatus):
    if loginStatus != None:
        print(User.Log.LOGOFF)
        loginStatus = None
        return loginStatus
    
    else:
        print(User.Log.USER_NOT_LOGGED)
        
# Cadastro
def singup():
    name = input("Digite o nome: ")
    email = input("Digite o email a ser cadastrado: ")
    password = input("Digite a senha: ")
    password2 = input("Confirme a senha: ")

    singupCheck = checkSingup(email, password, password2)

    if singupCheck == True:
        User.createUser(users, name, email, password)
        print("\nCadastro realizado com sucesso")

    else:
        print("\nNão foi possível realizar o cadastro!")
        print(singupCheck)


# Rotina
users = {}
loginStatus = None
WELCOME_MSG = (
    '\n#Bem-vindo a plataforma da Oliveira Trade!\n'
    'Para realizar Sing in ou Sing up em nossa plataforma,\n'
    'basta seguir as instruções abaixo.'
)
print(WELCOME_MSG)
while True:
    print(
        '\nDigite um comando:\n'
        'login  -> Realizar login\n'
        'singup -> Realizar cadastro\n'
        'logoff -> Realizar logoff\n'
        'status -> Checar status\n'
        'exit   -> Sair\n'
    )
    cmd = input()
    print('\n')

    if cmd == 'exit': break

    elif cmd == 'login':
        loginStatus = login(loginStatus)

    elif cmd == 'singup':
        singup()

    elif cmd == 'logoff':
        loginStatus = logoff(loginStatus)
        ...

    elif cmd == 'status':
        checkStauts(loginStatus)
        