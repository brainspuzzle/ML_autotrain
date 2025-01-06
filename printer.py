import os
from datetime import datetime


def print_files_and_content_to_file(directory, base_output_dir, excluded_files=None, excluded_dirs=None, excluded_extensions=None):
    if excluded_files is None:
        excluded_files = []
    if excluded_dirs is None:
        excluded_dirs = []
    if excluded_extensions is None:
        excluded_extensions = []

    # Sukurti išvesties katalogą, jei jo nėra
    os.makedirs(base_output_dir, exist_ok=True)

    # Sukurti failo pavadinimą su data ir laiku
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(base_output_dir, f"scan_{timestamp}.txt")

    ignored_items = []  # Sąrašas ignoruotiems failams ir katalogams
    with open(output_file, 'w', encoding='utf-8') as output:
        # Įrašyti antraštę ir informaciją apie nuskaitymą
        output.write(f"### Scan Results ({timestamp}) ###\n\n")

        for root, dirs, files in os.walk(directory):
            # Tikriname ir pašaliname ignoruotus katalogus
            ignored_dirs = [d for d in dirs if d in excluded_dirs]
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            # Pažymime ignoruotus katalogus
            for d in ignored_dirs:
                ignored_items.append(f"Directory: {os.path.join(root, d)}")

            for file in files:
                # Tikriname ir ignoruojame failus pagal pavadinimą arba plėtinį
                if file in excluded_files or any(file.endswith(ext) for ext in excluded_extensions):
                    ignored_items.append(f"File: {os.path.join(root, file)}")
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        output.write(f"\n### File: {file_path} ###\n")
                        output.write(content)
                except Exception as e:
                    output.write(f"\nCould not read file {file}: {e}\n")

        # Pridėti informaciją apie ignoruotus elementus
        if ignored_items:
            output.write("\n### Ignored Items ###\n")
            for item in ignored_items:
                output.write(f"{item}\n")

    print(f"Scan results saved to: {output_file}")


# Nurodykite pagrindinį aplanką
project_directory = os.path.dirname(os.path.abspath(__file__))  # dabartinio failo katalogas
output_directory = os.path.join(project_directory, "scan_results")  # Išvesties failų katalogas

# Atmetami failai, katalogai ir failų plėtiniai
excluded_files = [".env", "printer.py", "instruments.json", "readme.md"]
excluded_dirs = [".venv", ".git", "scan_results", ".idea", "data"]  # Pridėtas `.git`
excluded_extensions = [".pyc", ".bin", ".exe"]

print_files_and_content_to_file(project_directory, output_directory, excluded_files, excluded_dirs, excluded_extensions)