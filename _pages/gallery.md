---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 2
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
        display: block; /* 确保a标签包住卡片 */
        height: 100%;
        text-decoration: none !important;
    }
    .album-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    }
    .album-cover-box {
        height: 200px; /* 固定封面高度 */
        width: 100%;
        overflow: hidden;
        position: relative;
        border-bottom: 1px solid #f0f0f0;
    }
    .album-cover {
        height: 100%;
        width: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    .album-card:hover .album-cover {
        transform: scale(1.05);
    }
    .album-info {
        padding: 15px 10px;
        text-align: center;
    }
    .album-title {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    .album-count {
        display: block;
        font-size: 0.8em;
        color: #888;
        font-weight: normal;
        text-transform: uppercase;
    }
    /* 暗黑模式适配 */
    body.dark .album-card {
        background: #1e1e1e;
        border: 1px solid #333;
    }
    body.dark .album-title { color: #e0e0e0; }
</style>

<h2 class="mb-4 mt-4">🏔️ Fieldwork & Research (科考纪实)</h2>
<div class="row">
    {% assign fieldwork = "ali|阿里 (Ali), animaqin|阿尼玛卿 (Animaqin)" | split: ", " %}
    
    {% for item in fieldwork %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign name = parts[1] %}
        
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card">
                <div class="album-cover-box">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" 
                         alt="{{ name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ name }}</div>
                    <span class="album-count">Fieldwork</span>
                </div>
            </a>
        </div>
    {% endfor %}
</div>

<hr>

<h2 class="mb-4 mt-4">✈️ Travels & Life (风光旅途)</h2>
<div class="row">
    
    {% assign travels = "zhongnandaxue|中南大学, food|人间烟火(美食), changsha|长沙, wuhan|武汉, chongqing|重庆, hangzhou|杭州, guilin|桂林, guiyang|贵阳, chuanxi|川西, lasa|拉萨, xian|西安, yanan|延安, lanzhou|兰州, nanchang|南昌, zhangjiajie|张家界, yueyang|岳阳, liangshan|凉山, qionghai|邛海, qianhumiaozhai|千户苗寨, henan|河南" | split: ", " %}

    {% for item in travels %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign cn_name = parts[1] %}
        
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card">
                <div class="album-cover-box">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" 
                         alt="{{ cn_name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ cn_name }}</div>
                    <span class="album-count">{{ folder }}</span>
                </div>
            </a>
        </div>
    {% endfor %}

</div>
