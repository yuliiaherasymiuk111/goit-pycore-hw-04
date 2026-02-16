def get_cats_info(path):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")

                cat_id = parts[0]
                name = parts[1]
                age = parts[2]

                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_list.append(cat_dict)

        return cats_list

    except FileNotFoundError:
        print("File not found")
        return []


