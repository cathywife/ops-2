$(document).ready(function(){
	$('.big').bind({
		mouseenter:function(){
			$(".max").show();
			$(".big").addClass("add");
		},
		mouseleave:function(){
			$(".big").removeClass("add");
			$(".max").hide();
		}
	})
});