from flask import Flask, request, render_template

app = Flask(__name__)

def cifrario_di_cesare(parola, chiave):
    risultato = ""
    for carattere in parola:
        if carattere.isalpha():
            offset = ord('A') if carattere.isupper() else ord('a')
            risultato += chr(((ord(carattere) - offset + chiave) % 26) + offset)
        else:
            risultato += carattere
    return risultato

@app.route('/', methods=['GET', 'POST'])
def cifrare_parola():
    if request.method == 'POST':
        parola = request.form['parola']
        chiave = int(request.form['chiave'])
        parola_cifrata = cifrario_di_cesare(parola, chiave)
        return render_template('risultato.html', parola_cifrata=parola_cifrata)
    return render_template('cifrare.html')

if __name__ == '__main__':
    app.run()
