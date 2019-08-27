#!/bin/bash
set -e

# check that jq is installed for parsing meta.json
command -v jq >/dev/null 2>&1 || { echo >&2 "I require jq but it's not installed.  Aborting."; exit 1; }

# set current version
en_qai_sm_version=$(jq ".version" < meta.json | tr -d '"')

# optionally pass in a path to .pypirc
creds_location=$1

check_credential_file_exists ()
{
    if [ -f .pypirc ]; then
        echo "found .pypirc in project directory..."
        PYPIRC="here"
    elif [ -f ~/.pypirc ]; then
        echo "found .pypirc in user home directory..."
        PYPIRC="root"
    elif [ -f $creds_location]; then
        echo "credentials were passed in as argument"
        PYPIRC="creds"
    else
        echo "## MISSING .pypirc file, can't release to PyPi!"
        exit 1
    fi
}

rename_subdir ()
{
    subdir=$(find ./en_qai_sm -name "en_qai_sm*" -type d | tail -n 1)
    mv "$subdir" "./en_qai_sm/en_qai_sm-$en_qai_sm_version"
}

generate_sdist ()
{
    python3 setup.py sdist
}

upload_to_pypi ()
{
    echo "uploading to pypi"
    if [ $PYPIRC = "here" ]; then
        twine upload --config-file .pypirc dist/en_qai_sm-"$en_qai_sm_version".tar.gz
    elif [ $PYPIRC = "creds" ]; then
        twine upload --config-file $creds_location dist/en_qai_sm-"$en_qai_sm_version".tar.gz
    else
        twine upload --config-file ~/.pypirc dist/en_qai_sm-"$en_qai_sm_version".tar.gz
    fi
}

# Run functions
check_credential_file_exists
rename_subdir
generate_sdist
upload_to_pypi