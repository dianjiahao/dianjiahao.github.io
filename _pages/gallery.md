---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 2  # 设为2，确保它在 About(1) 和 Publications(3) 之间
dropdown: false
---

<style>
    /* 封面卡片样式优化 */
    .album-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 30px;
        cursor: pointer;
        border: none;
        border-radius: 12px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .album-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    }
    .album-cover {
        height: 200px; /* 固定封面高度，整齐划一 */
        width: 100%;
        object-fit: cover;
        border-bottom: 1px solid #f0f0f0;
    }
    .album-title {
        text-align: center;
        padding: 15px 10px;
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1em;
    }
    .album-count {
        display: block;
        font-size: 0.8em;
        color: #888;
        margin-top: 5px;
        font-weight: normal;
    }
    /* 暗黑模式适配 */
    body.dark .album-card {
        background: #1e1e1e;
        border: 1px solid #333;
    }
    body.dark .album-title {
        color: #e0e0e0;
    }
</style>

<h2 class="mb-4 mt-4">🏔️ Fieldwork & Research (科考纪实)</h2>
<div class="row">
    <div class="col-6 col-md-4 col-lg-3">
        <a href="/gallery/ali/" class="text-decoration-none">
            <div class="album-card">
                <img src="/assets/img/buka28glacier.jpg" class="album-cover" alt="Ali">
                <div class="album-title">
                    阿里 (Ali)
                    <span class="album-count">Fieldwork</span>
                </div>
            </div>
        </a>
    </div>

    <div class="col-6 col-md-4 col-lg-3">
        <a href="/gallery/anyemaqen/" class="text-decoration-none">
            <div class="album-card">
                <img src="/assets/img/buka28glacier.jpg" class="album-cover" alt="Anyemaqen">
                <div class="album-title">
                    阿尼玛卿
                    <span class="album-count">Fieldwork</span>
                </div>
            </div>
        </a>
    </div>
</div>

<hr>

<h2 class="mb-4 mt-4">✈️ Travels & Life (风光旅途)</h2>
<div class="row">
    
    {% assign travels = "Chongqing|重庆, Campus|校园, Hangzhou|杭州, Changsha|长沙, Nanchang|南昌, WestSichuan|川西, Guilin|桂林, Guiyang|贵阳, Henan|河南, MiaoVillage|千户苗寨, Liangshan|凉山, Qionghai|邛海, Wuhan|武汉, Zhangjiajie|张家界, Yueyang|岳阳, Chengdu|成都, Lhasa|拉萨, Xining|西宁, Xian|西安, Yanan|延安" | split: ", " %}

    {% for item in travels %}
        {% assign parts = item | split: "|" %}
        {% assign en_name = parts[0] %}
        {% assign cn_name = parts[1] %}
        
        <div class="col-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ en_name | downcase }}/" class="text-decoration-none">
                <div class="album-card">
                    <img src="/assets/img/covers/{{ en_name | downcase }}.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" 
                         alt="{{ cn_name }}">
                    <div class="album-title">
                        {{ cn_name }}
                        <span class="album-count">{{ en_name }}</span>
                    </div>
                </div>
            </a>
        </div>
    {% endfor %}

</div>
