# 08 — Time-box và thứ tự cắt giảm (degrade)

Lệch tiến độ 5 phút ở bất kỳ pha nào: cắt giảm theo **đúng thứ tự** dưới đây, không tự chọn thứ tự khác. Mỗi lần
cắt, chạy `make degrade STEP=<tên bước>` để công cụ ghi lại và hạ ngưỡng `make check` tương ứng.

## Thứ tự cắt (từ trước tới sau)

1. **`stretch`** — bỏ toàn bộ phần stretch (`docs/09-support-stretch-vi.md`). `make degrade STEP=stretch`.
2. **`k12`** — bỏ vẽ polygon K12 (đối chứng fill ratio). `make degrade STEP=k12`.
3. **`frame3`** — bỏ frame thứ ba của slice, chỉ làm 2 frame. `make degrade STEP=frame3`.
4. **`findings`** — hạ ngưỡng `findings.csv` từ 12 xuống 8 dòng (vẫn phải ≥3 giá trị `cell` khác nhau).
   `make degrade STEP=findings`.
5. **`zone_table`** — `zone_table.md` còn 3 dòng thay vì đủ. `make degrade STEP=zone_table`.
6. **`rework`** — rework chỉ còn 1 dòng mức P0. `make degrade STEP=rework`.
7. **`cvat_quality`** — bỏ `make cvat-quality`, dùng số của `make compare` thay thế. `make degrade
   STEP=cvat_quality`.

## Không bao giờ bỏ

- `make lock` mỗi vòng.
- `make reference` (mở sau khi đã khoá).
- Ít nhất 1 dòng `findings.csv` mỗi vai (`r1_craft`, `r2_qa`, `r3_diag`).
- `delta.md` (phải có số trước/sau, dù rework chỉ 1 dòng).
- `make check` chạy tới cùng, exit 0.

`mode.json` ghi lại mọi bước đã `degrade`; đây là tín hiệu tiến độ, không phải bị trừ điểm.
