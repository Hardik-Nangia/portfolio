from pathlib import Path

# Default folder (can be overridden)
DEFAULT_TARGET_DIR = Path.home() / "Downloads"

# Extension → Folder mapping
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".java", ".js", ".cpp"],
}

OTHER_FOLDER = "Others"
