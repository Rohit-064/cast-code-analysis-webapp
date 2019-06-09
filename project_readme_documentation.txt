++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
OS  Ubuntu i Used
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
======================================================================
Tech stack Used:
======================================================================
Front End: Reactjs
Back End: Python - Django
Database: Mysql(sqllite)
======================================================================
Github link: https://github.com/Rohit-064/cast-code-analysis-webapp

HerokuApp link : https://cast-code-analyser-tool-webapp.herokuapp.com/
-----------------------------------------------------------------------

Gitclone or Dowload zip and unzip to a folder

open terminal ->go to project dir

1.$ pip install pipenv
   start virtualenv

2.cd CAST_codeAnalyser
  -pip install -r requirements.txt

3. ./manage.py runserver

4. ctrl + shift + t => cd react frontend

5. check if npm is installed 
   npm -v

   if not installed 
   sudo apt-get install npm

6. ...CAST_codeAnalyser/react frontend$ npm install

   than all dependencies will be installed 

7. ...CAST_codeAnalyser/react frontend$ npm run

8. Open http://localhost:3000/ in the browser or it will be opened automatically

9. Select Python/CSS from the dropdowm and paste respective code ,then the status of 
   the uploaded code will be shown on right side

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
About Project

The code analyser tool is used to find the errors and remarks in the python code and css code

Done
------
1.Currently the tools helps in Analysis of Python script and CSS script
2.we can paste the python code or css code to get the remarks, errors and status of the code
3.Api for code has been done
  - 127.0.0.1:8000/api/code-analyser can be used to test the api in localhost .can also test using postman

************************request  CSS****************************************************
import requests

url = "http://127.0.0.1:8000/api/code-analyser"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"codestype\"\r\n\r\nCSS\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"codedata\"\r\n\r\nP{ color: red }\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "b6a2405d-b2ea-4256-b512-ab02ee044885"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

******************************************************************************************
****************************Response******************************************************

{
    "body": {
        "remarks": "The file is valid",
        "errors": "[]"
    },
    "head": {
        "status": 0,
        "description": "Success"
    }
}

*****************************************************************************

----------------------------request Python----------------------------------
import requests

url = "http://127.0.0.1:8000/api/code-analyser"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"codestype\"\r\n\r\nPython\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"codedata\"\r\n\r\n#!/usr/bin/env python\nimport os\nimport sys\n\nif __name__ == \"__main__\":\n    os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"CAST_codeAnalyser.settings\")\n    try:\n        from django.core.management import execute_from_command_line\n    except ImportError:\n        # The above import may fail for some other reason. Ensure that the\n        # issue is really that Django is missing to avoid masking other\n        # exceptions on Python 2.\n        try:\n            import django\n        except ImportError:\n            raise ImportError(\n                \"Couldn't import Django. Are you sure it's installed and \"\n                \"available on your PYTHONPATH environment variable? Did you \"\n                \"forget to activate a virtual environment?\"\n            )\n        raise\n    execute_from_command_line(sys.argv)\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "0013ee41-c5ef-468a-9bfc-0f29eb892e91"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
-------------------------------------------------------------------------------------------
--------------------------------response Python---------------------------------------------
{
    "body": {
        "remarks": "************* Module temp\n ./Analyser/temp/temp.py:14: warning (W0611, unused-import, ) Unused import django\n \n ------------------------------------------------------------------\n Your code has been rated at 9.23/10 (previous run: 9.23/10, +0.00)\n \n ",
        "errors": "No config file found, using default configuration\n"
    },
    "head": {
        "status": "",
        "description": ""
    }
}
--------------------------------------------------------------------------------------------


half way done
----
1.The database setup has been done
2.models setup has been done

TODO
------
-Create Signup /login and token or session authentication
-Show code uploaded for respective user in his Dashboard with the status
-Provide edit/delete for the above list of codes in the dashboard
-Perform  QA testing
-integrate more programming languages to the tool

Updates which can be done for the App
--------------------------------------
-Store the code along with date and time in the db
-Provide Interval search ie(start_date and end_date search for the uploaded code)
-Based on the interval show analytics for the code uploaded in the time interval
-Use graph or piechart to show the Errors and success status of the code over a period of time
-Provide filter and show analytics (ie show oly python analytics or only css anlytics and so on, over a period of time)



