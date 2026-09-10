
from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Empresa: ")
    stage = input("Etapa de vendas: ")

    # Verifique e valide os campos
    #depois modelar os dados
    #os leads serao estruturados como dict
    print(model_lead(name,email,company,stage))
    #com os dados modelado enviar para o DB
    #para isso vamos usar os metodos criados no control
    control.create_lead(model_lead(name,email,company,stage))

def list_leads():
    leads = control.list_leads()
    print(leads)

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar leads")
        print("[2] Listar leads")
        print("[3] Sair do programa")


        opt = input("Escolha uma opçao: ")
        if opt == "1":
            add_lead()
            print("Lead adicionado")
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Ate mais..")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()