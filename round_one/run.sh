#!/usr/bin/env bash
# cd to the script's directory
cd $(dirname $0)

mkdir -p output
mkdir -p logs

solver=$1
if ! [[ -e "$solver" ]]; then
  echo "Usage: $(basename $0) <solver_module>"
  exit 1
fi

log() { echo "$(date +'%Y-%m-%d %H:%M:%S') - $*" | tee -a "./logs/solver_${solver_num}.log"; }

log "Started with solver ${solver}"
for input in $(ls -1 input/); do
  input_file="input/${input}"
  log "* Solver $1 solving $input - Started"
  node ./main.js "input/${input}" "${solver}"
  python3 ./main.py "input/${input}" "${solver}"
  log "* Solver $1 solving $input - Done"
done;
log "Finished with solver ${solver_num}"

echo "Code zipped to code_submission.zip"
zip -r code_submission.zip $(find . -name '*.py') $(find . -name '*.sh')