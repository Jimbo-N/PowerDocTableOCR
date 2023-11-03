import subprocess
import os

def extract_table(image_path, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    # 获取图片文件的基本名称，不包含扩展名
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # 创建一个新的子目录路径
    output_dir = os.path.join(output_dir, base_name)

    # 确保新的输出目录存在，如果不存在则创建
    os.makedirs(output_dir, exist_ok=True)


    # 设置模型目录和其他参数
    det_model_dir = "models/text_detection/ch_PP-OCRv3_det_infer"
    rec_model_dir = "models/text_recognition/ch_PP-OCRv3_rec_infer"
    table_model_dir = "models/table_recognition/ch_ppstructure_mobile_v2.0_SLANet_infer"
    rec_char_dict_path = "resources/ppocr_keys_v1.txt"
    table_char_dict_path = "resources/table_structure_dict_ch.txt"

    # 构建命令
    command = f"python venv/Lib/site-packages/paddleocr/ppstructure/table/predict_table.py " \
              f"--det_model_dir={det_model_dir} " \
              f"--rec_model_dir={rec_model_dir} " \
              f"--table_model_dir={table_model_dir} " \
              f"--rec_char_dict_path={rec_char_dict_path} " \
              f"--table_char_dict_path={table_char_dict_path} " \
              f"--image_dir={image_path} " \
              f"--output={output_dir}"

    # 执行命令
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.decode()
    error = process.stderr.decode()

    if process.returncode == 0:
        print("Table extraction completed successfully")
        return output
    else:
        print("Table extraction failed")
        return error
