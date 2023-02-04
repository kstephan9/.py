import os
from pathlib import Path
from DefaultItems import MyDesktop

os.chdir(MyDesktop)
DIRECTORIES = {
    "BAT_CMD": [".bat", ".cmd"],
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
            ".heif", ".psd", ".xcf", ".PNG"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
            ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                ".rvg", ".rtf", ".rtfd", ".wpd", ".ppt", ".xlsm",
                "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
            ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "EXCEL": [".xls", ".xlsx", ".xlsm", ".csv", ".CSV"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "SQL": [".sql"],
    "PDF": [".pdf"],
    "POWERPOINT": [".ppt", ".pptx"],
    "POWERSHELL": [".ps1"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "RTF": [".rtf"],
    "EXE": [".exe"],
    "LNK": [".lnk"],
    "ACCESS": [".mdb", ".accdb"],
    "SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

print("line 40: ", FILE_FORMATS)
def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        print("At 45: ", file_path, entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            print("At 40: ", file_format)
            directory_path = Path(FILE_FORMATS[file_format])
            print("At 51: file_path", file_path,  " file_format", file_format, " directory_path: ", directory_path )
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
               os.rmdir(dir)
            except:
                pass

if __name__ == "__main__":
    organize_junk()
