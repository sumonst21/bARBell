$(document).ready(function(){
	console.log("loaded ;)...");
  	
	$('#calculator').hover(
				
    	function () {
        	$("#dropdwn").slideDown("fast");
        }, 
				
        function () {
            $("#dropdwn").slideUp('fast');
        }
    );
});