// keydown
document.addEventListener("keydown", function(event) {

    // console.log(event.key)
    console.log(event.key)

    if(event.key === "Enter" ) {
        console.log("Apertou Enter")
    }

})

// keyup
document.addEventListener("keyup", function(e) {

    console.log(e.key)

    if(e.key === "Enter") {
        console.log("Soltou o Enter")
    }

})