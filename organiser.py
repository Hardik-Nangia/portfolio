from pathlib import Path
from .config import EXTENSION_MAP, OTHER_FOLDER, DEFAULT_TARGET_DIR
from .utils import create_folder, move_file

def get_destination_folder(file_extension: str) -> str:
    for folder, extensions in EXTENSION_MAP.items():
        if file_extension in extensions:
            return folder
    return OTHER_FOLDER

def organize_directory(target_dir: Path, dry_run: bool = False) -> None:
    if not target_dir.exists():
        raise FileNotFoundError("Target directory does not exist.")

    for item in target_dir.iterdir():
        if item.is_file():
            destination_folder = get_destination_folder(item.suffix.lower())
            destination_path = target_dir / destination_folder

            create_folder(destination_path)
            move_file(item, destination_path / item.name, dry_run)

def main():
    print("📁 FILE ORGANIZER TOOL")
    print("---------------------")

    user_input = input(
        f"Enter directory path (Press Enter for default: {DEFAULT_TARGET_DIR}): "
    ).strip()

    target_dir = Path(user_input) if user_input else DEFAULT_TARGET_DIR

    dry_run_choice = input("Dry run? (y/n): ").lower()
    dry_run = dry_run_choice == "y"

    organize_directory(target_dir, dry_run)
    print("✅ Organization completed.")

def run_app():
    import streamlit as st
    from pathlib import Path

    st.subheader("📁 File Organizer Tool")

    directory = st.text_input("Enter directory path")
    dry_run = st.checkbox("Dry run (safe preview)")

    if st.button("Organize Files"):
        if directory:
            organize_directory(Path(directory), dry_run)
            st.success("Files organized successfully!")
        else:
            st.error("Please enter a directory path")

if __name__ == "__main__":
    main()
