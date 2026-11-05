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

# Build Mobile Poster HTML (9:16 - 1080x1920)
html_mobile = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>Poster Giải Golf Báo Lao Động Open 2026 - Mobile 9:16</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    position: relative;
    background: #0f0204;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}

  /* Background layers */
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 80% 20%, rgba(220, 20, 60, 0.45) 0%, transparent 50%),
      radial-gradient(circle at 20% 75%, rgba(180, 10, 30, 0.5) 0%, transparent 60%),
      radial-gradient(circle at 50% 50%, rgba(30, 0, 5, 0.8) 0%, #080102 100%);
    z-index: 1;
  }}

  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.22;
    filter: saturate(1.4) contrast(1.2);
    mix-blend-mode: luminosity;
    z-index: 2;
  }}

  .bg-glow-gold {{
    position: absolute;
    top: 240px;
    left: 50%;
    transform: translateX(-50%);
    width: 800px;
    height: 400px;
    background: radial-gradient(ellipse, rgba(212, 160, 23, 0.25) 0%, transparent 70%);
    z-index: 3;
    pointer-events: none;
  }}

  /* Content wrapper */
  .poster-wrapper {{
    position: relative;
    z-index: 10;
    width: 1080px;
    height: 1920px;
    padding: 45px 50px 35px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Header Bar */
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 215, 0, 0.3);
    border-radius: 20px;
    padding: 16px 28px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  }}

  .logos-group {{
    display: flex;
    align-items: center;
    gap: 22px;
  }}

  .logo-ldo-wrap {{
    display: flex;
    align-items: center;
    background: #ffffff;
    padding: 6px 14px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }}

  .logo-ldo-wrap img {{
    height: 42px;
    width: auto;
    display: block;
  }}

  .logo-divider {{
    width: 2px;
    height: 38px;
    background: linear-gradient(180deg, transparent, rgba(255, 215, 0, 0.8), transparent);
  }}

  .tsn-logo-wrap {{
    height: 46px;
    display: flex;
    align-items: center;
  }}

  .tsn-logo-wrap svg {{
    height: 36px;
    width: auto;
  }}

  .badge-milestone {{
    background: linear-gradient(135deg, #be1e2d 0%, #87000e 100%);
    border: 1px solid rgba(255, 215, 0, 0.6);
    color: #fff;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 15px rgba(190, 30, 45, 0.4);
  }}

  .badge-milestone span.gold {{
    color: #ffd700;
  }}

  /* Main Title Block */
  .title-block {{
    text-align: center;
    margin-top: 15px;
  }}

  .sub-tag {{
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 8px;
    text-transform: uppercase;
    color: #e5cca0;
    text-shadow: 0 2px 8px rgba(0,0,0,0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-bottom: 6px;
  }}

  .sub-tag::before, .sub-tag::after {{
    content: '';
    display: inline-block;
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c5a059);
  }}
  .sub-tag::after {{
    background: linear-gradient(90deg, #c5a059, transparent);
  }}

  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 66px;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: linear-gradient(180deg, #ffffff 0%, #ffeed2 40%, #d4a017 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 6px 18px rgba(0, 0, 0, 0.9));
  }}

  .open-pill {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(90deg, #BE1E2D 0%, #DA251D 50%, #BE1E2D 100%);
    border: 2px solid #FFD700;
    border-radius: 40px;
    padding: 6px 36px;
    font-size: 32px;
    font-weight: 900;
    letter-spacing: 6px;
    color: #ffffff;
    box-shadow: 0 8px 25px rgba(218, 37, 29, 0.6);
    margin-top: 6px;
  }}

  /* Venue & Time Bar */
  .meta-bar {{
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 15px;
  }}

  .meta-item {{
    background: rgba(0, 0, 0, 0.55);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 12px;
    padding: 10px 22px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 16px;
    font-weight: 700;
    color: #fff;
  }}

  .meta-item i-icon {{
    font-size: 20px;
  }}

  .meta-item .highlight {{
    color: #ffd700;
    font-weight: 800;
  }}

  /* Hero Graphic Banner (HIO Highlight) */
  .hio-banner {{
    margin-top: 12px;
    background: linear-gradient(135deg, rgba(160, 10, 25, 0.85) 0%, rgba(70, 0, 10, 0.95) 100%);
    border: 2px solid #d4a017;
    border-radius: 20px;
    padding: 18px 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.2);
    position: relative;
    overflow: hidden;
  }}

  .hio-banner::before {{
    content: 'HOLE IN ONE';
    position: absolute;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Cinzel', serif;
    font-size: 88px;
    font-weight: 900;
    color: rgba(255, 215, 0, 0.05);
    white-space: nowrap;
    pointer-events: none;
    letter-spacing: 4px;
  }}

  .hio-content {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 2;
  }}

  .hio-text {{
    flex: 1;
  }}

  .hio-badge {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(90deg, #d4a017, #ffd700);
    color: #000;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 1.5px;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }}

  .hio-heading {{
    font-size: 28px;
    font-weight: 900;
    line-height: 1.2;
    color: #ffffff;
    text-transform: uppercase;
  }}

  .hio-heading span.cars {{
    color: #ffd700;
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
  }}

  .hio-sub {{
    font-size: 14px;
    color: #e5cca0;
    margin-top: 4px;
    font-weight: 600;
  }}

  .hio-visual {{
    display: flex;
    align-items: center;
    gap: 15px;
  }}

  .hio-thumb {{
    width: 140px;
    height: 80px;
    border-radius: 10px;
    border: 1px solid rgba(255, 215, 0, 0.5);
    object-fit: cover;
    box-shadow: 0 6px 15px rgba(0,0,0,0.5);
  }}

  /* Grid 2 Columns */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 15px;
  }}

  .card-box {{
    background: rgba(20, 3, 5, 0.75);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(197, 160, 89, 0.35);
    border-radius: 18px;
    padding: 20px 22px;
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
    padding-bottom: 12px;
    margin-bottom: 12px;
  }}

  .card-icon {{
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #d4a017, #8e6d1b);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: #fff;
    flex-shrink: 0;
  }}

  .card-title {{
    font-size: 18px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #ffd700;
  }}

  .prize-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 9px;
  }}

  .prize-list li {{
    font-size: 15px;
    line-height: 1.35;
    color: #f0f0f0;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }}

  .prize-list li::before {{
    content: '◆';
    color: #d4a017;
    font-size: 10px;
    margin-top: 3px;
    flex-shrink: 0;
  }}

  .prize-list li strong {{
    color: #ffffff;
    font-weight: 700;
  }}

  .fee-badge {{
    background: linear-gradient(135deg, #be1e2d 0%, #7a0c17 100%);
    border: 1px solid #ffd700;
    border-radius: 12px;
    padding: 12px 14px;
    text-align: center;
    margin-bottom: 12px;
  }}

  .fee-badge .price {{
    font-size: 26px;
    font-weight: 900;
    color: #ffd700;
    letter-spacing: 0.5px;
  }}

  .fee-badge .note {{
    font-size: 13px;
    color: #ffcccc;
    margin-top: 3px;
    font-weight: 600;
  }}

  /* Schedule Card (Full Width) */
  .schedule-box {{
    margin-top: 15px;
    background: rgba(15, 2, 4, 0.8);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 18px;
    padding: 18px 24px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  }}

  .timeline-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 12px;
  }}

  .timeline-step {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 215, 0, 0.2);
    border-radius: 12px;
    padding: 10px 8px;
    text-align: center;
    position: relative;
  }}

  .timeline-step.active {{
    background: linear-gradient(180deg, rgba(190, 30, 45, 0.35) 0%, rgba(120, 10, 20, 0.4) 100%);
    border-color: #ffd700;
  }}

  .step-time {{
    font-size: 14px;
    font-weight: 800;
    color: #ffd700;
    margin-bottom: 4px;
  }}

  .step-name {{
    font-size: 12px;
    font-weight: 700;
    color: #e5e5e5;
    line-height: 1.3;
  }}

  /* Footer & Contacts Bar */
  .footer-contact {{
    margin-top: 15px;
    background: linear-gradient(180deg, rgba(30, 3, 6, 0.95) 0%, rgba(15, 1, 3, 0.98) 100%);
    border: 1.5px solid #d4a017;
    border-radius: 20px;
    padding: 18px 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}

  .contact-col {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .contact-title {{
    font-size: 14px;
    font-weight: 800;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .contact-items {{
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
  }}

  .contact-person {{
    font-size: 14px;
    color: #ffffff;
    font-weight: 600;
  }}

  .contact-person span.phone {{
    color: #ffd700;
    font-weight: 800;
  }}

  .qr-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    background: #ffffff;
    padding: 10px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    flex-shrink: 0;
  }}

  .qr-svg {{
    width: 82px;
    height: 82px;
  }}

  .qr-label {{
    font-size: 10px;
    font-weight: 800;
    color: #000;
    text-transform: uppercase;
    letter-spacing: 0.5px;
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

  <!-- Main Tournament Title -->
  <div class="title-block">
    <div class="sub-tag">GIẢI GOLF TRUYỀN THỐNG ĐỈNH CAO</div>
    <h1 class="main-title">GIẢI GOLF BÁO LAO ĐỘNG</h1>
    <div class="open-pill">OPEN 2026</div>
  </div>

  <!-- Venue & Time -->
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

  <!-- Hole In One Banner -->
  <div class="hio-banner">
    <div class="hio-content">
      <div class="hio-text">
        <div class="hio-badge">⭐ GIẢI THƯỞNG ĐẶC BIỆT HOLE-IN-ONE</div>
        <div class="hio-heading">XE Ô TÔ <span class="cars">VINFAST VF 7 & VF 3</span></div>
        <div class="hio-sub">CÙNG BỘ GẬY CAO CẤP PRGR & HÀNG TRĂM TRIỆU ĐỒNG TẠI CÁC HỐ PAR 3</div>
      </div>
      <div class="hio-visual">
        <img src="assets/images/golf_hio_luxury_car_podium.jpg" class="hio-thumb" alt="VinFast HIO" />
      </div>
    </div>
  </div>

  <!-- 2 Column Details: Prize & Golfer Benefits -->
  <div class="grid-2col">
    <!-- Column 1: Prizes -->
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
          <li>Cúp thiết kế mạ vàng thủ công độc quyền</li>
        </ul>
      </div>
    </div>

    <!-- Column 2: Package & Benefits -->
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
          <li><strong>Đại tiệc Gala Dinner</strong> tối sang trọng & Bia hảo hạng</li>
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

  <!-- Footer Contact & Registration -->
  <div class="footer-contact">
    <div class="contact-col">
      <div class="contact-title">
        <span>📞</span> BAN TỔ CHỨC BÁO LAO ĐỘNG
      </div>
      <div class="contact-items">
        <div class="contact-person">Nhà báo Đoàn Bá Trường: <span class="phone">0918.658.465</span></div>
        <div class="contact-person">Mr. Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div class="contact-person">Mr. Quang: <span class="phone">0973.777.589</span></div>
      </div>
      
      <div class="contact-title" style="margin-top: 6px;">
        <span>⛳</span> BỘ PHẬN GIẢI ĐẤU SÂN GOLF TÂN SƠN NHẤT
      </div>
      <div class="contact-items">
        <div class="contact-person">Ms. Lệ Quyên: <span class="phone">0939.301.090</span></div>
        <div class="contact-person">Ms. Dương Trang: <span class="phone">0909.059.990</span></div>
        <div class="contact-person">Ms. Hồng Hạnh: <span class="phone">0969.214.289</span></div>
      </div>
    </div>

    <div class="qr-box">
      <!-- High Contrast Vector QR Mockup -->
      <svg class="qr-svg" viewBox="0 0 100 100" fill="#000">
        <!-- Top Left Corner -->
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#be1e2d"/>
        
        <!-- Top Right Corner -->
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#be1e2d"/>
        
        <!-- Bottom Left Corner -->
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#be1e2d"/>
        
        <!-- Center & Data dots -->
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="42" y="24" width="6" height="6" fill="#111"/>
        <rect x="12" y="42" width="6" height="6" fill="#111"/>
        <rect x="24" y="42" width="6" height="6" fill="#111"/>
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#d4a017"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
        <rect x="80" y="42" width="6" height="6" fill="#111"/>
        <rect x="42" y="68" width="6" height="6" fill="#111"/>
        <rect x="54" y="68" width="6" height="6" fill="#111"/>
        <rect x="68" y="68" width="6" height="6" fill="#111"/>
        <rect x="78" y="78" width="8" height="8" fill="#111"/>
        <rect x="68" y="82" width="6" height="6" fill="#111"/>
      </svg>
      <div class="qr-label">QUÉT ĐĂNG KÝ</div>
    </div>
  </div>

</div>

</body>
</html>
"""

with open(WORKSPACE / "poster_mobile_9x16.html", "w", encoding="utf-8") as f:
    f.write(html_mobile)

print("Saved poster_mobile_9x16.html successfully!")
