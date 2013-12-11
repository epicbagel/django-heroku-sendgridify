# django-heroku-sendgridify

Automatic Send Grid configuration on Heroku.

## Install

To install the latest version of ``django-heroku-sendgridify``, simply run

```
pip install -e git://github.com/epicbagel/django-heroku-sendgridify.git#egg=django-heroku-sendgridify-dev
``` 


## Usage

Modify your Django ``settings.py`` file and add:

``` python
from sendgridify import *
```

That's it. It's normally best to create a separate heroku.py settings file, together with a local.py which can make use of the dummy email backend.
