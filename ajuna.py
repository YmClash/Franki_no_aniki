from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
import websocket

def main():
    # Remplacez l'URL ci-dessous par l'URL de votre propre nœud Substrate ou par un fournisseur d'API externe
    substrate = SubstrateInterface(
        url="ws://127.0.0.1",
        ss58_format=0,
        type_registry_preset='polkadot'
    )

    # Remplacez cette clé publique par celle du compte dont vous voulez vérifier le solde
    account_address = "bUMs9SouUoy36GFV4rzrUyVkKG1rTZkGBYrLMhbXUBumuTuck"

    try :
        # Récupérer les informations du compte
        account_info = substrate.query(
            module='System',
            storage_function='Account',
            params=[account_address]
        )

        if account_info :
            free_balance = account_info.value.get('data', {}).get('free', 0)
            print(f"Le solde du compte {account_address} est de {free_balance} units.")
        else :
            print(f"Impossible de récupérer les informations du compte {account_address}.")
    except SubstrateRequestException as e :
        print(f"Erreur lors de la récupération du solde : {str(e)}")

if __name__ == "__main__":
    main()


# address = ''
