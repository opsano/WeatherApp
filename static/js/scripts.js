document.addEventListener("DOMContentLoaded", function() {
    
    const body = document.body;
    const condition = body.getAttribute("data-conditon");
    const bg = document.getElementById("weather-bg");

    if (condition.includes("sun") || condition.includes("clear")) {
        bg.classList.add("sunny-bg");
    }
    else if (condition.includes("cloud") || condition.includes("overcast")) {
        bg.classList.add("cloudy-bg");
    }
    else if (condition.includes("rain") || condition.includes("drizzle")) {
        bg.classList.add("rainy-bg");
    }
})