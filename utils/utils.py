def append_text_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text + '\n')
        print(f"Текст успешно добавлен в файл {file_path}")
    except Exception as e:
        print(f"Ошибка при добавлении текста в файл: {e}")