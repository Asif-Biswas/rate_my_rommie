const navbtn = document.getElementById('nav-btn');
const navinput = document.getElementById('nav-input');
const headtext = document.getElementById('head-text');
const headtext2 = document.getElementById('head-text2');
const headerinput = document.getElementById('header-input');
const search_form = document.getElementById('search-form');
const nav_search_form = document.getElementById('nav-search-form');

const cngNavElemets = (e) => {
    navbtn.innerText = e
    navinput.placeholder = `Enter ${e}`
    if (navbtn.innerText == 'Address') {
        nav_search_form.action = '/search-address'
    } else {
        nav_search_form.action = '/search-roommate'
    }
}
const cngHeadText = () => {
    if (headtext.innerText == 'Welcome to Roommate Finder') {
        headtext.innerText = 'Welcome to Address Finder'
        headtext2.innerText = 'Find your perfect Roommate today!'
        headerinput.placeholder = 'Enter address name'
        search_form.action = '/search-address'
    }
    else {
        headtext.innerText = 'Welcome to Roommate Finder'
        headtext2.innerText = 'Find your perfect Address today!'
        headerinput.placeholder = 'Enter Roommate name'
        search_form.action = '/search-roommate'
    }

}

// check if search-address in url
const url = window.location.href;
if (url.includes('search-address')) {
    cngNavElemets('Address')
}