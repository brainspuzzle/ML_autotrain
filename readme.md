# Automatinio treniravimo įrankis SnapML šviesos šaltinių aptikimui 
Šis projektas leidžia aptikti šviesos šaltinius vaizduose, treniruoti modelį ir eksportuoti jį į ONNX formatą, 
## Projekto struktūra

* auto_training_tool/
* ├── data/
* │   ├── raw_images/         # Pradiniai vaizdai
* │   ├── prepared_images/    # Paruošti vaizdai
* │   ├── annotations/        # Anotacijų tekstiniai failai
* │   └── light_sources.json  # Eksportuoti šviesos šaltinių parametrai (JSON)
* ├── models/                 # Ištreniruoti modeliai
* ├── scripts/                # Pagalbiniai scenarijai
* │   ├── prepare_images.py               # Vaizdų filtravimas
* │   ├── generate_annotations.py         # Anotacijų generavimas
* │   ├── export_annotations_to_json.py   # Eksportas į JSON
* │   ├── train_model.py                  # Modelio treniravimas
* │   ├── evaluate_model.py               # Modelio įvertinimas
* │   ├── export_model.py                 # Modelio eksportavimas į ONNX
* │   └── lens_studio_integration.js      # Pavyzdinis scenarijus integracijai į Lens Studio
* ├── config.yaml                         # Treniruotės konfigūracija
* ├── requirements.txt                    # Reikalingų Python bibliotekų sąrašas
* ├── README.md                           # Dokumentacija

## Priklausomybės

Norint paleisti šį projektą, įdiekite būtinas Python bibliotekas:

```bash
pip install -r requirements.txt

Veikimo etapai
	1.	Vaizdų paruošimas: Filtruojami tinkamo formato vaizdai.

python scripts/prepare_images.py


	2.	Anotacijų generavimas: Sugeneruojamos anotacijos kiekvienam vaizdui.

python scripts/generate_annotations.py


	3.	JSON eksportas: Anotacijos konvertuojamos į JSON formatą.

python scripts/export_annotations_to_json.py


	4.	Modelio treniravimas: Naudojant YOLOv7 architektūrą, modelis treniruojamas aptikti šviesos šaltinius.

python scripts/train_model.py


	5.	Modelio įvertinimas (pasirinktinai):

python scripts/evaluate_model.py


	6.	Eksportavimas į ONNX: Modelis eksportuojamas į formatą, suderinamą su Lens Studio.

python scripts/export_model.py


Licencija

Šis projektas yra atviras ir gali būti naudojamas asmeniniais ar komerciniais tikslais pagal MIT licenciją.
