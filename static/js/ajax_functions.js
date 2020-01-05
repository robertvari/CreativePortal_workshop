function submit_comment(e, post_pk) {
    e.preventDefault();

    let post_comment_field = document.querySelector("#post_comment_field");
    if(post_comment_field.value.length === 0){return}

    // submit AJAX request
    $.ajax({
        url:'/ajax/comment_submit/',
        data: {"comment":post_comment_field.value, "post_pk":post_pk},
        dataType: 'json',

        success: function (data) {
            console.log(data)
        }
    });


    post_comment_field.value = ""
}