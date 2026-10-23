# HƯỚNG DẪN SỬ DỤNG: BỘ TEMPLATE CHUẨN ĐỒ HỌA & QUY CÁCH SPORTS LUXE
> **Bộ sản phẩm**: Master Template Suite (Tái tạo 100% chuẩn xác đồ họa, font chữ & layout)  
> **Áp dụng**: Ban Sự kiện Báo Lao Động & các dự án giải đấu thể thao đối ngoại

---

## I. TẠI SAO BỘ TEMPLATE NÀY ĐẢM BẢO "Y HỆT"?

Khác với các công cụ tạo sinh tự động thông thường (dễ làm sai lệch khoảng cách lề, font chữ, hiệu ứng bóng mờ hoặc làm vỡ ngắt trang in A4), bộ template này được đóng gói từ **chính 3 kiệt tác thiết kế đã được kiểm duyệt và nghiệm thu thực tế**:

1. **`template_index.html`**: Trang chủ Landing Page hoàn chỉnh (1.800+ dòng mã, hiệu ứng flycam hoàng hôn, bảng lịch trình, modal điều lệ, form bảo mật lead-gen).
2. **`template_dossier.html`**: Hồ sơ Doanh nghiệp **10 trang A4 chuẩn in tuyệt đối** (không nhảy dòng, không sinh trang trắng, hiệu ứng viền vàng hoàng gia, ma trận quyền lợi 4 gói).
3. **`template_dossier_ca_nhan.html`**: Hồ sơ Cá nhân **3 trang A4 chuẩn in tuyệt đối** (vinh danh Bảng vàng Clubhouse, quy tắc kích thước tên tỉ lệ thuận giá trị tài trợ).
4. **`assets/images/`**: Toàn bộ kho ảnh chụp flycam chất lượng cao, hình ảnh gala, cúp giải thưởng và logo chính thức.

---

## II. QUY TRÌNH 3 BƯỚC ĐỂ TẠO DỰ ÁN MỚI TRONG 1 PHÚT

### Bước 1: Sao chép file biến số
Mở file `variables_sample.json` và lưu thành `event_2027.json` (hoặc sửa trực tiếp):
```json
{
  "TOURNAMENT_NAME_UPPER": "GIẢI GOLF BÁO LAO ĐỘNG MÙA XUÂN 2027",
  "TOURNAMENT_NAME_TITLE": "Giải Golf Báo Lao Động Mùa Xuân 2027",
  "TOURNAMENT_SHORT_NAME": "Golf Lao Động Mùa Xuân 2027",
  "TOURNAMENT_FULL_SLOGAN": "Swing for Workers' Children - Gắn kết Doanh nhân, Tiếp bước Em đến trường",
  "TOURNAMENT_SLOGAN": "Swing for Workers' Children",
  "TOURNAMENT_DATE_FULL": "Chủ Nhật, ngày 28.03.2027",
  "TOURNAMENT_DATE_WITH_DAY": "Chủ Nhật, 28.03.2027",
  "TOURNAMENT_DATE_SHORT": "28.03.2027",
  "TOURNAMENT_DATE_ISO": "2027-03-28T06:00:00",
  "VENUE_FULL_NAME": "Sân Golf Tân Sơn Nhất (TP.HCM)",
  "VENUE_NAME": "Sân Golf Tân Sơn Nhất",
  "VENUE_NAME_EN": "Tan Son Nhat Golf Course",
  "VENUE_SHORT": "Tân Sơn Nhất",
  "VENUE_ADDRESS": "Số 6 Tân Sơn, Phường 12, Quận Gò Vấp, TP. Hồ Chí Minh",
  "PATRON_MIN_AMOUNT": "20.000.000 VNĐ",
  "PATRON_MIN_AMOUNT_SHORT": "20 triệu VNĐ",
  "DIAMOND_AMOUNT": "500.000.000 VNĐ",
  "PLATINUM_AMOUNT": "300.000.000 VNĐ",
  "GOLD_AMOUNT": "150.000.000 VNĐ",
  "SILVER_AMOUNT": "80.000.000 VNĐ",
  "CHARITY_FUND_NAME": "Quỹ Tấm Lòng Vàng Lao Động",
  "CHARITY_FUND_SHORT": "Quỹ Tấm Lòng Vàng"
}
```

### Bước 2: Chạy lệnh biên dịch (1 dòng lệnh)
Từ thư mục của bộ template, chạy:
```bash
python3 build_event.py --config event_2027.json --out ../Giai_Golf_2027
```

### Bước 3: Xuất file in PDF chuẩn A4 (1 click)
```bash
cd ../Giai_Golf_2027
python3 render_pdf.py
```
Ngay lập tức, bạn sẽ có 2 tệp PDF chất lượng cao:
- `HSTT_Ca_Nhan_Chuan_In.pdf` (Đúng 3 trang A4 không viền)
- `HSTT_Doanh_Nghiep_Chuan_In.pdf` (Đúng 10 trang A4 không viền)

---

## III. RA LỆNH TRỰC TIẾP CHO AI ANTIGRAVITY

Nếu bạn đang chat với AI, bạn không cần tự tay gõ lệnh. Chỉ cần gửi yêu cầu:
> *"Hãy dùng **Bộ Template Chuẩn Sports Luxe** để tạo dự án mới: [Tên giải], ngày [Thời gian], tại [Sân/Địa điểm]. Thay đổi nội dung theo thông tin này nhưng giữ NGUYÊN 100% quy cách đồ họa, font chữ và bố cục trang in."*

AI sẽ tự động đọc `variables_sample.json`, thay thế biến số và bàn giao thư mục mới cho bạn!
