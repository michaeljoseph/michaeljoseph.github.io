serve:
    poetry run mkdocs serve

build:
    poetry run mkdocs build

surge: build
    npx surge site michaeljoseph.surge.sh

try:
    poetry run python -m resume