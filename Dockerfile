FROM python:3.11-slim

RUN apt update -y && apt-get upgrade -y && apt install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pdm

WORKDIR /home/python/app

COPY . /home/python/app

# Cria o ambiente virtual com o PDM
RUN pdm venv create --force --with venv 3.11 && \
    pdm use -f 3.11

ENV MY_PYTHON_PACKAGES=/home/python/app/.venv/lib/python3.11/site-packages
ENV PYTHONPATH=${PYTHONPATH}:${MY_PYTHON_PACKAGES}
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

RUN echo "[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh" >> ~/.zshrc && \
    echo "HISTFILE=/home/python/zsh/.zsh_history" >> ~/.zshrc && \
    echo 'eval "$(pdm)"' >> ~/.zshrc && \
    echo 'eval "$(pdm)"' >> ~/.bashrc && \
    pdm install --no-lock --no-editable && \
    pdm run python manage.py collectstatic --noinput && \
    pdm run python manage.py makemigrations && \
    pdm run python manage.py migrate

EXPOSE 8000

CMD ["/home/python/app/commands.sh"]
