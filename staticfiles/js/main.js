$(document).ready(function(){
	animate();
});



function animate()
{
	$("li").each(function(){
		$(this).width('40%')
	});
}
