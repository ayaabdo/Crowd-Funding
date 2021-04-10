 var elements = document.getElementsByClassName('open-AddBookDialog');
    for (var i=0; i<elements.length; i++) {
        elements[i].addEventListener("click", function(){
               var commentId = $(this).data('commentid');
             $(".modal-body #commentId").val( commentId );

               var thecomment = $(this).data('comment');
             $(".modal-body #commentedited").val( thecomment );

        });
    }


<!--ratring-->
var rateelements = document.getElementsByClassName('open-rateelements');
for (var j=0; j<rateelements.length; j++) {
    rateelements[j].addEventListener("click", function(){
           var therate = $(this).data('value');
           $("#therate").val( therate )

    });
}

