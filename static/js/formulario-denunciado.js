$(document).ready(function () {

    /*
    $(".btn-agregar-servidorpublico").click(function () {
        $(this).hide();
        $(".btn-continuar-sinservidorpublico").hide();
        $(".btn-continuar-hechos").attr("hidden", true);
        $(".btn-agregar-particular").attr("hidden", true);
    });*/

    $("#btn-guardar-servidorpublico").click(function () { //Se da clic en el botón guardar
        $("#form-servidorpublico").attr("hidden", true);
        $(".btn-agregar-servidorpublico").attr("hidden", false);
        $(".btn-agregar-servidorpublico").html('<span class="uk-margin-small-right" uk-icon="plus"></span>Añadir otro servidor público');
        $(".btn-continuar-sinservidorpublico").hide();
        $(".datos-servidorpublico").attr("hidden", false);
        $(".btn-agregar-particular").attr("hidden", false);
        $(".btn-continuar-hechos").attr("hidden", false);
    })

    $("#btn-continuar-particular").click(function(){
        $("#form-servidorpublico").attr("hidden", true);
        $("#form-particular").attr("hidden", false);
    })

    $(".btn-agregar-particular").click(function () {
        $(this).hide();
        $(".btn-agregar-servidorpublico").hide();
        $(".btn-continuar-hechos").attr("hidden", true);
    })

    $("#btn-guardar-particular").click(function () {
        $(".btn-agregar-particular").show();
        $(".btn-agregar-particular").attr("hidden", false);
        $(".btn-agregar-servidorpublico").show();
        $("#form-particular").attr("hidden", true);
        $(".datos-particular").attr("hidden", false);
        $(".btn-continuar-hechos").attr("hidden", false);
    })

    /*$(".btn-continuar-sinservidorpublico").click(function () {
        $("#paso-uno").hide();
        $("#paso-dos").attr("hidden", false);
    })*/

    /*$(".btn-continuar-hechos").click(function () { 
        $("#paso-uno").hide();
        $("#paso-dos").attr("hidden", false);
    })*/

    $('.btn-agregar-hechos').click(function () {
		//$(".btn-continuar-terminardenuncia").hide();
		$("#form-hechos-probatorios").attr("hidden", false);
		$(this).hide();
    });
	
	$("#btn-agregar-hechos-archivo").click(function(){
		$(this).html("Subir otro archivo");
		$("#datos-hechos-archivos").append('<li>List item 1</li>');
	})
	
	$('.btn-continuar-terminardenuncia').click(function () {
		$("#paso-dos").attr("hidden", true);
    });
	
	/*$('.btn-continuar-terminardenuncia').click(function(){
		$("#paso-tres").attr("hidden", false);
	})*/
	
	/*$(".btn-continuar-presentardenuncia").click(function(){
		$("#paso-tres").attr("hidden", true);
		$("#paso-cuatro").attr("hidden", false);
	})*/
	
	$(".btn-enviar-denuncia").click(function(){
		$("#seccion-formulario-denuncias").attr("hidden", true);
	})

});
