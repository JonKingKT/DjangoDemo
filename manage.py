#!/usr/bin/env python
#django-admin startproject {项目名称} //pycharm社区版使用这个命令创建Django项目
#manage 一个命令行工具可以用多种方式和Django项目进行交互 这个py文件大量使用但不修改
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoDemo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
