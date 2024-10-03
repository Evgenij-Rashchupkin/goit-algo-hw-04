def get_cats_info(path):
    cats_info = list()
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    id_cat, name, age = line.split(',')
                    dict_cat = {
                        'id': id_cat,
                        'name': name,
                        'age': age
                    }
                    cats_info.append(dict_cat)
    except FileNotFoundError:
        return f"Error! File '{path}' not found."
    except Exception as e:
         return f"Error {e}"
    if not cats_info:
        return "Warning: file -cats.txt- is empty."

    return cats_info

cats_info = get_cats_info("cats.txt")
print(cats_info)