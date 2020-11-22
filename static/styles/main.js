document.onreadystatechange = function() { 
    if (document.readyState !== "complete") { 
        document.querySelector("script").style.visibility = "hidden"; 
        document.querySelector("spinner").style.visibility = "visible"; 
    } else { 
        document.querySelector("spinner").style.display = "none"; 
        document.querySelector("script").style.visibility = "visible"; 
    } 
}; 
