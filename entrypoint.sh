#!/bin/bash

set -Eeuo pipefail

function print_help {
    echo "Available options:"
    echo " start commands (Rasa Core cmdline arguments) - Start Rasa Core server"
    echo " train                                        - Train a dialogue model"
    echo " start -h                                     - Print Rasa Core help"
    echo " help                                         - Print this help"
    echo " run                                          - Run an arbitrary command inside the container"
}

case ${1} in
    start)
        exec python -m rasa_core_sdk.endpoint --actions actions & python -m rasa_core.run --enable_api --core models/dialogue --nlu models/nlu/current --cors '*' --endpoints endpoints.yml --debug
        ;;
    run)
        exec "${@:2}"
        ;;
    train)
        exec python -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data ./nlu_data.md -o models --project nlu --verbose & python -m rasa_core.train -s ./stories.md -d domain.yml -o models/dialogue -c ./default_config.yml --debug
        ;;
    *)
        print_help
        ;;
esac