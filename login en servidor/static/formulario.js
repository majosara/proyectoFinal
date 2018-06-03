var pos = 0,test,test_status,question,choice,choices,chA,chB,chC,chD,correct = 0;

	var questions = [
		["cuanto es 2 + 2","4","2","0","1","A"],
		["cuanto es 2 + 3","4","5","0","1","B"],
		["cuanto es 2 + 4","0","2","6","1","C"],
		["cuanto es 2 + 5","0","2","1","7","D"]
	];

	function _(x){
		return document.getElementById(x);
	}

	function renderQuestion(){
		test = _("test");
		if(pos >= questions.length){
			test.innerHTML = "<h2> You got" + correct + " of " + questions.length + " questions correct</h2>";
			_("test_status").innerHTML = "Test completed";
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
		test.innerHTML += "<button onclick='checkAnswer()'>Submit Answer</button>";
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