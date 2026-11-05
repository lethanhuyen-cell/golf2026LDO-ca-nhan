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

# -------------------------------------------------------------
# 1. MOBILE VIP POSTER (9:16 - 1080 x 1920)
# -------------------------------------------------------------
html_mobile = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>Poster Giải Golf Báo Lao Động Open 2026 - Mobile 9:16 Augusta Masters Green</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Playfair+Display:ital,wght@0,700;1,600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    position: relative;
    background: #01140b;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}

  /* Augusta Masters Green Canvas */
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 80% 12%, rgba(10, 108, 64, 0.45) 0%, transparent 55%),
      radial-gradient(circle at 20% 75%, rgba(0, 77, 44, 0.5) 0%, transparent 60%),
      radial-gradient(circle at 50% 50%, rgba(0, 51, 25, 0.85) 0%, #01140b 100%);
    z-index: 1;
  }}

  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.28;
    filter: saturate(1.3) contrast(1.15);
    mix-blend-mode: luminosity;
    z-index: 2;
  }}

  .bg-glow-gold {{
    position: absolute;
    top: 220px;
    left: 50%;
    transform: translateX(-50%);
    width: 850px;
    height: 380px;
    background: radial-gradient(ellipse, rgba(197, 160, 89, 0.22) 0%, transparent 70%);
    z-index: 3;
    pointer-events: none;
  }}

  .poster-wrapper {{
    position: relative;
    z-index: 10;
    width: 1080px;
    height: 1920px;
    padding: 42px 48px 36px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Header Bar */
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(1, 36, 19, 0.75);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1.5px solid rgba(197, 160, 89, 0.45);
    border-radius: 20px;
    padding: 15px 28px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
  }}

  .logos-group {{
    display: flex;
    align-items: center;
    gap: 22px;
  }}

  .logo-ldo-wrap {{
    background: #ffffff;
    padding: 6px 14px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    display: flex;
    align-items: center;
  }}

  .logo-ldo-wrap img {{
    height: 40px;
    width: auto;
    display: block;
  }}

  .logo-divider {{
    width: 2px;
    height: 38px;
    background: linear-gradient(180deg, transparent, rgba(197, 160, 89, 0.9), transparent);
  }}

  .tsn-logo-wrap {{
    height: 44px;
    display: flex;
    align-items: center;
  }}

  .tsn-logo-wrap svg {{
    height: 35px;
    width: auto;
  }}

  .badge-milestone {{
    background: linear-gradient(135deg, #BE1E2D 0%, #87000E 100%);
    border: 1.5px solid #FFD700;
    color: #ffffff;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 16px rgba(190, 30, 45, 0.5);
  }}

  .badge-milestone span.gold {{
    color: #FFD700;
  }}

  /* Title Block */
  .title-block {{
    text-align: center;
    margin-top: 10px;
  }}

  .sub-tag {{
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 8px;
    text-transform: uppercase;
    color: #c5a059;
    text-shadow: 0 2px 8px rgba(0,0,0,0.9);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-bottom: 6px;
  }}

  .sub-tag::before, .sub-tag::after {{
    content: '';
    display: inline-block;
    width: 65px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c5a059);
  }}
  .sub-tag::after {{
    background: linear-gradient(90deg, #c5a059, transparent);
  }}

  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 64px;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF3DB 40%, #C5A059 85%, #99742A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 6px 18px rgba(0, 0, 0, 0.95));
  }}

  .open-pill {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(90deg, #BE1E2D 0%, #DA251D 50%, #BE1E2D 100%);
    border: 2px solid #FFD700;
    border-radius: 40px;
    padding: 6px 36px;
    font-size: 30px;
    font-weight: 900;
    letter-spacing: 6px;
    color: #ffffff;
    box-shadow: 0 8px 25px rgba(190, 30, 45, 0.6);
    margin-top: 6px;
  }}

  /* Meta Bar */
  .meta-bar {{
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 14px;
  }}

  .meta-item {{
    background: rgba(0, 35, 18, 0.75);
    border: 1px solid rgba(197, 160, 89, 0.5);
    border-radius: 12px;
    padding: 9px 20px;
    display: flex;
    align-items: center;
    gap: 9px;
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
  }}

  .meta-item .highlight {{
    color: #FFD700;
    font-weight: 800;
  }}

  /* Key Visual / Hero Showcase Section */
  .hero-visual-box {{
    margin-top: 12px;
    background: linear-gradient(135deg, rgba(0, 45, 25, 0.88) 0%, rgba(1, 25, 14, 0.94) 100%);
    border: 2px solid rgba(197, 160, 89, 0.7);
    border-radius: 20px;
    padding: 16px 22px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    align-items: center;
    gap: 20px;
    position: relative;
    overflow: hidden;
  }}

  .hero-visual-box::before {{
    content: 'HOLE IN ONE';
    position: absolute;
    right: -15px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Cinzel', serif;
    font-size: 82px;
    font-weight: 900;
    color: rgba(197, 160, 89, 0.06);
    white-space: nowrap;
    pointer-events: none;
    letter-spacing: 4px;
  }}

  .visual-left {{
    flex: 1;
    position: relative;
    z-index: 2;
  }}

  .hio-badge {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(90deg, #C5A059, #FFD700);
    color: #012413;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 1.5px;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }}

  .hio-title {{
    font-size: 26px;
    font-weight: 900;
    line-height: 1.2;
    color: #ffffff;
    text-transform: uppercase;
  }}

  .hio-title span.cars {{
    color: #FFD700;
    text-shadow: 0 0 16px rgba(255, 215, 0, 0.6);
  }}

  .hio-sub {{
    font-size: 14px;
    color: #E4CA8C;
    margin-top: 5px;
    font-weight: 600;
    line-height: 1.35;
  }}

  .visual-media {{
    display: flex;
    align-items: center;
    gap: 12px;
    position: relative;
    z-index: 2;
  }}

  .media-thumb {{
    width: 145px;
    height: 84px;
    border-radius: 10px;
    border: 1.5px solid rgba(197, 160, 89, 0.6);
    object-fit: cover;
    box-shadow: 0 6px 16px rgba(0,0,0,0.6);
  }}

  /* 2-Column Grid: Prize & Package */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 12px;
  }}

  .card-box {{
    background: rgba(0, 30, 16, 0.8);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .card-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid rgba(197, 160, 89, 0.3);
    padding-bottom: 11px;
    margin-bottom: 11px;
  }}

  .card-icon {{
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #0A6C40, #004D2C);
    border: 1px solid rgba(197, 160, 89, 0.6);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    color: #fff;
    flex-shrink: 0;
  }}

  .card-title {{
    font-size: 17px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #FFD700;
  }}

  .prize-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}

  .prize-list li {{
    font-size: 14.5px;
    line-height: 1.35;
    color: #f0f0f0;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }}

  .prize-list li::before {{
    content: '◆';
    color: #C5A059;
    font-size: 10px;
    margin-top: 3px;
    flex-shrink: 0;
  }}

  .prize-list li strong {{
    color: #ffffff;
    font-weight: 700;
  }}

  .fee-badge {{
    background: linear-gradient(135deg, #0a5231 0%, #003319 100%);
    border: 1.5px solid #FFD700;
    border-radius: 12px;
    padding: 10px 12px;
    text-align: center;
    margin-bottom: 11px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }}

  .fee-badge .price {{
    font-size: 25px;
    font-weight: 900;
    color: #FFD700;
    letter-spacing: 0.5px;
  }}

  .fee-badge .note {{
    font-size: 12.5px;
    color: #E4CA8C;
    margin-top: 3px;
    font-weight: 600;
  }}

  /* Schedule Box */
  .schedule-box {{
    margin-top: 12px;
    background: rgba(0, 25, 13, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(197, 160, 89, 0.45);
    border-radius: 18px;
    padding: 16px 22px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.45);
  }}

  .timeline-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    margin-top: 11px;
  }}

  .timeline-step {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(197, 160, 89, 0.25);
    border-radius: 12px;
    padding: 10px 8px;
    text-align: center;
  }}

  .timeline-step.active {{
    background: linear-gradient(180deg, rgba(10, 108, 64, 0.45) 0%, rgba(0, 51, 25, 0.55) 100%);
    border-color: #FFD700;
  }}

  .step-time {{
    font-size: 13.5px;
    font-weight: 800;
    color: #FFD700;
    margin-bottom: 4px;
  }}

  .step-name {{
    font-size: 12px;
    font-weight: 700;
    color: #e5e5e5;
    line-height: 1.3;
  }}

  /* Bottom Contacts & QR Box */
  .footer-contact {{
    margin-top: 12px;
    background: linear-gradient(180deg, rgba(1, 28, 15, 0.96) 0%, rgba(0, 17, 9, 0.98) 100%);
    border: 1.8px solid #C5A059;
    border-radius: 20px;
    padding: 16px 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
  }}

  .contact-col {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
  }}

  .section-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    font-weight: 800;
    color: #FFD700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .contacts-line {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px 18px;
    font-size: 13.5px;
    color: #ffffff;
    font-weight: 600;
  }}

  .person-item {{
    display: flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
  }}

  .person-item .phone {{
    color: #FFD700;
    font-weight: 800;
  }}

  .qr-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    background: #ffffff;
    padding: 8px 10px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    flex-shrink: 0;
  }}

  .qr-svg {{
    width: 78px;
    height: 78px;
  }}

  .qr-label {{
    font-size: 9.5px;
    font-weight: 800;
    color: #012413;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
  }}
</style>
</head>
<body>

<div class="bg-canvas"></div>
<div class="bg-course"></div>
<div class="bg-glow-gold"></div>

<div class="poster-wrapper">

  <!-- Header -->
  <div class="header-bar">
    <div class="logos-group">
      <div class="logo-ldo-wrap">
        <img src="assets/images/logo_lao_dong_official.png" alt="Báo Lao Động" />
      </div>
      <div class="logo-divider"></div>
      <div class="tsn-logo-wrap">
        {tsn_svg_content}
      </div>
    </div>
    <div class="badge-milestone">
      <span>⛳ KỶ NIỆM <span class="gold">97 NĂM</span> BÁO LAO ĐỘNG</span>
    </div>
  </div>

  <!-- Tournament Title Block -->
  <div class="title-block">
    <div class="sub-tag">GIẢI GOLF TRUYỀN THỐNG ĐỈNH CAO</div>
    <h1 class="main-title">GIẢI GOLF BÁO LAO ĐỘNG</h1>
    <div class="open-pill">OPEN 2026</div>
  </div>

  <!-- Meta Info Bar -->
  <div class="meta-bar">
    <div class="meta-item">
      <span>📍</span>
      <span>SÂN GOLF <span class="highlight">TÂN SƠN NHẤT</span></span>
    </div>
    <div class="meta-item">
      <span>🗓️</span>
      <span>CHỦ NHẬT, <span class="highlight">15.11.2026</span></span>
    </div>
    <div class="meta-item">
      <span>⚡</span>
      <span>SHOTGUN: <span class="highlight">12:00</span></span>
    </div>
  </div>

  <!-- Key Visual Hero Showcase: Golfer Action + VinFast HIO Cars -->
  <div class="hero-visual-box">
    <div class="visual-left">
      <div class="hio-badge">⭐ ĐẠI GIẢI THƯỞNG HOLE-IN-ONE</div>
      <div class="hio-title">XE Ô TÔ <span class="cars">VINFAST VF 7 & VF 3</span></div>
      <div class="hio-sub">CÙNG BỘ GẬY CAO CẤP PRGR & HÀNG TRĂM TRIỆU ĐỒNG TẠI TẤT CẢ CÁC HỐ PAR 3</div>
    </div>
    <div class="visual-media">
      <img src="assets/images/golf_hio_luxury_car_podium.jpg" class="media-thumb" alt="VinFast HIO Podium" />
      <img src="assets/images/golf_trophy_gala.jpg" class="media-thumb" style="width:105px;" alt="Championship Trophy" />
    </div>
  </div>

  <!-- 2 Columns: Prize Structure & Golfer Package -->
  <div class="grid-2col">
    <!-- Col 1: Prizes -->
    <div class="card-box">
      <div>
        <div class="card-header">
          <div class="card-icon">🏆</div>
          <div class="card-title">Cơ Cấu Giải Thưởng</div>
        </div>
        <ul class="prize-list">
          <li><strong>Cúp Best Gross Danh Giá</strong> (Vô địch toàn giải)</li>
          <li><strong>Bảng Nam (A - B - C):</strong> Nhất, Nhì, Ba mỗi bảng</li>
          <li><strong>Bảng Nữ (A - B):</strong> Nhất, Nhì mỗi bảng</li>
          <li><strong>02 Giải Longest Drive</strong> (Đường bóng xa nhất)</li>
          <li><strong>02 Giải Nearest to the Pin</strong> (Bóng gần cờ nhất)</li>
          <li>Hệ thống Cúp mạ vàng thủ công độc quyền</li>
        </ul>
      </div>
    </div>

    <!-- Col 2: Benefits & Fee -->
    <div class="card-box">
      <div>
        <div class="card-header">
          <div class="card-icon">🎁</div>
          <div class="card-title">Quyền Lợi & Phí Tham Dự</div>
        </div>
        <div class="fee-badge">
          <div class="price">3.500.000 VNĐ / GOLFER</div>
          <div class="note">Trọn gói quyền lợi chuẩn dịch vụ cao cấp</div>
        </div>
        <ul class="prize-list">
          <li>Phí sân 18 hố, Caddie chuyên nghiệp & Xe điện Buggy</li>
          <li><strong>Doorgift VIP:</strong> Áo thi đấu, Mũ golf, Phụ kiện quà tặng</li>
          <li>Tiệc trưa buffet nhẹ trước giờ xuất phát</li>
          <li><strong>Đại tiệc Gala Dinner</strong> tối thượng hạng & Bia hảo hạng</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Timeline Schedule -->
  <div class="schedule-box">
    <div class="card-header" style="margin-bottom: 0; padding-bottom: 8px;">
      <div class="card-icon">⏰</div>
      <div class="card-title" style="font-size: 16px;">Lịch Trình Ngày Thi Đấu (Chủ Nhật, 15.11.2026)</div>
    </div>
    <div class="timeline-grid">
      <div class="timeline-step">
        <div class="step-time">09:00 - 11:15</div>
        <div class="step-name">Đón khách • Check-in Ăn trưa nhẹ</div>
      </div>
      <div class="timeline-step">
        <div class="step-time">11:30 - 11:45</div>
        <div class="step-name">Lễ Khai mạc Trang trọng</div>
      </div>
      <div class="timeline-step">
        <div class="step-time">11:45 - 12:00</div>
        <div class="step-name">Di chuyển ra Các Teebox</div>
      </div>
      <div class="timeline-step active">
        <div class="step-time">12:00 - 17:00</div>
        <div class="step-name">Shotgun 18 Hố Đồng loạt</div>
      </div>
      <div class="timeline-step active">
        <div class="step-time">18:00 - 20:30</div>
        <div class="step-name">Gala Dinner & Trao giải (Sảnh Grand)</div>
      </div>
    </div>
  </div>

  <!-- Bottom Contacts Bar & QR Code (Configured Exactly As Requested) -->
  <div class="footer-contact">
    <div class="contact-col">
      <!-- Row 1: Ban Tổ Chức (Thanh Uyên, Bá Trường, Đăng Văn) -->
      <div class="section-tag">
        <span>📞</span> LIÊN HỆ BAN TỔ CHỨC:
      </div>
      <div class="contacts-line">
        <div class="person-item">Nhà báo Thanh Uyên: <span class="phone">0932.311.012</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Nhà báo Bá Trường: <span class="phone">0918.658.465</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Nhà báo Đăng Văn: <span class="phone">090.556.7395</span></div>
      </div>

      <!-- Row 2: Điều Phối Sân TSN (Paky Nhất, Quang, Lệ Quyên, Dương Trang, Hồng Hạnh) -->
      <div class="section-tag" style="margin-top: 6px;">
        <span>⛳</span> BỘ PHẬN ĐIỀU PHỐI SÂN GOLF TÂN SƠN NHẤT:
      </div>
      <div class="contacts-line" style="font-size: 12.8px;">
        <div class="person-item">Mr. Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Mr. Quang: <span class="phone">0973.777.589</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Ms. Lệ Quyên: <span class="phone">0939.301.090</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Ms. Dương Trang: <span class="phone">0909.059.990</span></div>
        <div class="person-item">•</div>
        <div class="person-item">Ms. Hồng Hạnh: <span class="phone">0969.214.289</span></div>
      </div>
    </div>

    <!-- QR Code Scan Box -->
    <div class="qr-box">
      <svg class="qr-svg" viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#004d2c"/>
        
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#004d2c"/>
        
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#004d2c"/>
        
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#c5a059"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
        <rect x="80" y="42" width="6" height="6" fill="#111"/>
        <rect x="42" y="68" width="6" height="6" fill="#111"/>
        <rect x="54" y="68" width="6" height="6" fill="#111"/>
        <rect x="68" y="68" width="6" height="6" fill="#111"/>
        <rect x="78" y="78" width="8" height="8" fill="#111"/>
        <rect x="68" y="82" width="6" height="6" fill="#111"/>
      </svg>
      <div class="qr-label">QUÉT ĐĂNG KÝ<br>ĐIỀU LỆ GIẢI</div>
    </div>
  </div>

