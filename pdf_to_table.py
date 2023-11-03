from pdf2image import convert_from_path
from image_to_table import extract_table  # 假设你已经有了这个函数
import os

def extract_tables_from_pdf(pdf_path, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 将PDF转换为图片
    pages = convert_from_path(pdf_path, 300)  # 300 DPI是图片质量

    # 对每一页进行处理
    for i, page in enumerate(pages):
        # 为每一页创建一个子目录
        page_dir = os.path.join(output_dir, f'page_{i+1}')
        os.makedirs(page_dir, exist_ok=True)

        # 将页面保存为图片
        image_path = os.path.join(page_dir, f'page_{i+1}.jpg')
        page.save(image_path, 'JPEG')

        # 使用表格提取函数处理图片
        extract_table(image_path, page_dir)