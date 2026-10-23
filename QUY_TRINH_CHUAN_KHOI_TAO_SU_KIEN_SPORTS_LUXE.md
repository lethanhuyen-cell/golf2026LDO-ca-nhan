# BỘ QUY TRÌNH CHUẨN: KHỞI TẠO HỒ SƠ & LANDING PAGE SỰ KIỆN THỂ THAO CAO CẤP (SPORTS LUXE SUITE)
> **Phiên bản**: V2.0 Enterprise Automation  
> **Áp dụng cho**: Ban Tổ chức Sự kiện, Ban Thư ký & Bộ phận Công nghệ Báo Lao Động  
> **Mục tiêu**: Chuẩn hóa toàn diện để chỉ cần **"1 Câu lệnh"** hoặc **"1 File cấu hình"** là lập tức tạo ra trọn bộ Landing Page, Hồ sơ Doanh nghiệp (10 trang), Hồ sơ Cá nhân (3 trang), Dossier Mode bảo mật và Script xuất PDF chuẩn in.

---

## I. NGUYÊN TẮC VÀNG: "MỘT CÂU LỆNH - TRỌN BỘ SẢN PHẨM"

Khi cần khởi tạo bất kỳ sự kiện thể thao / golf / đại sự kiện nào mới tương tự Giải Golf Lao Động, bạn chỉ cần ra lệnh cho AI theo cấu trúc sau:

```text
"Hãy khởi tạo bộ hồ sơ và landing page cho [TÊN GIẢI ĐẤU], diễn ra ngày [NGÀY TỔ CHỨC] tại [SÂN/ĐỊA ĐIỂM]. 
- Cơ cấu tài trợ Doanh nghiệp gồm: [Gói Kim Cương ...Tr, Bạch Kim ...Tr, Vàng ...Tr, Bạc ...Tr]. 
- Mốc đồng hành Cá nhân: [Mốc ...Tr, 01 suất FOC, vinh danh Bảng vàng Clubhouse]. 
- Áp dụng chuẩn thiết kế Sports Luxe, Dossier Mode bảo mật và xuất PDF in ấn."
```

AI sẽ tự động đọc cấu hình, kích hoạt cỗ máy `scripts/scaffold_event.py`, biên dịch và bàn giao toàn bộ sản phẩm hoàn chỉnh chỉ trong vài chục giây.

---

## II. CHECKLIST 7 THÔNG TIN ĐẦU VÀO CẦN THIẾT (INPUT SPEC)

Trước khi khởi tạo, chỉ cần chuẩn bị hoặc cung cấp 7 nhóm thông tin sau:

| STT | Trường thông tin | Ví dụ mẫu | Ghi chú kỹ thuật |
| :--- | :--- | :--- | :--- |
| **1** | **Tên giải đấu & Slogan** | *Giải Golf Báo Lao Động Open 2026 - Swing for Workers' Children* | Thể hiện đẳng cấp, ngắn gọn, có thông điệp xã hội |
| **2** | **Đơn vị chủ trì & Đồng hành** | *Báo Lao Động, Tổng LĐLĐ VN, VGA, UBND TP.HCM* | Thể hiện tính chính danh cấp quốc gia/bộ ngành |
| **3** | **Thời gian & Địa điểm** | *Chủ Nhật, ngày 15.11.2026 tại Sân Golf Tân Sơn Nhất* | Ghi rõ quy mô sân (36 hố, 18 hố, sảnh tiệc) |
| **4** | **Quy mô & Mục đích** | *144 Golfer; Ủng hộ Quỹ Tấm Lòng Vàng Lao Động* | Tôn vinh giá trị nhân văn vượt trội |
| **5** | **Gói Tài Trợ Doanh Nghiệp** | *Kim Cương (500Tr), Bạch Kim (300Tr), Vàng (150Tr), Bạc (80Tr)* | Kèm số suất Golfer FOC và số bàn tiệc Gala |
| **6** | **Gói Đồng Hành Cá Nhân** | *Mốc cơ sở 20.000.000 VNĐ (01 Golfer FOC, Kỷ niệm chương mạ vàng)* | Áp dụng quy tắc: *Size chữ tỉ lệ thuận giá trị tài trợ* |
| **7** | **Tài khoản tiếp nhận & Hotline** | *BÁO LAO ĐỘNG - 001100xxxx tại Vietcombank TP.HCM* | Cú pháp chuyển khoản chuẩn hóa |

---

## III. BỘ SẢN PHẨM CHUẨN ĐƯỢC TỰ ĐỘNG TẠO RA (DELIVERABLES)

Mỗi lần chạy bộ quy trình, hệ sinh thái sẽ tự động tạo ra **06 sản phẩm cốt lõi**:

```
📁 [TÊN_DU_AN]/
├── 📄 index.html              # Landing Page thể thao chuẩn Sports Luxe (Responsive, Lucide, Countdown)
├── 📄 dossier.html            # Hồ sơ Doanh nghiệp 10 trang A4 Print-to-PDF hoàn chỉnh
├── 📄 dossier_ca_nhan.html     # Hồ sơ Cá nhân 3 trang A4 Print-to-PDF có Bảng vàng Clubhouse
├── 📄 robots.txt              # Khóa chặn Google Index bảo mật Dossier Mode
├── 📄 vercel.json             # Cấu hình Deploy Vercel (chống rò rỉ header noindex)
├── ⚙️ render_pdf.py           # Script tự động xuất PDF qua Headless Chrome
└── 📁 assets/                 # Thư mục hình ảnh, logo, flycam sân đấu
```

---

## IV. ĐẶC TẢ CHI TIẾT CÁC TÀI LIỆU CHUẨN MẪU