</div>

</body>
</html>
"""

# -------------------------------------------------------------
# 2. STANDEE IN ẤN (1200 x 2133 - Standard Rollup Standee)
# -------------------------------------------------------------
html_standee = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1200, height=2133, initial-scale=1.0">
<title>Standee Giải Golf Báo Lao Động Open 2026 - Augusta Masters Green</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px;
    height: 2133px;
    overflow: hidden;
    position: relative;
    background: #01140b;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 80% 12%, rgba(10, 108, 64, 0.45) 0%, transparent 55%),
      radial-gradient(circle at 20% 75%, rgba(0, 77, 44, 0.5) 0%, transparent 60%),
      radial-gradient(circle at 50% 50%, rgba(0, 51, 25, 0.85) 0%, #01140b 100%);
    z-index: 1;
  }}
  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.3;
    filter: saturate(1.3) contrast(1.15);
    mix-blend-mode: luminosity;
    z-index: 2;
  }}
  .standee-wrapper {{
    position: relative;
    z-index: 10;
    width: 1200px;
    height: 2133px;
    padding: 55px 60px 45px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(1, 36, 19, 0.8);
    backdrop-filter: blur(16px);
    border: 1.5px solid rgba(197, 160, 89, 0.5);
    border-radius: 24px;
    padding: 18px 32px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
  }}
  .logos-group {{ display: flex; align-items: center; gap: 24px; }}
  .logo-ldo {{ background: #fff; padding: 8px 16px; border-radius: 12px; }}
  .logo-ldo img {{ height: 48px; width: auto; display: block; }}
  .logo-divider {{ width: 2px; height: 44px; background: rgba(197, 160, 89, 0.8); }}
  .tsn-logo svg {{ height: 42px; width: auto; }}
  .badge-anniversary {{
    background: linear-gradient(135deg, #be1e2d 0%, #87000e 100%);
    border: 1.5px solid #ffd700;
    color: #fff;
    padding: 10px 24px;
    border-radius: 40px;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 2px;
  }}
  .badge-anniversary span {{ color: #ffd700; }}
  
  .title-block {{ text-align: center; margin-top: 15px; }}
  .sub-tag {{
    font-size: 19px; font-weight: 800; letter-spacing: 8px;
    text-transform: uppercase; color: #c5a059; margin-bottom: 8px;
  }}
  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 74px; font-weight: 900; line-height: 1.05;
    text-transform: uppercase;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF3DB 40%, #C5A059 85%, #99742A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .open-pill {{
    display: inline-block;
    background: linear-gradient(90deg, #BE1E2D 0%, #DA251D 50%, #BE1E2D 100%);
    border: 2px solid #FFD700;
    border-radius: 50px;
    padding: 8px 45px;
    font-size: 34px; font-weight: 900; letter-spacing: 8px;
    color: #ffffff; margin-top: 8px;
    box-shadow: 0 10px 30px rgba(190, 30, 45, 0.6);
  }}

  .meta-bar {{
    display: flex; justify-content: center; gap: 24px; margin-top: 18px;
  }}
  .meta-item {{
    background: rgba(0, 35, 18, 0.8);
    border: 1px solid rgba(197, 160, 89, 0.55);
    border-radius: 14px;
    padding: 12px 26px; font-size: 17px; font-weight: 700;
  }}
  .meta-item .gold {{ color: #ffd700; font-weight: 800; }}

  .hero-visual-box {{
    margin-top: 16px;
    background: linear-gradient(135deg, rgba(0, 45, 25, 0.9) 0%, rgba(1, 25, 14, 0.95) 100%);
    border: 2px solid rgba(197, 160, 89, 0.7);
    border-radius: 24px;
    padding: 20px 28px;
    display: flex; align-items: center; justify-content: space-between;
  }}
  .hio-badge {{
    background: linear-gradient(90deg, #c5a059, #ffd700);
    color: #012413; font-size: 14.5px; font-weight: 900;
    letter-spacing: 2px; padding: 5px 16px; border-radius: 20px;
    display: inline-block; margin-bottom: 6px;
  }}
  .hio-title {{ font-size: 30px; font-weight: 900; text-transform: uppercase; color: #fff; }}
  .hio-title span {{ color: #ffd700; }}
  .hio-sub {{ font-size: 15.5px; color: #e4ca8c; margin-top: 6px; font-weight: 600; }}
  .media-group {{ display: flex; align-items: center; gap: 14px; }}
  .media-group img {{ height: 95px; border-radius: 12px; border: 1.5px solid #c5a059; object-fit: cover; }}

  .grid-2col {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px;
  }}
  .card-box {{
    background: rgba(0, 30, 16, 0.85);
    border: 1px solid rgba(197, 160, 89, 0.45);
    border-radius: 20px; padding: 22px 26px;
  }}
  .card-header {{
    display: flex; align-items: center; gap: 12px;
    border-bottom: 1px solid rgba(197, 160, 89, 0.35);
    padding-bottom: 12px; margin-bottom: 14px;
  }}
  .card-icon {{
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #0A6C40, #004D2C);
    border: 1px solid rgba(197, 160, 89, 0.6);
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    font-size: 19px; color: #fff;
  }}
  .card-title {{ font-size: 19px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .card-list {{ list-style: none; display: flex; flex-direction: column; gap: 10px; }}
  .card-list li {{ font-size: 16px; line-height: 1.4; color: #f5f5f5; display: flex; gap: 10px; }}
  .card-list li::before {{ content: '◆'; color: #c5a059; font-size: 11px; margin-top: 3px; }}
  .card-list li strong {{ color: #fff; }}

  .fee-box {{
    background: linear-gradient(135deg, #0a5231 0%, #003319 100%);
    border: 1.5px solid #ffd700; border-radius: 14px;
    padding: 12px 16px; text-align: center; margin-bottom: 14px;
  }}
  .fee-box .price {{ font-size: 28px; font-weight: 900; color: #ffd700; }}
  .fee-box .note {{ font-size: 13.5px; color: #e4ca8c; margin-top: 4px; font-weight: 600; }}

  .schedule-box {{
    margin-top: 16px;
    background: rgba(0, 25, 13, 0.88);
    border: 1px solid rgba(197, 160, 89, 0.5);
    border-radius: 20px; padding: 20px 26px;
  }}
  .timeline-grid {{
    display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-top: 12px;
  }}
  .timeline-step {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(197, 160, 89, 0.25);
    border-radius: 14px; padding: 12px 10px; text-align: center;
  }}
  .timeline-step.active {{
    background: linear-gradient(180deg, rgba(10, 108, 64, 0.45) 0%, rgba(0, 51, 25, 0.6) 100%);
    border-color: #ffd700;
  }}
  .step-time {{ font-size: 14.5px; font-weight: 800; color: #ffd700; margin-bottom: 5px; }}
  .step-name {{ font-size: 12.5px; font-weight: 700; color: #e5e5e5; line-height: 1.35; }}

  .footer-contact {{
    margin-top: 16px;
    background: linear-gradient(180deg, rgba(1, 28, 15, 0.96) 0%, rgba(0, 17, 9, 0.98) 100%);
    border: 2px solid #c5a059; border-radius: 24px;
    padding: 20px 28px; display: flex; align-items: center; justify-content: space-between; gap: 20px;
  }}
  .contact-col {{ display: flex; flex-direction: column; gap: 8px; flex: 1; }}
  .contact-tag {{ font-size: 14px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .contact-row {{ display: flex; flex-wrap: wrap; gap: 10px 18px; font-size: 14.5px; }}
  .contact-row .phone {{ color: #ffd700; font-weight: 800; }}
  .qr-box {{
    background: #fff; padding: 10px 12px; border-radius: 16px;
    display: flex; flex-direction: column; align-items: center; gap: 6px; flex-shrink: 0;
  }}
  .qr-box svg {{ width: 85px; height: 85px; }}
  .qr-box .label {{ font-size: 10px; font-weight: 800; color: #012413; text-transform: uppercase; text-align: center; }}
</style>
</head>
<body>
<div class="bg-canvas"></div>
<div class="bg-course"></div>
<div class="standee-wrapper">

  <div class="header-bar">
    <div class="logos-group">
      <div class="logo-ldo"><img src="assets/images/logo_lao_dong_official.png" /></div>
      <div class="logo-divider"></div>
      <div class="tsn-logo">{tsn_svg_content}</div>
    </div>
    <div class="badge-anniversary">⛳ KỶ NIỆM <span>97 NĂM</span> BÁO LAO ĐỘNG</div>
  </div>

  <div class="title-block">
    <div class="sub-tag">GIẢI GOLF TRUYỀN THỐNG ĐỈNH CAO</div>
    <h1 class="main-title">GIẢI GOLF BÁO LAO ĐỘNG</h1>
    <div class="open-pill">OPEN 2026</div>
  </div>

  <div class="meta-bar">
    <div class="meta-item">📍 SÂN GOLF <span class="gold">TÂN SƠN NHẤT</span></div>
    <div class="meta-item">🗓️ CHỦ NHẬT, <span class="gold">15.11.2026</span></div>
    <div class="meta-item">⚡ SHOTGUN: <span class="gold">12:00</span></div>
  </div>

  <div class="hero-visual-box">
    <div>
      <div class="hio-badge">⭐ ĐẠI GIẢI THƯỞNG HOLE-IN-ONE</div>
      <div class="hio-title">XE Ô TÔ <span>VINFAST VF 7 & VF 3</span></div>
      <div class="hio-sub">CÙNG BỘ GẬY CAO CẤP PRGR & HÀNG TRĂM TRIỆU ĐỒNG TẠI TẤT CẢ CÁC HỐ PAR 3</div>
    </div>
    <div class="media-group">
      <img src="assets/images/golf_hio_luxury_car_podium.jpg" style="width:160px;" />
      <img src="assets/images/golf_trophy_gala.jpg" style="width:115px;" />
    </div>
  </div>

  <div class="grid-2col">
    <div class="card-box">
      <div class="card-header">
        <div class="card-icon">🏆</div>
        <div class="card-title">Cơ Cấu Giải Thưởng</div>
      </div>
      <ul class="card-list">
        <li><strong>Cúp Best Gross Danh Giá</strong> (Vô địch toàn giải)</li>
        <li><strong>Bảng Nam (A - B - C):</strong> Nhất, Nhì, Ba mỗi bảng</li>
        <li><strong>Bảng Nữ (A - B):</strong> Nhất, Nhì mỗi bảng</li>
        <li><strong>02 Giải Longest Drive</strong> (Đường bóng xa nhất)</li>
        <li><strong>02 Giải Nearest to the Pin</strong> (Bóng gần cờ nhất)</li>
        <li>Hệ thống Cúp mạ vàng chế tác độc quyền</li>
      </ul>
    </div>

    <div class="card-box">
      <div class="card-header">
        <div class="card-icon">🎁</div>
        <div class="card-title">Quyền Lợi & Phí Tham Dự</div>
      </div>
      <div class="fee-box">
        <div class="price">3.500.000 VNĐ / GOLFER</div>
        <div class="note">Trọn gói quyền lợi chuẩn dịch vụ cao cấp</div>
      </div>
      <ul class="card-list">
        <li>Phí sân 18 hố, Caddie chuyên nghiệp & Xe điện Buggy</li>
        <li><strong>Doorgift VIP:</strong> Áo thi đấu, Mũ golf, Phụ kiện quà tặng</li>
        <li>Tiệc trưa buffet nhẹ trước giờ xuất phát</li>
        <li><strong>Đại tiệc Gala Dinner</strong> tối thượng hạng & Bia hảo hạng</li>
      </ul>
    </div>
  </div>

  <div class="schedule-box">
    <div class="card-header" style="margin-bottom:0; padding-bottom:10px;">
      <div class="card-icon">⏰</div>
      <div class="card-title" style="font-size: 17px;">Lịch Trình Ngày Thi Đấu (Chủ Nhật, 15.11.2026)</div>
    </div>
    <div class="timeline-grid">
      <div class="timeline-step">
        <div class="step-time">09:00 - 11:15</div>
        <div class="step-name">Đón khách • Check-in Ăn trưa nhẹ</div>
      </div>
      <div class="timeline-step">
        <div class="step-time">11:30 - 11:45</div>
        <div class="step-name">Lễ Khai mạc Trang trọng</div>
      </div>
      <div class="timeline-step">
        <div class="step-time">11:45 - 12:00</div>
        <div class="step-name">Di chuyển ra Teebox</div>
      </div>
      <div class="timeline-step active">
        <div class="step-time">12:00 - 17:00</div>
        <div class="step-name">Shotgun 18 Hố Đồng loạt</div>
      </div>
      <div class="timeline-step active">
        <div class="step-time">18:00 - 20:30</div>
        <div class="step-name">Gala Dinner & Trao giải (Sảnh Grand)</div>
      </div>
    </div>
  </div>

  <div class="footer-contact">
    <div class="contact-col">
      <div class="contact-tag">📞 LIÊN HỆ BAN TỔ CHỨC:</div>
      <div class="contact-row">
        <div>Nhà báo Thanh Uyên: <span class="phone">0932.311.012</span></div>
        <div>•</div>
        <div>Nhà báo Bá Trường: <span class="phone">0918.658.465</span></div>
        <div>•</div>
        <div>Nhà báo Đăng Văn: <span class="phone">090.556.7395</span></div>
      </div>
      <div class="contact-tag" style="margin-top: 8px;">⛳ BỘ PHẬN ĐIỀU PHỐI SÂN GOLF TÂN SƠN NHẤT:</div>
      <div class="contact-row" style="font-size: 13.8px;">
        <div>Mr. Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div>•</div>
        <div>Mr. Quang: <span class="phone">0973.777.589</span></div>
        <div>•</div>
        <div>Ms. Lệ Quyên: <span class="phone">0939.301.090</span></div>
        <div>•</div>
        <div>Ms. Dương Trang: <span class="phone">0909.059.990</span></div>
        <div>•</div>
        <div>Ms. Hồng Hạnh: <span class="phone">0969.214.289</span></div>
      </div>
    </div>

    <div class="qr-box">
      <svg viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#004d2c"/>
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#004d2c"/>
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#004d2c"/>
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#c5a059"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
        <rect x="42" y="68" width="6" height="6" fill="#111"/>
        <rect x="68" y="68" width="6" height="6" fill="#111"/>
      </svg>
      <div class="label">QUÉT ĐĂNG KÝ<br>ĐIỀU LỆ GIẢI</div>
    </div>
  </div>

</div>
</body>
</html>
"""

