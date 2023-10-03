#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

pip install poetry

echo "Installing Poetry Version Plugin"
pip install poetry-version-plugin

poetry self show plugins
