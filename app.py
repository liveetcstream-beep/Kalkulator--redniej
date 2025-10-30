from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kalkulator Średniej – Darmowe Narzędzie</title>
        <meta name="description" content="Oblicz średnią ważoną i arytmetyczną. Dla uczniów i nauczycieli w Polsce.">
        <style>
            body { font-family: Arial; background: #f4f7f9; color: #333; padding: 20px; }
            .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
            h1 { color: #1a73e8; }
            a { color: #1a73e8; font-weight: bold; }
            footer { text-align: center; margin-top: 50px; color: #777; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Kalkulator Średniej Online – 2025</h1>
            <p><strong>Najlepsze darmowe narzędzie do obliczania średniej ważonej i arytmetycznej.</strong></p>
            <p>Stworzone przez <strong>dr inż. Martę Nowak</strong>.</p>

            <h2>Wypróbuj teraz!</h2>
            <p style="font-size: 1.2em;">
                <a href="https://kalkulatorsrednich.pl/" rel="dofollow" target="_blank">
                    Przejdź do kalkulatora średniej
                </a>
            </p>

            <h2>Kod na GitHub</h2>
            <p>
                <a href="https://github.com/liveetcstream-beep/Kalkulator--redniej" target="_blank">
                    Zobacz repozytorium
                </a>
            </p>
        </div>

        <footer>
            <p>© 2025 | <a href="https://kalkulatorsrednich.pl/">Kalkulator Średniej</a> | DA 91 Backlink z Heroku</p>
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=False)