# -------------------------------------------------------------
# 3. BANNER LED & EMAIL (1920 x 1080 - 16:9)
# -------------------------------------------------------------
html_banner = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1920, height=1080, initial-scale=1.0">
<title>Banner LED Giải Golf Báo Lao Động Open 2026 - 16:9 Augusta Masters Green</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    overflow: hidden;
    position: relative;
    background: #01140b;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 75% 25%, rgba(10, 108, 64, 0.45) 0%, transparent 60%),
      radial-gradient(circle at 15% 75%, rgba(0, 77, 44, 0.4) 0%, transparent 55%),
      radial-gradient(circle at 50% 50%, rgba(0, 51, 25, 0.88) 0%, #01140b 100%);
    z-index: 1;
  }}
  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.28;
    mix-blend-mode: luminosity;
    z-index: 2;
  }}
  .banner-wrapper {{
    position: relative;
    z-index: 10;
    width: 1920px;
    height: 1080px;
    padding: 38px 55px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(1, 36, 19, 0.8);
    backdrop-filter: blur(16px);
    border: 1.5px solid rgba(197, 160, 89, 0.45);
    border-radius: 20px;
    padding: 14px 28px;
  }}
  .logos-group {{ display: flex; align-items: center; gap: 20px; }}
  .logo-ldo {{ background: #fff; padding: 6px 14px; border-radius: 10px; }}
  .logo-ldo img {{ height: 42px; width: auto; display: block; }}
  .logo-divider {{ width: 2px; height: 38px; background: rgba(197, 160, 89, 0.8); }}
  .tsn-logo svg {{ height: 38px; width: auto; }}
  .badge-anniversary {{
    background: linear-gradient(135deg, #be1e2d 0%, #87000e 100%);
    border: 1px solid #ffd700;
    color: #fff;
    padding: 8px 20px;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1.5px;
  }}
  .badge-anniversary span {{ color: #ffd700; }}

  .content-grid {{
    display: grid;
    grid-template-columns: 1.12fr 0.88fr;
    gap: 35px;
    align-items: center;
    margin-top: 12px;
  }}
  .left-col {{ display: flex; flex-direction: column; gap: 14px; }}
  .sub-tag {{
    font-size: 16px; font-weight: 800; letter-spacing: 6px;
    color: #c5a059; text-transform: uppercase;
  }}
  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 56px; font-weight: 900; line-height: 1.08;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF3DB 40%, #C5A059 85%, #99742A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .open-pill {{
    display: inline-block;
    background: linear-gradient(90deg, #BE1E2D 0%, #DA251D 50%, #BE1E2D 100%);
    border: 2px solid #FFD700;
    border-radius: 40px;
    padding: 6px 32px;
    font-size: 26px; font-weight: 900; letter-spacing: 6px;
    color: #ffffff; margin-top: 6px;
  }}
  .meta-bar {{
    display: flex; gap: 14px; margin-top: 8px;
  }}
  .meta-item {{
    background: rgba(0, 35, 18, 0.8);
    border: 1px solid rgba(197, 160, 89, 0.45);
    border-radius: 12px;
    padding: 8px 18px; font-size: 14.5px; font-weight: 700;
  }}
  .meta-item .gold {{ color: #ffd700; font-weight: 800; }}

  .right-col {{
    display: flex; flex-direction: column; gap: 14px;
  }}
  .hio-card {{
    background: linear-gradient(135deg, rgba(0, 45, 25, 0.92) 0%, rgba(1, 25, 14, 0.96) 100%);
    border: 2px solid rgba(197, 160, 89, 0.7);
    border-radius: 20px;
    padding: 16px 22px;
    display: flex; align-items: center; justify-content: space-between;
  }}
  .hio-badge {{
    background: linear-gradient(90deg, #c5a059, #ffd700);
    color: #012413; font-size: 13px; font-weight: 900;
    letter-spacing: 1.5px; padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin-bottom: 5px;
  }}
  .hio-title {{ font-size: 23px; font-weight: 900; color: #fff; }}
  .hio-title span {{ color: #ffd700; }}
  .hio-sub {{ font-size: 13px; color: #e4ca8c; margin-top: 4px; font-weight: 600; }}
  .hio-thumb {{ width: 135px; height: 75px; border-radius: 10px; border: 1.5px solid #c5a059; object-fit: cover; }}

  .cards-2col {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 14px;
  }}
  .mini-card {{
    background: rgba(0, 30, 16, 0.85);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 16px; padding: 15px 18px;
  }}
  .mini-header {{
    font-size: 14.5px; font-weight: 800; color: #ffd700;
    text-transform: uppercase; margin-bottom: 8px;
    display: flex; align-items: center; gap: 8px;
  }}
  .mini-list {{ list-style: none; display: flex; flex-direction: column; gap: 6px; font-size: 12.8px; }}
  .mini-list li {{ display: flex; gap: 6px; color: #e5e5e5; }}
  .mini-list li::before {{ content: '◆'; color: #c5a059; font-size: 9px; margin-top: 3px; }}
  .mini-list strong {{ color: #fff; }}

  .footer-contact {{
    background: linear-gradient(180deg, rgba(1, 28, 15, 0.96) 0%, rgba(0, 17, 9, 0.98) 100%);
    border: 1.8px solid #c5a059;
    border-radius: 18px;
    padding: 13px 24px;
    display: flex; align-items: center; justify-content: space-between; gap: 20px;
  }}
  .contact-col {{ display: flex; flex-direction: column; gap: 4px; flex: 1; }}
  .contact-heading {{ font-size: 12.5px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .contact-row {{ display: flex; flex-wrap: wrap; gap: 8px 16px; font-size: 13.5px; }}
  .contact-row .phone {{ color: #ffd700; font-weight: 800; }}
  .qr-box {{
    background: #fff; padding: 6px 12px; border-radius: 12px;
    display: flex; align-items: center; gap: 10px; flex-shrink: 0;
  }}
  .qr-box svg {{ width: 48px; height: 48px; }}
  .qr-box .label {{ font-size: 10.5px; font-weight: 800; color: #012413; text-transform: uppercase; }}
</style>
</head>
<body>
<div class="bg-canvas"></div>
<div class="bg-course"></div>
<div class="banner-wrapper">

  <div class="header-bar">
    <div class="logos-group">
      <div class="logo-ldo"><img src="assets/images/logo_lao_dong_official.png" /></div>
      <div class="logo-divider"></div>
      <div class="tsn-logo">{tsn_svg_content}</div>
    </div>
    <div class="badge-anniversary">⛳ KỶ NIỆM <span>97 NĂM</span> BÁO LAO ĐỘNG</div>
  </div>

  <div class="content-grid">
    <div class="left-col">
      <div class="sub-tag">GIẢI GOLF TRUYỀN THỐNG ĐỈNH CAO</div>
      <h1 class="main-title">GIẢI GOLF BÁO LAO ĐỘNG</h1>
      <div><span class="open-pill">OPEN 2026</span></div>
      <div class="meta-bar">
        <div class="meta-item">📍 SÂN GOLF <span class="gold">TÂN SƠN NHẤT</span></div>
        <div class="meta-item">🗓️ CHỦ NHẬT, <span class="gold">15.11.2026</span></div>
        <div class="meta-item">⚡ SHOTGUN: <span class="gold">12:00</span></div>
      </div>
    </div>

    <div class="right-col">
      <div class="hio-card">
        <div>
          <div class="hio-badge">⭐ GIẢI THƯỞNG HOLE-IN-ONE</div>
          <div class="hio-title">XE Ô TÔ <span>VINFAST VF 7 & VF 3</span></div>
          <div class="hio-sub">BỘ GẬY PRGR & HÀNG TRĂM TRIỆU ĐỒNG TẠI CÁC HỐ PAR 3</div>
        </div>
        <img src="assets/images/golf_hio_luxury_car_podium.jpg" class="hio-thumb" />
      </div>

      <div class="cards-2col">
        <div class="mini-card">
          <div class="mini-header">🏆 Cơ Cấu Giải Thưởng</div>
          <ul class="mini-list">
            <li><strong>Best Gross:</strong> Vô địch toàn giải</li>
            <li><strong>Bảng Nam (A - B - C):</strong> Nhất, Nhì, Ba</li>
            <li><strong>Bảng Nữ (A - B):</strong> Nhất, Nhì</li>
            <li><strong>Kỹ thuật:</strong> 2 Longest & 2 Nearest</li>
          </ul>
        </div>
        <div class="mini-card">
          <div class="mini-header">🎁 Phí Tham Dự & Quyền Lợi</div>
          <div style="color:#ffd700; font-weight:800; font-size:15px; margin-bottom:4px;">3.500.000 VNĐ / GOLFER</div>
          <ul class="mini-list">
            <li>18 hố + Caddie + Xe điện Buggy</li>
            <li>Doorgift: Áo thi đấu + Mũ golf</li>
            <li>Ăn trưa nhẹ + Đại tiệc Gala Dinner tối</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="footer-contact">
    <div class="contact-col">
      <div class="contact-heading">📞 LIÊN HỆ BAN TỔ CHỨC:</div>
      <div class="contact-row">
        <div>Nhà báo Thanh Uyên: <span class="phone">0932.311.012</span></div>
        <div>•</div>
        <div>Nhà báo Bá Trường: <span class="phone">0918.658.465</span></div>
        <div>•</div>
        <div>Nhà báo Đăng Văn: <span class="phone">090.556.7395</span></div>
      </div>
      <div class="contact-heading" style="margin-top: 4px;">⛳ BỘ PHẬN ĐIỀU PHỐI SÂN GOLF TÂN SƠN NHẤT:</div>
      <div class="contact-row" style="font-size: 12.8px;">
        <div>Mr. Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div>•</div>
        <div>Mr. Quang: <span class="phone">0973.777.589</span></div>
        <div>•</div>
        <div>Ms. Lệ Quyên: <span class="phone">0939.301.090</span></div>
        <div>•</div>
        <div>Ms. Dương Trang: <span class="phone">0909.059.990</span></div>
        <div>•</div>
        <div>Ms. Hồng Hạnh: <span class="phone">0969.214.289</span></div>
      </div>
    </div>
    <div class="qr-box">
      <svg viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#004d2c"/>
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#004d2c"/>
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#004d2c"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#004d2c"/>
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#c5a059"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
      </svg>
      <div class="label">QUÉT ĐĂNG KÝ</div>
    </div>
  </div>

</div>
</body>
</html>
"""

with open(WORKSPACE / "poster_mobile_9x16.html", "w", encoding="utf-8") as f:
    f.write(html_mobile)

with open(WORKSPACE / "poster_standee_a4.html", "w", encoding="utf-8") as f:
    f.write(html_standee)

with open(WORKSPACE / "poster_banner_16x9.html", "w", encoding="utf-8") as f:
    f.write(html_banner)

print("Saved all 3 Masters Green templates successfully!")
