from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="google-site-verification" content="-xFNFxrezSaFvZ0qpxFVttAg1am6XoTHKuabpVT9u0I" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Google Site Verification -->
        <meta name="google-site-verification" content="9c08015d60d6c7e8" />
        
        <title>Kalkulator Średniej – Profesjonalne Narzędzie</title>
        <meta name="description" content="Najlepszy darmowy kalkulator średniej ważonej, arytmetycznej i geometrycznej dla uczniów, studentów i nauczycieli w Polsce. Dokładność do 6 miejsc po przecinku.">
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #f4f7f9, #e8f4fd); color: #333; padding: 0; margin: 0; line-height: 1.6; }
            .container { max-width: 900px; margin: 0 auto; background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); margin-top: 20px; margin-bottom: 20px; }
            h1 { color: #1a73e8; font-size: 2.5em; text-align: center; margin-bottom: 10px; }
            h2 { color: #1557b0; font-size: 1.8em; border-left: 5px solid #1a73e8; padding-left: 20px; }
            a { color: #1a73e8; text-decoration: none; font-weight: bold; transition: color 0.3s; }
            a:hover { color: #0d47a1; }
            ul, ol { padding-left: 25px; }
            .cta { background: linear-gradient(45deg, #1a73e8, #42a5f5); color: white; padding: 20px; border-radius: 15px; text-align: center; margin: 30px 0; font-size: 1.3em; }
            .tools { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 40px; }
            .tool-card { background: #f8fbff; padding: 25px; border-radius: 12px; border-left: 5px solid #1a73e8; }
            .tool-card h3 { color: #1a73e8; margin-top: 0; }
            footer { text-align: center; margin-top: 60px; padding-top: 30px; border-top: 1px solid #eee; color: #777; font-size: 0.95em; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background: #f0f7ff; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Kalkulator Średniej – Profesjonalne Narzędzie</h1>
            <p style="font-size: 1.2em; text-align: center; color: #555;">Najlepszy darmowy kalkulator średniej ważonej, arytmetycznej, geometrycznej i harmonicznej dla uczniów, studentów i nauczycieli w Polsce. Dokładność do 6 miejsc po przecinku. Zgodny z systemem edukacji.</p>

            <div class="cta">
                <a style="color:white" href="https://kalkulatorsrednich.pl/" rel="dofollow" target="_blank">
                    Wypróbuj Kalkulator Średniej Teraz – Oblicz Średnią w 30 Sekund!
                </a>
            </div>

            <h2>Co czyni nas najlepszym?</h2>
            <table>
                <tr>
                    <th>Funkcja</th>
                    <th>Korzyść</th>
                </tr>
                <tr>
                    <td><strong>Dokładność do 6 miejsc po przecinku</strong></td>
                    <td>Sprawdzone matematycznie – zero błędów zaokrągleń</td>
                </tr>
                <tr>
                    <td><strong>Wagi jako % lub liczby</strong></td>
                    <td>Elastyczne – idealnie do ocen szkolnych i ECTS</td>
                </tr>
                <tr>
                    <td><strong>Automatyczna normalizacja wag</strong></td>
                    <td>Wpisz 2, 3, 5 → dostaniesz 20%, 30%, 50% jednym kliknięciem</td>
                </tr>
                <tr>
                    <td><strong>Obsługa ułamków i ocen opisowych</strong></td>
                    <td>4-, 3.5, 5+ – wszystko obsługiwane</td>
                </tr>
                <tr>
                    <td><strong>Eksport do PDF</strong></td>
                    <td>Zapisz wynik jako dokument do druku</td>
                </tr>
                <tr>
                    <td><strong>Historia obliczeń</strong></td>
                    <td>Przeglądaj ostatnie 10 wyników</td>
                </tr>
                <tr>
                    <td><strong>Tryb ciemny</strong></td>
                    <td>Oszczędność oczu podczas wieczornego korzystania</td>
                </tr>
                <tr>
                    <td><strong>Działa offline (PWA)</strong></td>
                    <td>Możliwość instalacji na telefonie i komputerze</td>
                </tr>
            </table>

            <h2>Jak to działa? (Krok po kroku)</h2>
            <ol style="font-size: 1.1em;">
                <li><strong>Wejdź na stronę:</strong> <a href="https://kalkulatorsrednich.pl/" rel="dofollow" target="_blank">Kalkulator Średniej</a></li>
                <li>Wybierz typ średniej (ważona / arytmetyczna / geometryczna / harmoniczna)</li>
                <li>Dodaj wiersze: Ocena + Waga (np. Matematyka 5 [waga 3])</li>
                <li>Kliknij „Oblicz" – wynik pojawia się natychmiast!</li>
                <li>Pobierz PDF, skopiuj wynik lub eksportuj do Excela</li>
            </ol>

            <h2>Przykłady zastosowania</h2>
            <ul style="font-size: 1.1em;">
                <li><strong>Uczniowie:</strong> Średnia z ocen z wagami (np. matematyka ×3, polski ×2)</li>
                <li><strong>Studenci:</strong> Średnia ECTS z przedmiotów o różnych punktach</li>
                <li><strong>Rodzice:</strong> Szybka weryfikacja średniej dziecka</li>
                <li><strong>Nauczyciele:</strong> Obliczenia klasowe i raporty</li>
            </ul>

            <h2>Inne profesjonalne narzędzia</h2>
            <div class="tools">
                <div class="tool-card">
                    <h3>🎮 Bottleneck Calculator</h3>
                    <p><strong>Zaawansowane narzędzie do analizy wydajności PC</strong> – wykrywa wąskie gardła (bottleneck) między CPU, GPU, RAM i dyskiem. Obsługuje:</p>
                    <ul>
                        <li>Automatyczne obrazy CPU/GPU z fallbackiem</li>
                        <li>Analizę gier i scenariuszy (Gaming, Streaming, Content Creation)</li>
                        <li>RAM i storage impact assessment</li>
                        <li>Multi-GPU, eGPU, eksport PDF/JSON</li>
                        <li>Lokalizacja (język i waluta)</li>
                    </ul>
                    <a href="https://bottlenackcalculator.com/" rel="dofollow" target="_blank">Wypróbuj Bottleneck Calculator</a>
                </div>
                <div class="tool-card">
                    <h3>🎉 BilalMania</h3>
                    <p><strong>50+ życzeń i GIF-ów na Nowy Rok 2026</strong> w 10 językach (EN, FR, DE, NL, PL, ES, IT, RU, AR, HI). Idealne do WhatsApp, Facebook, Instagram. Darmowe i bez rejestracji.</p>
                    <a href="https://www.bilalmania.com/happy-new-year-2026-gif/" rel="dofollow" target="_blank">Happy New Year 2026 Gif</a>
                </div>

                <div class="tool-card">
  <h3>🎉 BonneAnnee2026GIF</h3>
  <p><strong>Piękna kolekcja GIF-ów na Nowy Rok 2026</strong> w różnych stylach: eleganckie, zabawne, kolorowe i animowane. Idealne do wysyłania rodzinie i znajomym na WhatsApp, Facebook, Instagram. Darmowe pobieranie, bez rejestracji.</p>
  <a href="https://bonneannee2025gif.com/" rel="dofollow" target="_blank">Bonne Année 2026 GIF →</a>
</div>

                <div class="tool-card">
                    <h3>🔮 Destiny Matrix Free</h3>
                    <p><strong>Darmowa numerologia</strong>: matryca przeznaczenia, kompatybilność partnerska, lekcje karmiczne, rok osobisty, ścieżka duszy. Wszystko w jednym miejscu – bez opłat.</p>
                    <a href="https://destinymatrixfree.com/" rel="dofollow" target="_blank">Odkryj matrycę przeznaczenia</a>
                </div>
            </div>

            <h2>Kod źródłowy na GitHub</h2>
            <p>
                <a href="https://github.com/liveetcstream-beep/Kalkulator--redniej" target="_blank">
                    Zobacz repozytorium na GitHub (Python + Flask + Heroku)
                </a>
            </p>

            <h2>O autorce</h2>
            <p><strong>Dr inż. Marta Nowak</strong> – wykładowczyni matematyki stosowanej na Politechnice Krakowskiej, autorka 12 publikacji z zakresu statystyki edukacyjnej. Pasjonatka tworzenia narzędzi, które ułatwiają naukę i pracę.</p>

            <blockquote style="border-left: 5px solid #1a73e8; padding: 15px; background: #f0f7ff; font-style: italic; margin: 30px 0;">
                „Matematyka powinna być prosta i dostępna dla wszystkich. Dlatego tworzę narzędzia, które pomagają, a nie komplikują życie.”
            </blockquote>
        </div>

        <footer>
            <p>© 2026 | <a href="https://kalkulatorsrednich.pl/">Kalkulator Średniej</a> | z Heroku | <a href="https://github.com/liveetcstream-beep/Kalkulator--redniej">GitHub</a></p>
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=False)
