    git clone https://github.com/Kengathua/oauth2-consumer.git
 
 Then

    cd oauth2-consumer

setup a virtualenv using python version >= 3.9

run:

    pip install -r requirements/all.txt

    ./manage.py makemigrations

    ./manage.py migrate

Ensure you have the [Authentication Server / Provider](https://github.com/Kengathua/oauth2-provider) set up: https://github.com/Kengathua/oauth2-provider

Ensure you have copied the **Client id** and **Client secret** from the app created in auth server to env file located next to the manage.py file

Source the env file using the command:

    . env.sh

or

    source env.sh

Run the server

    ./manage.py runserver 8000

or

    python manage.py runserver 8000

Ensure the auth server is running on port **9000**

On the client server go to this url which requires one to be authenticated to get the details of the currently logged in user.

http://127.0.0.1:8000/v1/users/me/

At the moment you will get the error

```"detail": "Authentication credentials were not provided."```

Now got to

http://127.0.0.1:8000/site_managers/sites/1/

Edit

Domain name:

    http://localhost:8000/

Display name:

    http://localhost:8000/

![Register Site](./screenshots/Screenshot%20from%202022-07-03%2020-52-15.png)

Then go to:
http://127.0.0.1:8000/site_managers/social_apps/

Populate the social login form with:

    Provider: <SELECT Portfolio Provider>

    Name: <ENTER A NAME>

    Client id: <ENTER the oauth2 client id>

    Secret key: <ENTER the oauth2 secret>

    Key: <Leave blank>

    Sites: <Select the site registered from above>

    **POST**

![Register Social App](./screenshots/Screenshot%20from%202022-07-03%2015-31-47.png)

Now go to:

http://127.0.0.1:8000/auth/provider/login/

You will get a sign in page.

Go Sign In Via Portfolio Provider and select **continue**

![Proceed to auth server](./screenshots/Screenshot%20from%202022-07-03%2012-41-03.png)


You will be redirected to the auth server admin login page

![Auth server login](./screenshots/Screenshot%20from%202022-07-03%2021-41-45.png)

Login and you will be redirected to the authorize page

![Auth server login](./screenshots/Screenshot%20from%202022-07-03%2021-46-58.png)

Select Authorize and you will be redirected back to the client

![Auth server login](./screenshots/Screenshot%20from%202022-07-03%2021-47-30.png)
