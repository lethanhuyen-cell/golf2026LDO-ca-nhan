#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
CỖ MÁY KHỞI TẠO HỒ SƠ & LANDING PAGE SỰ KIỆN THỂ THAO CAO CẤP (SPORTS LUXE SCAFFOLDER)
Tác giả: Ban Biên tập & Bộ phận Công nghệ Sự kiện Báo Lao Động
================================================================================
Công dụng:
- Tự động sinh trọn bộ:
  1. Landing Page thể thao đẳng cấp Sports Luxe (index.html)
  2. Hồ sơ tài trợ Doanh nghiệp 10 trang chuẩn A4 Print-to-PDF (dossier.html)
  3. Hồ sơ đồng hành Cá nhân 3 trang chuẩn A4 Print-to-PDF (dossier_ca_nhan.html)
  4. Cơ chế bảo mật Dossier Mode 3 tầng (robots.txt, noindex, lead-gated form)
  5. Script xuất PDF chuẩn A4 0 margin qua Headless Chrome (render_pdf.py)
  6. File cấu hình Vercel deployment (vercel.json)

Sử dụng:
  python3 scripts/scaffold_event.py --init event_config.json
  python3 scripts/scaffold_event.py --build --config event_config.json --out ./output_folder
"""

import os
import sys
import json
import argparse
import shutil
from pathlib import Path

def generate_landing_page(cfg):
    theme = cfg.get("theme", {})
    pkgs = cfg.get("corporate_packages", [])
    patron = cfg.get("personal_patron", {})
    venue = cfg.get("venue", {})
    contact = cfg.get("contact", {})
    banking = cfg.get("banking", {})

    pkg_cards_html = ""
    for p in pkgs:
        media_list = "".join([f'<li class="flex items-start gap-2 text-xs text-slate-300"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5"></i><span>{m}</span></li>' for m in p.get("media_rights", [])[:3]])
        pkg_cards_html += f"""
        <div class="relative bg-gradient-to-b from-slate-900/90 to-emerald-950/80 border border-amber-500/30 rounded-2xl p-6 hover:border-amber-400 transition-all duration-300 shadow-xl flex flex-col justify-between">
          <div>
            <div class="inline-block px-3 py-1 bg-amber-500/10 border border-amber-500/30 rounded-full text-[11px] font-semibold tracking-wider text-amber-300 uppercase mb-3">
              {p.get('badge', 'TÀI TRỢ')}
            </div>
            <h3 class="text-xl font-bold text-white font-serif tracking-tight">{p.get('name')}</h3>
            <div class="text-2xl font-extrabold text-amber-400 mt-2 font-cinzel">{p.get('value_text')}</div>
            <div class="text-xs text-slate-400 mt-1 mb-4 flex items-center gap-1.5">
              <i data-lucide="award" class="w-3.5 h-3.5 text-amber-400"></i>
              Số lượng: <span class="text-amber-200 font-semibold">{p.get('slots')}</span>
            </div>
            <div class="border-t border-slate-800/80 pt-4 mb-4">
              <div class="text-xs font-bold uppercase tracking-wider text-amber-300 mb-2">Đặc quyền thi đấu & Tiệc:</div>
              <div class="text-xs text-slate-200 mb-1 flex items-center gap-2"><i data-lucide="user-check" class="w-3.5 h-3.5 text-emerald-400"></i> {p.get('golfer_slots')}</div>
              <div class="text-xs text-slate-200 mb-3 flex items-center gap-2"><i data-lucide="glass-water" class="w-3.5 h-3.5 text-emerald-400"></i> {p.get('gala_seats')}</div>
              <div class="text-xs font-bold uppercase tracking-wider text-amber-300 mb-2">Quyền lợi truyền thông:</div>
              <ul class="space-y-1.5">
                {media_list}
              </ul>
            </div>
          </div>
          <a href="#sponsor-form" class="mt-4 w-full py-2.5 text-center text-xs font-bold uppercase tracking-widest text-emerald-950 bg-gradient-to-r from-amber-300 via-amber-400 to-amber-500 hover:from-amber-400 hover:to-amber-300 rounded-lg shadow-lg transition">
            Đăng Ký Tài Trợ Gói Này
          </a>
        </div>
        """

    co_orgs = " • ".join(cfg.get("co_organizers", []))

    html = f"""<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cfg.get('event_title')} | {cfg.get('organizer')}</title>
  <meta name="description" content="{cfg.get('event_subtitle')}" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              dark: '{theme.get("primary_dark", "#002013")}',
              green: '{theme.get("primary_green", "#004d2c")}',
              emerald: '{theme.get("emerald", "#056839")}',
              gold: '{theme.get("gold", "#C5A059")}',
              goldLight: '{theme.get("gold_light", "#E5CCA0")}',
              goldDark: '{theme.get("gold_dark", "#9E7D3B")}',
              red: '{theme.get("laodong_red", "#BE1E2D")}'
            }}
          }},
          fontFamily: {{
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            cinzel: ['"Cinzel"', 'serif'],
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: {theme.get("primary_dark", "#002013")};
      color: #f8fafc;
    }}
    .font-cinzel {{ font-family: 'Cinzel', serif; }}
    .font-serif {{ font-family: 'Playfair Display', Georgia, serif; }}
    .luxury-gold-gradient {{
      background: linear-gradient(135deg, #FFE8B8 0%, #C5A059 50%, #8A6828 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
  </style>
</head>
<body class="bg-[#00170d] text-slate-100 antialiased selection:bg-amber-400 selection:text-emerald-950">

  <!-- TOP HEADER / NAV -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-[#00170d]/90 backdrop-blur-md border-b border-amber-500/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full border border-amber-400/60 bg-emerald-950 flex items-center justify-center text-amber-400 font-cinzel font-bold text-lg shadow-md">
          LĐ
        </div>
        <div>
          <span class="text-xs uppercase tracking-widest text-amber-300/90 font-semibold block">BÁO LAO ĐỘNG</span>
          <span class="text-sm font-bold text-white tracking-wide">{cfg.get('short_title')}</span>
        </div>
      </div>
      <nav class="hidden md:flex items-center gap-8 text-xs font-semibold uppercase tracking-wider text-slate-300">
        <a href="#about" class="hover:text-amber-300 transition">Giới Thiệu</a>
        <a href="#schedule" class="hover:text-amber-300 transition">Lịch Trình</a>
        <a href="#sponsor-packages" class="hover:text-amber-300 transition">Tài Trợ Doanh Nghiệp</a>
        <a href="#personal-patron" class="hover:text-amber-300 transition">Đồng Hành Cá Nhân</a>
        <a href="#register" class="hover:text-amber-300 transition">Đăng Ký Golfer</a>
      </nav>
      <div class="flex items-center gap-3">
        <a href="#sponsor-form" class="px-4 py-2 text-xs font-bold uppercase tracking-wider text-emerald-950 bg-gradient-to-r from-amber-300 to-amber-500 hover:brightness-110 rounded-full shadow-lg transition flex items-center gap-1.5">
          <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
          Đăng Ký Tài Trợ
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="relative pt-32 pb-24 md:pt-40 md:pb-32 overflow-hidden border-b border-amber-500/20">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-emerald-900/40 via-[#00170d] to-[#00170d] -z-10"></div>
    <div class="max-w-5xl mx-auto px-4 text-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/10 border border-amber-400/30 text-amber-300 text-xs font-semibold tracking-widest uppercase mb-6">
        <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
        {cfg.get('date_display')} • {venue.get('name')}
      </div>
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold font-serif tracking-tight text-white mb-6 leading-tight">
        {cfg.get('event_title')}
      </h1>
      <p class="text-base sm:text-xl text-amber-200/90 font-light max-w-3xl mx-auto mb-8 italic">
        "{cfg.get('event_subtitle')}"
      </p>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto mb-10 text-left">
        <div class="p-4 rounded-xl bg-slate-900/60 border border-emerald-800/40">
          <div class="text-amber-400 text-xs font-semibold uppercase">Quy mô</div>
          <div class="text-lg font-bold text-white mt-1">144 Golfer</div>
          <div class="text-[11px] text-slate-400">Lãnh đạo & Doanh nhân</div>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/60 border border-emerald-800/40">
          <div class="text-amber-400 text-xs font-semibold uppercase">Địa điểm</div>
          <div class="text-lg font-bold text-white mt-1">36 Hố PGA</div>
          <div class="text-[11px] text-slate-400">{venue.get('name', 'Sân Golf')}</div>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/60 border border-emerald-800/40">
          <div class="text-amber-400 text-xs font-semibold uppercase">Đơn vị chủ trì</div>
          <div class="text-lg font-bold text-white mt-1">Báo Lao Động</div>
          <div class="text-[11px] text-slate-400">97 Năm Uy Tín Báo Chí</div>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/60 border border-emerald-800/40">
          <div class="text-amber-400 text-xs font-semibold uppercase">Mục tiêu thiện nguyện</div>
          <div class="text-lg font-bold text-white mt-1">Tấm Lòng Vàng</div>
          <div class="text-[11px] text-slate-400">Tiếp bước em đến trường</div>
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-4">
        <a href="#sponsor-form" class="px-8 py-3.5 text-xs font-bold uppercase tracking-widest text-emerald-950 bg-gradient-to-r from-amber-300 via-amber-400 to-amber-500 hover:brightness-110 rounded-full shadow-xl transition flex items-center gap-2">
          <i data-lucide="file-text" class="w-4 h-4"></i>
          Nhận Hồ Sơ Mời Tài Trợ Riêng
        </a>
        <a href="#register" class="px-8 py-3.5 text-xs font-bold uppercase tracking-widest text-white border border-amber-400/50 hover:bg-amber-400/10 rounded-full transition flex items-center gap-2">
          <i data-lucide="user-plus" class="w-4 h-4"></i>
          Đăng Ký Tham Dự
        </a>
      </div>
    </div>
  </section>

  <!-- CORPORATE PACKAGES -->
  <section id="sponsor-packages" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="text-xs font-bold uppercase tracking-widest text-amber-400 mb-2">ĐỒNG HÀNH & LAN TỎA THƯƠNG HIỆU</div>
      <h2 class="text-3xl sm:text-4xl font-bold font-serif text-white">Gói Quyền Lợi Tài Trợ Doanh Nghiệp</h2>
      <p class="text-sm text-slate-300 mt-3">Tiếp cận 144 golfer là các nhà lãnh đạo tập đoàn, mở rộng mạng lưới kinh doanh và gắn kết cùng sứ mệnh vì người lao động.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {pkg_cards_html}
    </div>
  </section>

  <!-- PERSONAL PATRON -->
  <section id="personal-patron" class="py-20 bg-gradient-to-b from-emerald-950/40 to-slate-950 border-y border-amber-500/20">
    <div class="max-w-5xl mx-auto px-4">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="text-xs font-bold uppercase tracking-widest text-amber-400 mb-2">DANH DỰ & TRI ÂN</div>
        <h2 class="text-3xl sm:text-4xl font-bold font-serif text-white">{patron.get('golden_board_title', 'Bảng Vàng Danh Dự Đồng Hành')}</h2>
        <p class="text-sm text-amber-200/90 mt-3">Dành riêng cho các cá nhân hảo tâm, doanh nhân & golfer có tấm lòng vàng muốn đồng hành cùng giải đấu.</p>
      </div>

      <div class="bg-gradient-to-br from-slate-900 to-emerald-950 border-2 border-amber-500/50 rounded-2xl p-8 sm:p-10 shadow-2xl relative">
        <div class="flex flex-col md:flex-row items-center justify-between gap-8 border-b border-amber-500/30 pb-8 mb-8">
          <div>
            <div class="text-xs uppercase font-bold tracking-widest text-amber-400 mb-1">MỨC ĐỒNG HÀNH CÁ NHÂN TIÊU CHUẨN</div>
            <div class="text-3xl sm:text-4xl font-extrabold text-white font-cinzel">TỪ {patron.get('min_value_text')}</div>
            <div class="text-xs text-slate-300 mt-2 italic">* Đóng góp tự nguyện, minh bạch, trích ủng hộ Quỹ Tấm Lòng Vàng</div>
          </div>
          <div class="text-center md:text-right">
            <a href="#sponsor-form" class="px-6 py-3 text-xs font-bold uppercase tracking-widest text-emerald-950 bg-amber-400 hover:bg-amber-300 rounded-lg shadow-lg inline-flex items-center gap-2">
              <i data-lucide="heart-handshake" class="w-4 h-4"></i> Đăng Ký Đồng Hành Cá Nhân
            </a>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-amber-500/20">
            <div class="text-amber-400 font-bold text-sm mb-1 flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Suất Thi Đấu FOC
            </div>
            <div class="text-xs text-slate-300">{patron.get('golfer_slots')}</div>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-amber-500/20">
            <div class="text-amber-400 font-bold text-sm mb-1 flex items-center gap-2">
              <i data-lucide="award" class="w-4 h-4 text-emerald-400"></i> Bảng Vàng Sảnh VIP
            </div>
            <div class="text-xs text-slate-300">Vinh danh trang trọng trên Bảng vàng tại Clubhouse & Sân khấu Gala.</div>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-amber-500/20">
            <div class="text-amber-400 font-bold text-sm mb-1 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i> Kỷ Niệm Chương Vàng
            </div>
            <div class="text-xs text-slate-300">{patron.get('memento')}</div>
          </div>
        </div>

        <div class="mt-6 p-4 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-200 text-xs">
          <strong>Lưu ý về quy cách hiển thị:</strong> {patron.get('proportional_rule')}
        </div>
      </div>
    </div>
  </section>

  <!-- SPONSOR REQUEST FORM (CONFIDENTIAL DOSSIER MODE) -->
  <section id="sponsor-form" class="py-20 max-w-3xl mx-auto px-4">
    <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-8 sm:p-10 shadow-2xl">
      <div class="text-center mb-8">
        <div class="inline-flex p-3 rounded-full bg-amber-500/10 text-amber-400 mb-3 border border-amber-500/30">
          <i data-lucide="lock" class="w-6 h-6"></i>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold font-serif text-white">Yêu Cầu Nhận Hồ Sơ Mời Tài Trợ Riêng</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">
          Nhằm bảo vệ quyền lợi đàm phán và tính bảo mật thương mại, Ban Tổ chức gửi trực tiếp Hồ sơ quyền lợi chi tiết (PDF) và thư mời qua Email/Zalo của Quý Đơn vị.
        </p>
      </div>

      <form class="space-y-4" onsubmit="event.preventDefault(); alert('Cảm ơn Quý khách! Ban Thư ký Giải Báo Lao Động sẽ liên hệ gửi Hồ sơ chi tiết trong vòng 15 phút.');">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase mb-1">Họ và tên người liên hệ *</label>
            <input type="text" required placeholder="Nguyễn Văn A" class="w-full px-4 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white text-sm focus:border-amber-400 outline-none" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase mb-1">Số điện thoại / Zalo *</label>
            <input type="tel" required placeholder="0908xxxxxx" class="w-full px-4 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white text-sm focus:border-amber-400 outline-none" />
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase mb-1">Tên Doanh nghiệp / Tổ chức</label>
            <input type="text" placeholder="Tập đoàn / Công ty ABC" class="w-full px-4 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white text-sm focus:border-amber-400 outline-none" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase mb-1">Email nhận hồ sơ *</label>
            <input type="email" required placeholder="contact@company.com" class="w-full px-4 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white text-sm focus:border-amber-400 outline-none" />
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-300 uppercase mb-1">Gói tài trợ hoặc hạng mục quan tâm</label>
          <select class="w-full px-4 py-2.5 rounded-lg bg-slate-800 border border-slate-700 text-white text-sm focus:border-amber-400 outline-none">
            <option value="kim_cuong">Gói Kim Cương (500 Triệu)</option>
            <option value="bach_kim">Gói Bạch Kim (300 Triệu)</option>
            <option value="vang">Gói Vàng (150 Triệu)</option>
            <option value="bac">Gói Bạc (80 Triệu)</option>
            <option value="ca_nhan">Đồng Hành Cá Nhân (Từ 20 Triệu)</option>
            <option value="hio_in_kind">Tài trợ Hole In One / Quà tặng / Sản phẩm</option>
          </select>
        </div>

        <button type="submit" class="w-full py-3.5 text-xs font-bold uppercase tracking-widest text-emerald-950 bg-gradient-to-r from-amber-300 via-amber-400 to-amber-500 hover:brightness-110 rounded-lg shadow-xl transition mt-4">
          Gửi Yêu Cầu Nhận Hồ Sơ Riêng
        </button>
      </form>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-black border-t border-slate-800 py-12 text-slate-400 text-xs">
    <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6">
      <div>
        <div class="text-sm font-bold text-white uppercase">{cfg.get('organizer')}</div>
        <div class="mt-1">{contact.get('address')}</div>
        <div class="mt-1">Hotline: <span class="text-amber-400 font-bold">{contact.get('hotline')}</span> • Email: {contact.get('email')}</div>
      </div>
      <div class="text-center md:text-right text-[11px] text-slate-500">
        © 2026 {cfg.get('short_title')} • Bản quyền thuộc Báo Lao Động.<br />
        Hồ sơ tài trợ được quản lý theo cơ chế Dossier Mode bảo mật thương mại.
      </div>
    </div>
  </footer>

  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""
    return html

def generate_personal_dossier(cfg):
    venue = cfg.get("venue", {})
    patron = cfg.get("personal_patron", {})
    banking = cfg.get("banking", {})
    contact = cfg.get("contact", {})

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, nofollow, noarchive" />
  <title>Thư Mời & Hồ Sơ Đồng Hành Cá Nhân - {cfg.get('event_title')}</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    @page {{
      size: A4 portrait;
      margin: 0;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #cbd5e1;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .font-serif-luxury {{ font-family: 'Playfair Display', Georgia, serif; }}
    .font-cinzel {{ font-family: 'Cinzel', serif; }}
    .page-sheet {{
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      margin: 20px auto;
      background: #ffffff;
      box-shadow: 0 16px 40px rgba(0,0,0,0.18);
      position: relative;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 26px 34px 20px 34px;
      overflow: hidden;
    }}
    @media print {{
      body {{ background: #ffffff !important; padding: 0 !important; }}
      .no-print {{ display: none !important; }}
      .page-sheet {{
        margin: 0 !important;
        box-shadow: none !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        padding: 26px 34px 20px 34px !important;
      }}
    }}
    .gold-gradient-text {{
      background: linear-gradient(135deg, #C5A059 0%, #E5CCA0 50%, #9E7D3B 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
  </style>
</head>
<body class="py-6 print:py-0">

  <!-- PRINT TOOLBAR -->
  <div class="no-print max-w-[210mm] mx-auto mb-4 flex items-center justify-between bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg border border-amber-500/40">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-full bg-amber-400 text-emerald-950 font-bold flex items-center justify-center text-xs">A4</div>
      <div>
        <div class="text-xs font-bold text-amber-300 uppercase">Hồ Sơ Đồng Hành Cá Nhân (3 Trang Chuẩn In)</div>
        <div class="text-[11px] text-slate-300">Đã tối ưu ngắt trang A4 không tràn lề</div>
      </div>
    </div>
    <button onclick="window.print()" class="px-4 py-2 bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-emerald-950 text-xs font-bold rounded-lg shadow flex items-center gap-1.5 transition">
      <i data-lucide="printer" class="w-4 h-4"></i> In PDF (3 Trang)
    </button>
  </div>

  <!-- TRANG 1: THƯ MỜI & Ý NGHĨA -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full bg-emerald-900 border border-amber-400 flex items-center justify-center text-amber-300 font-cinzel font-bold text-sm">LĐ</div>
        <div>
          <div class="text-[10px] font-bold tracking-widest uppercase text-amber-800">{cfg.get('organizer')}</div>
          <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
        </div>
      </div>
      <div class="text-right">
        <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">HỒ SƠ CÁ NHÂN</span>
      </div>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <div class="text-[11px] font-bold tracking-widest text-amber-700 uppercase mb-1">THƯ MỜI DANH DỰ ĐỒNG HÀNH</div>
        <h1 class="text-2xl font-serif-luxury font-black text-emerald-950 leading-tight mb-2">{cfg.get('event_title')}</h1>
        <div class="text-xs text-slate-600 italic">"{cfg.get('event_subtitle')}"</div>
      </div>

      <div class="p-4 rounded-xl bg-emerald-50/70 border border-emerald-200 text-slate-800 text-xs leading-relaxed space-y-2">
        <p><strong>Kính gửi Quý Golfer, Doanh nhân & Quý Vị Hảo Tâm,</strong></p>
        <p>Nhân kỷ niệm dấu mốc tự hào của Báo Lao Động, Ban Tổ chức trân trọng tổ chức giải đấu thể thao đỉnh cao gắn kết cộng đồng doanh nhân, lan tỏa tinh thần tương thân tương ái.</p>
        <p>Đặc biệt, giải đấu là cầu nối nhân văn đóng góp trực tiếp vào <strong>{cfg.get('charity_cause')}</strong>, thắp sáng ước mơ học tập cho hàng ngàn trẻ em là con em người lao động vượt khó.</p>
      </div>

      <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 rounded-lg border border-slate-200 bg-slate-50">
          <div class="text-amber-800 font-bold uppercase text-[10px]">Thời gian tổ chức</div>
          <div class="text-slate-900 font-bold mt-0.5">{cfg.get('date_display')}</div>
        </div>
        <div class="p-3 rounded-lg border border-slate-200 bg-slate-50">
          <div class="text-amber-800 font-bold uppercase text-[10px]">Địa điểm thi đấu</div>
          <div class="text-slate-900 font-bold mt-0.5">{venue.get('name')}</div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Đồng Hành Cá Nhân • Trang 1/3</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 2: BẢNG VÀNG & QUY TẮC SIZE CHỮ -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">ĐẶC QUYỀN DANH DỰ</span>
    </div>

    <div class="my-auto space-y-5">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase mb-1">{patron.get('golden_board_title')}</h2>
        <div class="text-xs text-amber-800 font-bold">Mốc đóng góp cơ sở: Từ {patron.get('min_value_text')}</div>
      </div>

      <div class="p-4 rounded-xl bg-amber-50/80 border-2 border-amber-400 text-slate-800 space-y-3">
        <div class="text-xs font-bold uppercase text-amber-900 flex items-center gap-1.5">
          <i data-lucide="award" class="w-4 h-4 text-amber-700"></i> QUY ĐỊNH VINH DANH TRANG TRỌNG
        </div>
        <p class="text-xs leading-relaxed text-slate-700">
          Tên của Quý Cá nhân hảo tâm sẽ được khắc ghi trang trọng trên <strong>Bảng Vàng Danh Dự Độc Quyền</strong> đặt tại Sảnh chính Clubhouse và trình chiếu trên màn hình LED đêm Gala Trao giải.
        </p>
        <div class="p-3 rounded-lg bg-white border border-amber-300 text-xs text-amber-950 font-semibold shadow-sm">
          <strong>Quy tắc kích thước chữ:</strong> {patron.get('proportional_rule')}
        </div>
      </div>

      <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 rounded-lg border border-slate-200 bg-slate-50">
          <div class="text-emerald-900 font-bold flex items-center gap-1.5 mb-1">
            <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-700"></i> Suất Thi Đấu FOC
          </div>
          <div class="text-slate-600 text-[11px]">{patron.get('golfer_slots')}</div>
        </div>
        <div class="p-3 rounded-lg border border-slate-200 bg-slate-50">
          <div class="text-emerald-900 font-bold flex items-center gap-1.5 mb-1">
            <i data-lucide="gift" class="w-3.5 h-3.5 text-emerald-700"></i> Kỷ Niệm Chương
          </div>
          <div class="text-slate-600 text-[11px]">{patron.get('memento')}</div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Đồng Hành Cá Nhân • Trang 2/3</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 3: ĐĂNG KÝ & THÔNG TIN TIẾP NHẬN -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">TIẾP NHẬN ĐỒNG HÀNH</span>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase mb-1">PHIẾU TIẾP NHẬN ĐỒNG HÀNH</h2>
        <div class="text-xs text-slate-500">Ban Tổ chức trân trọng cảm ơn tấm lòng vàng của Quý vị</div>
      </div>

      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 text-xs space-y-2">
        <div class="grid grid-cols-2 gap-2">
          <div><strong>Họ và tên:</strong> ............................................................</div>
          <div><strong>Số điện thoại:</strong> ....................................................</div>
        </div>
        <div><strong>Tên hiển thị Bảng vàng:</strong> ............................................................................................</div>
        <div><strong>Mức tài trợ tự nguyện:</strong> ........................................................... VNĐ</div>
      </div>

      <div class="p-4 rounded-xl bg-emerald-950 text-amber-200 text-xs space-y-2 border border-amber-400">
        <div class="font-bold uppercase tracking-wider text-amber-300 text-sm flex items-center gap-2">
          <i data-lucide="credit-card" class="w-4 h-4 text-amber-400"></i> THÔNG TIN TÀI KHOẢN TIẾP NHẬN
        </div>
        <div class="space-y-1 text-slate-200">
          <div>• Đơn vị thụ hưởng: <strong class="text-white">{banking.get('account_name')}</strong></div>
          <div>• Số tài khoản: <strong class="text-amber-300 font-mono text-sm">{banking.get('account_number')}</strong></div>
          <div>• Ngân hàng: <strong class="text-white">{banking.get('bank_name')}</strong></div>
          <div>• Cú pháp: <span class="text-amber-200 font-mono">{banking.get('syntax')}</span></div>
        </div>
      </div>

      <div class="text-center text-xs text-slate-600">
        Hotline xác nhận: <strong class="text-emerald-900">{contact.get('hotline')}</strong> • Email: <strong class="text-emerald-900">{contact.get('email')}</strong>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Đồng Hành Cá Nhân • Trang 3/3</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <script>lucide.createIcons();</script>
</body>
</html>
"""
    return html

def generate_corporate_dossier(cfg):
    venue = cfg.get("venue", {})
    pkgs = cfg.get("corporate_packages", [])
    contact = cfg.get("contact", {})
    banking = cfg.get("banking", {})

    pkg_pages_html = ""
    for idx, p in enumerate(pkgs, start=5):
        m_list = "".join([f'<li class="flex items-start gap-2 mb-1.5"><i data-lucide="check-circle" class="w-3.5 h-3.5 text-amber-700 shrink-0 mt-0.5"></i><span>{m}</span></li>' for m in p.get("media_rights", [])])
        b_list = "".join([f'<li class="flex items-start gap-2 mb-1.5"><i data-lucide="award" class="w-3.5 h-3.5 text-emerald-700 shrink-0 mt-0.5"></i><span>{b}</span></li>' for b in p.get("branding_rights", [])])
        pkg_pages_html += f"""
  <!-- TRANG {idx}: GÓI {p.get('name')} -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">{p.get('badge')}</span>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <h2 class="text-2xl font-serif-luxury font-black text-emerald-950 uppercase">{p.get('name')}</h2>
        <div class="text-2xl font-cinzel font-black text-amber-700 mt-1">{p.get('value_text')}</div>
        <div class="text-xs text-slate-500 mt-0.5">Số lượng tối đa: <strong class="text-slate-800">{p.get('slots')}</strong></div>
      </div>

      <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 rounded-lg bg-emerald-50 border border-emerald-200">
          <div class="font-bold text-emerald-900 uppercase text-[10px] mb-1">Suất Thi Đấu Golfer</div>
          <div class="text-slate-800 font-semibold">{p.get('golfer_slots')}</div>
        </div>
        <div class="p-3 rounded-lg bg-amber-50 border border-amber-200">
          <div class="font-bold text-amber-900 uppercase text-[10px] mb-1">Tiệc Gala Dinner</div>
          <div class="text-slate-800 font-semibold">{p.get('gala_seats')}</div>
        </div>
      </div>

      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 text-xs">
        <div class="font-bold text-emerald-950 uppercase mb-2 text-[11px] flex items-center gap-1.5">
          <i data-lucide="tv" class="w-4 h-4 text-emerald-800"></i> QUYỀN LỢI TRUYỀN THÔNG BÁO LAO ĐỘNG
        </div>
        <ul class="text-slate-700 leading-relaxed">
          {m_list}
        </ul>
      </div>

      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 text-xs">
        <div class="font-bold text-amber-900 uppercase mb-2 text-[11px] flex items-center gap-1.5">
          <i data-lucide="flag" class="w-4 h-4 text-amber-800"></i> QUYỀN LỢI NHẬN DIỆN TẠI SÂN & SỰ KIỆN
        </div>
        <ul class="text-slate-700 leading-relaxed">
          {b_list}
        </ul>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang {idx}/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, nofollow, noarchive" />
  <title>Hồ Sơ Mời Tài Trợ - {cfg.get('event_title')}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    @page {{ size: A4 portrait; margin: 0; }}
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: #cbd5e1; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .font-serif-luxury {{ font-family: 'Playfair Display', Georgia, serif; }}
    .font-cinzel {{ font-family: 'Cinzel', serif; }}
    .page-sheet {{
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      margin: 20px auto;
      background: #ffffff;
      box-shadow: 0 16px 40px rgba(0,0,0,0.18);
      position: relative;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px 32px 18px 32px;
      overflow: hidden;
    }}
    @media print {{
      body {{ background: #ffffff !important; padding: 0 !important; }}
      .no-print {{ display: none !important; }}
      .page-sheet {{
        margin: 0 !important;
        box-shadow: none !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        padding: 24px 32px 18px 32px !important;
      }}
    }}
  </style>
</head>
<body class="py-6 print:py-0">

  <!-- PRINT TOOLBAR -->
  <div class="no-print max-w-[210mm] mx-auto mb-4 flex items-center justify-between bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg border border-amber-500/40">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-full bg-amber-400 text-emerald-950 font-bold flex items-center justify-center text-xs">10P</div>
      <div>
        <div class="text-xs font-bold text-amber-300 uppercase">Hồ Sơ Doanh Nghiệp (10 Trang A4)</div>
        <div class="text-[11px] text-slate-300">Chuẩn in ấn đối ngoại cao cấp</div>
      </div>
    </div>
    <button onclick="window.print()" class="px-4 py-2 bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-emerald-950 text-xs font-bold rounded-lg shadow flex items-center gap-1.5 transition">
      <i data-lucide="printer" class="w-4 h-4"></i> In PDF (10 Trang)
    </button>
  </div>

  <!-- TRANG 1: BÌA HỒ SƠ -->
  <div class="page-sheet bg-gradient-to-b from-[#00170d] via-[#002e1b] to-[#00170d] text-white">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-[11px] uppercase tracking-widest text-amber-400 font-bold">{cfg.get('organizer')}</div>
      <div class="text-[10px] uppercase tracking-widest text-slate-300 font-mono">CONFIDENTIAL DOSSIER</div>
    </div>

    <div class="my-auto text-center py-12">
      <div class="w-20 h-20 rounded-full border-2 border-amber-400/80 mx-auto mb-6 flex items-center justify-center text-amber-300 font-cinzel font-black text-3xl shadow-2xl bg-emerald-950">
        LĐ
      </div>
      <div class="text-xs font-bold tracking-[0.3em] text-amber-400 uppercase mb-3">HỒ SƠ MỜI TÀI TRỢ CHÍNH THỨC</div>
      <h1 class="text-3xl sm:text-4xl font-serif-luxury font-black text-white leading-tight mb-4 tracking-tight">
        {cfg.get('event_title')}
      </h1>
      <div class="text-sm text-amber-200/90 italic max-w-lg mx-auto mb-8 font-light">
        "{cfg.get('event_subtitle')}"
      </div>
      <div class="inline-block px-5 py-2 rounded-full border border-amber-400/50 bg-emerald-900/60 text-amber-300 text-xs font-bold tracking-widest uppercase">
        {cfg.get('date_display')} • {venue.get('name')}
      </div>
    </div>

    <div class="border-t border-amber-500/30 pt-3 flex items-center justify-between text-[10px] text-amber-200/70">
      <div>Hồ Sơ Quyền Lợi Doanh Nghiệp • Trang 1/10</div>
      <div class="font-bold text-amber-400 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 2: THƯ NGỎ TỪ BAN TỔ CHỨC -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">THƯ NGỎ</span>
    </div>

    <div class="my-auto space-y-4 text-xs leading-relaxed text-slate-800">
      <div class="text-center mb-4">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase">THƯ NGỎ MỜI TÀI TRỢ</h2>
        <div class="text-xs text-amber-800 font-bold mt-1">Gắn kết Doanh nghiệp - Phụng sự Cộng đồng</div>
      </div>
      <p><strong>Kính gửi Ban Lãnh đạo Quý Doanh nghiệp,</strong></p>
      <p>{cfg.get('organizer')} xin gửi lời chào trân trọng nhất đến Quý Doanh nghiệp.</p>
      <p>Nhằm tạo dựng không gian giao lưu thể thao đỉnh cao kết nối 144 nhà lãnh đạo doanh nghiệp tiêu biểu, đồng thời thực hiện trách nhiệm xã hội nhân văn, chúng tôi long trọng tổ chức <strong>{cfg.get('event_title')}</strong>.</p>
      <p>Sự đồng hành của Quý Doanh nghiệp không chỉ mang lại giá trị quảng bá vượt trội trên hệ sinh thái truyền thông Báo Lao Động mà còn đóng góp trực tiếp vào <strong>{cfg.get('charity_cause')}</strong>.</p>
      <p>Ban Tổ chức cam kết mang đến những đặc quyền truyền thông và quyền lợi nhận diện tương xứng nhất với vị thế của Quý vị.</p>
      <div class="text-right pt-6">
        <div class="font-bold uppercase text-emerald-950 text-xs">TRƯỞNG BAN TỔ CHỨC</div>
        <div class="text-xs text-slate-600 mt-0.5">Báo Lao Động</div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang 2/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 3: ĐỊA ĐIỂM & ĐẲNG CẤP SÂN -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">ĐỊA ĐIỂM</span>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase">{venue.get('name')}</h2>
        <div class="text-xs text-slate-600">{venue.get('address')}</div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 leading-relaxed space-y-2">
        <p><strong>Quy mô sân:</strong> {venue.get('scale')}</p>
        <p>{venue.get('description')}</p>
        <p>Khu vực Clubhouse sang trọng, sảnh tiệc Gala đẳng cấp 5 sao với sức chứa hơn 300 khách, là không gian hoàn hảo cho Lễ Trao giải và đêm tiệc giao lưu kinh tế đỉnh cao.</p>
      </div>

      <div class="grid grid-cols-3 gap-3 text-center text-xs">
        <div class="p-3 bg-emerald-50 rounded-lg border border-emerald-200">
          <div class="text-lg font-bold text-emerald-950">144</div>
          <div class="text-[10px] text-slate-600 uppercase font-semibold">Golfer VIP</div>
        </div>
        <div class="p-3 bg-emerald-50 rounded-lg border border-emerald-200">
          <div class="text-lg font-bold text-emerald-950">36 Hố</div>
          <div class="text-[10px] text-slate-600 uppercase font-semibold">Tiêu Chuẩn PGA</div>
        </div>
        <div class="p-3 bg-emerald-50 rounded-lg border border-emerald-200">
          <div class="text-lg font-bold text-emerald-950">04 Bảng</div>
          <div class="text-[10px] text-slate-600 uppercase font-semibold">A, B, C & Nữ</div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang 3/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 4: HỆ SINH THÁI TRUYỀN THÔNG BÁO LAO ĐỘNG -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">TRUYỀN THÔNG</span>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase">NGUỒN LỰC TRUYỀN THÔNG BÁO LAO ĐỘNG</h2>
        <div class="text-xs text-amber-800 font-bold mt-1">Sức Mạnh Lan Tỏa Thương Hiệu Đa Nền Tảng</div>
      </div>

      <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
          <div class="font-bold text-emerald-900 mb-1 flex items-center gap-1.5 text-sm">
            <i data-lucide="globe" class="w-4 h-4 text-emerald-700"></i> Báo Điện Tử Laodong.vn
          </div>
          <p class="text-slate-600 text-[11px] leading-relaxed">
            Thuộc top báo điện tử chính luận uy tín nhất Việt Nam, tiếp cận hàng chục triệu độc giả mỗi tháng. Đảm bảo vị trí PR trang trọng.
          </p>
        </div>
        <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
          <div class="font-bold text-emerald-900 mb-1 flex items-center gap-1.5 text-sm">
            <i data-lucide="video" class="w-4 h-4 text-emerald-700"></i> Kênh Lao Động TV
          </div>
          <p class="text-slate-600 text-[11px] leading-relaxed">
            Sản xuất các bản tin chuyên đề, phỏng vấn sâu độc quyền các lãnh đạo doanh nghiệp tài trợ.
          </p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-amber-50 border border-amber-300 text-xs text-slate-700 leading-relaxed">
        <strong>Mạng xã hội & Đa nền tảng:</strong> Độ phủ sóng rộng khắp trên Facebook Fanpage tích xanh, YouTube, TikTok Báo Lao Động giúp thương hiệu của Nhà tài trợ tiếp cận cộng đồng doanh nhân và công chúng một cách hiệu quả nhất.
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang 4/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  {pkg_pages_html}

  <!-- TRANG 9: MA TRẬN QUYỀN LỢI TỔNG THỂ -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">MA TRẬN QUYỀN LỢI</span>
    </div>

    <div class="my-auto space-y-3">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase">BẢNG SO SÁNH QUYỀN LỢI CÁC GÓI</h2>
      </div>

      <div class="overflow-hidden rounded-xl border border-slate-200 text-[10px]">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-emerald-950 text-amber-300">
              <th class="p-2 font-bold border-b border-slate-800">HẠNG MỤC QUYỀN LỢI</th>
              <th class="p-2 font-bold border-b border-slate-800 text-center">KIM CƯƠNG (500Tr)</th>
              <th class="p-2 font-bold border-b border-slate-800 text-center">BẠCH KIM (300Tr)</th>
              <th class="p-2 font-bold border-b border-slate-800 text-center">VÀNG (150Tr)</th>
              <th class="p-2 font-bold border-b border-slate-800 text-center">BẠC (80Tr)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 text-slate-700">
            <tr>
              <td class="p-2 font-semibold">Suất thi đấu Golfer FOC</td>
              <td class="p-2 text-center font-bold text-emerald-900">08 Golfer</td>
              <td class="p-2 text-center font-bold text-emerald-900">05 Golfer</td>
              <td class="p-2 text-center font-bold text-emerald-900">03 Golfer</td>
              <td class="p-2 text-center font-bold text-emerald-900">01 Golfer</td>
            </tr>
            <tr class="bg-slate-50">
              <td class="p-2 font-semibold">Thư mời Tiệc Gala VIP</td>
              <td class="p-2 text-center">02 Bàn (20 khách)</td>
              <td class="p-2 text-center">01 Bàn (10 khách)</td>
              <td class="p-2 text-center">05 Thư mời</td>
              <td class="p-2 text-center">02 Thư mời</td>
            </tr>
            <tr>
              <td class="p-2 font-semibold">Bài PR trên laodong.vn</td>
              <td class="p-2 text-center text-emerald-800 font-bold">02 Bài Nổi Bật</td>
              <td class="p-2 text-center text-emerald-800 font-bold">01 Bài Nổi Bật</td>
              <td class="p-2 text-center">Bài Cảm Ơn</td>
              <td class="p-2 text-center">Ghi danh</td>
            </tr>
            <tr class="bg-slate-50">
              <td class="p-2 font-semibold">Phát biểu Đêm Gala</td>
              <td class="p-2 text-center text-amber-700 font-bold">Độc quyền</td>
              <td class="p-2 text-center text-slate-400">-</td>
              <td class="p-2 text-center text-slate-400">-</td>
              <td class="p-2 text-center text-slate-400">-</td>
            </tr>
            <tr>
              <td class="p-2 font-semibold">Biển hiệu trên sân (Tee-box)</td>
              <td class="p-2 text-center">04 Biển Đẹp Nhất</td>
              <td class="p-2 text-center">02 Biển</td>
              <td class="p-2 text-center">01 Biển</td>
              <td class="p-2 text-center text-slate-400">-</td>
            </tr>
            <tr class="bg-slate-50">
              <td class="p-2 font-semibold">Gian trưng bày sản phẩm Clubhouse</td>
              <td class="p-2 text-center text-emerald-800 font-bold">Vị trí VIP nhất</td>
              <td class="p-2 text-center">Có bố trí</td>
              <td class="p-2 text-center text-slate-400">-</td>
              <td class="p-2 text-center text-slate-400">-</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang 9/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <!-- TRANG 10: XÁC NHẬN TÀI TRỢ & THÔNG TIN LIÊN HỆ -->
  <div class="page-sheet">
    <div class="flex items-center justify-between border-b border-amber-500/30 pb-3">
      <div class="text-xs font-extrabold text-slate-900">{cfg.get('short_title')}</div>
      <span class="text-[9px] uppercase px-2 py-0.5 rounded bg-emerald-900 text-amber-200 font-bold tracking-wider">XÁC NHẬN</span>
    </div>

    <div class="my-auto space-y-4">
      <div class="text-center">
        <h2 class="text-xl font-serif-luxury font-black text-emerald-950 uppercase">PHIẾU ĐĂNG KÝ TÀI TRỢ DOANH NGHIỆP</h2>
      </div>

      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 text-xs space-y-2 text-slate-700">
        <div><strong>Tên Doanh nghiệp:</strong> ..........................................................................................................</div>
        <div class="grid grid-cols-2 gap-2">
          <div><strong>Người đại diện:</strong> .....................................................</div>
          <div><strong>Chức vụ:</strong> ......................................................</div>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div><strong>Điện thoại:</strong> ...........................................................</div>
          <div><strong>Email:</strong> ...........................................................</div>
        </div>
        <div><strong>Gói tài trợ đăng ký:</strong> [ ] Kim Cương &nbsp;&nbsp; [ ] Bạch Kim &nbsp;&nbsp; [ ] Vàng &nbsp;&nbsp; [ ] Bạc &nbsp;&nbsp; [ ] Khác</div>
      </div>

      <div class="p-4 rounded-xl bg-emerald-950 text-amber-200 text-xs space-y-2 border border-amber-400">
        <div class="font-bold uppercase tracking-wider text-amber-300 text-sm">THÔNG TIN TÀI KHOẢN TIẾP NHẬN</div>
        <div class="space-y-1 text-slate-200">
          <div>• Tên tài khoản: <strong class="text-white">{banking.get('account_name')}</strong></div>
          <div>• Số tài khoản: <strong class="text-amber-300 font-mono text-sm">{banking.get('account_number')}</strong></div>
          <div>• Ngân hàng: <strong class="text-white">{banking.get('bank_name')}</strong></div>
        </div>
      </div>

      <div class="text-center text-xs text-slate-600">
        Địa chỉ tiếp nhận: {contact.get('address')}<br />
        Hotline: <strong class="text-emerald-900">{contact.get('hotline')}</strong> • Email: <strong class="text-emerald-900">{contact.get('email')}</strong>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>Hồ Sơ Mời Tài Trợ • Trang 10/10</div>
      <div class="font-bold text-amber-800 uppercase">BAN TỔ CHỨC</div>
    </div>
  </div>

  <script>lucide.createIcons();</script>
</body>
</html>
"""
    return html

def generate_robots_txt():
    return """User-agent: *
Disallow: /dossier.html
Disallow: /dossier_ca_nhan.html
Disallow: /*.pdf
Disallow: /du_toan*
"""

def generate_render_pdf_script():
    return """#!/usr/bin/env python3
import os
import subprocess
import sys

def render_pdf(html_path, pdf_path):
    print(f"[*] Rendering {html_path} -> {pdf_path}...")
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if not os.path.exists(chrome_path):
        print(f"[!] Chrome binary not found at {chrome_path}")
        return False

    abs_html = os.path.abspath(html_path)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        f"file://{abs_html}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] Successfully exported {pdf_path} ({os.path.getsize(pdf_path):,} bytes)")
        return True
    else:
        print(f"[!] Export failed: {res.stderr}")
        return False

if __name__ == '__main__':
    render_pdf("dossier_ca_nhan.html", "HSTT_Ca_Nhan.pdf")
    render_pdf("dossier.html", "HSTT_Doanh_Nghiep.pdf")
"""

def generate_vercel_config():
    return """{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/dossier(.*)",
      "headers": [
        { "key": "X-Robots-Tag", "value": "noindex, nofollow, noarchive" }
      ]
    },
    {
      "source": "/(.*).pdf",
      "headers": [
        { "key": "X-Robots-Tag", "value": "noindex, nofollow, noarchive" }
      ]
    }
  ]
}
"""

def main():
    parser = argparse.ArgumentParser(description="Sports Luxe Event Scaffolding Engine")
    parser.add_argument("--init", dest="init_file", help="Initialize a sample event configuration JSON")
    parser.add_argument("--build", action="store_true", help="Build full event bundle from configuration")
    parser.add_argument("--config", dest="config_file", help="Path to event configuration JSON")
    parser.add_argument("--out", dest="out_dir", default="./dist", help="Output directory for generated files")

    args = parser.parse_args()

    if args.init_file:
        sample_path = Path(__file__).resolve().parent.parent / "_templates_sports_luxe" / "sample_event_config.json"
        if sample_path.exists():
            shutil.copyfile(sample_path, args.init_file)
            print(f"[+] Initialized sample event config at: {args.init_file}")
        else:
            print("[!] sample_event_config.json not found.")
        sys.exit(0)

    if args.build:
        if not args.config_file or not os.path.exists(args.config_file):
            print(f"[!] Error: Config file not found at {args.config_file}")
            sys.exit(1)

        with open(args.config_file, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        out_path = Path(args.out_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        print(f"[*] Building Sports Luxe Event: {cfg.get('event_title')}...")

        # 1. Landing Page
        landing_html = generate_landing_page(cfg)
        with open(out_path / "index.html", "w", encoding="utf-8") as f:
            f.write(landing_html)
        print(f"  [+] Generated Landing Page: {out_path / 'index.html'}")

        # 2. Corporate Dossier (10 pages)
        corp_html = generate_corporate_dossier(cfg)
        with open(out_path / "dossier.html", "w", encoding="utf-8") as f:
            f.write(corp_html)
        print(f"  [+] Generated Corporate Dossier (10 pages): {out_path / 'dossier.html'}")

        # 3. Personal Dossier (3 pages)
        personal_html = generate_personal_dossier(cfg)
        with open(out_path / "dossier_ca_nhan.html", "w", encoding="utf-8") as f:
            f.write(personal_html)
        print(f"  [+] Generated Personal Dossier (3 pages): {out_path / 'dossier_ca_nhan.html'}")

        # 4. Robots.txt
        with open(out_path / "robots.txt", "w", encoding="utf-8") as f:
            f.write(generate_robots_txt())
        print(f"  [+] Generated robots.txt (Dossier Mode)")

        # 5. Vercel config
        with open(out_path / "vercel.json", "w", encoding="utf-8") as f:
            f.write(generate_vercel_config())
        print(f"  [+] Generated vercel.json")

        # 6. Render PDF script
        render_script = out_path / "render_pdf.py"
        with open(render_script, "w", encoding="utf-8") as f:
            f.write(generate_render_pdf_script())
        os.chmod(render_script, 0o755)
        print(f"  [+] Generated render_pdf.py (Headless Chrome)")

        print(f"[SUCCESS] All deliverables generated in: {out_path.resolve()}")

if __name__ == "__main__":
    main()
