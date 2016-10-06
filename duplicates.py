import os


def are_files_duplicates(file_path):
    lst = []
    result = []
    for root, dirs, files in os.walk(file_path):
        for item in files:
            file_name = os.path.join(root, item)
            file_size = os.path.getsize(file_name)
            temp = (item, file_size)
            if temp not in lst:
                lst.append(temp)
            else:
                result.append(file_name)
    return result


if __name__ == '__main__':
    file_path = input('Введите путь к папке: ')
    result = are_files_duplicates(file_path)
    for item in result:
        os.remove(item)
        print ('Удален файл:', item)
