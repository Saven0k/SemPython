import csv


def generate_csv_file() -> None:
    list = [["Math", "[5;1;2;2;3;1;2;5]", "[15; 12; 12; 52;65; 98; 89; 21]"],
            ["Russian", "[2;2;2;2;1;1]", "[20; 15;25; 12; 12; 95; 25;25]"],
            ["PI", "[5;4;2;2;1;1;2;2;3]", "[95; 22 ; 12; 22;5; 58; 69; 21]"],
            ["Geography", "[2;1;2;2;23;1;1;2]", "[15; 22 ; 22; 12;15; 58; 89; 71]"],
            ["English", "[5;5;5;5;5;5;2]", "[25; 1 ; 1; 22;55; 18; 29; 51]"]]
    with open('Students.csv', 'w') as f:
        rows = []
        for i in list:
            rows.append({'Object': i[0],
                         'grade': i[1],
                         'points': i[2]})

        csv_write = csv.DictWriter(f, fieldnames=['Object',
                                                  'grade',
                                                  'points'])
        csv_write.writeheader()
        csv_write.writerows(rows)


generate_csv_file()
