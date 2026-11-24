# Szuter Rally

Przeglądarkowa gra rajdowa na szutrze w 3D, w klimacie klasycznych rajdówek z przełomu wieków. Jeden plik HTML, Three.js z CDN, bez instalacji i bez serwera.

## Jak uruchomić

- Otwórz `index.html` w przeglądarce (najlepiej Chrome albo Edge, bo mają polski głos pilota).
- Albo włącz GitHub Pages dla gałęzi `main` (Settings → Pages → Deploy from branch → `main` / root) i graj pod adresem `https://<login>.github.io/szuter-rally/`.

## Co jest w grze

- **Fizyka rajdowa**: napęd 4×4, poślizgi i kontra, ręczny na nawroty, przenoszenie masy przy hamowaniu, mniejsza przyczepność na poboczu, hopy z prawdziwym lotem.
- **Pilot**: noty generowane z geometrii trasy („uwaga, prawy jeden i lewy cztery długi, sto”), czytane głosem i pokazane jak w roadbooku.
- **Przeszkody**: stalowe barierki z tablicami kierunkowymi na części szybkich zakrętów i pojedyncze drzewa tuż przy drodze. Pilot ostrzega: „drzewo na zewnątrz”.
- **Odcinki**: 4 stałe OS-y i losowy odcinek proceduralny; start z odliczaniem, dwa międzyczasy, rekordy zapisywane w przeglądarce.
- **Tryb rajdu**: 4 odcinki po kolei, 7 rywali, trzy poziomy trudności, klasyfikacja odcinka i generalna, zapis postępu.
- **Park serwisowy**: po każdym odcinku masz limit minut (20 / 60 / 20). Każda naprawa kosztuje czas, a minuta ponad limit to 10 s kary.
- **Uszkodzenia** z wpływem na jazdę:

  | Podzespół | Skutek |
  |---|---|
  | Silnik | spadek mocy, przerywanie, dym spod maski |
  | Skrzynia biegów | wolniejsza zmiana, gubienie biegów |
  | Zawieszenie | mniej przyczepności, auto przysiada i drży |
  | Układ kierowniczy | auto ściąga w bok, mniejszy skręt |
  | Nadwozie | większy opór, wgniecenia, odpadające zderzaki, spojler i chlapacze, pęknięta szyba, zgaszone lampy |
  | Opony | przebicie ściąga auto i odbiera przyczepność |

- **Wspomaganie jazdy** (menu lub pauza): *średnie* to auto-kontra, stabilizacja i kontrola trakcji; *pełne* dodaje hamowanie przed zakrętami i pomoc w trzymaniu drogi, za cenę wolniejszej jazdy.

## Sterowanie

| Klawisz | Akcja |
|---|---|
| ↑ / W | gaz |
| ↓ / S | hamulec, wsteczny |
| ← → / A D | skręt |
| Spacja | ręczny |
| C | kamera zza auta / z maski |
| R | powrót na drogę (+5 s) |
| Esc / P | pauza |
| V / M | pilot / dźwięk |

Działa też pad (lewa gałka, spusty, X/B ręczny) i dotyk na telefonie.

## Struktura

- `src/game.html` to źródło gry: fragment strony bez `<html>` i `<head>`, w tej postaci publikowany jako artefakt Claude.
- `index.html` to samodzielna strona zbudowana z `src/game.html`.
- `tools/build.py` buduje `index.html`: `python3 tools/build.py`.

Po każdej zmianie w `src/game.html` uruchom build, żeby zaktualizować `index.html`.

## Własna grafika (np. z Magnific)

Na początku skryptu w `src/game.html` jest obiekt `ASSETS` z miejscami na tekstury:

```js
const ASSETS = {
  gravel: null,   // nawierzchnia drogi
  grass:  null,   // trawa i teren
  sky:    null,   // panorama nieba (equirectangular)
  livery: null,   // malowanie boku auta (2:1)
};
```

Wpisz ścieżkę do pliku, np. `"tex/gravel.jpg"`. Przy `null` gra rysuje tekstury sama. Tekstury powinny być kafelkowe, 512–1024 px.
