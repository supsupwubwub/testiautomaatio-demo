---
layout: default
title: Arkkitehtuuri
nav_order: 2
---

# 🏗️ Arkkitehtuurikuvaus

Tässä osiossa kuvataan testausympäristön rakenne ja automaatioprosessit.

## Testausympäristön rakenne
Testit on jaettu kolmeen tasoon:
1. **Yksikkötestit (Jest):** Komponenttien logiikka.
2. **Integraatiotestit:** Rajapintojen välinen kommunikaatio.
3. **E2E-testit (Playwright):** Käyttäjäpolut selaimessa.

---

## 🔄 CI/CD Putki (Workflow)
Automaatio on toteutettu GitHub Actions -työnkuluilla, jotka ajavat testit jokaisen `push`-tapahtuman yhteydessä.

![CI/CD Kaavio](https://mermaid.ink/img/pako:eNptkEELwjAMhf9KyGkH_QMeBA96E_S2S6mzbS06m7IuYfTf3ToUvYpPyEvyeS8vSAtNo8Y_SreD0YEnayzI_ZAmW8rWNoM6F_I-LAs9O8PZAnkK6mHq0zAsWfKAs5K97-f0Y4f2D-SNoZ0Xk6x8E3-Sj7nI_rF-z9W_T-M-A1mE0qKAnUORP-G_pUvD0P8-XfFkCQ)

---

## Teknologiat
* **Kieli:** Node.js / JavaScript
* **Testauskehykset:** Jest & Playwright
* **Ajoalusta:** GitHub Actions (Ubuntu-latest)
