# Day 11 · SVM/360 Fisheye Lab — học viên

Repo này dựng từ template `Day11-SVM360-Fisheye-Lab-Student`. Dữ liệu và bài nộp **chỉ dùng cho buổi Day 11**, không
dùng lại cho mục đích khác.

## Bắt đầu

1. Xác nhận repo của bạn ở chế độ **Private** (GitHub → Settings → repo, mục Danger Zone/Visibility).
2. `make doctor` — kiểm python3, CVAT Day 2 đang chạy, repo private, không có `.env` bị track.
3. Mở `docs/00-START-HERE-vi.md` — bản đồ P0–P6, mỗi bước một lệnh.
4. Không có `make`: dùng `python3 lab11.py <lệnh>` thay `make <lệnh>`.

`make status` luôn in đúng một việc kế tiếp. Kẹt quá 3 phút ở một thao tác: gọi Lab Coach.

## Bài Day 11 và file cần mở

- [Hướng dẫn từ đầu đến nộp](docs/00-START-HERE-vi.md) gồm bài ảnh bãi đỗ trong phần giảng và lab CVAT 240 phút.
- [Ảnh bãi đỗ và luật vạch ô đỗ](docs/11-parking-lines-vi.md): ảnh trong `assets/parking/`; nộp XML và ghi chú ở `submission/parking/`.
- [Rubric tự đối chiếu](docs/rubric-vi.md): tiêu chí và bằng chứng, chưa có trọng số chính thức.
- [Notebook Google Colab](notebooks/README.md): trợ giúp lập kế hoạch bốn camera; không bắt buộc, không thay bài nộp.
- `make local-quality`: sau khi khóa export và mở teaching reference, tính chỉ số rectangle, ma trận nhầm lớp và
  xung đột offline; không cần CVAT Premium. Đọc giới hạn phép tính trong `docs/05-taxonomy-vi.md`.
- `submission/45_sampling_plan.csv` và `submission/46_gold_set_plan.md`: **bài lõi** theo tình huống bốn camera giả lập, không phải stretch.

Sau khi làm, chạy `make check`. Lệnh này kiểm **hình thức và tính đầy đủ**, còn người soát đánh giá chất lượng nhãn
và lập luận theo rubric.
