from doctest import testfile
import requests
import logging
from abstract_class.abstract_logs import AbstractLogs
from utils.utils import append_text_to_file
from settings import res_file
# %%
# from __future__ import print_function,unicode_literals
import subprocess
from tabulate import tabulate
import copy
import re
import time
import datetime
import os
# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class EGAISLogs(AbstractLogs):
    def __init__(self):
        pass

    @staticmethod
    def get_logs(path, services, context, message):
        date = time.strftime('%Y-%m-%d', time.localtime())
        path = path+f'/{date}_{services}_{context}_{message}'
        if not os.path.exists(path):
            # Если папки нет, создаем ее
            os.makedirs(path)
            logger.info(f"EGAISLogs Папка '{path}' создана.")
            print(f"Папка '{path}' создана.")
        else:
            logger.info(f"EGAISLogs Папка '{path}' уже существует.")
            print(f"Папка '{path}' уже существует.")

        # Подключаемся к DockerHub
        sshProcess = subprocess.Popen(['ssh', 'DockerHub'], stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)

        sshProcess.stdin.write(f'kubectl config use-context {context}\n')
        # sshProcess.stdin.write('kubectl config use-context test-kuber\n')
        sshProcess.stdin.write('kubectl get pods --all-namespaces')
        sshProcess.stdin.close()
        time.sleep(1)
        # %%
        list = []
        for line in sshProcess.stdout:
            if line == "END\n":
                break
            list.append(line)
            print(line, end="")

        # to catch the lines up to logout
        for line in sshProcess.stdout:
            print(line, end="")

        # %%

        data = tuple(x.split() for x in list[17:])
        find_str = services
        str_list = [[x[0], x[1]] for x in data if find_str in x[1]]
        logger.info(f"EGAISLogs {str_list}")
        print(str_list)
        command = f'kubectl logs -n {str_list[0][0]} {str_list[0][1]}'
        logger.info(
            f'EGAISLogs -> kubectl logs -n {str_list[0][0]} {str_list[0][1]}')
        sshProcess_save_log = subprocess.Popen(
            ['ssh', 'DockerHub'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
        sshProcess_save_log.stdin.write(command)
        sshProcess_save_log.stdin.close()
        save_text = sshProcess_save_log.stdout.readlines()
        save_text = [x.split('\n') for x in save_text]
        logger.info(
            f'EGAISLogs -> пишем в файл - path/{context}{services}_{time.asctime()}.log')
        with open(f"{path}/{context}{services}.log", "a") as output:
            for x in save_text:
                output.write(str(x) + '\n')