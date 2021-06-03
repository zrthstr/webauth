# Web Auth - web auth implementations for educational purpose (not for human consumption)

## OIDC
implemented as in https://realpython.com/flask-google-login/

### oauth setup
* cd OICD
* goto https://console.developers.google.com/apis/credentials
	* create new credentials / Oauth Client ID 
	* set Authorized JavaScript origins to https://127.0.0.1:5000
	* set Authorized redirect URIs to https://127.0.0.1:5000/login/callback.
	* note of the client ID and client secret
* populate ```SECRETS```, see ```SECRETS.blank```

### run
	make run  # on first run sqlite db will be initialized
	make run

goto https://127.0.0.1:5000

## Basic access authentication / RFC 7617
see https://flask-httpauth.readthedocs.io/en/latest/

	cd BasicAccessAuthentication
	make run
goto http://127.0.0.1:5000
use admin / admin 

## SessionCookieVanilla
see:
* https://flask-login.readthedocs.io/en/latest/
* https://github.com/marcelomd/flask-wtf-login-example/blob/master/app/models.py

### run
	cd SessionCookieVanilla
	make run
goto http://127.0.0.1:5000
use ```admin``` ```secure```

## JWTLocalStorage
see:
* https://flask-jwt-extended.readthedocs.io/en/stable/token_locations/

### run
	cd JWTLocalStorage
	make run
goto https://127.0.0.1:5000
login and logout, no credentials needed
