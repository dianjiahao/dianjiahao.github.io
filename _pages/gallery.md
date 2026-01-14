---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 5
dropdown: false
---

<style>
    /* 卡片基础样式 */
    .album-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 30px;
        cursor: pointer;
        border: none;
        border-radius: 12px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        display: block;
        height: 100%;
        text-decoration: none !important;
    }
    .album-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    }
    /* 封面图容器 */
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
        transition: transform 0.6s ease;
    }
    .album-card:hover .album-cover {
        transform: scale(1.08);
    }
    /* 文字区域 */
    .album-info {
        padding: 15px 15px 20px 15px;
        text-align: center;
    }
    .album-title {
        font-weight: 700;
        color: #2c3e50;
        font-size: 1.15em;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }
    /* 相册描述样式 */
    .album-desc {
        font-size: 0.85em;
        color: #666;
        line-height: 1.5;
        margin-bottom: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    /* 分类标签样式 */
    .album-tag {
        display: inline-block;
        font-size: 0.7em;
        color: #fff;
        background-color: #3498db;
        padding: 2px 8px;
        border-radius: 10px;
        position: absolute;
        top: 10px;
        right: 10px;
        opacity: 0.9;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .tag-fieldwork { background-color: #e74c3c; } 
    .tag-travel { background-color: #3498db; }    

    /* 诗句引言样式 (新增) */
    .section-quote {
        margin-bottom: 30px;
        padding-left: 15px;
        border-left: 4px solid #3498db; /* 蓝色竖线 */
        color: #555;
    }
    .quote-cn {
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 4px;
        color: #2c3e50;
    }
    .quote-en {
        font-family: Georgia, "Times New Roman", serif; /* 英文衬线体，更有书卷气 */
        font-style: italic;
        font-size: 0.95em;
        color: #777;
    }

    /* 暗黑模式适配 */
    body.dark .album-card {
        background: #1e1e1e;
        border: 1px solid #333;
    }
    body.dark .album-title { color: #f0f0f0; }
    body.dark .album-desc { color: #aaa; }
    body.dark .album-cover-box { border-bottom: 1px solid #333; }
    body.dark .quote-cn { color: #e0e0e0; }
    body.dark .quote-en { color: #aaa; }
</style>

<h2 class="mb-4 mt-4">🏔️ Fieldwork & Research (科考纪实)</h2>
<div class="row">
    
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/ali/" class="album-card">
            <div class="album-cover-box">
                <span class="album-tag tag-fieldwork">Research</span>
                <img src="/assets/img/ali/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="阿里">
            </div>
            <div class="album-info">
                <div class="album-title">阿里 (Ali)</div>
                <div class="album-desc">
                    🧊 藏西秘境，冰川与苍穹的邂逅。<br>
                    <small>Mysterious Western Tibet, where glaciers meet the sky.</small>
                </div>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/animaqin/" class="album-card">
            <div class="album-cover-box">
                <span class="album-tag tag-fieldwork">Research</span>
                <img src="/assets/img/animaqin/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="阿尼玛卿">
            </div>
            <div class="album-info">
                <div class="album-title">阿尼玛卿 (Animaqin)</div>
                <div class="album-desc">
                    ⛰️ 神山巍峨，见证冰冻圈的脉动。<br>
                    <small>The majesty of the holy mountain, witnessing the cryosphere.</small>
                </div>
            </div>
        </a>
    </div>

</div>

<hr style="opacity: 0.1; margin: 40px 0;">

<h2 class="mb-3 mt-4">✈️ Travels & Life (风光旅途)</h2>

<div class="section-quote">
    <div class="quote-cn">“读万卷书，行万里路”</div>
    <div class="quote-en">With books unbound, the mind takes flight; By miles of earth, the soul gains sight.</div>
</div>

<div class="row">

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/zhongnandaxue/" class="album-card">
            <div class="album-cover-box">
                <span class="album-tag tag-travel">Campus</span>
                <img src="/assets/img/zhongnandaxue/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="中南大学">
            </div>
            <div class="album-info">
                <div class="album-title">中南大学</div>
                <div class="album-desc">
                    🎓 研途起点，定格岳麓山下的青春。<br>
                    <small>Research journey begins at the foot of Yuelu Mountain.</small>
                </div>
            </div>
        </a>
    </div>

    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <a href="/gallery/food/" class="album-card">
            <div class="album-cover-box">
                <span class="album-tag tag-travel">Life</span>
                <img src="/assets/img/food/cover.jpg" 
                     onerror="this.src='/assets/img/buka28glacier.jpg'" 
                     class="album-cover" alt="人间烟火">
            </div>
            <div class="album-info">
                <div class="album-title">人间烟火 (Food)</div>
                <div class="album-desc">
                    🍜 尝遍人间烟火，记录味蕾的感动。<br>
                    <small>Savoring the flavors of life, one bite at a time.</small>
                </div>
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
                <div class="album-title">长沙 (Changsha)</div>
                <div class="album-desc">
                    🌶️ 星城长沙，热辣与古韵交织。<br>
                    <small>The Star City, blending spicy heat with history.</small>
                </div>
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
                <div class="album-title">武汉 (Wuhan)</div>
                <div class="album-desc">
                    🌊 江城浩渺，黄鹤楼畔听涛声。<br>
                    <small>The River City, echoing history at Yellow Crane Tower.</small>
                </div>
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
                <div class="album-title">重庆 (Chongqing)</div>
                <div class="album-desc">
                    🚡 8D魔幻山城，穿梭雾气与火锅香。<br>
                    <small>8D mountain city, navigating through fog and spice.</small>
                </div>
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
                <div class="album-title">杭州 (Hangzhou)</div>
                <div class="album-desc">
                    🍃 西湖烟雨，一场婉约的江南梦。<br>
                    <small>Mist over West Lake, a poetic Jiangnan dream.</small>
                </div>
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
                <div class="album-title">桂林 (Guilin)</div>
                <div class="album-desc">
                    🏞️ 山水甲天下，现实中的水墨画。<br>
                    <small>Landscape unparalleled, an ink painting in reality.</small>
                </div>
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
                <div class="album-title">贵阳 (Guiyang)</div>
                <div class="album-desc">
                    🌲 林城筑韵，寻觅爽爽的清凉。<br>
                    <small>The Forest City, escaping into the cool nature.</small>
                </div>
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
                <div class="album-title">川西 (W. Sichuan)</div>
                <div class="album-desc">
                    🏔️ 雪山草甸，一场洗涤心灵的朝圣。<br>
                    <small>Snow peaks and grasslands, a pilgrimage to the soul.</small>
                </div>
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
                <div class="album-title">拉萨 (Lhasa)</div>
                <div class="album-desc">
                    ☀️ 日光之城，沐浴在信仰与暖阳下。<br>
                    <small>The City of Sunshine, bathing in faith and light.</small>
                </div>
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
                <div class="album-title">西安 (Xi'an)</div>
                <div class="album-desc">
                    🏛️ 十三朝古都，聆听千年的历史长风。<br>
                    <small>Ancient capital, listening to the wind of history.</small>
                </div>
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
                <div class="album-title">延安 (Yan'an)</div>
                <div class="album-desc">
                    🚩 黄土高坡的脊梁，红色的记忆。<br>
                    <small>Spirit of the Loess Plateau, the red memory.</small>
                </div>
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
                <div class="album-title">兰州 (Lanzhou)</div>
                <div class="album-desc">
                    🍜 黄河穿城而过，一碗牛肉面的乡愁。<br>
                    <small>Yellow River flows through, aroma of beef noodles.</small>
                </div>
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
                <div class="album-title">南昌 (Nanchang)</div>
                <div class="album-desc">
                    🦅 英雄之地，落霞与孤鹜齐飞。<br>
                    <small>Heroes' city, sunset over Tengwang Pavilion.</small>
                </div>
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
                <div class="album-title">张家界 (Zhangjiajie)</div>
                <div class="album-desc">
                    ⛰️ 奇峰三千，误入阿凡达的仙境。<br>
                    <small>Floating peaks, entering the world of Avatar.</small>
                </div>
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
                <div class="album-title">岳阳 (Yueyang)</div>
                <div class="album-desc">
                    ⛵ 洞庭波涌，登楼远眺忧乐天下。<br>
                    <small>Dongting Lake's vast waves, climbing the Tower.</small>
                </div>
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
                <div class="album-title">凉山 (Liangshan)</div>
                <div class="album-desc">
                    🔥 凉山深处，淳朴而厚重的彝家风情。<br>
                    <small>Deep mountains, simple and profound Yi culture.</small>
                </div>
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
                <div class="album-title">邛海 (Qionghai)</div>
                <div class="album-desc">
                    🦢 川西明珠，享受邛海边的静谧时光。<br>
                    <small>Pearl of Western Sichuan, tranquil lake time.</small>
                </div>
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
                <div class="album-title">千户苗寨 (Miao Village)</div>
                <div class="album-desc">
                    🏮 万家灯火，谱写梦幻的苗家史诗。<br>
                    <small>Thousands of lights, a dreamy Miao epic.</small>
                </div>
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
                <div class="album-title">河南 (Henan)</div>
                <div class="album-desc">
                    🌾 华夏之中，厚重的中原大地。<br>
                    <small>The cradle of civilization, the vast Central Plains.</small>
                </div>
            </div>
        </a>
    </div>

</div>
