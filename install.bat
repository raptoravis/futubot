conda create -n futubot python=3.8 -y
conda activate futubot

pip install -r requirements.txt

rem "-v" for verbose option.
rem "-e" means installing the project in editable mode,
rem so any local modifications on the project can be used without reinstalling it.
pip install -v -e .
