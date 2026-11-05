#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

# Read Tân Sơn Nhất SVG
tsn_svg_path = WORKSPACE / "LOGO-white- sân golf tân sơn nhất.svg"
tsn_svg_content = ""
if tsn_svg_path.exists():
    with open(tsn_svg_path, 'r', encoding='utf-8') as f:
        tsn_svg_content = f.read()

# Laurel Wreath SVG template with realistic gold leaf gradient
def make_wreath_svg(num, title, sub="", is_top=False):
    width = 175 if is_top else 150
    height = 175 if is_top else 150
    return f"""
    <div class="wreath-card {'is-top' if is_top else ''}">
      <svg class="wreath-graphic" viewBox="0 0 140 140" style="width:{width}px; height:{height}px;">
        <defs>
          <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF3B0"/>
            <stop offset="35%" stop-color="#FFD700"/>
            <stop offset="70%" stop-color="#E5A910"/>
            <stop offset="100%" stop-color="#B8860B"/>
          </linearGradient>
          <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.5)"/>
          </filter>
        </defs>
        <g fill="url(#goldGrad)" stroke="url(#goldGrad)" stroke-width="0.8" filter="url(#goldGlow)">
          <!-- Left branch -->
          <path d="M 70,128 C 36,128 12,98 12,64 C 12,38 24,20 38,10" fill="none" stroke="url(#goldGrad)" stroke-width="3"/>
          <path d="M 18,88 Q 5,82 10,72 Q 20,76 18,88 Z"/>
          <path d="M 13,68 Q 1,60 7,51 Q 17,56 13,68 Z"/>
          <path d="M 16,48 Q 5,39 14,32 Q 22,38 16,48 Z"/>
          <path d="M 26,32 Q 18,23 28,17 Q 34,25 26,32 Z"/>
          <path d="M 39,19 Q 32,9 43,6 Q 47,15 39,19 Z"/>
          <path d="M 28,105 Q 16,101 19,90 Q 30,94 28,105 Z"/>
          <path d="M 46,121 Q 34,121 35,110 Q 47,112 46,121 Z"/>
          
          <!-- Right branch -->
          <path d="M 70,128 C 104,128 128,98 128,64 C 128,38 116,20 102,10" fill="none" stroke="url(#goldGrad)" stroke-width="3"/>
          <path d="M 122,88 Q 135,82 130,72 Q 120,76 122,88 Z"/>
          <path d="M 127,68 Q 139,60 133,51 Q 123,56 127,68 Z"/>
          <path d="M 124,48 Q 135,39 126,32 Q 118,38 124,48 Z"/>
          <path d="M 114,32 Q 122,23 112,17 Q 106,25 114,32 Z"/>
          <path d="M 101,19 Q 108,9 97,6 Q 93,15 101,19 Z"/>
          <path d="M 112,105 Q 124,101 121,90 Q 110,94 112,105 Z"/>
          <path d="M 94,121 Q 106,121 105,110 Q 93,112 94,121 Z"/>
        </g>
      </svg>
      <div class="wreath-inner">
        <div class="w-num">{num}</div>
        <div class="w-title">{title}</div>
        {f'<div class="w-sub">{sub}</div>' if sub else ''}
      </div>
    </div>
    """

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=2048, height=1896, initial-scale=1.0">
<title>Thư Mời & Poster Giải Golf Báo Lao Động Open 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800;1,900&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 2048px;
    height: 1896px;
    overflow: hidden;
    position: relative;
    background: #000000;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
  }}

  /* Main 2-Page Grid */
  .poster-spread {{
    width: 2048px;
    height: 1896px;
    display: grid;
    grid-template-columns: 1024px 1024px;
    position: relative;
  }}

  /* ============================================================
     LEFT PAGE: INVITATION HERO & KEY VISUAL
     ============================================================ */
  .left-page {{
    width: 1024px;
    height: 1896px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(180deg, #ea8513 0%, #f6ab38 22%, #fdf2dc 45%, #9bc752 68%, #418b20 86%, #21560b 100%);
    padding: 35px 45px 145px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Background Course Image subtle overlay */
  .left-bg-img {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/hero_golf_course.jpg');
    background-size: cover;
    background-position: center bottom;
    opacity: 0.38;
    mix-blend-mode: multiply;
    pointer-events: none;
    z-index: 1;
  }}

  .left-content {{
    position: relative;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }}

  /* Top Logos */
  .left-logos {{
    display: flex;
    align-items: center;
    gap: 16px;
    background: rgba(255, 255, 255, 0.95);
    padding: 8px 24px;
    border-radius: 40px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.18);
  }}

  .left-logos img.ldo {{
    height: 40px;
    width: auto;
  }}

  .logo-sep {{
    width: 1.5px;
    height: 32px;
    background: #d4a017;
  }}

  .tsn-wrap {{
    height: 36px;
    display: flex;
    align-items: center;
  }}

  .tsn-wrap svg {{
    height: 32px;
    width: auto;
  }}
  .tsn-wrap svg path {{
    fill: #004d2c !important;
  }}

  /* Calligraphy "Thư mời" */
  .script-thu-moi {{
    font-family: 'Great Vibes', cursive;
    font-size: 96px;
    color: #ffffff;
    text-shadow: 0 4px 18px rgba(180, 50, 0, 0.65), 0 2px 4px rgba(0,0,0,0.4);
    margin-top: 10px;
    line-height: 0.95;
  }}

  /* Invitation Subtitle */
  .sub-invitation {{
    font-size: 17.5px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 0 2px 6px rgba(0,0,0,0.45);
    margin-top: 6px;
  }}

  .sub-for-who {{
    font-size: 22px;
    font-weight: 900;
    color: #551200;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-top: 3px;
    text-shadow: 0 1px 2px rgba(255,255,255,0.7);
  }}

  .sub-participate {{
    font-size: 15px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 4px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.35);
  }}

  /* Tournament Big 3D Title */
  .main-tournament-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 48px;
    font-weight: 900;
    line-height: 1.08;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: linear-gradient(180deg, #b91c1c 0%, #850b0b 60%, #520000 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 3px 6px rgba(255, 255, 255, 0.85));
    margin-top: 6px;
  }}

  .open-year {{
    font-family: 'Oswald', sans-serif;
    font-size: 76px;
    font-weight: 700;
    line-height: 1;
    letter-spacing: 4px;
    color: #d94d1a;
    -webkit-text-stroke: 2.5px #ffffff;
    text-shadow: 0 6px 18px rgba(180, 50, 0, 0.45);
    margin-top: 2px;
  }}

  /* White Capsule Box: Venue & Date/Shotgun */
  .venue-capsule {{
    background: #ffffff;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.18);
    display: flex;
    align-items: center;
    padding: 12px 30px;
    gap: 28px;
    margin-top: 14px;
    border: 1px solid rgba(212, 160, 23, 0.45);
  }}

  .capsule-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }}

  .cap-label {{
    font-size: 12px;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}

  .cap-val {{
    font-family: 'Oswald', sans-serif;
    font-size: 25px;
    font-weight: 700;
    color: #be1e2d;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .capsule-divider {{
    width: 1.5px;
    height: 40px;
    background: #e2e8f0;
  }}

  .notice-time {{
    font-size: 13px;
    font-style: italic;
    font-weight: 700;
    color: #7c2d12;
    margin-top: 9px;
    line-height: 1.3;
  }}

  /* Hole In One Banner Callout */
  .hio-callout {{
    margin-top: 14px;
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 12px;
  }}

  .hio-badge-txt {{
    font-family: 'Oswald', sans-serif;
    font-size: 44px;
    font-weight: 700;
    color: #be1e2d;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 0 2px 0 #ffffff;
  }}

  .hio-billion {{
    font-family: 'Oswald', sans-serif;
    font-size: 78px;
    font-weight: 700;
    color: #be1e2d;
    line-height: 0.9;
    letter-spacing: 1px;
    text-shadow: 0 4px 10px rgba(0,0,0,0.25);
  }}

  .hio-sub-note {{
    font-size: 13.5px;
    font-weight: 800;
    color: #ffffff;
    background: #ea580c;
    padding: 4px 16px;
    border-radius: 20px;
    display: inline-block;
    margin-top: 4px;
    text-shadow: 0 1px 2px rgba(0,0,0,0.3);
  }}

  /* Segmented Fan Arch Photo Collage (EXPANDED TO FULL PROPORTION) */
  .fan-container {{
    position: relative;
    width: 820px;
    height: 400px;
    margin-top: 14px;
    display: flex;
    justify-content: center;
  }}

  .fan-arch {{
    width: 780px;
    height: 390px;
    position: relative;
  }}

  .fan-slice {{
    position: absolute;
    width: 220px;
    height: 350px;
    border-radius: 120px 120px 0 0;
    border: 4px solid #FFD700;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    background: #000;
  }}

  .fan-slice img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  .slice-1 {{
    left: 20px;
    bottom: 0;
    transform: rotate(-30deg);
    transform-origin: bottom center;
  }}

  .slice-2 {{
    left: 155px;
    bottom: 15px;
    transform: rotate(-15deg);
    transform-origin: bottom center;
  }}

  .slice-3 {{
    left: 280px;
    bottom: 30px;
    transform: rotate(0deg);
    z-index: 3;
    border-color: #ffffff;
    width: 230px;
    height: 365px;
  }}

  .slice-4 {{
    right: 155px;
    bottom: 15px;
    transform: rotate(15deg);
    transform-origin: bottom center;
  }}

  .slice-5 {{
    right: 20px;
    bottom: 0;
    transform: rotate(30deg);
    transform-origin: bottom center;
  }}

  /* Clean Golfer Cutout */
  .hero-golfer-wrap {{
    position: absolute;
    bottom: 135px;
    left: 50%;
    transform: translateX(-50%);
    width: 580px;
    height: 640px;
    z-index: 25;
    pointer-events: none;
    display: flex;
    justify-content: center;
    align-items: flex-end;
  }}

  .hero-golfer-wrap img {{
    height: 620px;
    width: auto;
    filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.7));
  }}

  /* QR Code Box on Left Page */
  .left-qr-box {{
    position: absolute;
    bottom: 150px;
    right: 45px;
    z-index: 30;
    background: #ffffff;
    border-radius: 12px;
    padding: 8px 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.28);
  }}

  .left-qr-box svg {{
    width: 72px;
    height: 72px;
  }}

  .left-qr-lbl {{
    font-size: 9.5px;
    font-weight: 800;
    color: #1e293b;
    text-transform: uppercase;
  }}


  /* ============================================================
     RIGHT PAGE: PROGRAM, PRIZES, FEE, PAYMENT & BANNER
     ============================================================ */
  .right-page {{
    width: 1024px;
    height: 1896px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(145deg, #c41c1c 0%, #a40e1b 50%, #780611 100%);
    padding: 42px 50px 145px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .right-page::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 85% 12%, rgba(255, 215, 0, 0.16) 0%, transparent 50%),
                radial-gradient(circle at 12% 88%, rgba(0, 0, 0, 0.35) 0%, transparent 60%);
    pointer-events: none;
  }}

  .section-headline {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    font-size: 30px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: #ffffff;
    margin-bottom: 22px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.35);
  }}

  .section-headline span.dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #FFD700;
    display: inline-block;
  }}

  /* Timeline Program */
  .timeline-container {{
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 28px;
  }}

  .timeline-row {{
    display: flex;
    align-items: flex-start;
    gap: 20px;
    position: relative;
  }}

  .tl-bullet {{
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #ffffff;
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.85);
    margin-top: 6px;
    flex-shrink: 0;
  }}

  .tl-content {{
    flex: 1;
  }}

  .tl-time {{
    font-family: 'Oswald', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #FFD700;
    letter-spacing: 1.2px;
    line-height: 1.1;
  }}

  .tl-desc {{
    font-size: 16.5px;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.4;
    margin-top: 3px;
  }}

  /* Wreaths Prize Structure Section */
  .prizes-wrap {{
    margin-bottom: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}

  .wreath-top {{
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
  }}

  .wreath-grid-4 {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    width: 100%;
  }}

  .wreath-card {{
    position: relative;
    width: 155px;
    height: 155px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
  }}

  .wreath-card.is-top {{
    width: 180px;
    height: 180px;
  }}

  .wreath-graphic {{
    position: absolute;
    inset: 0;
  }}

  .wreath-inner {{
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 0 12px;
  }}

  .w-num {{
    font-family: 'Oswald', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1;
  }}

  .wreath-card.is-top .w-num {{
    font-size: 38px;
    color: #FFD700;
  }}

  .w-title {{
    font-size: 13.5px;
    font-weight: 800;
    color: #ffffff;
    text-transform: uppercase;
    line-height: 1.25;
    margin-top: 3px;
  }}

  .wreath-card.is-top .w-title {{
    font-size: 15.5px;
    color: #ffffff;
  }}

  .w-sub {{
    font-size: 10.5px;
    font-weight: 700;
    color: #ffe4e6;
    margin-top: 3px;
  }}

  /* Fee Box */
  .fee-section {{
    text-align: center;
    margin-bottom: 24px;
  }}

  .fee-tag {{
    font-size: 20px;
    font-weight: 800;
    color: #FFD700;
    text-transform: uppercase;
    letter-spacing: 2.5px;
  }}

  .fee-amount {{
    font-family: 'Montserrat', sans-serif;
    font-size: 58px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 1px;
    line-height: 1.1;
    margin: 6px 0;
    text-shadow: 0 4px 18px rgba(0,0,0,0.35);
  }}

  .fee-include {{
    font-size: 14px;
    font-style: italic;
    font-weight: 600;
    color: #fef2f2;
    line-height: 1.45;
  }}

  /* Payment Section */
  .payment-section {{
    background: rgba(0, 0, 0, 0.25);
    border: 1.5px solid rgba(255, 215, 0, 0.45);
    border-radius: 18px;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 22px;
    margin-bottom: 12px;
  }}

  .pay-qr {{
    background: #ffffff;
    padding: 8px;
    border-radius: 12px;
    flex-shrink: 0;
  }}

  .pay-qr svg {{
    width: 82px;
    height: 82px;
    display: block;
  }}

  .pay-info {{
    flex: 1;
    font-size: 14.5px;
    color: #f8fafc;
    line-height: 1.55;
  }}

  .pay-title {{
    font-size: 15px;
    font-weight: 800;
    color: #FFD700;
    text-transform: uppercase;
    margin-bottom: 4px;
    letter-spacing: 0.8px;
  }}

  .pay-row {{
    display: flex;
    gap: 8px;
  }}

  .pay-row span.val {{
    font-weight: 800;
    color: #ffffff;
  }}


  /* ============================================================
     FOOTER BAR (Spanning across full bottom)
     ============================================================ */
  .global-footer {{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 2048px;
    height: 130px;
    background: #d83a14;
    border-top: 3.5px solid #FFD700;
    z-index: 100;
    display: flex;
    align-items: center;
    padding: 0 45px;
  }}

  .footer-left-label {{
    width: 330px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-right: 2px solid rgba(255, 255, 255, 0.35);
    padding-right: 25px;
    flex-shrink: 0;
  }}

  .ft-title-main {{
    font-size: 19px;
    font-weight: 900;
    text-transform: uppercase;
    color: #ffffff;
    letter-spacing: 1px;
    line-height: 1.15;
  }}

  .ft-title-sub {{
    font-size: 13.5px;
    font-weight: 700;
    color: #ffe4e6;
    margin-top: 4px;
  }}

  .footer-contacts-cols {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 35px;
  }}

  .ft-group {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .ft-group-title {{
    font-size: 13px;
    font-weight: 800;
    color: #FFD700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }}

  .ft-row {{
    display: flex;
    align-items: center;
    gap: 18px;
    font-size: 14px;
    color: #ffffff;
    font-weight: 600;
  }}

  .ft-row span.phone {{
    font-family: 'Oswald', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
  }}
</style>
</head>
<body>

<div class="poster-spread">

  <!-- ================= LEFT PAGE ================= -->
  <div class="left-page">
    <div class="left-bg-img"></div>

    <div class="left-content">
      <!-- Logos -->
      <div class="left-logos">
        <img class="ldo" src="assets/images/logo_lao_dong_official.png" alt="Báo Lao Động" />
        <div class="logo-sep"></div>
        <div class="tsn-wrap">{tsn_svg_content}</div>
      </div>

      <!-- Thư mời -->
      <div class="script-thu-moi">Thư mời</div>

      <!-- Invitation text -->
      <div class="sub-invitation">TRÂN TRỌNG KÍNH MỜI</div>
      <div class="sub-for-who">QUÝ GOLFER & QUÝ DOANH NHÂN</div>
      <div class="sub-participate">THAM DỰ GIẢI GOLF</div>

      <!-- Main Title -->
      <h1 class="main-tournament-title">BÁO LAO ĐỘNG</h1>
      <div class="open-year">OPEN 2026</div>

      <!-- White Venue & Date Capsule -->
      <div class="venue-capsule">
        <div class="capsule-col">
          <div class="cap-label">SÂN THI ĐẤU</div>
          <div class="cap-val">SÂN GOLF TÂN SƠN NHẤT</div>
        </div>
        <div class="capsule-divider"></div>
        <div class="capsule-col">
          <div class="cap-label">XUẤT PHÁT ĐỒNG LOẠT</div>
          <div class="cap-val">SHOTGUN 12:00 • 15/11/2026</div>
        </div>
      </div>

      <div class="notice-time">
        * Các golfer vui lòng có mặt muộn nhất lúc 11:15AM tại sảnh chính để check-in & chụp ảnh khai mạc *
      </div>

      <!-- Hole in One Callout -->
      <div class="hio-callout">
        <div class="hio-badge-txt">HOLE IN ONE</div>
        <div class="hio-billion">XE VINFAST</div>
      </div>
      <div>
        <span class="hio-sub-note">VF 7, VF 3 & BỘ GẬY PRGR • TỔNG GIẢI THƯỞNG HÀNG TỶ ĐỒNG</span>
      </div>

      <!-- Segmented Fan Arch Photo Collage (EXPANDED TO FULL PROPORTION) -->
      <div class="fan-container">
        <div class="fan-arch">
          <!-- Slice 1: Palm trees & fairway -->
          <div class="fan-slice slice-1">
            <img src="assets/images/tsn_course_landscape.jpg" />
          </div>
          <!-- Slice 2: Fairway panorama -->
          <div class="fan-slice slice-2">
            <img src="assets/images/tsn_course_fairway_panorama.jpg" />
          </div>
          <!-- Slice 3: Clubhouse night -->
          <div class="fan-slice slice-3">
            <img src="assets/images/tsn_clubhouse_night.jpg" />
          </div>
          <!-- Slice 4: Greens water -->
          <div class="fan-slice slice-4">
            <img src="assets/images/tsn_course_greens_water.jpg" />
          </div>
          <!-- Slice 5: Aerial fairway -->
          <div class="fan-slice slice-5">
            <img src="assets/images/tsn_aerial_twilight_fairway.jpg" />
          </div>
        </div>
      </div>
    </div>

    <!-- Clean Golfer Cutout -->
    <div class="hero-golfer-wrap">
      <img src="assets/images/golfer_cutout_clean.png" alt="Golfer Action" />
    </div>

    <!-- QR Code on left page -->
    <div class="left-qr-box">
      <svg viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="2" fill="#be1e2d"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="66" y="10" width="24" height="24" rx="2" fill="#be1e2d"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="10" y="66" width="24" height="24" rx="2" fill="#be1e2d"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#be1e2d"/>
        <rect x="40" y="40" width="20" height="20" rx="2" fill="#d4a017"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
        <rect x="42" y="68" width="6" height="6" fill="#111"/>
        <rect x="68" y="68" width="6" height="6" fill="#111"/>
      </svg>
      <div class="left-qr-lbl">QUÉT ĐĂNG KÝ</div>
    </div>
  </div>


  <!-- ================= RIGHT PAGE ================= -->
  <div class="right-page">
    
    <!-- Top: Program -->
    <div>
      <div class="section-headline">
        <span class="dot"></span>
        <span>CHƯƠNG TRÌNH GIẢI ĐẤU</span>
        <span class="dot"></span>
      </div>

      <div class="timeline-container">
        <div class="timeline-row">
          <div class="tl-bullet"></div>
          <div class="tl-content">
            <div class="tl-time">09H00 - 11H15</div>
            <div class="tl-desc">Đón khách, check-in & tặng quà Doorgift cao cấp</div>
          </div>
        </div>

        <div class="timeline-row">
          <div class="tl-bullet"></div>
          <div class="tl-content">
            <div class="tl-time">11H15 - 11H45</div>
            <div class="tl-desc">Dùng tiệc trưa nhẹ theo coupon tại nhà hàng sân Tân Sơn Nhất</div>
          </div>
        </div>

        <div class="timeline-row">
          <div class="tl-bullet"></div>
          <div class="tl-content">
            <div class="tl-time">11H45</div>
            <div class="tl-desc">Tập trung khai mạc trang trọng, chụp ảnh lưu niệm & di chuyển ra xe điện</div>
          </div>
        </div>

        <div class="timeline-row">
          <div class="tl-bullet"></div>
          <div class="tl-content">
            <div class="tl-time">12H00</div>
            <div class="tl-desc">SHOTGUN thi đấu đồng loạt 18 hố kịch tính</div>
          </div>
        </div>

        <div class="timeline-row">
          <div class="tl-bullet"></div>
          <div class="tl-content">
            <div class="tl-time">18H00 - 20H30</div>
            <div class="tl-desc">Gala Dinner & Trao giải vinh danh tại Sảnh Grand Ballroom (Lầu 3 Nhà Hội Viên TSN)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Middle: Prize Structure Laurel Wreaths -->
    <div class="prizes-wrap">
      <div class="section-headline" style="font-size: 24px; margin-bottom: 14px;">
        <span>🏆 CƠ CẤU GIẢI THƯỞNG 🏆</span>
      </div>

      <!-- Top wreath: Best Gross -->
      <div class="wreath-top">
        {make_wreath_svg("01", "GIẢI BEST GROSS", "Cúp Vô Địch Toàn Giải", is_top=True)}
      </div>

      <!-- 4 Wreaths Grid -->
      <div class="wreath-grid-4">
        {make_wreath_svg("GIẢI", "NHẤT", "Bảng A, B, C, Nữ")}
        {make_wreath_svg("GIẢI", "NHÌ", "Bảng A, B, C, Nữ")}
        {make_wreath_svg("02", "NEAREST", "To The Pin")}
        {make_wreath_svg("02", "LONGEST", "Drive")}
      </div>
    </div>

    <!-- Fee Section -->
    <div class="fee-section">
      <div class="fee-tag">PHÍ THAM DỰ</div>
      <div class="fee-amount">3.500.000 <span style="font-size: 30px; font-weight:700;">VNĐ/Golfer</span></div>
      <div class="fee-include">
        (Bao gồm: Green fee 18 hố, Caddie, xe điện Buggy, ăn trưa nhẹ, tiệc tối Gala Dinner sang trọng, áo thi đấu & mũ quà tặng)
      </div>
    </div>

    <!-- Payment Section -->
    <div class="payment-section">
      <div class="pay-qr">
        <svg viewBox="0 0 100 100" fill="#000">
          <rect x="10" y="10" width="24" height="24" rx="2" fill="#be1e2d"/>
          <rect x="15" y="15" width="14" height="14" fill="#fff"/>
          <rect x="18" y="18" width="8" height="8" fill="#be1e2d"/>
          <rect x="66" y="10" width="24" height="24" rx="2" fill="#be1e2d"/>
          <rect x="71" y="15" width="14" height="14" fill="#fff"/>
          <rect x="74" y="18" width="8" height="8" fill="#be1e2d"/>
          <rect x="10" y="66" width="24" height="24" rx="2" fill="#be1e2d"/>
          <rect x="15" y="71" width="14" height="14" fill="#fff"/>
          <rect x="18" y="74" width="8" height="8" fill="#be1e2d"/>
          <rect x="40" y="40" width="20" height="20" rx="2" fill="#d4a017"/>
          <rect x="44" y="44" width="12" height="12" fill="#fff"/>
          <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
          <rect x="42" y="12" width="6" height="6" fill="#111"/>
          <rect x="52" y="12" width="6" height="6" fill="#111"/>
          <rect x="68" y="42" width="6" height="6" fill="#111"/>
          <rect x="42" y="68" width="6" height="6" fill="#111"/>
          <rect x="68" y="68" width="6" height="6" fill="#111"/>
        </svg>
      </div>
      <div class="pay-info">
        <div class="pay-title">THÔNG TIN TIẾP NHẬN & THANH TOÁN</div>
        <div class="pay-row"><span>Tên tài khoản:</span> <span class="val">BÁO LAO ĐỘNG</span></div>
        <div class="pay-row"><span>Số tài khoản:</span> <span class="val" style="color:#FFD700;">0918 658 465</span></div>
        <div class="pay-row"><span>Ngân hàng:</span> <span class="val">BIDV (Chi nhánh TP.HCM)</span></div>
        <div class="pay-row"><span>Nội dung chuyển khoản:</span> <span class="val">Họ và Tên Golfer + Số ĐT</span></div>
      </div>
    </div>

  </div>

  <!-- ================= GLOBAL BOTTOM FOOTER BAR ================= -->
  <div class="global-footer">
    <div class="footer-left-label">
      <div class="ft-title-main">THÔNG TIN LIÊN HỆ</div>
      <div class="ft-title-sub">BAN TỔ CHỨC & ĐIỀU PHỐI SÂN</div>
    </div>

    <div class="footer-contacts-cols">
      <!-- Ban Tổ Chức (Thanh Uyên, Bá Trường, Đăng Văn) -->
      <div class="ft-group">
        <div class="ft-group-title">BAN TỔ CHỨC BÁO LAO ĐỘNG</div>
        <div class="ft-row">
          <div>Nhà báo Thanh Uyên: <span class="phone">0932 311 012</span></div>
          <div>•</div>
          <div>Nhà báo Bá Trường: <span class="phone">0918 658 465</span></div>
          <div>•</div>
          <div>Nhà báo Đăng Văn: <span class="phone">090 556 7395</span></div>
        </div>
      </div>

      <!-- Sân Golf TSN (Paky Nhất, Quang, Lệ Quyên, Dương Trang, Hồng Hạnh) -->
      <div class="ft-group" style="margin-left: 20px;">
        <div class="ft-group-title">BỘ PHẬN ĐIỀU PHỐI SÂN GOLF TÂN SƠN NHẤT</div>
        <div class="ft-row" style="font-size: 13.5px;">
          <div>Mr. Paky Nhất: <span class="phone">0909 282 861</span></div>
          <div>•</div>
          <div>Mr Quang: <span class="phone">0973 777 589</span></div>
          <div>•</div>
          <div>Ms. Lệ Quyên: <span class="phone">0939 301 090</span></div>
          <div>•</div>
          <div>Ms. Dương Trang: <span class="phone">0909 059 990</span></div>
          <div>•</div>
          <div>Ms. Hồng Hạnh: <span class="phone">0969 214 289</span></div>
        </div>
      </div>
    </div>
  </div>

</div>

</body>
</html>
"""

with open(WORKSPACE / "poster_invitation_2page.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved updated poster_invitation_2page.html successfully!")
