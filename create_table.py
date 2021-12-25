import os
import re


def create_table_from_console():
  table = []
  columns = 0
  paddings = []

  # table name
  tableName = input("Table name (default 'New table'): ")
  tableName = re.sub(r'[^А-яA-z0-9]', '', tableName)
  tableName = tableName.strip()  # удалить все проблемы по бокам
  tableName = ' New table ' if tableName.strip() == '' else f' {tableName} '

  # separater
  separater = input("Separater (default '|'): ")
  separater = separater.strip()  # удалить все проблемы по бокам
  separater = separater if 0 < len(separater) < 4 else '|'

  # get row
  print(f"\ninfo:\t* Write the row values by separating the columns with '{separater}'.")
  print("\t* Write the command 'end' to finish.\n")
  i = 0
  while True:
    newRow = input('row ' + str(i) + ': ')
    if newRow == 'end':
      break
    if newRow.strip() == '':
      continue
    i += 1
    
    # обработка строки
    newRow = newRow.split(separater)  # разбить данные
    for idx, val in enumerate(newRow):
      val = val.strip()  # удалить все проблемы по бокам
      val = ' ' if val == '' else val  # 1 пробел, если значение пустое
      newRow[idx] = f' {val} '  # добавить по 1 проблему по бокам
      
      # посчитать кол-во столбцов
      if len(newRow) > columns:
        paddings += [0] * (len(newRow) - columns)
        columns = len(newRow)

      # найти самые длинные значения в каждом столбце
      if len(newRow[idx]) > paddings[idx]:
        paddings[idx] = len(newRow[idx])

    table.append(newRow)

  # если таблица пуста
  if not table:
    return
  
  # уровнять количество столбцов
  for row in table:
    if len(row) != columns:
      for _ in range(columns - len(row)):
        row.append('  ')
  
  show_table(table, tableName, paddings, columns)
  table_to_file(table, tableName, paddings, columns)


def show_table(table:list, tableName:str, paddings:list, columns:int):
  # длинна строки
  countChars = sum(paddings) + columns - 1
  if countChars < len(tableName):
    countChars = len(tableName)
    paddings[-1] = len(tableName) - sum(paddings[:-1]) - columns + 1
  
  # разделяющая линия
  line = '+'
  for pad in paddings:
    line += '-' * pad + '+'
  
  # вывести название таблицы
  print('+' + '-' * countChars + '+')
  print('|' + tableName.center(countChars) + '|')
  
  # вывести значения таблицы
  for row in table:
    print(line)
    for idx, val in enumerate(row):
      print('|' + val.ljust(paddings[idx]), end='')
    print('|')
  print(line)


def table_to_file(table:list, tableName:str, paddings:list, columns:int):
  # директория выходного файла
  dirFile = os.path.join(os.getcwd(), 'tables')
  if not os.path.exists(dirFile):
    os.makedirs(dirFile)
  
  # название выходного файла и полный путь
  fileName = f'{tableName.strip()}.txt'
  filePath = os.path.join(dirFile, fileName)
  i = 1
  while os.path.exists(filePath):
    fileName = f'{tableName.strip()}_copy{i}.txt'
    filePath = os.path.join(dirFile, fileName)
    i += 1

  # длинна строки
  countChars = sum(paddings) + columns - 1
  if countChars < len(tableName):
    countChars = len(tableName)
    paddings[-1] = len(tableName) - sum(paddings[:-1]) - columns + 1
  
  # разделяющая линия
  line = '+'
  for pad in paddings:
    line += '-' * pad + '+'

  # запись в файл
  with open(filePath, 'w') as f:
    # название таблицы
    f.write('+' + '-' * countChars + '+\n')
    f.write('|' + tableName.center(countChars) + '|\n')
  
    # значения таблицы
    for row in table:
      f.write(line + '\n')
      for idx, val in enumerate(row):
        f.write('|' + val.ljust(paddings[idx]))
      f.write('|\n')
    f.write(line)


if __name__ == '__main__':
  create_table_from_console()
