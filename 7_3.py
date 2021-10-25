"""Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.

"""
from os import path, walk
import shutil

for root, dirs, files in walk('my_project'):
    for _ in dirs:
        if 'templates' in dirs:
            if not path.exists('my_templates'):
                shutil.copytree(path.join(root, _), 'my_templates')
# У меня копируется только одна папка. Тонкости я пока не уловил =С