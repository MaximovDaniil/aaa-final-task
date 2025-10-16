import csv
FILE_PATH = "/Users/daniilmaksimov/Downloads/Corp_Summary.csv"

"""
Получаем список словарий с каждой записью из файла
"""
def load_data() -> list[dict]:
    with open(FILE_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)

"""
Создаём словарь для иерархии,
потом заполняем его по колонком и выводим 
"""
def show_hierarchy(data: list[dict]) -> None:

    hierarchy = {}

    for row in data:
        dep = row.get('Департамент', '').strip()
        team = row.get('Отдел', '').strip()
        if dep and team:
            hierarchy.setdefault(dep, set()).add(team)

    print("\nИерархия команд:\n")

    for dep, teams in hierarchy.items():
        print(f"{dep}")
        for team in sorted(teams):
            print(f"      {team}")
    print()

def main() -> None:

    data = load_data()

    while True:
        print("1. Показать иерархию департаментов и отделов")
        print("2. Показать сводный отчёт по департаментам")
        print("3. Сохранить сводный отчёт в CSV")
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            show_hierarchy(data)
        elif choice == "2":
            print("Пока не готово")
        elif choice == "3":
            print("Пока не готов")


if __name__ == "__main__":
    main()