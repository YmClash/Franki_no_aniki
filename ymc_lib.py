import requests
import socket


def web_ip_adresse() :
    # envoyer une requête GET à un service d'adresse IP pour récupérer l'adresse IP publique
    url = input("URL : ")
    response = requests.get(url)
    # extraire l'adresse IP à partir de la réponse
    ip_adresse = response.text.strip()
    print(f"Votre adresse IP est : {ip_adresse}")


def ip_adresse() :
    # récupérer le nom d'hôte de l'ordinateur
    hostname = socket.gethostname()
    # récupérer l'adresse IP associée au nom d'hôte
    ip_adresse = socket.gethostbyname(hostname)
    print(f"Votre adresse IP est : {ip_adresse}")


def method_list(*args) :  # ce  *args  definit  que   on peux entre n'inport quel argument  a la fonction
    for method in dir(*args) :
        if '__' not in method :
            print(method)

def get_output_size(input_size, kernel_size, stride=1, padding=0) :
    return (input_size - kernel_size + 2 * padding) // stride + 1


input_size = 28
output_size = get_output_size(input_size, kernel_size=3)  # Conv1
output_size = get_output_size(output_size, kernel_size=3)  # Conv2
output_size = get_output_size(output_size, kernel_size=5)  # Conv3
output_size = get_output_size(output_size, kernel_size=5)  # Conv4

print(f"Output size after conv layers: {output_size}")
