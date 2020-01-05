function submit_comment(e, post_pk) {
    e.preventDefault();

    let comment_list_layout = document.querySelector('#comment_list_layout')
    let post_comment_field = document.querySelector("#post_comment_field");
    if(post_comment_field.value.length === 0){return}

    // submit AJAX request
    $.ajax({
        url:'/ajax/comment_submit/',
        data: {"comment":post_comment_field.value, "post_pk":post_pk},
        dataType: 'json',

        success: function (data) {
            comment_list_layout.insertBefore(

                comment_element(data, comment_list_layout),
                comment_list_layout.childNodes[0] || null

            )
        }
    });


    post_comment_field.value = ""
}


function comment_element(data, parent_element){
    let comment_item = create_element("div", parent_element, "comment_item");

    // create comment head
    let comment_head = create_element("div", comment_item, "post_author_head");

    // user picture
    let user_pic = create_element("div", comment_head, "user_pic");
    user_pic.style.marginRight = '10px';
    user_pic.style.backgroundImage = 'url('+ data["user"]["profile_pic"] + ')';

    // author name
    let author_name = create_element("div", comment_head, "author_name");
    let name_div = create_element("div", author_name);
    create_element("text", name_div, false, false, data["user"]["user"]);

    // author bio
    let author_bio_div = create_element("div", author_name, "help_text");
    create_element("text", author_bio_div, false, false, data["user"]["bio"]);

    // comment text
    let commen_element = create_element("div", comment_item, 'comment_text');
    commen_element.style.fontSize = "14px";
    create_element("text", commen_element, false, false, data["comment"]);

    // comment date
    let comment_date = create_element("div", comment_item, "help_text");
    comment_date.style.textAlign = 'right';
    comment_date.style.marginTop = '10px';
    create_element("text", comment_date, false, false, data["created_on"]);

    return comment_item
}


// handle likes
function submit_like(e, post_pk) {
    let like_button = document.querySelector('#like_button');
    let button_value;

    if(like_button.className.includes("creative")){
        like_button.className = 'like_button';
        button_value = 0;
    }else{
        like_button.className = 'like_button creative'
        button_value = 1;
    }

    let like_text_element = document.querySelector('#like_button_text');
    let current_likes = parseInt(like_text_element.textContent,10);
    if(button_value === 1){
        current_likes += 1
    }else{
        current_likes -= 1
    }

    like_text_element.textContent = current_likes + ' Likes'

    // submit with AJAX
    $.ajax({
        url:"/ajax/like_submit/",
        data:{
            "value": button_value,
            "post_pk": post_pk,
        },
        dataType: 'json',

        success: function (data) {}

    });

}


// helper function for creating DOM elements
function create_element(element_type,
                        parent_node,
                        class_name=false,
                        id=false,
                        text= undefined) {
    let DOM_node;

    if(element_type === 'text'){

        DOM_node = document.createTextNode(text)

    }else{

        DOM_node = document.createElement(element_type);
        if (class_name){
            DOM_node.className = class_name
        }
        if(id){
            DOM_node.id = id
        }
    }

    parent_node.appendChild(DOM_node);

    return DOM_node
}