<h2>Install</h2>
Clone repository </br> 
cd flask-rest-login-register </br>
python views.py </br>

<h2>login</h2>
POST : http://localhost:5000/rest/login </br>
Parametros entrada </br>
{
	"username":"jtravolta",
	"password":"123456"
} </br>
resultado token </br>
{ "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ4OTg2NTI5NCwiaWF0IjoxNDg5ODY0Njk0fQ.eyJpZCI6Mn0.98LP3k6967OAcV47mTT3ObE385JHK3yRtcfH18Hc-D8" }
</br>

<h2>get user</h2>
GET: http://localhost:5000/rest/user </br>
Basic Authentication : Pasar como parametro el token obtenido en el momento de hacer login </br>
El resultado que se debe obtener es el hobbie del usuario
<br/>
{
  "hobbie": "bailar!"
}

<h2>Create user</h2>
POST : http://localhost:5000/rest/user </br>
{
	"username": "user1",
	"password": "123456",
	"nombres": "Usuario1",
	"hobbie" : "Cantar"
}
Si el usuario existe se  muestra el siguiente mensaje <br/>
{
  "message": "El usuario ya existe"
} <br/>

Si se creo correctamente el usuario se muestra el siguiente mensaje <br/>
{
  "resultado": "ok"
}
