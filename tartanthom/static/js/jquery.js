$(document).ready(function() {

let index = 0
let right = $('.button-right');
let left = $('.button-left');
let testimonial = $('.testimonial');
$(testimonial[0]).css("display", "block");

right.on('click', function () {
    for (i = 0; i < testimonial.length; i++) {
        $(testimonial[i]).css("display", "none");
    }
    index++;
    if (index > testimonial.length - 1) {
        $(testimonial[testimonial.length - 1]).css("display", "block");
        index = 0;
        return false;
    }
    $(testimonial[index - 1]).css("display", "block");
})

left.on('click', function () {
    for (i = 0; i < testimonial.length; i++) {
        $(testimonial[i]).css("display", "none");
    }
    index--;
    if (index < 1) {
        $(testimonial[testimonial.length + 1]).css("display", "block");
        index = testimonial.length
    }
    $(testimonial[index - 1]).css("display", "block");
})

})