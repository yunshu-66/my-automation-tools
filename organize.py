import os

folder = "D:/my-automation-tools/整理测试"

# 扩展名 -> 目标文件夹 的对应关系
type_map = {
    ".jpg": "图片", ".png": "图片", ".gif": "图片",
    ".mp4": "视频",
    ".txt": "文档", ".doc": "文档", ".pdf": "文档",
}

for filename in os.listdir(folder):
    old_path = folder + "/" + filename

    # 跳过文件夹本身，只处理文件
    if os.path.isdir(old_path):
        continue

    # 取扩展名，转小写
    ext = os.path.splitext(filename)[1].lower()

    # 按扩展名决定分到哪个子文件夹
    if ext in type_map:
        target = type_map[ext]
    else:
        target = "其他"

    # 目标文件夹路径，不存在就新建
    target_folder = folder + "/" + target
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 移动文件
    os.rename(old_path, target_folder + "/" + filename)
    print(filename, "->", target)
