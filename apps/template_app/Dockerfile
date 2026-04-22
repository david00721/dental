# Phase 1: Builder
FROM python:3.14-slim AS builder

# Use ARG to make the package name dynamic for the monorepo
ARG PACKAGE_NAME=template_app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1

# Copy root config and the specific app config
COPY pyproject.toml uv.lock ./
COPY apps/${PACKAGE_NAME}/pyproject.toml ./apps/${PACKAGE_NAME}/

# Install only the dependencies for the specific package
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace --no-dev --package ${PACKAGE_NAME}

COPY . .

# Final sync for the specific package
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package ${PACKAGE_NAME}

# Phase 2: Runtime
FROM python:3.14-slim
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
ENV PORT=10000
EXPOSE 10000

# Use a shell script or direct command - ensuring it points to the right package
CMD ["streamlit", "run", "apps/template_app/src/template_app/main.py", "--server.port=10000", "--server.address=0.0.0.0"]
