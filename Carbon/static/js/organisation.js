//line
console.log("Organisation.js is connected")

$(document).ready(function() {
	// hide results template and error alerts on initial page load
	$("#results").hide();
	$(".alert").hide();

	// prevent ability to type negative numbers or spaces in input fields
	$("[type='number']").bind("keydown", function(e) {
		var code = e.keyCode || e.which;

		if (code == 189 || code == 173 || code == 32 || code == 69 || code == 109) {
			return false;
		}
	});

	$("#calculate-btn").on("click", function() {
		var calculateAndDisplayScore = function() {
			window.scrollTo(0, 400);
			// hide form template if all inputs are completed
			$("#form").hide();

			// get input values
			var electricInput = document.getElementById("electric").value;
			var fuelInput = document.getElementById("fuel").value;
			var carInput = document.getElementById("car").value;
			
			// set variables for calculating each component score
			var electricScore = "";
			var fuelScore = "";
			var carScore = "";
			var newspaperScore = "";
			var ghgScore = "";

			var totalScore = "";

			if (document.getElementById("optionsRadio1").checked) {
				newspaperScore = 0;
			} else {
				newspaperScore = 184;
			}
			// console.log("Newspaper score is: " + newspaperScore);

			if (document.getElementById("optionsRadio3").checked) {
				ghgScore = 0;
			} else {
				ghgScore = 60;
			}
			// console.log("Aluminum and tin score is: " + ghgScore);

			if (electricInput === 0 || electricInput === "undefined") {
				electricScore = 0;
			} else {
				electricScore = electricInput * 0.82;
			}
			// console.log("Electric score is: " + electricScore);

			if (fuelInput === 0 || fuelInput === "undefined") {
				fuelScore = 0;
			} else {
				fuelScore = fuelInput * 2.68;
			}
			// console.log("fuel score is: " + fuel);

			if (carInput === 0 || carInput === "undefined") {
				carScore = 0;
			} else {
				carScore = carInput * 0.18;
			}
			// console.log("Car score is: " + carScore);

			// calculate scores for each category
			var orgScore = electricScore + fuelScore + carScore	 ;
			var wasteScore = newspaperScore + ghgScore;

			// calculate total score and round to nearest whole integer
			totalScore = Math.round(orgScore + wasteScore);
			var formattedScore = totalScore.toLocaleString("en");
			// console.log(totalScore);

			document.getElementById("score").innerHTML = formattedScore;

			// display results
			$("#results").show();

			
			
		}

		// check selection made for recycling newspaper before calculating and displaying score
		var recycleNewspaperSelectionYes = document.getElementById("optionsRadio1").checked;
		var recycleNewspaperSelectionNo = document.getElementById("optionsRadio2").checked;
		var recycleghgSelectionYes = document.getElementById("optionsRadio3").checked;
		var recycleghgSelectionNo = document.getElementById("optionsRadio4").checked;

		if (recycleNewspaperSelectionYes == false && recycleNewspaperSelectionNo == false || recycleghgSelectionYes == false && recycleghgSelectionNo == false) {
			if (recycleNewspaperSelectionYes == false && recycleNewspaperSelectionNo == false) {
				$("#newspaper-alert").show();
			} else {
				$("#newspaper-alert").hide();
			}

			if (recycleghgSelectionYes == false && recycleghgSelectionNo == false) {
				$("#alum-tin-alert").show();
			} else {
				$("#alum-tin-alert").hide();
			}
		} else {
			calculateAndDisplayScore();
		}
	});	
});