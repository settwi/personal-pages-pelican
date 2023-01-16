'use strict';

// make development easier by having this be dynamic
function onLoad() {
    const homeId = "home-but";
    const but = document.getElementById(homeId);
    const maybe = window.location.origin;
    but.href = "index.html";
    // but.href = (maybe === 'null')? "" : maybe;
}
