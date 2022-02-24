#!/usr/bin/env bash
# cd to the script's directory
cd $(dirname $0)

mkdir -p output
mkdir -p logs

solver=$1
if ! [[ -e "solvers/$solver.py" ]]; then
  echo "Usage: $(basename $0) <solver_basename_without_py>"
  exit 1
fi

log() { echo "$(date +'%Y-%m-%d %H:%M:%S') - $*" | tee -a "./logs/solver_${solver_num}.log"; }

zip -r code_submission.zip $(find . -name '*.py') $(find . -name '*.sh')
echo "Code zipped to code_submission.zip"

log "Started with solver ${solver}"
for input in $(ls -1 input/); do
  input_file="input/${input}"
  log "* Solver $1 solving $input - Started"
#  node ./main.js "input/${input}" "${solver}"
  PYTHONPATH=. python3.8 ./main.py "input/${input}" "${solver}"
  log "* Solver $1 solving $input - Done"
  echo -e "\n\n\n\n"
done;
log "Finished with solver ${solver_num}"