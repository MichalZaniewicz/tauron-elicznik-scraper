# tauron-elicznik-scraper
Simple python3 script that outputs JSON with energy meter data from Tauron eLicznik service

1. Add login info and energy meter ID into script
2. Run with ```python3 elicznik.py```
3. Get JSON output with energy meter data from last day

Energy meter ID can be obtained from https://elicznik.tauron-dystrybucja.pl/ website under "Punkt poboru:" field.

Script is currently tested only with G11 tariff.

Optionally you can save JSON as file - just uncomment 3 last lines.

You can change dane[chartDay] to get data from another day (not only the last one).

If JSON should contain energy produced from solar panels, please change the [checkOZE] data from "Off" to "On".

Enjoy :)

![Example usage with Grafana](https://i.imgur.com/ysQwW3m.png)
