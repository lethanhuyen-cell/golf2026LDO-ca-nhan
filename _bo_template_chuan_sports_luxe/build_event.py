#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
CỖ MÁY BIÊN DỊCH BỘ TEMPLATE CHUẨN SPORTS LUXE (EXACT REPLICATION ENGINE)
Tác giả: Ban Biên tập & Bộ phận Công nghệ Sự kiện Báo Lao Động
================================================================================
Công dụng:
- Giữ NGUYÊN 100% quy cách, mẫu chữ, bố trí đồ họa, hiệu ứng viền vàng, thẻ meta,
  ngắt trang A4 chuẩn in của bộ thiết kế gốc.
- Tự động thay thế toàn bộ biến số nội dung của sự kiện mới từ file JSON.
- Sao chép toàn bộ kho tài nguyên đồ họa (assets/images) sang dự án mới.
- Tự động thiết lập Dossier Mode (robots.txt, vercel.json) và script in PDF.

Sử dụng:
  python3 build_event.py --config variables_sample.json --out ../Giai_Dau_Moi_2027
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path

def apply_template(template_path, variables):
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for key, val in variables.items():
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, str(val))
    
    return content

def generate_robots_txt():
    return """User-agent: *
Disallow: /dossier.html
Disallow: /dossier_ca_nhan.html
Disallow: /*.pdf
Disallow: /du_toan*
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

def generate_render_pdf_script():
    return """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def render_pdf(html_file, pdf_output):
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if not os.path.exists(chrome_path):
        print(f"[!] Không tìm thấy Google Chrome tại: {chrome_path}")
        return False
    
    abs_html = os.path.abspath(html_file)
    print(f"[*] Đang xuất in: {html_file} -> {pdf_output}...")
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--disable-background-networking",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_output}",
        f"file://{abs_html}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_output):
        print(f"  [+] Thành công: {pdf_output} ({os.path.getsize(pdf_output):,} bytes)")
        return True
    else:
        print(f"  [!] Lỗi khi xuất PDF: {res.stderr}")
        return False

if __name__ == '__main__':
    render_pdf("dossier_ca_nhan.html", "HSTT_Ca_Nhan_Chuan_In.pdf")
    render_pdf("dossier.html", "HSTT_Doanh_Nghiep_Chuan_In.pdf")
"""

def main():
    parser = argparse.ArgumentParser(description="Build sports luxe event clone from master templates")
    parser.add_argument("--config", dest="config", default="variables_sample.json", help="Path to event variables JSON")
    parser.add_argument("--out", dest="out_dir", required=True, help="Destination directory for the new event")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent

    if not os.path.exists(args.config):
        print(f"[!] Error: File biến số không tồn tại tại {args.config}")
        sys.exit(1)

    with open(args.config, 'r', encoding='utf-8') as f:
        vars_map = json.load(f)

    out_path = Path(args.out_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"[*] Bắt đầu nhân bản sự kiện theo bộ template chuẩn Sports Luxe...")
    print(f"    • Sự kiện: {vars_map.get('TOURNAMENT_NAME_UPPER', 'GIẢI ĐẤU')}")
    print(f"    • Thư mục đích: {out_path}")

    # 1. Landing Page
    print("[1/5] Biên dịch Landing Page (index.html)...")
    landing_tpl = base_dir / "template_index.html"
    landing_out = apply_template(landing_tpl, vars_map)
    with open(out_path / "index.html", "w", encoding="utf-8") as f:
        f.write(landing_out)

    # 2. Corporate Dossier (10 pages)
    print("[2/5] Biên dịch Hồ sơ Doanh nghiệp 10 trang (dossier.html)...")
    corp_tpl = base_dir / "template_dossier.html"
    corp_out = apply_template(corp_tpl, vars_map)
    with open(out_path / "dossier.html", "w", encoding="utf-8") as f:
        f.write(corp_out)

    # 3. Personal Dossier (3 pages)
    print("[3/5] Biên dịch Hồ sơ Cá nhân 3 trang (dossier_ca_nhan.html)...")
    pers_tpl = base_dir / "template_dossier_ca_nhan.html"
    pers_out = apply_template(pers_tpl, vars_map)
    with open(out_path / "dossier_ca_nhan.html", "w", encoding="utf-8") as f:
        f.write(pers_out)

    # 4. Copy Assets (Images, Logos, Textures)
    print("[4/5] Sao chép toàn bộ kho tài nguyên đồ họa (assets/images)...")
    src_assets = base_dir / "assets"
    dst_assets = out_path / "assets"
    if src_assets.exists():
        if dst_assets.exists():
            shutil.rmtree(dst_assets)
        shutil.copytree(src_assets, dst_assets)

    # 5. Security & Build Tools
    print("[5/5] Cài đặt Dossier Mode bảo mật & Tool in PDF...")
    with open(out_path / "robots.txt", "w", encoding="utf-8") as f:
        f.write(generate_robots_txt())
    with open(out_path / "vercel.json", "w", encoding="utf-8") as f:
        f.write(generate_vercel_config())
    
    render_script = out_path / "render_pdf.py"
    with open(render_script, "w", encoding="utf-8") as f:
        f.write(generate_render_pdf_script())
    os.chmod(render_script, 0o755)

    print("\n[THÀNH CÔNG] Đã tạo hoàn chỉnh dự án mới với đồ họa, quy cách và mẫu chữ Y HỆT!")
    print(f"👉 Thư mục dự án: {out_path}")
    print("👉 Chạy lệnh in PDF: cd '{}' && python3 render_pdf.py".format(out_path))

if __name__ == '__main__':
    main()
