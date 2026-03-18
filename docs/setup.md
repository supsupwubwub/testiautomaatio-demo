Tässä on kattava ja ammattimainen `docs/setup.md` -tiedosto, joka on räätälöity testiautomaatioprojektille. Se sisältää selkeät vaiheet asennukseen, testien ajamiseen ja raporttien tarkasteluun.

Kopioi tästä koodiblokista sisältö uuteen tiedostoon nimeltä `docs/setup.md`:

````markdown
# 🛠️ Asennus- ja käyttöohje

Tämä ohje auttaa sinua pystyttämään testausympäristön paikallisesti ja suorittamaan automaatiotestejä.

---

## 📋 Esivaatimukset

Varmista, että koneellesi on asennettu seuraavat työkalut:
* **Node.js** (suositus: v18.0.0 tai uudempi)
* **npm** (tulee Noden mukana)
* **Git** (versionhallintaa varten)

---

## ⚙️ Asennusvaiheet

Noudata näitä ohjeita järjestyksessä:

1. **Kloonaa repositorio:**
   ```bash
   git clone [https://github.com/supsupwubwub/testiautomaatio-demo.git](https://github.com/supsupwubwub/testiautomaatio-demo.git)
   cd testiautomaatio-demo
````

2.  **Asenna riippuvuudet:**

    ```bash
    npm install
    ```

3.  **Asenna selainympäristöt (Playwright):**
    Playwright tarvitsee omat selaimensa toimiakseen. Asenna ne komennolla:

    ```bash
    npx playwright install
    ```

-----

## 🧪 Testien suorittaminen

Voit ajaa testejä eri tavoin riippuen siitä, mitä haluat testata:

### 1\. Kaikki testit (Yksikkö- ja integraatiotestit)

Ajaa kaikki Jest-pohjaiset testit:

```bash
npm test
```

### 2\. E2E-testit (Playwright)

Suorittaa selainpohjaiset käyttöliittymätestit:

```bash
npx playwright test
```

### 3\. Testit käyttöliittymätilassa (UI Mode)

Tämä on hyödyllinen kehityksen aikana, sillä näet testien etenemisen livenä:

```bash
npx playwright test --ui
```

-----

## 📊 Testiraportit

Kun testit on ajettu, voit tarkastella visuaalista raporttia mahdollisista virheistä ja onnistumisista:

```bash
npx playwright show-report
```

Raportti avautuu oletusselaimeesi ja näyttää tarkat tiedot jokaisesta testivaiheesta, mukaan lukien kuvakaappaukset virhetilanteista.

-----

## 🛠️ Vianetsintä

  * **Virhe: `playwright executable not found`**
      * Ratkaisu: Muista ajaa `npx playwright install`.
  * **Riippuvuusongelmat:**
      * Ratkaisu: Poista `node_modules` ja aja `npm install` uudelleen.

