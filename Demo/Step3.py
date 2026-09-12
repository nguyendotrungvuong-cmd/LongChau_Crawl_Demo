# markdown_to_csv.py
import csv
import re


def convert_markdown_to_csv():
  md_file = "longchau_clean.md"
  csv_file = "longchau_products.csv"

  try:
    with open(md_file, "r", encoding="utf-8") as f:
      content = f.read()
  except FileNotFoundError:
    print(f"❌ Không tìm thấy file '{md_file}'.")
    return

  products = []
  lines = content.split("\n")

  # Mặc định danh mục ban đầu dựa theo trang cào (Thần kinh não)
  current_category = "Thần kinh não"

  i = 0
  while i < len(lines):
    line = lines[i].strip()

    # 1. Chỉ bắt tiêu đề lớn thực sự của trang hoặc nhóm sản phẩm (Ví dụ: # Thần kinh não hoặc các tiêu đề có ý nghĩa)
    if line.startswith("# ") or line.startswith("## "):
      clean_title = re.sub(r"[\#\*\-\[\]]", "", line).strip()
      # Loại bỏ các tiêu đề rác không phải tên danh mục sản phẩm
      if clean_title and len(clean_title) < 40 and "Danh sách" not in clean_title and "Bộ lọc" not in clean_title:
        current_category = clean_title

    # 2. Nhận diện dòng tên sản phẩm bắt đầu bằng ### [
    if line.startswith("### ["):
      name_match = re.search(r"### \[(.*?)\]", line)
      if name_match:
        prod_name = name_match.group(1)
        prod_price = ""
        prod_spec = ""

        # Dòng kế tiếp (i + 1) thường là Giá tiền
        if i + 1 < len(lines):
          price_line = lines[i + 1].strip()
          if "đ" in price_line:
            prod_price = price_line
            i += 1

        # Dòng kế tiếp nữa (i + 2) thường là Quy cách
        if i + 2 < len(lines):
          spec_line = lines[i + 2].strip()
          if spec_line and not spec_line.startswith("### [") and "đ" not in spec_line:
            prod_spec = spec_line
            i += 1

        products.append({
            "LoaiSanPham": current_category,
            "TenSanPham": prod_name,
            "GiaBan": prod_price,
            "QuyCach": prod_spec
        })
    i += 1

  # Ghi ra file CSV
  with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["LoaiSanPham", "TenSanPham", "GiaBan", "QuyCach"])
    writer.writeheader()
    writer.writerows(products)

  print(f"✨ Thành công! Đã trích xuất chính xác {len(products)} sản phẩm vào file '{csv_file}'.")

  # In thử kết quả mẫu kiểm tra
  print("\n--- 🔍 MẪU KẾT QUẢ SAU KHI LỌC SẠCH DANH MỤC ---")
  for idx, p in enumerate(products[:5], 1):
    print(f"{idx}. [{p['LoaiSanPham']}] {p['TenSanPham']} | Giá: {p['GiaBan']} | Quy cách: {p['QuyCach']}")

if __name__ == "__main__":
  convert_markdown_to_csv()