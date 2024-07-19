import os
import xml.dom.minidom


def format_xml_file(file_path):
    # ファイルの読み込み
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        # XMLをパースして整形
        dom = xml.dom.minidom.parseString(content)
        pretty_xml = dom.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8")

        # 不要な空行を取り除く
        pretty_xml = "\n".join(
            [line for line in pretty_xml.splitlines() if line.strip()]
        )

        # 整形したXMLをファイルに書き込み（上書き）
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(pretty_xml)

        print(f"{file_path} を整形しました。")

    except Exception as e:
        print(f"エラー: {file_path} を整形する際にエラーが発生しました。")
        print(str(e))


def format_all_cmsetting_files(root_dir):
    # 指定したディレクトリ以下のすべてのファイルを走査
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".cmsetting"):
                file_path = os.path.join(root, file)
                format_xml_file(file_path)


# メイン処理
if __name__ == "__main__":
    # 整形したいフォルダのパスを指定する
    target_directory = "directoryをここで指定"
    format_all_cmsetting_files(target_directory)
