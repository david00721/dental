# 1. fázis: Építés
FROM python:3.14-slim AS builder

# uv telepítése
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Csak a konfigurációs fájlok másolása
COPY pyproject.toml uv.lock ./
COPY apps/template_app/pyproject.toml ./apps/template_app/

# 2. TRÜKK: Létrehozzuk az üres forráskódot ÉS a metaadat fájlokat
RUN mkdir -p apps/template_app/src/template_app && \
    touch apps/template_app/src/template_app/__init__.py && \
    touch apps/template_app/README.md && \
    touch README.md

# 3. Függőségek letöltése és cache-elése
RUN uv sync --frozen --no-install-project --no-dev

# 4. Most másoljuk át a valódi forráskódot
COPY . .

# 5. Teljes szinkronizálás (most már a valódi kódot is installálja)
RUN uv sync --frozen --no-dev

# 2. fázis: Futtatás
FROM python:3.14-slim

WORKDIR /app

# Átmásoljuk a builderben felépített környezetet és kódot
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PORT=10000
EXPOSE 10000

# Streamlit indítása
CMD ["streamlit", "run", "apps/template_app/src/template_app/main.py", "--server.port=10000", "--server.address=0.0.0.0"]
