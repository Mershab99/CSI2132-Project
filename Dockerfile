FROM node:16.19.0-buster-slim as node
FROM jarredsumner/bun:edge as bun


FROM python:3.10-buster as builder
# python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONUTF8=1 \
    PYTHONIOENCODING=UTF-8 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# copy requirements.txt
COPY requirements.txt /root/

# install pip dependencies
RUN pip install --no-cache-dir -U pip  &&\
    pip install --no-cache-dir -U setuptools  && \
    pip install --no-cache-dir -U wheel  && \
    pip install --no-cache-dir -r /root/requirements.txt


FROM python:3.10-slim-buster as runner
# set work directory
WORKDIR /app

# copy nodejs binaries
COPY --from=node /usr/local/bin /usr/local/bin
COPY --from=node /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
COPY --from=node /opt/yarn* /opt/yarn
RUN ln -fs /opt/yarn/bin/yarn /usr/local/bin/yarn && \
    ln -fs /opt/yarn/bin/yarnpkg /usr/local/bin/yarnpkg

# copy bun binaries
COPY --from=bun /usr/local/bin/bun /usr/local/bin/bun

# copy python package
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/pc /usr/local/bin/pc

# permission settings
RUN groupadd -r app && useradd -r -m -g app app
RUN chown -R app:app /app
USER app

# copy source code
COPY --chown=app:app . ./

# init pynecone
RUN pc init

# start process
ENTRYPOINT ["pc", "run"]
