//Variables con respecto al puntaje
var materia = "{{materia}}";
var puntajeMatematicas = 0;
var puntajeEspañol = 0;
var puntajeNaturales = 0;
var puntajeSociales = 0;

var pos = 0,test,test_status,question,choice,choices,chA,chB,chC,chD,correct = 0;

var gradoPreguntas = '{{gradoPreguntas}}';
var gradoPreguntasStr = gradoPreguntas.replace(/&#39;/g,'"');
//var gradoPreguntasArray = gradoPreguntasStr.replace(/&#34;/g,'"');
var questions = JSON.parse(gradoPreguntasStr);

function _(x){
	return document.getElementById(x);
}

function renderQuestion(){
	test = _("test");
	if(pos >= questions.length){
		test.innerHTML = "<h2> Obtuviste " + correct + " de " + questions.length + "  preguntas correctas</h2>";
		_("test_status").innerHTML = "Test completado";
		test.innerHTML += "<li><a href='/users/{{rol}}/{{username}}' class='active'>regresar menu</a></li>";
		if (materia == "Matematicas"){
			puntajeMatematicas = {{puntajeMatematicas}} + correct;
		} else if (materia == "Español") {
			puntajeEspañol = {{puntajeEspañol}} + correct;
		} else if (materia == "Naturales") {
			puntajeNaturales = {{puntajeNaturales}} + correct;
		} else {
			puntajeSociales = {{puntajeSociales}} + correct;
		}
		pos = 0;
		correct=0;
		return false; //detiene la funcion para que no se ejecute mas alla si llega al tope
	}
	
	_("test_status").innerHTML = "Question " + (pos+1) + " of " + questions.length;
	question = questions[pos][0];
	chA = questions[pos][1];
	chB = questions[pos][2];
	chC = questions[pos][3];
	chD = questions[pos][4];

	test.innerHTML = "<h3>" + question + "</h3>";
	test.innerHTML += "<input type='radio' name='choices' value='A'>" + chA+"<br>";
	test.innerHTML += "<input type='radio' name='choices' value='B'>" + chB+"<br>";
	test.innerHTML += "<input type='radio' name='choices' value='C'>" + chC+"<br>";
	test.innerHTML += "<input type='radio' name='choices' value='D'>" + chD+"<br><br>"; //cuando se da un value de una letra se refiere a la lista donde estan las opciones, el ultimo indice en esa tabla es la letra de la respuesta correcta
	test.innerHTML += "<button onclick='checkAnswer()'>Enviar respuesta</button>";
}

function checkAnswer(){
	choices = document.getElementsByName("choices");
	for(var i=0; i<choices.length; i++){
		if(choices[i].checked){
			choice = choices[i].value;
		}
	}
	if(choice == questions[pos][5]){
		correct++;
	}
	pos++; 
	//para que la funcion render se pueda seguir ejecutando nos tenemos que asegurar de que este aumente y lo hara la cantidad de veces que quiera
	renderQuestion();
}

window.addEventListener("load", renderQuestion,false);