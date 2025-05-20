import yaml
import os
from pathlib import Path

def convert_homes_file(input_file: str, output_dir: str) -> bool:
    """
    Converts a YAML file from an old homes format to a new format.

    Args:
        input_file (str): Path to the old-format YAML file.
        output_dir (str): Directory to save the converted file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        old_data = yaml.safe_load(f)

    uuid = Path(input_file).stem

    new_data = {
        'homes': {},
        'first-join': None,
        'last-seen': None,
        'playtime': None,
        'last-death': None,
        'last-location': None
    }

    for home_name, home_data in old_data.get('homes', {}).items():
        new_data['homes'][home_name] = {
            'world': home_data.get('world', 'world'),
            'x': float(home_data.get('x', 0.0)),
            'y': float(home_data.get('y', 0.0)),
            'z': float(home_data.get('z', 0.0)),
            'yaw': float(home_data.get('yaw', 0.0)),
            'pitch': float(home_data.get('pitch', 0.0))
        }

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{uuid}.yml")

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(new_data, f, allow_unicode=True, sort_keys=False)

    return True

def main():
    print("=== Homes File Converter ===")
    print("Converts old .yml home files to the new format.")
    print()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, "old_homes")
    output_dir = os.path.join(script_dir, "new_homes")

    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created input folder: {input_dir}")
        print("Add your old .yml files and run this script again.")
        input("\nPress Enter to exit...")
        return

    yaml_files = list(Path(input_dir).glob('*.yml'))

    if not yaml_files:
        print(f"No .yml files found in: {input_dir}")
        print("Place your old home files in the folder and rerun the script.")
        input("\nPress Enter to exit...")
        return

    print(f"Found {len(yaml_files)} file(s) to convert...\n")

    converted = 0
    errors = 0

    for file in yaml_files:
        try:
            if convert_homes_file(str(file), output_dir):
                print(f"[✓] Converted: {file.name}")
                converted += 1
        except Exception as e:
            print(f"[✗] Error converting {file.name}: {e}")
            errors += 1

    print("\n=== Conversion Summary ===")
    print(f"Successfully converted: {converted}")
    print(f"Failed conversions:    {errors}")
    print(f"Output folder:         {output_dir}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
