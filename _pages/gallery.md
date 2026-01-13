---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 2
dropdown: false
---

{% assign fieldwork_list = "ali|阿里科考, animaqin|阿尼玛卿" | split: ", " %}

{% assign travel_list = "zhongnandaxue|中南大学, food|人间烟火(美食), changsha|长沙, wuhan|武汉, chongqing|重庆, chengdu|成都, hangzhou|杭州, guilin|桂林, guiyang|贵阳, chuanxi|川西, lasa|拉萨, xian|西安, yanan|延安, lanzhou|兰州, xining|西宁, nanchang|南昌, zhangjiajie|张家界, yueyang|岳阳, liangshan|凉山, qionghai|邛海, qianhumiaozhai|千户苗寨, henan|河南" | split: ", " %}

<style>
    /* 卡片样式 */
    .album-card {
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 30px;
        border: none;
        border-radius: 16px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        height: 100%;
        text-decoration: none !important; /* 去掉链接下划线 */
    }
    .album-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    .album-cover-container {
        height: 220px; /* 封面高度 */
        width: 100%;
        overflow: hidden;
        position: relative;
    }
    .album-cover {
        height: 100%;
        width: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    .album-card:hover .album-cover {
        transform: scale(1.05); /* 鼠标悬停时图片微放大 */
    }
    .album-info {
        padding: 15px;
        text-align: center;
        background: #fff;
        border-top: 1px solid #f1f1f1;
    }
    .album-title {
        font-weight: 700;
        color: #2c3e50;
        font-size: 1.1rem;
        margin: 0;
    }
    .album-folder {
        display: block;
        font-size: 0.8rem;
        color: #999;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* 暗黑模式 */
    body.dark .album-card, body.dark .album-info {
        background: #1e1e1e;
        border-color: #333;
    }
    body.dark .album-title { color: #f0f0f0; }
</style>

<h2 class="mb-4 mt-5"><i class="fas fa-mountain"></i> Fieldwork & Research</h2>
<div class="row">
    {% for item in fieldwork_list %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign name = parts[1] %}
        
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card d-block">
                <div class="album-cover-container">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" 
                         alt="{{ name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ name }}</div>
                    <span class="album-folder">{{ folder }}</span>
                </div>
            </a>
        </div>
    {% endfor %}
</div>

<hr style="margin: 3rem 0; opacity: 0.1;">

<h2 class="mb-4"><i class="fas fa-plane-departure"></i> Travels & Life</h2>
<div class="row">
    {% for item in travel_list %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign name = parts[1] %}
        
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card d-block">
                <div class="album-cover-container">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" 
                         alt="{{ name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ name }}</div>
                    <span class="album-folder">{{ folder }}</span>
                </div>
            </a>
        </div>
    {% endfor %}
</div>
