# Qujini
Qujini is a free and open source question paper generator for teacher, and schools to manage a question bank and generate highly customizable question papers to conduct tests.


## How to Install?
1. Create and activate a `python 3` virtual environment
```bash
virtualenv -p python3 .
source bin/activate
```
2. Install django dependencies
```bash
pip install -r requirements.txt
```
3. Migrate changes, and run django normally
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## License
This project is licensed under [GNU General Public License v3.0](./LICENSE)
