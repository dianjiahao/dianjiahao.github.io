---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 3
dropdown: false
---

{% assign fieldwork_list = "ali|阿里科考 (Ali), animaqin|阿尼玛卿 (Animaqin)" | split: ", " %}

{% assign travel_list = "zhongnandaxue|中南大学 (CSU), food|人间烟火 (Food), changsha|长沙, wuhan|武汉, chongqing|重庆, chengdu|成都, hangzhou|杭州, guilin|桂林, guiyang|贵阳, chuanxi|川西, lasa|拉萨, xian|西安, yanan|延安, lanzhou|兰州, xining|西宁, nanchang|南昌, zhangjiajie|张家界, yueyang|岳阳, liangshan|凉山, qionghai|邛海, qianhumiaozhai|千户苗寨, henan|河南" | split: ", " %}

<style>
    .album-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 30px;
        border: none;
        border-radius: 12px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        display: block;
        text-decoration: none !important;
        height: 100%;
    }
    .album-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.1);
    }
    .album-cover-box {
        height: 200px;
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
        transform: scale(1.05);
    }
    .album-info {
        padding: 15px;
        text-align: center;
        border-top: 1px solid #eee;
    }
    .album-title {
        font-weight: bold;
        color: #333;
        font-size: 1.1em;
        margin: 0;
    }
    .album-meta {
        font-size: 0.8em;
        color: #888;
        margin-top: 5px;
        text-transform: uppercase;
    }
    /* 暗黑模式适配 */
    body.dark .album-card { background: #222; }
    body.dark .album-title { color: #eee; }
    body.dark .album-info { border-top: 1px solid #444; }
</style>

<h3 class="mb-4 mt-4">🏔️ Fieldwork & Research</h3>
<div class="row">
    {% for item in fieldwork_list %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign name = parts[1] %}
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card">
                <div class="album-cover-box">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" alt="{{ name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ name }}</div>
                    <span class="album-meta">{{ folder }}</span>
                </div>
            </a>
        </div>
    {% endfor %}
</div>

<hr style="opacity: 0.1; margin: 40px 0;">

<h3 class="mb-4">✈️ Travels & Life</h3>
<div class="row">
    {% for item in travel_list %}
        {% assign parts = item | split: "|" %}
        {% assign folder = parts[0] %}
        {% assign name = parts[1] %}
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <a href="/gallery/{{ folder }}/" class="album-card">
                <div class="album-cover-box">
                    <img src="/assets/img/{{ folder }}/cover.jpg" 
                         onerror="this.src='/assets/img/buka28glacier.jpg'" 
                         class="album-cover" alt="{{ name }}">
                </div>
                <div class="album-info">
                    <div class="album-title">{{ name }}</div>
                    <span class="album-meta">{{ folder }}</span>
                </div>
            </a>
        </div>
    {% endfor %}
</div>
