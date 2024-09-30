import os
import subprocess

# 设置源文件目录和输出目录
input_dir = './FLAC'
output_dir = './MP3'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

"""
# 获取所有的.flac文件
# os.listdir() 获取当前目录下的文件和文件夹  for filename in os.listdir(input_dir):
# os.walk() 函数获取所有目录下的文件和文件夹 ↓ 
"""
for root, folders, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith('.flac'):
            # 构建ffmpeg命令
            input_path = os.path.join(root, filename)
            root_output = root.replace(input_dir, output_dir, 1).replace('/', '\\', 1)
            output_path = os.path.join(root_output, filename).replace('.flac', '.mp3')
            '''
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.mp3')
            '''
            # 如果不存在目录, 通过 os.makedirs() 方法创建一个目录
            if not os.path.exists(root_output):
                os.makedirs(root_output)
            '''
                或者 os.makedirs(root_output, exist_ok=True) ，
                当 exist_ok 设置为 True 时，如果目录已经存在，函数将不会引发错误，而是直接返回。
            '''
            # 转换命令
            command = ['ffmpeg', '-i', input_path, output_path]
            # 执行转换
            subprocess.run(command)