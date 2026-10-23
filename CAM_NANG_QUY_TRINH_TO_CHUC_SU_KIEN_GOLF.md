# CẨM NANG & SỔ TAY QUY TRÌNH TỔ CHỨC GIẢI GOLF & ĐẠI SỰ KIỆN THỂ THAO
### Cơ Quan Chủ Trì: Ban Biên Tập Báo Lao Động — Văn Phòng Đại Diện tại TP.HCM & Đông Nam Bộ
*Phiên bản: Master 2026 • Bảo lưu toàn bộ tri thức thực chiến và quy chuẩn xuất bản số*

---

## 🎯 LỜI NÓI ĐẦU: VÌ SAO CẦN CUỐN SỔ TAY NÀY?
Cuốn cẩm nang này được đúc kết từ toàn bộ quá trình xây dựng, thiết kế và tối ưu dự án **Giải Golf Báo Lao Động Open 2026** (Kỷ niệm 97 năm Báo Lao Động).

Mục tiêu của tài liệu này là cung cấp **Bộ công cụ & Phương pháp luận nhân bản (Replication Blueprint)**, giúp bất kỳ phóng viên, chuyên viên đối ngoại hay ban tổ chức nào của Báo Lao Động có thể **tạo dựng một giải đấu thể thao hoặc đại sự kiện mới chỉ trong 24 – 48 giờ** với chuẩn mực cao nhất, không xảy ra sai sót pháp lý hay rò rỉ thương mại.

---

## 🏛️ PHẦN I: MA TRẬN TÀI LIỆU VÀ CẤU TRÚC THƯ MỤC CHUẨN

Khi bắt đầu một giải đấu mới, hãy tạo cấu trúc thư mục chuẩn theo mô hình sau:

```
📁 [TÊN_GIAI_DAU_NAM]/
├── 📄 index.html                       # Landing Page chính thức (Public & Sports Luxe)
├── 📄 dossier.html                     # Hồ sơ Mời tài trợ Doanh nghiệp (10-12 trang A4)
├── 📄 dossier_ca_nhan.html             # Hồ sơ Đồng hành Cá nhân (3 trang A4 Quiet Luxury)
├── 📄 trailer.html                     # Video Motion / Trailer tương tác 60s
├── 📄 robots.txt                       # Chặn Google lập chỉ mục dossier & pdf
├── 📄 NHAT_KY_LAM_VIEC.md              # Session Log ghi nhận tiến độ & audit trail
├── 📄 CAM_NANG_QUY_TRINH_TO_CHUC.md    # Cẩm nang vận hành (Tài liệu này)
├── 📕 Ho_So_Moi_Tai_Tro_*.pdf          # File PDF Doanh nghiệp in ấn & gửi VIP
├── 📕 HSTT_Ca_Nhan_*.pdf               # File PDF Cá nhân in ấn & gửi VIP
├── 📁 assets/
│   └── 📁 images/                      # Ảnh flycam thực tế, logo chuẩn, cúp, gala
├── 📁 _backups/                        # Lưu trữ các điểm phục hồi (Restore points & zip)
└── 🔒 .gitignore                       # Chặn 100% file tài chính (DU_TOAN*, *.xlsx, *.xls)
```

---

## 🛡️ PHẦN II: CHIẾN LƯỢC BẢO MẬT 3 TẦNG (CONFIDENTIAL DOSSIER MODE)

### 1. Bản chất vấn đề
- Cơ cấu tài trợ và đặc biệt là **Gói Đồng Hành Cá Nhân** (với quy chuẩn *Size chữ trên Bảng Vàng tỉ lệ thuận với giá trị tài trợ mốc 20 triệu*) là **tài sản sáng tạo độc quyền của Báo Lao Động**.
- Nếu để link tải file công khai trên web, các báo khác hoặc công ty tổ chức giải phong trào sẽ sao chép nguyên xi.
- Việc công khai giá cũng làm giảm vị thế ngoại giao khi tiếp xúc lãnh đạo doanh nghiệp lớn.

### 2. Quy tắc triển khai
1. **Trên Trang chủ (`index.html`)**:
   - Nút hành động phải là: `Đăng Ký Tài Trợ` hoặc `Liên Hệ Ban Tài Trợ` (Dẫn xuống form để thu thập Lead: Tên, Doanh nghiệp, Số điện thoại).
   - Tuyệt đối không gắn link trực tiếp sang `dossier.html` hay file PDF.
