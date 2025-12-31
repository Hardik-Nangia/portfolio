import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_folder(folder_path: Path) -> None:
    folder_path.mkdir(exist_ok=True)

def move_file(file_path: Path, destination: Path, dry_run: bool) -> None:
    if dry_run:
        logging.info(f"[DRY RUN] Would move: {file_path.name} → {destination}")
    else:
        shutil.move(str(file_path), destination)
        logging.info(f"Moved: {file_path.name} → {destination}")
