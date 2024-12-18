# Usando imagem do Python
FROM python:3.10-slim

# Diretório do contêiner
WORKDIR /app

# Gera o requirements.txt
RUN pip freeze > requirements.txt

# Copia arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Variável de ambiente
ENV PYTHONUNBUFFERED=1

#
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]