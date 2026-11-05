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

# 1. Standee / Print Poster (1200 x 2133 - Ratio 9:16 Standee Standard)
html_standee = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1200, height=2133, initial-scale=1.0">
<title>Standee Giải Golf Báo Lao Động Open 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px;
    height: 2133px;
    overflow: hidden;
    position: relative;
    background: #0d0103;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 80% 15%, rgba(190, 30, 45, 0.4) 0%, transparent 55%),
      radial-gradient(circle at 20% 80%, rgba(160, 10, 25, 0.45) 0%, transparent 60%),
      radial-gradient(circle at 50% 50%, rgba(25, 2, 4, 0.85) 0%, #060102 100%);
    z-index: 1;
  }}
  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.25;
    mix-blend-mode: luminosity;
    z-index: 2;
  }}
  .standee-wrapper {{
    position: relative;
    z-index: 10;
    width: 1200px;
    height: 2133px;
    padding: 60px 65px 50px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 215, 0, 0.35);
    border-radius: 24px;
    padding: 20px 32px;
  }}
  .logos-group {{ display: flex; align-items: center; gap: 25px; }}
  .logo-ldo {{ background: #fff; padding: 8px 16px; border-radius: 12px; }}
  .logo-ldo img {{ height: 50px; width: auto; display: block; }}
  .logo-divider {{ width: 2px; height: 46px; background: rgba(255,215,0,0.6); }}
  .tsn-logo svg {{ height: 44px; width: auto; }}
  .badge-anniversary {{
    background: linear-gradient(135deg, #be1e2d 0%, #7a0c17 100%);
    border: 1px solid #ffd700;
    color: #fff;
    padding: 10px 24px;
    border-radius: 40px;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 2px;
  }}
  .badge-anniversary span {{ color: #ffd700; }}
  
  .title-block {{ text-align: center; margin-top: 25px; }}
  .sub-tag {{
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 8px;
    text-transform: uppercase;
    color: #e5cca0;
    margin-bottom: 8px;
  }}
  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 76px;
    font-weight: 900;
    line-height: 1.05;
    text-transform: uppercase;
    background: linear-gradient(180deg, #ffffff 0%, #ffeed2 40%, #d4a017 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .open-pill {{
    display: inline-block;
    background: linear-gradient(90deg, #BE1E2D 0%, #DA251D 50%, #BE1E2D 100%);
    border: 2px solid #FFD700;
    border-radius: 50px;
    padding: 8px 45px;
    font-size: 36px;
    font-weight: 900;
    letter-spacing: 8px;
    color: #ffffff;
    margin-top: 10px;
    box-shadow: 0 10px 30px rgba(218, 37, 29, 0.6);
  }}

  .meta-bar {{
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;
  }}
  .meta-item {{
    background: rgba(0, 0, 0, 0.65);
    border: 1px solid rgba(197, 160, 89, 0.5);
    border-radius: 14px;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: 700;
  }}
  .meta-item .gold {{ color: #ffd700; font-weight: 800; }}

  .hio-banner {{
    margin-top: 20px;
    background: linear-gradient(135deg, rgba(160, 10, 25, 0.9) 0%, rgba(60, 0, 10, 0.95) 100%);
    border: 2px solid #d4a017;
    border-radius: 24px;
    padding: 22px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .hio-badge {{
    background: linear-gradient(90deg, #d4a017, #ffd700);
    color: #000;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: 2px;
    padding: 5px 16px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 8px;
  }}
  .hio-title {{
    font-size: 32px;
    font-weight: 900;
    text-transform: uppercase;
    color: #fff;
  }}
  .hio-title span {{ color: #ffd700; }}
  .hio-sub {{ font-size: 16px; color: #e5cca0; margin-top: 6px; font-weight: 600; }}
  .hio-img {{ width: 170px; height: 95px; border-radius: 12px; border: 1.5px solid #ffd700; object-fit: cover; }}

  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-top: 20px;
  }}
  .card-box {{
    background: rgba(20, 2, 5, 0.8);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 20px;
    padding: 24px 28px;
  }}
  .card-header {{
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 1px solid rgba(197, 160, 89, 0.3);
    padding-bottom: 14px;
    margin-bottom: 16px;
  }}
  .card-icon {{
    width: 38px; height: 38px;
    background: linear-gradient(135deg, #d4a017, #8e6d1b);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; color: #fff;
  }}
  .card-title {{ font-size: 20px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .card-list {{ list-style: none; display: flex; flex-direction: column; gap: 11px; }}
  .card-list li {{ font-size: 17px; line-height: 1.4; color: #f5f5f5; display: flex; gap: 10px; }}
  .card-list li::before {{ content: '◆'; color: #d4a017; font-size: 12px; margin-top: 3px; }}
  .card-list li strong {{ color: #fff; }}

  .fee-box {{
    background: linear-gradient(135deg, #be1e2d 0%, #7a0c17 100%);
    border: 1.5px solid #ffd700;
    border-radius: 14px;
    padding: 14px 18px;
    text-align: center;
    margin-bottom: 16px;
  }}
  .fee-box .price {{ font-size: 30px; font-weight: 900; color: #ffd700; }}
  .fee-box .note {{ font-size: 14px; color: #ffe6e6; margin-top: 4px; font-weight: 600; }}

  .schedule-box {{
    margin-top: 20px;
    background: rgba(15, 2, 4, 0.85);
    border: 1px solid rgba(197, 160, 89, 0.45);
    border-radius: 20px;
    padding: 22px 28px;
  }}
  .timeline-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
    margin-top: 14px;
  }}
  .timeline-step {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 215, 0, 0.25);
    border-radius: 14px;
    padding: 12px 10px;
    text-align: center;
  }}
  .timeline-step.active {{
    background: linear-gradient(180deg, rgba(190, 30, 45, 0.4) 0%, rgba(120, 10, 20, 0.5) 100%);
    border-color: #ffd700;
  }}
  .step-time {{ font-size: 15px; font-weight: 800; color: #ffd700; margin-bottom: 6px; }}
  .step-name {{ font-size: 13px; font-weight: 700; color: #e5e5e5; line-height: 1.35; }}

  .footer-contact {{
    margin-top: 20px;
    background: linear-gradient(180deg, rgba(30, 3, 6, 0.95) 0%, rgba(15, 1, 3, 0.98) 100%);
    border: 2px solid #d4a017;
    border-radius: 24px;
    padding: 22px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .contact-col {{ display: flex; flex-direction: column; gap: 8px; }}
  .contact-heading {{ font-size: 15px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .contact-row {{ display: flex; flex-wrap: wrap; gap: 16px; font-size: 15px; }}
  .contact-row .phone {{ color: #ffd700; font-weight: 800; }}
  .qr-box {{
    background: #fff;
    padding: 12px;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    flex-shrink: 0;
  }}
  .qr-box svg {{ width: 90px; height: 90px; }}
  .qr-box .label {{ font-size: 11px; font-weight: 800; color: #000; text-transform: uppercase; }}
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

  <div class="hio-banner">
    <div>
      <div class="hio-badge">⭐ GIẢI THƯỞNG ĐẶC BIỆT HOLE-IN-ONE</div>
      <div class="hio-title">XE Ô TÔ <span>VINFAST VF 7 & VF 3</span></div>
      <div class="hio-sub">CÙNG BỘ GẬY CAO CẤP PRGR & HÀNG TRĂM TRIỆU ĐỒNG TẠI CÁC HỐ PAR 3</div>
    </div>
    <img src="assets/images/golf_hio_luxury_car_podium.jpg" class="hio-img" />
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
        <li>Tiệc trưa nhẹ buffet trước giờ xuất phát</li>
        <li><strong>Đại tiệc Gala Dinner</strong> tối thượng hạng & Bia hảo hạng</li>
      </ul>
    </div>
  </div>

  <div class="schedule-box">
    <div class="card-header" style="margin-bottom:0; padding-bottom:10px;">
      <div class="card-icon">⏰</div>
      <div class="card-title" style="font-size: 18px;">Lịch Trình Ngày Thi Đấu (Chủ Nhật, 15.11.2026)</div>
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
      <div class="contact-heading">📞 BAN TỔ CHỨC BÁO LAO ĐỘNG</div>
      <div class="contact-row">
        <div>Đoàn Bá Trường: <span class="phone">0918.658.465</span></div>
        <div>Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div>Mr. Quang: <span class="phone">0973.777.589</span></div>
      </div>
      <div class="contact-heading" style="margin-top: 6px;">⛳ BỘ PHẬN GIẢI ĐẤU SÂN GOLF TÂN SƠN NHẤT</div>
      <div class="contact-row">
        <div>Ms. Lệ Quyên: <span class="phone">0939.301.090</span></div>
        <div>Ms. Dương Trang: <span class="phone">0909.059.990</span></div>
        <div>Ms. Hồng Hạnh: <span class="phone">0969.214.289</span></div>
      </div>
    </div>
    <div class="qr-box">
      <svg viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#be1e2d"/>
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#d4a017"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
        <rect x="42" y="68" width="6" height="6" fill="#111"/>
        <rect x="68" y="68" width="6" height="6" fill="#111"/>
      </svg>
      <div class="label">QUÉT ĐĂNG KÝ</div>
    </div>
  </div>

</div>
</body>
</html>
"""

# 2. Horizontal Banner / LED Screen (1920 x 1080 - 16:9)
html_banner = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1920, height=1080, initial-scale=1.0">
<title>Banner LED Giải Golf Báo Lao Động Open 2026 - 16:9</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    overflow: hidden;
    position: relative;
    background: #0a0102;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
  }}
  .bg-canvas {{
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 75% 30%, rgba(190, 30, 45, 0.45) 0%, transparent 60%),
      radial-gradient(circle at 15% 70%, rgba(140, 5, 20, 0.4) 0%, transparent 55%),
      radial-gradient(circle at 50% 50%, rgba(20, 2, 4, 0.9) 0%, #050102 100%);
    z-index: 1;
  }}
  .bg-course {{
    position: absolute;
    inset: 0;
    background-image: url('assets/images/tsn_aerial_twilight_fairway.jpg');
    background-size: cover;
    background-position: center;
    opacity: 0.22;
    mix-blend-mode: luminosity;
    z-index: 2;
  }}
  .banner-wrapper {{
    position: relative;
    z-index: 10;
    width: 1920px;
    height: 1080px;
    padding: 40px 60px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .header-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 215, 0, 0.35);
    border-radius: 20px;
    padding: 14px 28px;
  }}
  .logos-group {{ display: flex; align-items: center; gap: 20px; }}
  .logo-ldo {{ background: #fff; padding: 6px 14px; border-radius: 10px; }}
  .logo-ldo img {{ height: 42px; width: auto; display: block; }}
  .logo-divider {{ width: 2px; height: 38px; background: rgba(255,215,0,0.6); }}
  .tsn-logo svg {{ height: 38px; width: auto; }}
  .badge-anniversary {{
    background: linear-gradient(135deg, #be1e2d 0%, #7a0c17 100%);
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
    grid-template-columns: 1.15fr 0.85fr;
    gap: 40px;
    align-items: center;
    margin-top: 15px;
  }}
  .left-col {{ display: flex; flex-direction: column; gap: 15px; }}
  .sub-tag {{
    font-size: 16px; font-weight: 800; letter-spacing: 6px;
    color: #e5cca0; text-transform: uppercase;
  }}
  .main-title {{
    font-family: 'Cinzel', serif;
    font-size: 58px; font-weight: 900; line-height: 1.08;
    background: linear-gradient(180deg, #ffffff 0%, #ffeed2 40%, #d4a017 100%);
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
    display: flex; gap: 16px; margin-top: 10px;
  }}
  .meta-item {{
    background: rgba(0, 0, 0, 0.6);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-radius: 12px;
    padding: 8px 18px;
    font-size: 15px; font-weight: 700;
  }}
  .meta-item .gold {{ color: #ffd700; font-weight: 800; }}

  .right-col {{
    display: flex; flex-direction: column; gap: 14px;
  }}
  .hio-card {{
    background: linear-gradient(135deg, rgba(160, 10, 25, 0.9) 0%, rgba(60, 0, 10, 0.95) 100%);
    border: 2px solid #d4a017;
    border-radius: 20px;
    padding: 18px 24px;
    display: flex; align-items: center; justify-content: space-between;
  }}
  .hio-badge {{
    background: linear-gradient(90deg, #d4a017, #ffd700);
    color: #000; font-size: 13px; font-weight: 900;
    letter-spacing: 1.5px; padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin-bottom: 6px;
  }}
  .hio-title {{ font-size: 24px; font-weight: 900; color: #fff; }}
  .hio-title span {{ color: #ffd700; }}
  .hio-sub {{ font-size: 13px; color: #e5cca0; margin-top: 4px; font-weight: 600; }}
  .hio-thumb {{ width: 130px; height: 75px; border-radius: 10px; border: 1.5px solid #ffd700; object-fit: cover; }}

  .cards-2col {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 14px;
  }}
  .mini-card {{
    background: rgba(20, 2, 5, 0.85);
    border: 1px solid rgba(197, 160, 89, 0.35);
    border-radius: 16px;
    padding: 16px 18px;
  }}
  .mini-header {{
    font-size: 15px; font-weight: 800; color: #ffd700;
    text-transform: uppercase; margin-bottom: 10px;
    display: flex; align-items: center; gap: 8px;
  }}
  .mini-list {{ list-style: none; display: flex; flex-direction: column; gap: 7px; font-size: 13px; }}
  .mini-list li {{ display: flex; gap: 6px; color: #e5e5e5; }}
  .mini-list li::before {{ content: '◆'; color: #d4a017; font-size: 9px; margin-top: 3px; }}
  .mini-list strong {{ color: #fff; }}

  .footer-contact {{
    background: linear-gradient(180deg, rgba(30, 3, 6, 0.95) 0%, rgba(15, 1, 3, 0.98) 100%);
    border: 1.5px solid #d4a017;
    border-radius: 18px;
    padding: 14px 28px;
    display: flex; align-items: center; justify-content: space-between;
  }}
  .contact-col {{ display: flex; flex-direction: column; gap: 4px; }}
  .contact-heading {{ font-size: 13px; font-weight: 800; color: #ffd700; text-transform: uppercase; }}
  .contact-row {{ display: flex; gap: 20px; font-size: 14px; }}
  .contact-row .phone {{ color: #ffd700; font-weight: 800; }}
  .qr-box {{
    background: #fff; padding: 6px 12px; border-radius: 12px;
    display: flex; align-items: center; gap: 10px;
  }}
  .qr-box svg {{ width: 50px; height: 50px; }}
  .qr-box .label {{ font-size: 11px; font-weight: 800; color: #000; text-transform: uppercase; }}
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
          <div style="color:#ffd700; font-weight:800; font-size:16px; margin-bottom:4px;">3.500.000 VNĐ / GOLFER</div>
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
      <div class="contact-heading">📞 BAN TỔ CHỨC BÁO LAO ĐỘNG</div>
      <div class="contact-row">
        <div>Đoàn Bá Trường: <span class="phone">0918.658.465</span></div>
        <div>Paky Nhất: <span class="phone">0909.282.861</span></div>
        <div>Mr. Quang: <span class="phone">0973.777.589</span></div>
      </div>
      <div class="contact-heading" style="margin-top: 4px;">⛳ SÂN GOLF TÂN SƠN NHẤT: Ms. Lệ Quyên (0939.301.090) • Ms. Dương Trang (0909.059.990) • Ms. Hồng Hạnh (0969.214.289)</div>
    </div>
    <div class="qr-box">
      <svg viewBox="0 0 100 100" fill="#000">
        <rect x="10" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="15" width="14" height="14" fill="#fff"/>
        <rect x="18" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="66" y="10" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="71" y="15" width="14" height="14" fill="#fff"/>
        <rect x="74" y="18" width="8" height="8" fill="#be1e2d"/>
        <rect x="10" y="66" width="24" height="24" rx="3" fill="#be1e2d"/>
        <rect x="15" y="71" width="14" height="14" fill="#fff"/>
        <rect x="18" y="74" width="8" height="8" fill="#be1e2d"/>
        <rect x="40" y="40" width="20" height="20" rx="3" fill="#d4a017"/>
        <rect x="44" y="44" width="12" height="12" fill="#fff"/>
        <rect x="47" y="47" width="6" height="6" fill="#be1e2d"/>
        <rect x="42" y="12" width="6" height="6" fill="#111"/>
        <rect x="52" y="12" width="6" height="6" fill="#111"/>
        <rect x="68" y="42" width="6" height="6" fill="#111"/>
      </svg>
      <div class="label">QUÉT ĐĂNG KÝ</div>
    </div>
  </div>

</div>
</body>
</html>
"""

with open(WORKSPACE / "poster_standee_a4.html", "w", encoding="utf-8") as f:
    f.write(html_standee)

with open(WORKSPACE / "poster_banner_16x9.html", "w", encoding="utf-8") as f:
    f.write(html_banner)

print("Saved all HTML poster templates!")