2. **Trên Search Engine (Google, Bing)**:
   - Tạo file `robots.txt` cấm bot thu thập dữ liệu:
     ```txt
     User-agent: *
     Disallow: /dossier.html
     Disallow: /dossier_ca_nhan.html
     Disallow: /*.pdf
     Allow: /
     ```
   - Thêm thẻ `<meta name="robots" content="noindex, nofollow, noarchive" />` vào thẻ `<head>` của cả 2 file dossier.
3. **Trong Khâu Chăm Sóc Đối Ngoại (1-1)**:
   - Khi doanh nghiệp điền form hoặc gọi hotline -> Ban Thư ký thẩm định và gửi file PDF hoặc gửi link riêng có kèm thư mời trang trọng.

---

## 🎨 PHẦN III: TIÊU CHUẨN THIẾT KẾ & THẨM MỸ MAJOR (SPORTS LUXE)

### 1. Bảng màu di sản
- **Xanh Masters Green (`#004d2c`, `#00331e`)**: Màu truyền thống thể thao quý tộc, tượng trưng cho uy tín của tổ chức Công đoàn và Báo Lao Động.
- **Vàng Claret Gold (`#C5A059`, `#E5CCA0`, `#9E7D3B`)**: Điểm xuyết ở viền thẻ, badge vinh danh, text gold-foil.
- **Nền sáng trang trọng (`#FFFFFF`, `#F8FAF9`, `#CBD5E1`)**: Giữ cho trang web và tài liệu đọc dễ chịu, sang trọng chuẩn Quiet Luxury.
- **Đỏ Lao Động (`#BE1E2D`)**: Điểm xuyết ở logo và các nhãn quan trọng của cơ quan chủ trì.

### 2. Quy chuẩn hình ảnh
- **Ảnh Sân Golf**: Phải là ảnh flycam thực tế sắc nét:
  - 01 ảnh góc rộng hoàng hôn / đêm rực sáng đèn Night Golf.
  - 01 ảnh góc cao chụp green uốn lượn và bẫy cát (sand bunkers).
- **Ảnh Nhân vật minh họa**: 100% người Châu Á / Việt Nam. Không mặc đồ lòe loẹt. Ưu tiên phong thái lịch lãm (Polo thi đấu hoặc Polo kết hợp Blazer smart-casual).
- **Tránh lỗi AI**: Tuyệt đối không dùng ảnh AI có lỗi biến dạng ngón tay, cán gậy golf méo mó hay bàn tay chơi golf đè chồng nhau.

---

## 📄 PHẦN IV: CÔNG THỨC 2 BỘ HỒ SƠ TÀI TRỢ CHUẨN MỰC

### 1. Bộ Hồ Sơ Doanh Nghiệp (10 Trang A4)
| Trang | Tiêu đề | Nội dung cốt lõi |
|:---:|---|---|
| **01** | Bìa chính | Tiêu đề giải, thời gian, địa điểm, logo Báo Lao Động & Sân Golf. |
| **02** | Thư ngỏ | Ký tên duy nhất: **BAN TỔ CHỨC**. Nêu bật ý nghĩa 97 năm Báo Lao Động. |
| **03** | Khung lịch trình | Lịch trình 4 mốc (Check-in, Khai mạc, Shotgun 18 hố, Gala Dinner). |
| **04** | Đơn vị phối hợp | Giới thiệu Sân golf 36 hố và Hệ sinh thái truyền thông Báo Lao Động. |
| **05** | Điểm chạm thương hiệu | Sơ đồ 07 điểm chạm (Tee-box, Photowall, Cúp, Màn hình Gala...). |
| **06** | Ma trận quyền lợi | Bảng tổng hợp đối soát 06 cấp gói tài trợ. |
| **07-09** | Bóc tách từng gói | Chi tiết số lượng suất thi đấu, logo trên báo in/điện tử, banner... |
| **10** | Nguyên tắc & Hotline | Hướng dẫn đăng ký, hotline 24/7 của Tiểu ban Tài trợ. |

### 2. Bộ Hồ Sơ Cá Nhân (3 Trang A4 — Độc Bản Không Trùng Lặp)
| Trang | Tiêu đề | Trọng tâm nội dung |
|:---:|---|---|
| **01** | Bìa & Tầm vóc | Ảnh flycam sân golf + **3 Trụ cột tầm vóc**: Bản lĩnh 97 năm, 144 Golfer tinh hoa, Dấu ấn danh dự. *(Không đưa quyền lợi FOC/size chữ vào trang này).* |
| **02** | Thư mời trang trọng | Thư mời tham gia với tư cách **Golfer Danh Dự** (mốc 20 triệu VNĐ), ký tên **BAN TỔ CHỨC**, mở rộng 2 ảnh flycam sân 36 hố và Clubhouse 10.000m². |
| **03** | Đặc quyền & Bảng vàng | **Nơi DUY NHẤT** thể hiện chi tiết: 01 Suất FOC + Vinh danh Bảng vàng + Quy chuẩn bôi đậm: **Kích thước size chữ họ tên tỉ lệ thuận với giá trị tài trợ (mốc 20 triệu VNĐ). Mức tài trợ càng cao, kích thước họ tên hiển thị càng lớn tương ứng.** + Mockup 3D Bảng vàng + Hotline Mrs. Thanh Thuỳ (0908221195). |

