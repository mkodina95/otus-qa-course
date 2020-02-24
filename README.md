![Travis CI](https://travis-ci.org/mkodina95/otus-qa-course.svg?branch=master)

Для запуска тестов необходимо:
1. Склонировать проект в заранее выбранную директорию 
[https://github.com/mkodina95/otus-qa-course.git]
2. Установить pyenv командой brew install pyenv
3. Установить python 3.7.3 командой pyenv install 3.7.3
4. Установить pytest командами:
 pip install -U virtualenv # создаем виртуальную среду
 python3 -m virtualenv venv
 source venv/bin/activate
 pip install pytest # устанавливаем pytest
5. Запустить тесты командой pytest test_py_test_introduction.py в директории проекта