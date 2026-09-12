# parse_with_crawl4ai.py
import asyncio
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig


async def parse_local_html_with_crawl4ai():
  file_path = "longchau.html"

  if not os.path.exists(file_path):
    print(
        f"❌ Không tìm thấy file '{file_path}'. Hãy chạy Bot 1 để lưu file trước"
        " nhé!"
    )
    return

  print("🤖 [Crawl4AI] Đang đọc nội dung file 'longchau.html' vào bộ nhớ...")
  with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

  # Sử dụng tiền tố raw:// để Crawl4AI nhận trực tiếp chuỗi HTML cục bộ mà không cần tìm file qua đường dẫn OS
  raw_url = f"raw://{html_content}"

  print(
      "🤖 [Crawl4AI] Đang phân tích và chuyển đổi cấu trúc HTML sang Markdown..."
  )

  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
        url=raw_url,
        config=CrawlerRunConfig(
            # Loại bỏ các thành phần rác không liên quan đến sản phẩm
            excluded_tags=["header", "footer", "nav", "script", "style"],
            word_count_threshold=1,
        ),
    )

    if result.success:
      print("✨ Đã xử lý xong dữ liệu cục bộ!")

      # Lưu kết quả ra file Markdown sạch sẽ
      markdown_output_path = "longchau_clean.md"
      with open(markdown_output_path, "w", encoding="utf-8") as f:
        f.write(result.markdown)
      print(
          f"💾 Đã lưu thành công bản Markdown tinh gọn vào file"
          f" '{markdown_output_path}'!"
      )

      # In thử phần đầu nội dung thu được
      print("\n--- 📄 MỘT PHẦN NỘI DUNG MARKDOWN ĐÃ ĐƯỢC LỌC SẠCH ---")
      print(result.markdown[:1200] + "\n...\n")
    else:
      print("❌ Crawl4AI gặp lỗi khi xử lý:", result.error_message)


if __name__ == "__main__":
  asyncio.run(parse_local_html_with_crawl4ai())