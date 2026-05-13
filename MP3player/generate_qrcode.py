"""
网站二维码生成器
生成 GitHub Pages 网站的二维码
"""

import qrcode
import os

# GitHub Pages 网址 - 部署后修改为您的实际URL
# 格式: https://<用户名>.github.io/<仓库名>/
SITE_URL = "https://FryWhite.github.io/Fry-mp3player/"

def generate_qrcode(url, filename="qrcode.png"):
    """生成二维码图片"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ 二维码已生成: {filename}")
    print(f"🔗 链接: {url}")
    return filename

if __name__ == "__main__":
    # 保存到 mp3-website 目录
    output_path = os.path.join(os.path.dirname(__file__), "qrcode.png")
    generate_qrcode(SITE_URL, output_path)
    
    print("\n📌 提示: 如果您更改了仓库名，请修改 SITE_URL 变量")
    print("📌 GitHub Pages 需要在仓库 Settings > Pages 中启用")
