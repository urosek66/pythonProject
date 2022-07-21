with open("text.csv", "r") as csv_file:
    content_lines = csv_file.read().splitlines()

    for row in content_lines:
        data_row = row.split(",")
        print(f"{data_row[0]} is {data_row[1]} years old and {data_row[2]} ")


