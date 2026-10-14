"""生成带作品名和作者名的二维码展示卡。"""

from argparse import ArgumentParser
from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont


CARD_WIDTH = 1100
CARD_HEIGHT = 1370
QR_SIZE = 900


def find_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = (
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/System/Library/Fonts/PingFang.ttc"),
    )
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def centered_text(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill: str) -> None:
    bounds = draw.textbbox((0, 0), text, font=font)
    width = bounds[2] - bounds[0]
    draw.text(((CARD_WIDTH - width) / 2, y), text, font=font, fill=fill)


def generate_card(title: str, author: str, url: str, output: Path) -> None:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=18,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="#172027", back_color="white").convert("RGB")
    qr_image = qr_image.resize((QR_SIZE, QR_SIZE), Image.Resampling.NEAREST)

    card = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "#F8F4EA")
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        (24, 24, CARD_WIDTH - 24, CARD_HEIGHT - 24),
        radius=42,
        outline="#C8A968",
        width=4,
    )
    centered_text(draw, 88, title, find_font(94), "#392C22")
    centered_text(draw, 210, f"作者：{author}", find_font(46), "#765E47")
    card.paste(qr_image, ((CARD_WIDTH - QR_SIZE) // 2, 330))
    centered_text(draw, 1265, "扫码聆听作品", find_font(34), "#8A745B")

    output.parent.mkdir(parents=True, exist_ok=True)
    card.save(output, format="PNG", optimize=True)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    generate_card(args.title, args.author, args.url, args.output)


if __name__ == "__main__":
    main()
