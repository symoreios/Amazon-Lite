$(document).ready(function(){
    
    $("#dialog2").dialog({
        autoOpen: false
    })
    
    $("#submitButton").click(function(e){
        e.preventDefault();
        checkInput();
        
        
    })
    $("#new_similar").keypress(function(e){
        if(e.which == 13){
            e.preventDefault();
            checkInput();
        }
    })

})

    function checkInput(){
        let title = $.trim($("#new_title").val())
        let author = $.trim($("#new_author").val())
        let year = $.trim($("#new_year").val())
        let summary = $.trim($("#new_summary").val())
        let score = $.trim($("#new_score").val())
        let pages = $.trim($("#new_pages").val())
        let alt = $.trim($("#new_alt").val())
        let image = $.trim($("#new_image").val())
        let similar = $.trim($("#new_similar").val())
        $("#new_title").next(".check").remove();
        $("#new_author").next(".check").remove();
        $("#new_year").next(".check").remove();
        $("#new_summary").next(".check").remove();
        $("#new_score").next(".check").remove();
        $("#new_pages").next(".check").remove();
        $("#new_image").next(".check").remove();
        $("#new_similar").next(".check").remove();
        if(isNaN(year)  || year.charAt(0) == ""){
            $("#new_year").after("<div class='check'> Must be a number </div>");
            $("#new_year").val(' ')
            $("#new_year").focus()
            return
          }
           else if(isNaN(pages) || pages.charAt(0) == ""){
            $("#new_pages").after("<div class='check'> Must be a number </div>");
            $("#new_pages").val(' ')
            $("#new_pages").focus()
            return
          }
           else if(isNaN(score) || score.charAt(0) == ""){
            $("#new_score").after("<div class='check'> Must be a number </div>");
            $("#new_score").val(' ')
            $("#new_score").focus()
            return
          }
          else if(title.charAt(0) == ""){
            $("#new_title").after("<div class='check'> Must not be empty </div>");
            $("#new_title").val(' ')
            $("#new_title").focus()
            return
          }
          else if(alt.charAt(0) == ""){
            $("#new_alt").after("<div class='check'> Must not be empty </div>");
            $("#new_alt").val(' ')
            $("#new_alt").focus()
            return
          }
          else if(author.charAt(0) == ""){
            $("#new_author").after("<div class='check'> Must not be empty </div>");
            $("#new_author").val(' ')
            $("#new_author").focus()
            return
          }
          else if(image.charAt(0) == ""){
            $("#new_image").after("<div class='check'> Must not be empty </div>");
            $("#new_image").val(' ')
            $("#new_image").focus()
            return
          }
          else if(summary.charAt(0) == ""){
            $("#new_summary").after("<div class='check'> Must not be empty </div>");
            $("#new_summary").val(' ')
            $("#new_summary").focus()
            return
          }
          else if(similar.charAt(0) == ""){
            $("#new_similar").after("<div class='check'> Must not be empty </div>");
            $("#new_similar").val(' ')
            $("#new_similar").focus()
            return
          }
          
        
        
       
            
        let data_to_send = {
            "title": title,
            "author":author,
            "year": year,
            "summary": summary,
            "score": score,
            "alt": alt,
            "pages": pages,
            "image": image,
            "similar": similar
        }
        $.ajax({
            type: "POST",
            url: "add_new",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_send),
            success:function(result){
                let id = current_id
                $('input[type="text"]').val('');
                $("#dialog2").dialog({
                    buttons: {
                        "Yes": function(){
                            window.location.replace("/view/" + id);
                        },
                        "No": function(){
                            $(this).dialog("close");
                        }
                    }
                })
                $("#dialog2").dialog("open");
                
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
                
            })
            


    }
    
    
  
