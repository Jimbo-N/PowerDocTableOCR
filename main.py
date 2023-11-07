from convert import extract_tables_to_csv

file_path = "table/excel/table_excel.xlsx"
extract_tables_to_csv(file_path)
# 测试文件都放在table目录下
# output_dir='resources/outputFiles/'默认输出路径，是extract_tables_to_csv的参数，可以更改
# word和excel文件的表格都会被提取为csv文件
# 图片文件会被提取到一个文件夹，这个文件夹下有三个文件：
# 分别为html文件（用来展示原始图片、识别后添加标注的图片、识别出的数据）、识别后添加标注的图片和excel文件
# pdf文件会被提取到一个同名文件夹下，这个文件夹有多个子文件夹，名称分别为page_1、page_2、……
# 每个子文件夹下（如page_1)会有一个page_1_table文件夹（同样由三个文件）和一个当页pdf转化成的图片
