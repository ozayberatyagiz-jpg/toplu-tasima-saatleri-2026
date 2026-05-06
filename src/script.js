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