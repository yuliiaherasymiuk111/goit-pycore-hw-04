def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")

                name = parts[0]
                salary = int(parts[1])

                total += salary
                count += 1

        if count == 0:
            average = 0
        else:
            average = total / count

        return total, average

    except FileNotFoundError:
        print("File not found")
        return 0, 0

