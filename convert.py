import csv
import os
import pandas
import image_to_table
from docx import Document
from pdf_to_table import extract_tables_from_pdf
from image_to_table import extract_table

# 设置数据默认的输出路径
DATA_CATALOG_OUTPUT = 'resources/outputFiles/'


# 提取表格转换为csv文件
def extract_tables_to_csv(doc_path, csv_path=''):
    if not check_input_file(doc_path):
        return

    # 创建输出目录
    if csv_path == '':
        csv_path = DATA_CATALOG_OUTPUT + extract_name(doc_path)
    #create_dir(os.path.dirname(csv_path))

    fix = os.path.splitext(doc_path)[1]
    # 判断是否为docx文件
    if fix == '.docx':
        extract_word_tables_to_csv(doc_path, csv_path+'.csv')
    elif fix == '.xlsx':
        extract_excel_tables_to_csv(doc_path, csv_path+'.csv')
    elif fix == '.pdf':
        extract_tables_from_pdf(doc_path, csv_path)
    else:
        extract_table(doc_path, csv_path)   #图片

    print("提取完成，输出路径为：{}".format(os.path.abspath(csv_path)))


# 创建目录
def create_dir(path):
    if not os.path.exists(path):
        if path is None:
            os.makedirs(DATA_CATALOG_OUTPUT)
        else:
            os.makedirs(path)
    else:
        return


# 提取文件名
def extract_name(file_path):
    # 获取文件名（含后缀）
    file_name = os.path.basename(file_path)

    # 获取文件名（不含后缀）
    return os.path.splitext(file_name)[0]


# 检查转换文件是否符合格式
def check_input_file(file_path):
    # 给出提示信息
    print("路径：{}".format(file_path))

    # 判断是否为绝对路径
    # if not os.path.isabs(file_path):
    #     print("文件路径需要为绝对路径")
    #     return False

    # 判断文件是否存在
    if not os.path.exists(file_path):
        print("文件不存在")
        return False

    return True


# 提取word文件表格数据
def extract_word_tables_to_csv(doc_path, csv_path):
    # 打开Word文档
    doc = Document(doc_path)

    # 创建CSV文件
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # 遍历文档中的每个表格
        for table in doc.tables:
            # 遍历表格的每一行
            for row in table.rows:
                # 提取单元格数据并写入CSV文件
                data = [cell.text for cell in row.cells]
                writer.writerow(data)


# 提取Excel表格内容
def extract_excel_tables_to_csv(file_path, csv_path):
    df = pandas.read_excel(file_path)
    df.to_csv(csv_path, index=False)
