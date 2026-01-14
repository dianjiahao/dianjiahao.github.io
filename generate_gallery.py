import os

# ================= 配置区域 =================
# 图片所在的根目录
IMG_ROOT = "assets/img"
# 页面生成的目录
PAGE_ROOT = "_pages/gallery"

# 标题映射表
TITLES = {
    "ali": "阿里科考 (Ali)",
    "animaqin": "阿尼玛卿 (Animaqin)",
    "zhongnandaxue": "中南大学 (CSU Campus)",
    "food": "人间烟火 (Food & Life)",
    "changsha": "长沙 (Changsha)",
    "wuhan": "武汉 (Wuhan)",
    "chongqing": "重庆 (Chongqing)",
    "hangzhou": "杭州 (Hangzhou)",
    "guilin": "桂林 (Guilin)",
    "guiyang": "贵阳 (Guiyang)",
    "chuanxi": "川西 (West Sichuan)",
    "lasa": "拉萨 (Lhasa)",
    "xian": "西安 (Xi'an)",
    "yanan": "延安 (Yan'an)",
    "lanzhou": "兰州 (Lanzhou)",
    "xining": "西宁 (Xining)",
    "nanchang": "南昌 (Nanchang)",
    "zhangjiajie": "张家界 (Zhangjiajie)",
    "yueyang": "岳阳 (Yueyang)",
    "liangshan": "凉山 (Liangshan)",
    "qionghai": "邛海 (Qionghai)",
    "qianhumiaozhai": "千户苗寨 (Miao Village)",
    "henan": "河南 (Henan)"
}

# 页面通用模板
PAGE_TEMPLATE = """---
layout: page
title: "{title}"
permalink: /gallery/{folder}/
nav: false
---

<div class="mb-4">
    <a href="/gallery/" class="btn btn-sm btn-outline-secondary">
        <i class="fas fa-arrow-left"></i> 返回相册列表 (Back)
    </a>
</div>

<div class="row">
{images_html}
</div>
"""

# 图片展示模板
IMG_BLOCK = """    <div class="col-sm-12 col-md-6 col-lg-4 mb-4">
        {{% include figure.liquid loading="lazy" path="{path}" class="img-fluid rounded z-depth-1" zoomable=true %}}
    </div>
"""


def generate():
    # 1. 确保 _pages/gallery 目录存在
    if not os.path.exists(PAGE_ROOT):
        os.makedirs(PAGE_ROOT)
        print(f"📁 检查输出目录: {PAGE_ROOT}")

    # 2. 遍历 assets/img 下的一级目录
    for folder in sorted(os.listdir(IMG_ROOT)):
        album_path = os.path.join(IMG_ROOT, folder)

        # 只处理文件夹，且跳过系统文件夹
        if not os.path.isdir(album_path) or folder in ['icons', 'favicons', 'covers', '.git']:
            continue

        print(f"🔍 正在扫描相册: {folder} ...")

        # 3. 递归收集所有图片（包含 cover.jpg）
        valid_images = []

        for root, dirs, files in os.walk(album_path):
            for f in files:
                # 检查后缀名 (只要是图片就要！)
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    # 【核心修改】这里删除了 "if f == cover.jpg continue" 的判断
                    # 现在 cover.jpg 也会被加进来

                    # 获取图片的完整物理路径
                    full_file_path = os.path.join(root, f)

                    # 转换为网站需要的相对路径 (把 \ 替换为 /)
                    rel_path = os.path.relpath(full_file_path, start=os.getcwd()).replace("\\", "/")

                    valid_images.append(rel_path)

        # 4. 排序
        # 这一步会让图片按文件名排列。
        # 通常 'cover.jpg' (c开头) 会排在 'IMG_xxx' (I开头) 的前面。
        valid_images.sort()

        # 5. 生成 HTML
        img_html = ""
        for img_path in valid_images:
            img_html += IMG_BLOCK.format(path=img_path)

        # 6. 获取标题
        page_title = TITLES.get(folder, folder.capitalize())

        # 7. 组合内容
        page_content = PAGE_TEMPLATE.format(title=page_title, folder=folder, images_html=img_html)

        # 8. 写入文件
        page_filename = f"{folder}.md"
        page_path = os.path.join(PAGE_ROOT, page_filename)

        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        print(f"  --> ✅ 生成成功: {page_filename} (共 {len(valid_images)} 张图片，已包含封面)")


if __name__ == "__main__":
    generate()