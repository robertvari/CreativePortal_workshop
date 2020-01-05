// prevent default drop event on window
window.addEventListener('dragover', function(e) {
    e.preventDefault();
}, false);

window.addEventListener('drop', function(e) {
    e.preventDefault();
}, false);


// get elements on page
let image_drop_area = document.querySelector('#image_drop_area');
let image_canvas = document.querySelector('#image_canvas');
let image_file_input = document.querySelector('#image_file_input');
let drop_text = document.querySelector('#drop_text');


// add event listener to image_drop_area
image_drop_area.addEventListener('dragenter', drag_enter_event);
image_drop_area.addEventListener('dragleave', drag_leave_event);
image_drop_area.addEventListener('drop', drop_event);

function drag_enter_event() {
    image_drop_area.style.backgroundColor = 'rgba(19, 175, 240, 0.2)';
}

function drag_leave_event() {
    image_drop_area.style.backgroundColor = 'transparent';
}

function drop_event(event) {
    image_drop_area.style.backgroundColor = 'transparent';

    if(drop_text){
        drop_text.style.display = 'none';
    }

    image_canvas.style.display = 'block';

    // get files from drop event
    let dropped_files = event.dataTransfer.files;

    image_file_input.files = dropped_files;

    // set preview image on image_canvas
    set_canvas_image(dropped_files[0], image_canvas)
}


function set_canvas_image(f, element) {
    let reader = new FileReader();

    // Closure to capture the file information.
    reader.onload = (function() {
    return function(e) {
        // Render thumbnail.
        element.src = e.target.result
    };
    })(f);

    // Read in the image file as a data URL.
    reader.readAsDataURL(f);

}