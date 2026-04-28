# IVS Projekt 2 - Kalkulačka a Matematická knižnica

Tento projekt bol vytvorený v rámci predmetu **Praktické aspekty vývoja softwaru (IVS)** na FIT VUT v Brne. Jedná sa o návrh a implementáciu softvérovej kalkulačky s grafickým používateľským rozhraním, profilovaním a automatizovaným testovaním.

Prostredie
----------
Ubuntu 64bit

Autori
------
Segedínsky Guláš

- xhulinj00 Jakub Hulín
- xrybarr00 Ronnie Rybarik
- xrzeszm00 Marek Rzeszoto
- xvercim00 Michal Verčík

## Popis projektu
Súčasťou repozitára je:
* Implementácia matematickej knižnice (`math_lib.py`) s podporou základných aj pokročilých operácií (vrátane goniometrických funkcií).
* Grafické používateľské rozhranie kalkulačky napísané v Pythone pomocou knižnice `customtkinter` (`calc.py`).
* Skript pre výpočet smerodajnej odchýlky slúžiaci na profilovanie (`stddev.py`).
* Automatizované testy matematickej knižnice pomocou `unittest` (`math_test.py`).
* Inštalátor pre OS Linux (Debian/Ubuntu) umiestnený v zložke `installation/`.
* Mockupy a návrhy dizajnu v zložke `mockup/`.

## Inštalácia
Pre inštaláciu aplikácie v prostredí Linux (Ubuntu/Debian) najprv aktualizujte systém a následne nainštalujte pripravený inštalátor zo zložky `installation/`:

```bash
sudo apt update && sudo apt upgrade
sudo apt install ./installation/calculator_1.0_amd64.deb
```

Licencia
--------
Tento projekt je slobodný softvér: môžete ho šíriť a upravovať
podľa podmienok licencie GNU General Public License, ako ju
zverejnila Nadácia pre slobodný softvér (Free Software Foundation),
a to verzie 3 tejto licencie.

Tento program je distribuovaný v nádeji, že bude užitočný, ale bez
akejkoľvek záruky, dokonca aj bez predpokladanej záruky predajnosti
alebo vhodnosti pre daný účel. Podrobnosti nájdete v licencii GNU
General Public License.

Použité knižnice (CustomTkinter):
---------------------------------
Tento projekt využíva pre grafické používateľské rozhranie knižnicu 
CustomTkinter, ktorá je licencovaná pod MIT licenciou.

- Zdrojový kód CustomTkinter je dostupný na https://github.com/TomSchimansky/CustomTkinter

Celé znenie licencií:
---------------
Úplné znenie licencií nájdete na adrese:
- GNU General Public License v3: https://www.gnu.org/licenses/gpl-3.0
- MIT License: https://opensource.org/licenses/MIT
