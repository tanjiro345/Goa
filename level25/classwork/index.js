//IMAGE SLIDER

const slides = document.querySelectorAll(".slides img");
let slideIndex = 0;
let intervalid = null;

//intializeSlider();
document.addEventListener("DOMContentLoaded", intializeSlider);

function initializeSlider(){
     if(slides.length > 0){
        slides[slideIndex].classList.add("displaySlide");
        intervalid = setInterval(nextSlide, 5000);
     }
}
function showSlide(index){

    if(index >= slides.length){
         slideIndex = 0;
    }
    else if(index < 0){
        slideIndex = slides.length - 1;
    }

    slides.forEach(slide => {
        slide.classList.remove("displaySlide");
    });
    slides[slideIndex].classList.add("displaySlide");

}
function prevSlide(){

}
function nextSlide(){
    slideIndex++;
    showSlide(slideIndex);
}