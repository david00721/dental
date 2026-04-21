.. Dental AI Platform documentation master file.

🦷 Dental AI Platform
=====================

Üdvözöljük a **Dental AI Platform** központi dokumentációjában!
Ez a rendszer egy moduláris monorepo architektúrára épül, amely fogászati diagnosztikai
és döntéstámogató eszközöket foglal magában.

.. image:: https://img.shields.io/badge/Python-3.14-blue.svg
   :target: https://www.python.org/downloads/release/python-3140/
.. image:: https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg
   :target: https://streamlit.io/

Rendszer áttekintés
-------------------
A platform célja a fogászati munkafolyamatok automatizálása, a 3D mérésektől kezdve
a páciens-edukációs felületekig. Minden alkalmazásunk azonos minőségbiztosítási
alapelveket követ (Ruff linting, MyPy típusellenőrzés, Pytest tesztelés).

.. toctree::
   :maxdepth: 1
   :caption: Alkalmazások leírása:

Fejlesztői útmutató
-------------------
Ha új modult szeretne hozzáadni a rendszerhez, kérjük, kövesse a belső
fejlesztési sztenderdjeinket:

* **Modularitás:** A logikai számításokat (`utils`) mindig különítsük el a felhasználói felülettől (`main.py`).
* **Tesztelés:** Minden új funkcióhoz kötelező egységtesztet (unit test) írni.
* **Dokumentáció:** Az alkalmazás mappáján belüli ``docs/`` könyvtár frissítése kötelező minden változtatásnál.

Indexek és keresés
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
