from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import random
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class Database:
    def __init__(self):
        self.db_name = "routex.db"

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        db = self.connect()
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS biletler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firma TEXT,
            rota TEXT,
            tarih TEXT,
            koltuk TEXT,
            fiyat TEXT,
            pnr TEXT,
            created_at TEXT
        )
        """)

        db.commit()
        db.close()


database = Database()
database.create_tables()


@app.get("/", response_class=HTMLResponse)
async def home():
    try:
        with open("templates/index.html", "r", encoding="utf-8") as file:
            return file.read()
    except:
        return "<h1>index.html bulunamadı</h1>"


@app.get("/bilet-kaydet")
async def bilet_kaydet(
    firma: str,
    rota: str,
    tarih: str,
    koltuk: str,
    fiyat: str
):
    try:

        pnr = "RTX" + str(random.randint(10000, 99999))

        db = database.connect()
        cursor = db.cursor()

        cursor.execute("""
        INSERT INTO biletler
        (firma, rota, tarih, koltuk, fiyat, pnr, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            firma,
            rota,
            tarih,
            koltuk,
            fiyat,
            pnr,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        db.commit()
        db.close()

        return {
            "durum": "basarili",
            "pnr": pnr
        }

    except Exception as hata:
        return {
            "durum": "hata",
            "mesaj": str(hata)
        }


@app.get("/biletler")
async def biletlerim():

    try:
        db = database.connect()
        cursor = db.cursor()

        cursor.execute("""
        SELECT firma, rota, tarih, koltuk, fiyat, pnr
        FROM biletler
        ORDER BY id DESC
        """)

        veriler = cursor.fetchall()

        db.close()

        biletler = []

        for veri in veriler:
            biletler.append({
                "firma": veri[0],
                "rota": veri[1],
                "tarih": veri[2],
                "koltuk": veri[3],
                "fiyat": veri[4],
                "pnr": veri[5]
            })

        return {
            "biletler": biletler
        }

    except Exception as hata:
        return {
            "hata": str(hata)
        }


@app.get("/admin-ozet")
async def admin_ozet():

    db = database.connect()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM biletler")
    toplam_bilet = cursor.fetchone()[0]

    cursor.execute("SELECT fiyat FROM biletler")
    fiyatlar = cursor.fetchall()

    toplam_gelir = 0

    for fiyat in fiyatlar:
        try:
            toplam_gelir += int(float(fiyat[0]))
        except:
            pass

    db.close()

    return {
        "toplam_bilet": toplam_bilet,
        "toplam_gelir": toplam_gelir,
        "toplam_sefer": 10
    }
@app.get("/kullanici-kayit")
async def kullanici_kayit(ad: str, email: str, sifre: str):
    try:
        db = database.connect()
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            email TEXT UNIQUE,
            sifre TEXT,
            created_at TEXT
        )
        """)

        cursor.execute("""
        INSERT INTO kullanicilar (ad, email, sifre, created_at)
        VALUES (?, ?, ?, ?)
        """, (ad, email, sifre, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        db.commit()
        db.close()

        return {"durum": "basarili", "mesaj": "Kayıt başarılı"}

    except Exception as hata:
        return {"durum": "hata", "mesaj": str(hata)}


@app.get("/kullanici-giris")
async def kullanici_giris(email: str, sifre: str):
    try:
        db = database.connect()
        cursor = db.cursor()

        cursor.execute("""
        SELECT ad, email
        FROM kullanicilar
        WHERE email = ? AND sifre = ?
        """, (email, sifre))

        kullanici = cursor.fetchone()
        db.close()

        if kullanici:
            return {
                "durum": "basarili",
                "ad": kullanici[0],
                "email": kullanici[1]
            }

        return {"durum": "hata", "mesaj": "Email veya şifre hatalı"}

    except Exception as hata:
        return {"durum": "hata", "mesaj": str(hata)}