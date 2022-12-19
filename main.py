# -*- coding: cp1251 -*-
from pprint import pprint
import os


class CookHelper:
    def __init__(self):
        with open('recipes.txt') as f:
            self.cook_book = {}
            for line in f:
                dish = line.strip()
                num = int(f.readline())
                i = 0
                ingr = []
                while i < num:
                    i += 1
                    ingr_str = f.readline().strip()
                    row = {
                        'ingredient_name': ingr_str[0: ingr_str.find(' | ')],
                        'quantity': int(ingr_str[ingr_str.find(' | ') + 3: ingr_str.rfind(' | ')]),
                        'measure': ingr_str[ingr_str.rfind(' | ') + 3:]
                    }
                    ingr.append(row)
                self.cook_book[dish] = ingr
                f.readline()

    def cook_book_view(self):
        pprint(self.cook_book)

    def get_shop_list(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if dish in self.cook_book:
                for row in self.cook_book[dish]:
                    if shop_list.get(row['ingredient_name']) is None:
                        shop_list[row['ingredient_name']] = {'measure': row['measure'],
                                                             'quantity': row['quantity'] * person_count}
                    else:
                        shop_list[row['ingredient_name']]['quantity'] += row['quantity'] * person_count
            else:
                print(f"Рецепт {dish} в вашей книге рецептов не обнаружен")
        return shop_list


def txt_file_sort_combine():
    file_path = os.path.join(os.getcwd(), "TXT_DIR")
    dir_list = os.listdir(file_path)
    txt_files_list = [file for file in dir_list if '.txt' == file[len(file) - 4 :] and file != 'out.txt']
    lines_list = []
    tmp_box = {}

    for file in txt_files_list:
        with open(os.path.join(os.getcwd(), "TXT_DIR",file)) as f:
            tmp_file = f.readlines()
            len_tmp_file = len(tmp_file)
            lines_list.append(len_tmp_file)
            tmp_box[len_tmp_file] = (file, tmp_file)

    lines_list.sort()

    with open('out.txt', 'w') as f:
        for lines in lines_list:
            f.write(tmp_box[lines][0])
            f.write('\n')
            f.write(str(lines))
            f.write('\n')
            f.writelines(tmp_box[lines][1])
            f.write('\n')


if __name__ == '__main__':
    cook = CookHelper()
    sl = cook.get_shop_list(['Омлет', 'Омлет', 'Фахитос'], 2)
    pprint(sl)
    txt_file_sort_combine()
