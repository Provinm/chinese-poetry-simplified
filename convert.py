#coding=utf-8

import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.append(BASE_DIR)


from zhtools.langconv import Converter


def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

def convert_anything(obj):

    if isinstance(obj, str):
        return cht_to_chs(obj)
    elif isinstance(obj, (list, tuple, set)):
        obj = list(obj)
        for idx, value in enumerate(obj):
            obj[idx] = convert_anything(value)
        return obj
    elif isinstance(obj, dict):
        for key in list(obj):
            new_key = cht_to_chs(key)
            obj[new_key] = convert_anything(obj[key])
            if new_key != key:
                del obj[key]

        return obj

    return obj


class T2S:

    def __init__(self, dir_path=""):
        self.dir_path = dir_path

    def rebuild_file(self, file_path):
        with open(file_path, "r")as file:
            data = file.read()

        data = json.loads(data)

        new_data = convert_anything(data)
        with open(file_path, "w", encoding="utf-8")as file:
            file_data = json.dumps(new_data, ensure_ascii=False, indent=4, sort_keys=True)
            file.write(file_data)

        return True

    def find_json_file(self, dir_path):

        valid_path = []
        for root, dirs, files in os.walk(dir_path):
            for f in files:
                if f.endswith(".json"):
                    new_path = os.path.join(root, f)
                    valid_path.append(new_path)

        return valid_path

    def rebuild(self):

        valid_files = self.find_json_file(self.dir_path)
        for f in valid_files:
            try:
                # print("start to rebuild {}".format(f))
                self.rebuild_file(f)
                # print("end to rebuild {}".format(f))
            except Exception as err:
                print("failed to rebuild {}".format(f))
                

        return True

if __name__ == "__main__":
    dir_path = os.path.abspath("./chinese-poetry")
    t2s = T2S(dir_path)
    t2s.rebuild()
