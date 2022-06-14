$(document).ready(function(){
	console.log("loaded ;)...");

	var clicks = 0

		$('#calculator').click(function(){
          if(clicks == 0){
            $('#dropdwn').slideDown('fast');
            clicks++;
            console.log("open");
          }else{
            $('#dropdwn').slideUp('fast');
            $('#dropdwn2').slideUp('fast');
            clicks--;
            console.log("closed");
          }
          console.log(clicks);
        });
        $('#Betting').click(function(){
          if(clicks == 0){
            $('#dropdwn2').slideDown('fast');
            clicks++;
            console.log("open");
          }else{
            $('#dropdwn2').slideUp('fast');
            $('#dropdwn').slideUp('fast');
            clicks--;
            console.log("closed");
          }
          console.log(clicks);
        });




	/*
	$('#calculator').hover(
				
    	function () {
        	$("#dropdwn").slideDown("fast");
        }, 
				
        function () {
            $("#dropdwn2").slideUp('fast');
        }

    );
    $("#calculator").click(function(){
	    $("#dropdwn").slideUp("fast");
	});	 
	*/   
});