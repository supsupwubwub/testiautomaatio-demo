# Arkkitehtuurikuvaus

## Testausympäristön rakenne
Testit on jaettu kolmeen tasoon:
1. **Yksikkötestit (Jest):** Komponenttien logiikka.
2. **Integraatiotestit:** Rajapintojen välinen kommunikaatio.
3. **E2E-testit (Playwright):** Käyttäjäpolut selaimessa.

## CI/CD Putki (Workflow)

<pre class="mermaid">
graph LR
    A[Koodin Push] --> B(GitHub Actions)
    B --> C{Testit läpi?}
    C -->|Kyllä| D[Deploy Stage]
    C -->|Ei| E[Ilmoitus tiimille]
</pre>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default' });
</script>

---
## 4. Käyttöönotto
Tämä on tärkein tiedosto arvosanan kannalta (että ope saa testit pyörimään).

👉 **[Lue asennusohje täältä](./setup.md)**
