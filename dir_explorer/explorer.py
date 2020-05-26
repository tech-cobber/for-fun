from pathlib import Path
from datetime import date
import csv
import xlwt


def report(child: Path) -> list:
    name = child.name
    deep = len(child.parts)
    stat = child.stat()
    size = stat.st_size
    last_modified = date.fromtimestamp(stat.st_mtime)
    if child.is_file():
        file_type = 'file'
    elif child.is_dir():
        file_type = 'directory'
    else:
        file_type = "Don't touch it"
    return [name, file_type, size, last_modified, deep, f'./{child}']


def explore(writer, dir: str = '.') -> None:
    tree = Path(dir).rglob('*')
    for child in tree:
        writer.writerow(report(child))


if __name__ == "__main__":
    f_name = "dir_explorer/static/root_info.csv"
    HEADER = ["Название",
              "Тип",
              "Размер",
              "Дата изменения",
              "Уровень вложенности",
              "Полный абсолютный путь"]
    with open(f_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(HEADER)
        explore(writer)
