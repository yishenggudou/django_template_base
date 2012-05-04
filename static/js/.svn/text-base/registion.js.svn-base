$(document).ready(function(){
	var invitecode = $('input[name=invicode]');
	var name = $('input[name=name]');
	var email = $('input[name=email]');
	var password = $('input[name=password]');
	var repassword = $('input[name=repassword]');
	$('button[type=submit]').click(function(){
	    var rst = [];
	    $('input').each(function(){
		if (!$(this).val()){
			$(this).parent().addClass('error');
			rst.push(false);
		}
		else{
			$(this).parent().removeClass('error');
			rst.push(true);
		}
		});
	    console.log(rst)
	    if (!_.all(rst, _.identity)){
	    	return false
		}
	    if (!(password.val() == repassword.val())){
		$(password).parent().addClass('error');
		$(repassword).parent().addClass('error');
		return false;
		}
            else{
		$(password).parent().removeClass('error');
		$(repassword).parent().removeClass('error');
		}
	})

})
