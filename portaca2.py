import socket


def get_service_name(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Imposta il timeout per la connessione

    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            service_name = socket.getservbyport(port)
            return f"Port {port} is open. Service: {service_name}"
        else:
            return f"Port {port} is closed"
    except socket.error:
        return f"Port {port} is closed"
    finally:
        sock.close()


if __name__ == '__main__':
    target = input("Inserisci l'indirizzo IP del dispositivo da scansionare: ")
    port_to_check = int(input("Inserisci la porta che desideri verificare: "))

    try:
        result = get_service_name(target, port_to_check)
        print(result)
    except Exception as e:
        print(f"Errore: {e}")
