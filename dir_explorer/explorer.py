from pathlib import Path
from datetime import date
import csv
import xlwt
from typing import List


def report(child: Path) -> list:
    name = child.name
    deep = len(child.parts)
    stat = child.stat()
    size = str(stat.st_size/1024) + ' Kb'
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


def explore_xls(book, header: List[str], dir: str = '.') -> None:
    df = book.add_sheet('Directories and files')
    for col, data in enumerate(header):
        df.write(0, col, data)
    tree = Path(dir).rglob('*')
    for row, child in enumerate(tree):
        for col, data in enumerate(report(child)):
            if col == 3:
                df.write(row + 1, col, data,
                         xlwt.easyxf(num_format_str='YYYY-MM-DD'))
            else:
                df.write(row + 1, col, data)


if __name__ == "__main__":
    filename_csv = "dir_explorer/static/root_info.csv"
    HEADER = ["Название",
              "Тип",
              "Размер",
              "Дата изменения",
              "Уровень вложенности",
              "Полный абсолютный путь"]
    with open(filename_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(HEADER)
        explore(writer)

    filename_xls = "dir_explorer/static/root_info.xls"
    book = xlwt.Workbook()
    explore_xls(book, HEADER)
    book.save(filename_xls)
