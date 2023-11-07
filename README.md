# PowerDocTableOCR
面向电力设计文档的表格信息提取方法和系统

  测试文件都放在table目录下
  output_dir='resources/outputFiles/'默认输出路径，是extract_tables_to_csv的参数，可以更改
  word和excel文件的表格都会被提取为csv文件
  图片文件会被提取到一个文件夹，这个文件夹下有三个文件：
![image](https://github.com/Jimbo-N/PowerDocTableOCR/assets/121077820/da51277a-de3d-4c36-845b-48fbe965377e)

  分别为html文件（用来展示原始图片、识别后添加标注的图片、识别出的数据）、识别后添加标注的图片和excel文件：
  
  示例html:
![image](https://github.com/Jimbo-N/PowerDocTableOCR/assets/121077820/16f31189-1048-4f30-becd-3f02f4ed3e09)
  pdf文件会被提取到一个同名文件夹下，这个文件夹有多个子文件夹，名称分别为page_1、page_2、……，
  每个子文件夹下（如page_1)会有一个page_1_table文件夹（同样由三个文件）和一个当页pdf转化成的图片：
![image](https://github.com/Jimbo-N/PowerDocTableOCR/assets/121077820/e3edc050-79a4-4d46-a3a1-05e67e3a18de)

