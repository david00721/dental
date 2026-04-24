FROM mcr.microsoft.com/devcontainers/base:ubuntu

ARG USER_NAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN if id "vscode" >/dev/null 2>&1; then \
        usermod -l ${USER_NAME} vscode && \
        groupmod -n ${USER_NAME} vscode && \
        usermod -d /home/${USER_NAME} -m ${USER_NAME}; \
    else \
        groupadd --gid ${USER_GID} ${USER_NAME} || true && \
        useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USER_NAME}; \
    fi \
    && echo ${USER_NAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}

USER ${USER_NAME}

ENV UV_PROJECT_ENVIRONMENT="/home/${USER_NAME}/venv"

RUN mkdir -p ${UV_PROJECT_ENVIRONMENT}

ENV PATH="${UV_PROJECT_ENVIRONMENT}/bin:$PATH"

RUN rm -rf ~/.oh-my-zsh && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

RUN touch ~/.zshrc && \
    sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc
