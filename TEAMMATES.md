# TEAMMATES — Bảng phân công vai trò Day 11 (SVM-360 Fisheye Lab)

**Repo nhóm:** [Day11-SVM360-Fisheye-Lab-Student](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student)  
**Đại diện nộp:** **Đỗ Trung Kiên (Vai C - Lead)** — MSSV: `2A202602283`

---

## 👥 Bảng phân công & Truy xuất bằng chứng đóng góp

| Họ và tên | MSSV | Tên trong mode | Slice được giao | QA bài của ai | Phần việc và bằng chứng | Link hồ sơ cá nhân / branch | Commit nộp chốt |
|---|---|---|---|---|---|---|---|
| **Đỗ Trung Kiên** *(Đại diện nộp)* | 2A202602283 | `kien` | `B4-dense` | `tin` (review bài của Tín) | Vai C: Điều phối, P0 setup, P1/P3 mở reference, P4 benchmark metric ([local_quality.md](submission/r3_diag/local_quality.md), [model_compare.md](submission/r3_diag/model_compare.md), [10_error_card.md](submission/10_error_card.md)), hoàn thiện các ticket P6 và chạy kiểm tra `check` | [Repo nhóm (Main)](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/tree/main) | [`9f4b91b`](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/commit/9f4b91b) |
| **Nguyễn Trí Tín** | 2A202602275 | `tin` | `B4-center` | `nghia` (review bài của Nghĩa) | Vai A: Gán nhãn P0 vạch ô đỗ ([annotations.xml](submission/parking/annotations.xml)), P1 hiệu chuẩn C0 ([lock.txt](submission/p1_calib/lock.txt) `78D7-86D3`), P2 gán nhãn slice chính ([lock.txt](submission/r1_craft/lock.txt) `6997-BF13`), P5 sửa nhãn rework ([lock2.txt](submission/rework/lock2.txt) `9313-188F`, [delta.md](submission/rework/delta.md)) | [Branch p0-parking-export](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/tree/p0-parking-export) | [`ac57504`](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/commit/ac57504969f37fe41f1f2500c2cb3f3007a0b171) |
| **Võ Trọng Nghĩa** | 2A202602072 | `nghia` | `B2-mid` | `kien` (review bài của Kiên) | Vai B: Soát nhãn độc lập (QA Reviewer): Báo cáo soát C0 ([b_review_notes.md](submission/p1_calib/b_review_notes.md)), Báo cáo QA mù slice B4-center ([qa_review.md](submission/r2_qa/qa_review.md)), ảnh minh chứng ([qa_B_295948_overlay.png](submission/screenshots/qa_B_295948_overlay.png)) | [Branch nghia-qa-notes](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/tree/nghia-qa-notes) | [`0503c78`](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/commit/0503c786afa0bd493ca25157b62b31382648a3af) |

---

## 🔄 Vòng xoay QA Review (theo `submission/00_setup/team.json`):
- `tin` → được review bởi `nghia`
- `nghia` → được review bởi `kien`
- `kien` → được review bởi `tin`

## 📋 Tóm tắt giải quyết bất đồng & Quy chuẩn nộp bài:
- **Phân bổ 200 frame:** Nhóm thống nhất chung một kế hoạch phân bổ 8 tổ hợp camera × normal/hard tại [45_sampling_plan.csv](submission/45_sampling_plan.csv), tổng đúng 200 frame.
- **Xử lý bất đồng:** Thảo luận và thống nhất đề xuất quy tắc mới R10 tại [20_guideline_patch.md](submission/20_guideline_patch.md) và lập phiếu Escalation tại [30_escalation_ticket.md](submission/30_escalation_ticket.md).
- **Hồ sơ nghiệm thu:** Đã chạy `py lab11.py check` đạt `✓ Hồ sơ hình thức đầy đủ` với `failed_gates: []` lưu tại [submission/manifest.json](submission/manifest.json).
