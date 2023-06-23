# djtry

[![codecov.io](https://codecov.io/github/sshmo/djtry/coverage.svg?branch=master)](https://codecov.io/github/sshmo/djtry?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://sshmo.github.io/djtry/)
[![CodeQL](https://github.com/sshmo/djtry/actions/workflows/codeql.yml/badge.svg)](https://github.com/sshmo/djtry/actions/workflows/codeql.yml)
[![pre-commit](https://github.com/sshmo/djtry/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/sshmo/djtry/actions/workflows/pre-commit.yml)

djtry is a place to try python django.

## developmant

``` sh
    make dev
```

## Test

``` sh
    make test
```

## usage

First download the code from djtry GitHub repository:

``` sh
    git clone git@github.com:sshmo/djtry.git
    cd djtry
```

To run app:

``` sh
    python manage.py makemigrations blog
    python manage.py migrate
    python manage.py runserver
```

For creating superuser:

``` sh
    python manage.py createsuperuser
```
