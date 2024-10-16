import re
import subprocess
import io
import logging
import urllib3

urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def append_text_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text + '\n')
        print(f"Текст успешно добавлен в файл {file_path}")
    except Exception as e:
        print(f"Ошибка при добавлении текста в файл: {e}")


def grep_file(file_path:str, search_string:str, vol:int):
    file_path = file_path
    search_string = search_string
    result = subprocess.check_output(
        f"grep -C{vol} '{search_string}' {file_path}", shell=True).decode()
    return result


def save_logs_context(file_path: str, keywords: str, output_file: str, vol: int, message: str):
    found_lines = [grep_file(file_path, keywords, 30)]
    found_lines.insert(0, f'''
{{{{collapse({message})
<pre><code class='shell'>
''')
    found_lines.append('''
</code></pre>
}}}}              
''')
    try:
        with open(output_file, 'w') as f_out:
            f_out.writelines(found_lines)
        
        logging.info(f"save_logs_context файл успешно записан {output_file}")
    except:
        logging.error(f"save_logs_context Ошибка записи в файл {output_file}")