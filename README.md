
## Specific Meraki Dashlet

This repo is based on the https://github.com/rnplett/FlaskBareDash repo which covers off a step by step installation process for a VERY simple implementation. Reference that for a step by step installation procedure.

This repo takes it one step further to deploy a simple Meraki Network dashlet.

Start the mqdMain.py app as follows:
```
For Windows:
>set FLASK_APP=mqdMain
>flask run

For all other systems:
FLASK_APP=mqdMain.py flask run
```

After you issue the above command you can now put the following url into your web browser to test this simple vote collecting app.
