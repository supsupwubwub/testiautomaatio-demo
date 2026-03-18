# Arkkitehtuurikuvaus

## Testausympäristön rakenne
Testit on jaettu kolmeen tasoon:
1. **Yksikkötestit (Jest):** Komponenttien logiikka.
2. **Integraatiotestit:** Rajapintojen välinen kommunikaatio.
3. **E2E-testit (Playwright):** Käyttäjäpolut selaimessa.

## CI/CD Putki (Workflow)
```mermaid
graph LR
    A[Koodin Push] --> B(GitHub Actions)
    B --> C{Testit läpi?}
    C -->|Kyllä| D[Deploy Stage]
    C -->|Ei| E[Ilmoitus tiimille]

### 4. Käyttöönotto: `docs/setup.md`
Tämä on tärkein tiedosto arvosanan kannalta (että ope saa testit pyörimään).

```markdown
# Käyttöönotto-ohje

## Esivaatimukset
- Node.js (v18 tai uudempi)
- npm

## Asennus
```bash
npm install
npx playwright install
