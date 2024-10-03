def total_salary(path):
    salary = list()
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                salary.append(int(line.strip().split(',')[1]))
    except FileNotFoundError:
        print(f"Error! File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"Error {e}")
        return 0, 0
    if not salary:
        print("Warning: file -salary.txt- is empty.")
        return 0, 0
    total = sum(salary)
    avarage = int(total / len(salary))
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}")
    return total, avarage

total, avarage = total_salary("salary.txt")