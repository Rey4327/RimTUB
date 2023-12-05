# RimMirK Telegram User Bot [RimTUB]

## содержание
 + [описание](#описание)
 + [первая настройка](#Первая-настройка)
   - [компьютер](#Компьютер)


## Описание
**🤖 ЮзерБоты - это скрипты которые работают от лица личного аккаунта и могут выполнять все тоже что и человек (почти)**


## Первая настройка

### Windows 
1. Скачайте весь код себе на компьютер ZIP \
   ![1. </> Code 2. Download ZIP](https://github.com/RimMirK/RimTUB/assets/115800822/07275682-7c4d-47ea-9058-3f2161bb41e3)
3. Распакуйте архив в удобное для вас место
4. Откройте на редактирование файл `config/user_config.py` и в нем замените номер телефона на свой. Следуйте указанием в файле.
5. Установите Python версии 3.10 или выше с [официального сайта Python](https://www.python.org/downloads/)
6. Откройте консоль. Для этого
    - Нажмите `Win` + `R`
    - В открывшимся окне введите `cmd`
    - Напишите команду Буква диска `:; cd` и полный путь к файлу. Например `D:; cd D:\RimTUB\`
7. Введите комманду `python -m pip install -r requirements.txt`
8. Наконец запускайте `python main.py`


### Android
1. Скачайте и установите [Tremux](https://f-droid.org/repo/com.termux_118.apk)
2. Введите команду ` cd ~ && apt update && apt upgrade && apt-get update && apt-get upgrade && pkg install python && pkg install python3 && termux-setup-storage`
3. Скачайте и распакуйте ZIP арихв в корневую дерикторию телефона (там где папки Android и Downloads)
4. Найдите эту папку в проводнике. Там откройте на редактирование файл `config/user_config.py` и замените номер телефона на свой следуя инструкциям в файле.
5. Введите комманду `python3 -m pip install -r requirements.txt`
6. в Tremux пропишите команду `cd storage/shared/RimTUB-main/RimTUB-main && python3 main.py`
