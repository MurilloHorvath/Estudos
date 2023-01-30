// keydown
document.addEventListener("keydown", function(event) {

    // console.log(event.key)

    if(event.key === "Enter" ) {
        console.log("Apertou Enter")
    }

})

// keyup
document.addEventListener("keyup", function(e) {

    if(e.key === "Enter") {
        console.log("Soltou o Enter")
    }

})