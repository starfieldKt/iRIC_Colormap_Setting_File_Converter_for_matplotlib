# xml.etree.ElementTreeをETとしてインポート、ファイル選択のためのライブラリ、ファイルパスのためのos.pathをインポート
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import csv
import ast


# CSVファイルのパス
csv_path = "colorname_3.csv"

# データを格納するリスト
colorname_list = []

# CSVファイルを開く
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    # 各行のデータをリストに格納する
    for row in reader:
        colorname_list.append(row)

# テンプレートファイル名
template_filename = "template.cmsetting"

# テンプレートファイルを読み込み
tree_template = ET.parse(template_filename)
root_template = tree_template.getroot()

for i in range(len(colorname_list)):
    name = colorname_list[i][0]
    division = ast.literal_eval(colorname_list[i][1])
    # テンプレートの既存のItem要素を削除
    for item in root_template.findall(".//Item"):
        root_template.remove(item)

    cmap = plt.get_cmap(name)
    colors = cmap(division)
    colors = (colors[:, :3] * 255).astype(int)

    # 新たなItem要素を作成
    for i in range(len(colors)):
        value = division[i]
        rgb = colors[i][:]
        color = "#{:02x}{:02x}{:02x}".format(*rgb)
        item = ET.Element("Item")
        item.set("value", str(value))
        item.set("color", color)
        item.set("transparent", "false")
        root_template.append(item)

    # ファイル出力
    new_filename = name + "_" + str(len(division)) + "color.cmsetting"
    tree_template.write(new_filename, encoding="utf-8", xml_declaration=True)
