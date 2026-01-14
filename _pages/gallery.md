---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 2
dropdown: false
---

<style>
    .album-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 30px;
        cursor: pointer;
        border: none;
        border-radius: 12px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        display: block;
        height: 100%;
        text-decoration: none !important;
    }
    .album-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    }
    .album-cover-box {
        height: 200px;
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
    body.dark .album-card {
        background: #1e1e1e;
        border: 1px solid #333;
    }
    body.dark .album-title { color: #e0e0e0; }
</style>

<h2 class="mb-4 mt-4">🏔️ Fieldwork & Research (科考纪实)</h2>
<div class="row">
    
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/ali/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/ali/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="阿里">
            </div>
            <div class="album-info">
                <div class="album-title">阿里 (Ali)</div>
                <span class="album-count">Fieldwork</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/animaqin/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/animaqin/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="阿尼玛卿">
            </div>
            <div class="album-info">
                <div class="album-title">阿尼玛卿 (Animaqin)</div>
                <span class="album-count">Fieldwork</span>
            </div>
        </a>
    </div>

</div>

<hr>

<h2 class="mb-4 mt-4">✈️ Travels & Life (风光旅途)</h2>
<div class="row">

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/zhongnandaxue/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/zhongnandaxue/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="中南大学">
            </div>
            <div class="album-info">
                <div class="album-title">中南大学</div>
                <span class="album-count">zhongnandaxue</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/food/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/food/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="人间烟火">
            </div>
            <div class="album-info">
                <div class="album-title">人间烟火(美食)</div>
                <span class="album-count">food</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/changsha/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/changsha/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="长沙">
            </div>
            <div class="album-info">
                <div class="album-title">长沙</div>
                <span class="album-count">changsha</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/wuhan/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/wuhan/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="武汉">
            </div>
            <div class="album-info">
                <div class="album-title">武汉</div>
                <span class="album-count">wuhan</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/chongqing/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/chongqing/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="重庆">
            </div>
            <div class="album-info">
                <div class="album-title">重庆</div>
                <span class="album-count">chongqing</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/hangzhou/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/hangzhou/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="杭州">
            </div>
            <div class="album-info">
                <div class="album-title">杭州</div>
                <span class="album-count">hangzhou</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/guilin/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/guilin/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="桂林">
            </div>
            <div class="album-info">
                <div class="album-title">桂林</div>
                <span class="album-count">guilin</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/guiyang/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/guiyang/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="贵阳">
            </div>
            <div class="album-info">
                <div class="album-title">贵阳</div>
                <span class="album-count">guiyang</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/chuanxi/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/chuanxi/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="川西">
            </div>
            <div class="album-info">
                <div class="album-title">川西</div>
                <span class="album-count">chuanxi</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/lasa/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/lasa/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="拉萨">
            </div>
            <div class="album-info">
                <div class="album-title">拉萨</div>
                <span class="album-count">lasa</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/xian/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/xian/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="西安">
            </div>
            <div class="album-info">
                <div class="album-title">西安</div>
                <span class="album-count">xian</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/yanan/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/yanan/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="延安">
            </div>
            <div class="album-info">
                <div class="album-title">延安</div>
                <span class="album-count">yanan</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/lanzhou/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/lanzhou/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="兰州">
            </div>
            <div class="album-info">
                <div class="album-title">兰州</div>
                <span class="album-count">lanzhou</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/nanchang/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/nanchang/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="南昌">
            </div>
            <div class="album-info">
                <div class="album-title">南昌</div>
                <span class="album-count">nanchang</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/zhangjiajie/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/zhangjiajie/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="张家界">
            </div>
            <div class="album-info">
                <div class="album-title">张家界</div>
                <span class="album-count">zhangjiajie</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/yueyang/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/yueyang/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="岳阳">
            </div>
            <div class="album-info">
                <div class="album-title">岳阳</div>
                <span class="album-count">yueyang</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/liangshan/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/liangshan/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="凉山">
            </div>
            <div class="album-info">
                <div class="album-title">凉山</div>
                <span class="album-count">liangshan</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/qionghai/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/qionghai/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="邛海">
            </div>
            <div class="album-info">
                <div class="album-title">邛海</div>
                <span class="album-count">qionghai</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/qianhumiaozhai/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/qianhumiaozhai/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="千户苗寨">
            </div>
            <div class="album-info">
                <div class="album-title">千户苗寨</div>
                <span class="album-count">qianhumiaozhai</span>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/henan/" class="album-card">
            <div class="album-cover-box">
                <img src="/assets/img/henan/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="河南">
            </div>
            <div class="album-info">
                <div class="album-title">河南</div>
                <span class="album-count">henan</span>
            </div>
        </a>
    </div>

</div>