### 1. Landing Page (`index.html`)
- **Tông màu chủ đạo**: *Sports Luxe Emerald & Royal Gold*
  - Nền tối thượng lưu: `#00170d` / `#002013`
  - Xanh Masters/PGA: `#004d2c` / `#056839`
  - Vàng Hoàng gia mạ kim: `#C5A059` / `#FFE8B8`
- **Bộ Font chữ kết hợp**: `Playfair Display` (Tiêu đề sang trọng), `Cinzel` (Bộ số & Hạng mục danh dự), `Plus Jakarta Sans` (Nội dung dễ đọc).
- **Cơ chế Lead-Gen Form**: Không để link tải PDF công khai trên trang chủ. Nút CTA chuyển hướng tới `#sponsor-form` để thu thập data doanh nghiệp, sau đó gửi hồ sơ bảo mật qua kênh riêng.

### 2. Hồ sơ Doanh nghiệp (`dossier.html` - 10 Trang A4 Chuẩn In)
- **Trang 1**: Bìa sang trọng chuẩn Confidential Dossier.
- **Trang 2**: Thư ngỏ từ Trưởng Ban Tổ chức Báo Lao Động.
- **Trang 3**: Địa điểm & Đẳng cấp sân đấu (Flycam hoàng hôn / sân bãi).
- **Trang 4**: Hệ sinh thái truyền thông Báo Lao Động (laodong.vn, Lao Động TV, Mạng xã hội).
- **Trang 5**: Quyền lợi Độc quyền Gói Kim Cương (500Tr).
- **Trang 6**: Quyền lợi Gói Bạch Kim (300Tr).
- **Trang 7**: Quyền lợi Gói Vàng (150Tr).
- **Trang 8**: Quyền lợi Gói Bạc (80Tr).
- **Trang 9**: Ma trận so sánh quyền lợi tổng thể (Full Matrix Table).
- **Trang 10**: Phiếu tiếp nhận tài trợ, tài khoản ngân hàng & Hotline ký kết.

### 3. Hồ sơ Cá nhân (`dossier_ca_nhan.html` - 3 Trang A4 Chuẩn In)
- **Trang 1**: Thư mời danh dự & Ý nghĩa nhân văn ủng hộ Quỹ Tấm Lòng Vàng.
- **Trang 2**: Vinh danh Bảng Vàng (Golden Board) tại sảnh Clubhouse với **Quy định in đậm**:  
  > *"Kích thước size chữ họ tên hiển thị tỉ lệ thuận với giá trị tài trợ (mốc cơ sở 20 triệu VNĐ). Mức tài trợ càng cao, kích thước họ tên hiển thị càng lớn tương ứng."*
- **Trang 3**: Phiếu đăng ký đóng góp hảo tâm & Tài khoản tiếp nhận chính danh Báo Lao Động.

---

## V. CÁCH VẬN HÀNH BỘ CÔNG CỤ TỰ ĐỘNG (HOW TO OPERATE)

### Cách 1: Chạy bằng Dòng lệnh CLI (Tự động 100%)
1. **Khởi tạo file cấu hình mới**:
   ```bash
   python3 scripts/scaffold_event.py --init su_kien_moi.json
   ```
2. **Chỉnh sửa thông số trong `su_kien_moi.json`** (Tên giải, ngày, sân, các gói).
3. **Sinh toàn bộ dự án**:
   ```bash
   python3 scripts/scaffold_event.py --build --config su_kien_moi.json --out ./Du_An_Moi
   ```
4. **Xuất PDF chuẩn in chỉ bằng 1 lệnh**:
   ```bash
   cd ./Du_An_Moi
   python3 render_pdf.py
   ```

### Cách 2: Ra lệnh trực tiếp cho AI Antigravity
Chỉ cần gửi tin nhắn:
> *"Tạo bộ hồ sơ Giải Golf Mùa Xuân Báo Lao Động 2027, ngày 28.03.2027 tại Sân Sông Bé Golf Resort, Gói Kim Cương 400Tr, Bạch Kim 250Tr, Vàng 120Tr, Bạc 60Tr, Cá nhân từ 15Tr. Dùng bộ quy trình chuẩn Sports Luxe."*

---

## VI. 8 VÒNG KIM CÔ KIỂM ĐỊNH CHẤT LƯỢNG (AUDIT CHECKLIST)

Trước khi xuất xưởng hoặc gửi hồ sơ cho Nhà tài trợ, phải rà soát qua 8 điểm kiểm định:

- [ ] **1. Kích thước trang A4 tuyệt đối**: Mỗi trang CSS `.page-sheet` đúng `210mm x 297mm`, `overflow: hidden`, không sinh trang trắng khi in.
- [ ] **2. Không để lộ hồ sơ công khai**: Trang chủ `index.html` không có link trực tiếp tải PDF; form dẫn về `#sponsor-form`.
- [ ] **3. Thẻ meta bảo mật**: Cả 2 file hồ sơ có `<meta name="robots" content="noindex, nofollow, noarchive" />`.
- [ ] **4. File robots.txt**: Đã cấm crawl `/dossier*` và `/*.pdf`.
- [ ] **5. File nội bộ tuyệt đối không đẩy Git/Vercel**: `.gitignore` phải chặn file `DU_TOAN*`, `*.xlsx`, `*.xls`, `*.docx`.
- [ ] **6. Quy tắc Bảng Vàng Cá Nhân**: Phải có câu quy định kích thước font chữ tỉ lệ thuận giá trị tài trợ.
- [ ] **7. Chữ ký hồ sơ**: Ký chuẩn danh xưng **BAN TỔ CHỨC**, không ghi cá nhân tùy tiện.
- [ ] **8. Bản sao lưu**: Đã sao lưu bản snapshot an toàn vào thư mục `_backups/` trước khi sửa đổi.
