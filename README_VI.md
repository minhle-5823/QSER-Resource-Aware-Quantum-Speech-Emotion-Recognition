# QSER tại PDCAT 2026 (hướng dẫn ngắn)

Đây là repo nghiên cứu cho bài *Resource-Aware Quantum Downstream Classification for Speech Emotion Recognition under Compact Feature Budgets*, **đã được chấp nhận tại PDCAT 2026, chưa trình bày và chưa xuất bản** (tháng 11/2026).

## Repo đang có gì?

- `README.md`: giới thiệu nghiên cứu, tác giả, kết quả chính và trích dẫn.
- `figures/`: biểu đồ tóm tắt được vẽ lại từ số liệu, không chứa 4 hình gốc của bản thảo.
- `results/paper_tables/`: các bảng số liệu được **chép lại từ bản thảo** (không phải kết quả tính lại từ file raw).
- **Đã loại:** các CSV/JSON log thực nghiệm nội bộ, file cấu hình, đường dẫn môi trường, ảnh gốc trong manuscript và tài liệu minh chứng acceptance.
- `scripts/`: chạy kiểm tra CSV, xem bảng kết quả và vẽ biểu đồ từ dữ liệu có sẵn.
- `docs/`: phương pháp, dữ liệu, giới hạn tái lập và checklist trước khi công khai.

**Chưa có:** code gốc chạy thí nghiệm QSVC/VQC/QCNN, notebook Kaggle, hoặc toàn bộ log 10-seed của bản thảo. ZIP gốc cậu gửi không chứa những file đó, nên repo chưa thể thực hiện lại quá trình training từ đầu.

## Chạy công cụ phân tích

```bash
pip install -r requirements.txt
python scripts/validate_results.py
python scripts/show_summary.py
python scripts/plot_paper_results.py
```

**Trước khi public:** xác nhận với đồng tác giả, kiểm tra chính sách của Springer/LNCS, và cập nhật DOI sau khi xuất bản. Không đưa email acceptance, ảnh chụp hồ sơ nội bộ, dữ liệu RAVDESS/CMU-MOSEI hoặc PDF camera-ready lên public khi chưa rõ quyền chia sẻ.