---

## ⚙️ PHẦN V: QUY TRÌNH KỸ THUẬT & LỆNH XUẤT BẢN

### 1. Kỹ thuật Print CSS A4 (Chống tràn trang)
Mỗi trang hồ sơ phải nằm trong thẻ `<div class="page-sheet">` với CSS chuẩn:
```css
@page {
  size: A4 portrait;
  margin: 0;
}
.page-sheet {
  width: 210mm;
  height: 297mm;
  min-height: 297mm;
  max-height: 297mm;
  margin: 20px auto;
  box-sizing: border-box;
  overflow: hidden;
  page-break-after: always;
}
@media print {
  .page-sheet {
    margin: 0 !important;
    width: 100% !important;
    height: 100vh !important;
  }
}
```

### 2. Lệnh Render PDF Headless Chrome
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless=new \
  --disable-gpu \
  --disable-background-networking \
  --no-pdf-header-footer \
  --print-to-pdf="TEN_FILE_XUAT.pdf" \
  --user-data-dir="/tmp/chrome_print_tmp" \
  "file://$(pwd)/ten_file.html"
```

### 3. Quy trình Đóng gói Bản sao lưu dự phòng (Backup)
Khi chốt phiên bản chính thức:
```bash
BACKUP_DIR="_backups/YYYY-MM-DD_ten_phien_ban"
mkdir -p "$BACKUP_DIR"
cp index.html dossier.html dossier_ca_nhan.html trailer.html robots.txt NHAT_KY_LAM_VIEC.md *.pdf "$BACKUP_DIR/"
cd "$BACKUP_DIR" && zip -r "../BAN_SAO_DU_PHONG.zip" . && cd -
git add _backups/ && git commit -m "chore: save backup restore point" && git push
```

---

## 🚫 PHẦN VI: 5 ĐIỀU NÊN LÀM VÀ 5 ĐIỀU TUYỆT ĐỐI TRÁNH

### ✅ 5 Điều NÊN làm:
1. **Luôn kiểm toán ngày thi đấu**: Đảm bảo ngày thi đấu (ví dụ: Chủ Nhật 15.11.2026) thống nhất 100% từ Landing Page, đếm ngược, dossier đến PDF.
2. **Để 2 đầu mối liên hệ rõ ràng**: Một đầu mối Chuyên môn Golfer/Handicap và một đầu mối Đối ngoại/Tài trợ.
3. **Dùng ảnh flycam thực tế**: Nâng tầm đẳng cấp sân đấu thật, tạo niềm tin cho người tham gia.
4. **Kiểm tra số trang PDF sau khi xuất**: Dùng lệnh kiểm tra trang đảm bảo đúng số trang quy định (không tràn trang trắng thừa).
5. **Đóng gói backup ZIP ngay khi nghiệm thu**: Bảo vệ tài sản số phòng ngừa mọi sự cố.

### ❌ 5 Điều TUYỆT ĐỐI TRÁNH:
1. **TUYỆT ĐỐI KHÔNG** đẩy file Excel/Word dự toán nội bộ lên Git hoặc máy chủ công khai. Luôn thêm vào `.gitignore`.
2. **TUYỆT ĐỐI KHÔNG** đưa link công khai vào 2 file dossier lên thanh điều hướng của website (phải qua cổng đăng ký bảo mật).
3. **TUYỆT ĐỐI KHÔNG** dùng từ "Nghiệp dư" trong các văn bản và tiêu đề chính.
4. **TUYỆT ĐỐI KHÔNG** lặp lại thông tin quyền lợi FOC / size chữ ở Trang 1 và Trang 2 của hồ sơ cá nhân (chỉ để duy nhất tại Trang 3).
5. **TUYỆT ĐỐI KHÔNG** để người ký là chức danh dài dòng; chỉ ghi gọn gàng và trang trọng: **BAN TỔ CHỨC**.

---
*© 2026 Ban Biên Tập Báo Lao Động — Văn phòng Đại diện tại TP.HCM & Đông Nam Bộ. Lưu hành nội bộ.*
