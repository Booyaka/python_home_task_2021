"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""
import os

root_name = 'my_project'
dirs_name = ['settings', 'mainapp', 'adminapp', 'authmap']
if not os.path.exists(root_name):
    for i in range(len(dirs_name)):
        os.makedirs(os.path.join(root_name, dirs_name[i]))
else:
    print('Already exists')