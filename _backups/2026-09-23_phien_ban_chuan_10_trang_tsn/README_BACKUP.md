# BẢN LƯU TRỮ THIẾT KẾ & HỒ SƠ GIẢI GOLF BÁO LAO ĐỘNG OPEN 2026
**Thời điểm lưu trữ:** 23/09/2026  
**Phiên bản:** `v1.0.0-tsn-10pages-official` (Phiên bản chuẩn đối ngoại)

---

## 📌 1. DANH MỤC CÁC FILE LƯU TRỮ
1. **`index.html`**: Giao diện Landing Page chính thức của giải đấu
   - Tích hợp đồng hồ đếm ngược trực tiếp tới 07.11.2026.
   - Thẻ liên hệ nhanh Ban Tổ chức 24/7 ngay Hero: `090 5567395 - Mr. Đăng Văn`.
   - Đơn vị phối hợp tổ chức: Sân Golf Tân Sơn Nhất (Địa chỉ sau sáp nhập: `Số 6 Tân Sơn, Phường An Hội Tây, TP. Hồ Chí Minh`).
   - Lịch trình chuẩn: 10:00 Đón khách & buffet trưa nhẹ, 12:00 Tee-off Shotgun 18 hố, 18:30 Gala Dinner.
   - Bộ nhận diện đồng bộ không bị lặp chữ Báo Lao Động ở thanh điều hướng.

2. **`dossier.html`**: Quyển Hồ Sơ Quyền Lợi Mời Tài Trợ Chuẩn **10 Trang A4**:
   - **Trang 01 / 10**: Bìa trang trọng với đại cảnh Sân Golf Tân Sơn Nhất & Golfer Châu Á.
   - **Trang 02 / 10**: Thư Ngỏ Ban Tổ Chức (TM. Ban Biên Tập Báo Lao Động).
   - **Trang 03 / 10**: Tổng Quan Quy Mô & Lịch Trình Sự Kiện 07.11.2026.
   - **Trang 04 / 10**: Đơn Vị Phối Hợp Sân Golf TSN & Hệ Sinh Thái Truyền Thông Báo Lao Động.
   - **Trang 05 / 10**: Hiện Diện Logo Tại 07 Không Gian & Ma Trận 06 Gói Tài Trợ.
   - **Trang 06 / 10**: Gói Tài Trợ Chính (1 Tỷ) & Kim Cương (500 Triệu).
   - **Trang 07 / 10**: Gói Bạch Kim (300 Triệu) & Vàng (200 Triệu).
   - **Trang 08 / 10**: Gói Bạc (100 Triệu) & Đồng (50 Triệu).
   - **Trang 09 / 10**: Tài Trợ Chuyên Biệt (HIO, Kỹ Thuật, Quà Tặng) & Quy Chế Hợp Tác Nghiệm Thu.
   - **Trang 10 / 10 (Trang Cuối)**: Phiếu Đăng Ký & Thông Tin Tiếp Nhận Tài Trợ (Hotline 24/7: `090 5567395 - Mr. Đăng Văn`).

3. **`assets/`**: Toàn bộ thư viện hình ảnh độ phân giải cao, logo chuẩn Báo Lao Động và Sân Golf Tân Sơn Nhất.
4. **`Ho_So_Moi_Tai_Tro_Golf_Bao_Lao_Dong_Open_2026.pdf`**: Bản in PDF hoàn chỉnh của bộ hồ sơ tài trợ 10 trang.
5. **`Giao_dien_Demo_Landing_Page_Golf_Lao_Dong_2026_V1.pdf`**: Bản in PDF toàn bộ giao diện Landing Page.

---

## 🔄 2. HƯỚNG DẪN PHỤC HỒI (RESTORE)
Khi cần khôi phục lại trạng thái của phiên bản này:

### Cách 1: Phục hồi bằng Thư mục Backup
Copy đè các file từ thư mục `_backups/2026-09-23_phien_ban_chuan_10_trang_tsn/` ra thư mục gốc dự án:
```bash
cp _backups/2026-09-23_phien_ban_chuan_10_trang_tsn/index.html .
cp _backups/2026-09-23_phien_ban_chuan_10_trang_tsn/dossier.html .
cp -r _backups/2026-09-23_phien_ban_chuan_10_trang_tsn/assets/* assets/
```

### Cách 2: Phục hồi qua Git Tag
```bash
git checkout v1.0.0-tsn-10pages-official
```
hoặc tạo nhánh mới từ tag này:
```bash
git checkout -b restore-phien-ban-chuan v1.0.0-tsn-10pages-official
```
