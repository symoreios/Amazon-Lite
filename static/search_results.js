// function sendSearch(search_text){
// }

$(document).ready(function(){
    $("#search_button").click(function(){
      
        let search = $("#search_bar").val()
        let trimd = $.trim(search)
        if(trimd.charAt(0) == ""){
            $("#search_bar").val('')
            $("#search_bar").focus()
            return
        }
    //    send_search(search)
        window.location.replace("/search_results/" + search)
        })
    $("#search_bar").keypress(function(e){
        if(e.which == 13){
        let search = $("#search_bar").val()
        let trimd = $.trim(search)
        if(trimd.charAt(0) == ""){
            $("#search_bar").val('')
            $("#search_bar").focus()
            return
        }
        window.location.replace("/search_results/" + search)
    }
    })
})