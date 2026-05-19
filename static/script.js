class Sefer {
    constructor(sehir, saat) {
        this._sehir = sehir;
        this._saat = saat;
    }

    getSehir() {
        return this._sehir;
    }

    getSaat() {
        return this._saat;
    }
}

class OtobusSeferi extends Sefer {
    constructor(sehir, saat, otobusTipi) {
        super(sehir, saat);
        this._otobusTipi = otobusTipi;
    }

    getOtobusTipi() {
        return this._otobusTipi;
    }
}

class TopluTasimaSistemi {
    constructor() {
        this.seferler = [];
    }

    seferEkle(sefer) {
        this.seferler.push(sefer);
        this.listeyiGoster();
    }

    listeyiGoster() {

        let liste = document.getElementById("liste");

        liste.innerHTML = "";

        for(let i = 0; i < this.seferler.length; i++) {

            liste.innerHTML += `

            <div class="sefer">
                <b>Şehir:</b> ${this.seferler[i].getSehir()} <br>
                <b>Saat:</b> ${this.seferler[i].getSaat()} <br>
                <b>Otobüs Tipi:</b> ${this.seferler[i].getOtobusTipi()}
            </div>

            `;
        }
    }
}

const sistem = new TopluTasimaSistemi();

function seferEkle() {

    let sehir = document.getElementById("sehir").value;
    let saat = document.getElementById("saat").value;

    if(sehir === "" || saat === "") {
        alert("Lütfen tüm alanları doldurun!");
        return;
    }

    let yeniSefer = new OtobusSeferi(
        sehir,
        saat,
        "Şehirlerarası"
    );

    sistem.seferEkle(yeniSefer);

    document.getElementById("sehir").value = "";
    document.getElementById("saat").value = "";
}
const firmalar = [
    "Pamukkale Turizm",
    "Metro Turizm",
    "Kamil Koç",
    "Anadolu Star",
    "RouteX Express"
];

function rastgeleFiyat() {
    return Math.floor(Math.random() * 1000) + 350;
}

function seferAra() {

    const nereden = document.getElementById("nereden").value;
    const nereye = document.getElementById("nereye").value;
    const tarih = document.getElementById("tarih").value;

    const sonucDiv = document.getElementById("sonuclar");

    sonucDiv.innerHTML = "";

    for(let i = 0; i < 5; i++) {

        const firma = firmalar[i];
        const fiyat = rastgeleFiyat();

        sonucDiv.innerHTML += `
            <div class="sefer-kart">
                <h3>${firma}</h3>

                <p>${nereden} → ${nereye}</p>

                <p>Tarih: ${tarih}</p>

                <p>Fiyat: ₺${fiyat}</p>

                <button onclick="
                    window.location.href=
                    '/kaydet?firma=${firma}&rota=${nereden}-${nereye}&tarih=${tarih}&koltuk=${i+1}&fiyat=${fiyat}'
                ">
                    Bilet Al
                </button>
            </div>
        `;
    }
}