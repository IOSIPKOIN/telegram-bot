from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from PIL import Image, ImageDraw, ImageFont
import os, random

router = Router()
FONT = "images/Montserrat-Regular.ttf"

def base_screen(w=1080, h=1900):
    img = Image.new("RGB", (w, h), "#0b0f14")
    d = ImageDraw.Draw(img)
    return img, d

def rounded(d, xy, r, fill):
    d.rounded_rectangle(xy, r, fill=fill)

def check_icon(d, x, y):
    d.ellipse([x, y, x+36, y+36], fill="#1f3d2b")
    d.line([x+10, y+20, x+17, y+27], fill="#4ADE80", width=4)
    d.line([x+17, y+27, x+28, y+10], fill="#4ADE80", width=4)

# ================= SUCCESS / SUC =================

@router.message(F.text.startswith("/suc"))
async def suc(message: Message):
    try:
        _, data = message.text.split("/suc", 1)
        user, balance, amount, card = [x.strip() for x in data.split("|")]
    except:
        await message.answer("Format:\n/suc Name | Balance | Amount | Card")
        return

    img, d = base_screen()
    title = ImageFont.truetype(FONT, 42)
    big = ImageFont.truetype(FONT, 56)
    mid = ImageFont.truetype(FONT, 32)
    small = ImageFont.truetype(FONT, 24)

    # Header
    d.text((60, 50), "CryptoX", fill="#60A5FA", font=title)
    d.text((900, 50), user, fill="white", font=mid)

    # Balance card
    rounded(d, [60, 130, 1020, 430], 50, "#121826")
    d.text((120, 180), "Available Balance", fill="#9CA3AF", font=small)
    d.text((120, 240), f"${balance}", fill="white", font=big)

    rounded(d, [120, 320, 480, 390], 30, "#3B82F6")
    d.text((300, 345), "Withdraw", fill="white", font=mid, anchor="mm")

    rounded(d, [520, 320, 880, 390], 30, "#1f2937")
    d.text((700, 345), "Deposit", fill="white", font=mid, anchor="mm")

    # Verified line
    d.text((120, 470),
           "● Account verified   ● KYC verified   ● Network online",
           fill="#4ADE80",
           font=small)

    # History
    y = 540
    d.text((60, y), "Withdrawal History", fill="white", font=mid)
    y += 60

    def row(amount, when):
        nonlocal y
        check_icon(d, 60, y)
        d.text((120, y), f"- ${amount}", fill="#4ADE80", font=mid)
        d.text((120, y+34), f"{user} · {card}", fill="#9CA3AF", font=small)
        d.text((900, y), when, fill="#9CA3AF", font=small)
        y += 90

    row(amount, "Just now")
    for days in [30, 32, 45, 49, 57]:
        row(random.randint(1200, 6000), f"{days} days ago")

    os.makedirs("images", exist_ok=True)
    path = "images/success.png"
    img.save(path)
    await message.answer_photo(FSInputFile(path))


# ================= BALANCE / BAL =================

@router.message(F.text.startswith("/bal"))
async def bal(message: Message):
    try:
        _, data = message.text.split("/bal", 1)
        user, balance, failed = [x.strip() for x in data.split("|")]
    except:
        await message.answer("Format:\n/bal Name | Balance | Failed")
        return

    img, d = base_screen()
    title = ImageFont.truetype(FONT, 42)
    big = ImageFont.truetype(FONT, 56)
    mid = ImageFont.truetype(FONT, 32)
    small = ImageFont.truetype(FONT, 24)

    d.text((60, 50), "CryptoX", fill="#60A5FA", font=title)
    d.text((900, 50), user, fill="white", font=mid)

    rounded(d, [60, 130, 1020, 430], 50, "#121826")
    d.text((120, 180), "Available Balance", fill="#9CA3AF", font=small)
    d.text((120, 240), f"${balance}", fill="white", font=big)

    y = 520
    d.text((60, y), "Transaction History", fill="white", font=mid)
    y += 60

    d.ellipse([60, y, 96, y+36], fill="#3b1111")
    d.line([70, y+18, 86, y+18], fill="#FF6C6C", width=4)
    d.text((120, y), f"- ${failed}", fill="#FF6C6C", font=mid)
    d.text((900, y), "Failed", fill="#FF6C6C", font=small)

    os.makedirs("images", exist_ok=True)
    path = "images/balance.png"
    img.save(path)
    await message.answer_photo(FSInputFile(path))
