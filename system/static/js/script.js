/**
 * Created by Igna on 24/03/2016.
 */
function recargarMensajes() {
    $(".notificaciones").load("/notificaciones/")
    $(".notificaciones").fadeIn(300);
    $(".notificaciones").fadeOut(3000);
}


