var options = [{
//Boolean - Whether we should show a stroke on each segment
segmentShowStroke : true,

//String - The colour of each segment stroke
segmentStrokeColor : "#fff",

//Number - The width of each segment stroke
segmentStrokeWidth : 2,

//Number - The percentage of the chart that we cut out of the middle
percentageInnerCutout : 50, // This is 0 for Pie charts

//Number - Amount of animation steps
animationSteps : 100,

//String - Animation easing effect
animationEasing : "easeOutBounce",

//Boolean - Whether we animate the rotation of the Doughnut
animateRotate : true,

//Boolean - Whether we animate scaling the Doughnut from the centre
animateScale : false,

}];

var home_data = [
	[{
	value: 30,
	label: "Python",
	color: "#788200",
	highlight: "#788200"

	},
	{
	value: 40,
	label: "C++",
	color: "#ff005a",
	highlight: "#ff005a" 

	},
	{
	value: 30,
	label: "Haskell",
	color: "#730073",
	highlight: "#730073"
	}],
	[{
	value: 15,
	label: "Scala",
	color: "#b2b2ff",
	highlight: "#b2b2ff"

	},
	{
	value: 65,
	label: "Javascript",
	color: "#00ff25",
	highlight: "#00ff25" 

	},
	{
	value: 20,
	label: "Rust",
	color: "#cf7700",
	highlight: "#cf7700"
	}],
	[{
	value: 10,
	label: "CSS",
	color: "#730073",
	highlight: "#730073"

	},
	{
	value: 20,
	label: "PHP",
	color: "#00824b",
	highlight: "#00824b"

	},
	{
	value: 70,
	label: "Java",
	color: "#ff005a",
	highlight: "#ff005a"
	}],


];

var colors = {
	"Red": {
		"color":"#F7464A",
	    "highlight": "#F7464A",
	},
	"Green": {
		"color": "#46BFBD",
	    "highlight": "#5AD3D1"
	},
	"Yellow": {
		"color": "#FDB45C",
	    "highlight": "#FFC870"
	},
	"Light Salmon": {
		"color":"#ffa07a",
	    "highlight": "#ffa07a",
	},
	"Purple": {
		"color": "#730073",
	    "highlight": "#730073"
	},
	"Sky Blue": {
		"color": "#b2b2ff",
	    "highlight": "#b2b2ff"
	},
	"Orange": {
		"color":"#ff2500",
	    "highlight": "#ff2500",
	},
	"Bright Green": {
		"color": "#00ff25",
	    "highlight": "#00ff25"
	},
	"Hot Pink": {
		"color": "#ff005a",
	    "highlight": "#ff005a"
	},
	"Aqua": {
		"color":"#00824b",
	    "highlight": "#00824b",
	},
	"Golden Rod": {
		"color": "#cf7700",
	    "highlight": "#cf7700"
	},
	"Pea Green": {
		"color": "#788200",
	    "highlight": "#788200"
	}

};

var timer = 0;

function setResetInterval(bool){
  if(bool){
    timer = setInterval(function(){
      count--;
      console.log(count)
      myPieChart = new Chart(ctx).Pie(home_data[count],options);
      $(".home_languages_container").empty();
      for (item in home_data[count]) {
      	$(".home_languages_container").append('<div class="coding_language" style="color:' + home_data[count][item].color + '">' + home_data[count][item].label +  ' : ' + home_data[count][item].value + '.0%</div>')
      }
      if (count == 0) {
        count=3;
      }
    }, 2000);
  }else{
    clearInterval(timer); 
  }
};

var format_languages = function(){
	$('.follower_title').on('click', function() {
		$('.followers_container').hide()
	})

	$('.lang_num').each(function() {
		var lang_num = $(this).text();
		$(this).text(((lang_num / total) * 100).toFixed(2) + '%')
	});

	$('.coding_language').each(function(index) {
		$(this).css('color', (language_data[index].color).toString());
	})

	var all_languages = $('.languages_container');
	var language_list = all_languages.find('.coding_language');

	language_list.sort(function(a,b){
		var an = parseInt(a.getAttribute('data-name'), 10),
		bn = parseInt(b.getAttribute('data-name'), 10);

		if(an < bn) {
			return 1;
		}
		if(an > bn) {
			return -1;
		}
			return 0;
	});

	language_list.detach().appendTo(all_languages);
};

