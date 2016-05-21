#!/usr/bin/env bash

PROJECT_ROOT=$(dirname ${BASH_SOURCE[0]})


if type greadlink > /dev/null 2>&1; then
    READ_LINK=`which greadlink`
else
    READ_LINK=`which readlink`
fi

PYENV_PATH=`$READ_LINK -f $0`
SCR_DIR=$(dirname $($READ_LINK -f $0))
PYENV=$($READ_LINK -f ${PROJECT_ROOT}"/env")

if ! [[ -d $PYENV ]]; then
    echo "error: virtual env not found."
fi

if [[ ${@} == "" ]]; then
    bash --init-file $PYENV/bin/activate
    exit
fi

. ${PYENV}/bin/activate
exec "$@"
