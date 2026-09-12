# bot_loader_direct.py
import asyncio
from playwright.async_api import async_playwright


async def run():
  target_url = (
      "https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/than-kinh-nao"
  )

  async with async_playwright() as p:
    # Mở trình duyệt Chromium với headless=False để thấy rõ giao diện
    browser = await p.chromium.launch(headless=False, slow_mo=100)
    page = await browser.new_page()

    print("🤖 [BOT 1] Đang mở trang web...")
    await page.goto(target_url)
    await page.wait_for_load_state("networkidle")

    # Vòng lặp ép bấm nút "Xem thêm"
    max_tries = 50
    tries = 0

    while tries < max_tries:
      # Cuộn xuống cuối trang
      await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
      await asyncio.sleep(2)

      # Tìm nút "Xem thêm" bằng văn bản bên trong
      try:
        # Tìm nút có chứa chữ "Xem thêm"
        xem_them_btn = page.locator("button", has_text="Xem thêm").first

        if await xem_them_btn.is_visible():
          await xem_them_btn.scroll_into_view_if_needed()
          await xem_them_btn.click()
          tries += 1
          print(f"🚀 [BOT 1] Đã bấm 'Xem thêm' lần thứ {tries}")
          # Chờ dữ liệu mẻ sản phẩm mới tải về
          await asyncio.sleep(3)
        else:
          print(
              "🏁 [BOT 1] Đã bấm hết sạch nút 'Xem thêm'. Quá trình hoàn tất!"
          )
          break
      except Exception as e:
        print(
            "🏁 [BOT 1] Không tìm thấy nút 'Xem thêm' nữa hoặc đã tải xong hết"
            " sản phẩm."
        )
        break

    # Lấy toàn bộ mã nguồn HTML sau khi đã bung lụa hết sản phẩm
    html_content = await page.content()

    # Lưu vào file longchau.html (ghi đè file cũ)
    with open("longchau.html", "w", encoding="utf-8") as f:
      f.write(html_content)

    print("💾 [BOT 1] Đã lưu thành công file 'longchau.html'!")
    await browser.close()


if __name__ == "__main__":
  asyncio.run(run())


