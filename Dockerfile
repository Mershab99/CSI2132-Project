FROM python:3.11-slim as base

RUN adduser --disabled-password pynecone


FROM base as build

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

RUN echo pip install wheel \
    && pip install -r requirements.txt


FROM base as runtime

RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
    && apt-get update && apt-get install -y \
    nodejs \
    unzip \
    graphviz \
    && rm -rf /var/lib/apt/lists/*



# copy python package
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin/pc /usr/local/bin/pc


FROM runtime as init

WORKDIR /app
ENV BUN_INSTALL="/app/.bun"
COPY --from=build /app/ /app/

#RUN echo $PATH
RUN pc init


FROM runtime

COPY --chown=pynecone --from=init /app/ /app/
#COPY --from=init /app/ /app/
USER pynecone
WORKDIR /app

#CMD ["pc","run" , "--env", "prod"]
CMD ["pc", "run","--env", "dev"]

EXPOSE 3000
EXPOSE 8000