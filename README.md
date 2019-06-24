# Qujini

[![Join the chat at https://gitter.im/amfoss/Qujini](https://badges.gitter.im/amfoss/Qujini.svg)](https://gitter.im/amfoss/Qujini?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

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

## Paper Setting Procedure
* Set Title, and Description of the Question Paper
* Select Paper Pattern - User Defined / Pre Defined (import presets) / System Defined
* Set total marks for the paper
* Set minimum & maximum number of questions
* Select difficulty of the paper - Easy / Moderate / Hard / Random
    * Percentage of each type
* Set marks weightage from each topic
    * Set maximum & minimum mark range from each topic
    * Bonus: OR condition between Topics
* Set type weightage - Objective, Subjective, Theory etc.
    * Set maximum & minimum number of questions from each type
    * Set maximum & minimum marks from each type 
* Divide into sections by marks/type
    * Define sections - naming, total marks
* Save and export presets after setting paper - allowing same strategy for future papers 
* Save question paper on database
* Export question paper -> PDF, JSON

    
## License
This project is licensed under [GNU General Public License v3.0](./LICENSE)
