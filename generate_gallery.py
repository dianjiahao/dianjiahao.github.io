import os

# ================= 设置 =================
# 图片文件夹在哪里
IMG_DIR = "assets/img"
# 页面生成到哪里
PAGE_DIR = "_pages/gallery"

# 这是一个标题映射表，脚本会自动查这个表来起标题
TITLES = {
    "ali": "阿里科考 (Ali)",
    "animaqin": "阿尼玛卿 (Animaqin)",
    "zhongnandaxue": "中南大学 (Central South Univ.)",
    "food": "人间烟火 (Food & Delicacies)",
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
    "nanchang": "南昌 (Nanchang)",
    "zhangjiajie": "张家界 (Zhangjiajie)",
    "yueyang": "岳阳 (Yueyang)",
    "liangshan": "凉山 (Liangshan)",
    "qionghai": "邛海 (Qionghai)",
    "qianhumiaozhai": "千户苗寨 (Miao Village)",
    "henan": "河南 (Henan)"
}

# 页面内容的模板
PAGE_TEMPLATE = """---
layout: page
title: "{title}"
permalink: /gallery/{folder}/
nav: false
---

<div class="mb-4">
    <a href="/gallery/" class="btn btn-sm z-depth-0" style="background-color: #f0f0f0; color: #333;">
        <i class="fas fa-arrow-left"></i> 返回相册列表
    </a>
</div>

<div class="row">
{images_html}
</div>
"""

# 单张图片的模板
IMG_TEMPLATE = """    <div class="col-sm-12 col-md-6 col-lg-4 mb-4">
        {{% include figure.liquid loading="lazy" path="{path}" class="img-fluid rounded z-depth-1" zoomable=true %}}
    </div>
"""

def make_gallery():
    # 1. 如果 _pages/gallery 文件夹不存在，就创建一个
    if not os.path.exists(PAGE_DIR):
        os.makedirs(PAGE_DIR)

    # 2. 扫描 assets/img 下的所有文件夹
    for folder in os.listdir(IMG_DIR):
        folder_path = os.path.join(IMG_DIR, folder)

        # 只要文件夹，不要单独的文件
        if os.path.isdir(folder_path):
            
            # 跳过 icon 等无关文件夹
            if folder in ['icons', 'favicons', 'covers']: 
                continue

            print(f"正在处理相册: {folder} ...")

            # 3. 收集这个文件夹里所有的图片
            images_html = ""
            count = 0
            # 按文件名排序，保证照片顺序一致
            for img_file in sorted(os.listdir(folder_path)):
                if img_file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    # 不把封面图重复显示在列表里
                    if img_file.lower() == 'cover.jpg':
                        continue
                    
                    # 生成图片的 HTML 代码
                    full_path = f"{IMG_DIR}/{folder}/{img_file}"
                    images_html += IMG_TEMPLATE.format(path=full_path)
                    count += 1

            # 4. 获取标题（如果没有在映射表里，就直接用英文名）
            page_title = TITLES.get(folder, folder.capitalize())

            # 5. 组合成完整的页面内容
            final_content = PAGE_TEMPLATE.format(
                title=page_title,
                folder=folder,
                images_html=images_html
            )

            # 6. 写入到 _pages/gallery/xxx.md
            output_file = os.path.join(PAGE_DIR, f"{folder}.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            print(f"  --> ✅ 已生成 {folder}.md (包含 {count} 张照片)")

if __name__ == "__main__":
    make_gallery()