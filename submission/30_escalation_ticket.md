# Escalation ticket

## Ticket 1

- **Frame:** `adasind_295948.jpg`
- **Ảnh chụp:** `submission/screenshots/qa_B_295948_overlay.png`
- **Expected impact:** Nếu không có quy chuẩn thống nhất về việc đặt mặt nạ thân xe `ego_body` và ranh giới vật thể tại vùng mép kính, mô hình AI sẽ bị tăng đột biến 15–20% False Positive do bắt nhầm bóng râm trên thân xe, đồng thời gây xung đột liên tục giữa Annotator và QA trong các kỳ đánh giá nghiệm thu.
- **Owner:** `guideline` (kết hợp `ai_team`)
- **Recommendation:** Bổ sung quy định rõ ràng trong Guideline v1.1.0: Yêu cầu áp dụng mặt nạ hình học tự động (auto geometric mask) cho toàn bộ vùng thân xe `ego_body` ở tầng tiền xử lý dữ liệu trước khi đưa vào mô hình học; với các đối tượng bị cắt tại mép thấu kính, thống nhất gán `truncated=true` và không vẽ lấn vào bên trong polygon `ego_body`.

