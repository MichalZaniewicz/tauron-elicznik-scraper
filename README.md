# tauron-elicznik-scraper
Simple python3 script that outputs JSON with energy meter data from Tauron eLicznik service

1. Add login info and energy meter ID into script
2. Run
3. Get JSON with energy meter data from last day

Energy meter ID can be obtained from https://elicznik.tauron-dystrybucja.pl/ website under "Punkt poboru:" field.
Script currently supports only G11 tariff.

You can change dane[chartDay] to get data from another day (not only the last one).

Enjoy :)
